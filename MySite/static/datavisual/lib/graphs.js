var ZoomChartsLicense = "ZCP-w4sm9lg0n: Production licence for *.zoomcharts.com";
var ZoomChartsLicenseKey = "577dc0aa9e80ab25c83df560952407bfb23369d8c5566347c7"+
    "b54a64a4fbc45ccf4a1e7dbaf0827249c6676c19c918ed548f67ae225e813c5f57dfdc0709137"+
    "7b72c6c3883f1ae343abf24153ef77d3470ee58a8d62781eac016e311d12122256184e9b3efed"+
    "8b7e38d326e1fc10efc599576f803e7a173d128115eb57dabc5f4bf7ae520a50c6963e2ab8c56"+
    "2fa24fa46d246e57afb5bb129fb4507e738251b644f0bd9235665138f043cbce5acfa8197f934"+
    "c58e805963693344ff5240ad98d5aba8ed583f5990cd79e109ab23daaf8cba9ac5c3fee0471b2"+
    "f8f5abff432bff536d8980d582411724f60e01244c8ae94e3e31a4afe4e3322dc9aa5567eabc9";
var t;
//var graphColor = ["#9467BD","#E377C2","#2CA02C","#FF7F0E","#7F7F7F","#D62728","#8C564B","#1F77B4"];
var graphColor = ["#1790cf","#d3691f","#7f7f7f","#22bb22","#1ab2d9","#88b0ba","#D62728","#1F77B4"];
var allRelationsType = {"专利分类":1,"发明人":1,"专利类型":1,"申请人":0,"标签":1,"公司":0};
var allRelationsName = {"专利分类":1,"发明人":4,"专利类型":2,"申请人":3,"标签":5,"公司":2};
var allNodeNameMap = {1:"专利",2:"类型",3:"分类",4:"发明人",5:"公司",10000:"标签"};
var allNodeNameColorMap = {1:8,2:6,3:7,4:4,5:5,10000:3};
var allNodeType = new Array();
var allToType = new Array();
var tagIds = {};
var newTagId = 200000000000;

function emptyGraph(){
	t.replaceData({
		nodes: [],
	    links: []
	});
}

var localization_zh = {
		closeButton: "关闭",
		dataRequestFailed: "请求数据失败",
		loadingLabel: "加载中...",
		menu : {
			collapse: "折叠",
			dynaminc: "动态",
			expand: "展开",
			fixed: "Fixed",
			focus: "Focus",
			hide: "隐藏",
			unfocus: "Unfocus"
		},
		toolbar : {
			backButton: "回退",
			backTitle: "导航中回退一步",
			exportButton: "导出",
			exportCSV: "Spreadsheet (csv)",
			exportJpeg: "For Office and Web (jpeg)",
			exportPDF: "For Printer (pdf)",
			exportPNG: "For Photoshop (png)",
			exportTitle: "Export Data",
			exportXLS: "Spreadsheet (xls)",
			fitButton: "Fit",
			fitTitle: "适合屏幕",
			freezeButton: "Freeze",
			freezeTitle: "全部锁定",
			fullscreenButton: "全屏",
			fullscreenTitle: "切换全屏模式",
			rearrangeButton: "重新排列",
			rearrangeTitle: "重新排列元素",
			unfreezeTitle: "解锁全部",
			zoomoutButton: "Zoom-out",
			zoomoutTitle: "Zoom out"
		}
	};

var exRelation = {};

function draw_graph_basic(nodeData,inputData,refresh){
	for ( var k in nodeData) {
		var n = nodeData[k];
		if(n.classId == 10000){
			var nid = nodeData[k].id;
			if(!tagIds[n.name]){
				tagIds[n.name] = newTagId;
				newTagId++;
			}
			nodeData[k].id = tagIds[n.name];
			for ( var k2 in inputData) {
				if(inputData[k2].fromId == nid){
					inputData[k2].fromId = tagIds[n.name];
				}
				if(inputData[k2].toId == nid){
					inputData[k2].toId = tagIds[n.name];
				}
				if(inputData[k2].from == nid){
					inputData[k2].from = tagIds[n.name];
				}
				if(inputData[k2].to == nid){
					inputData[k2].to = tagIds[n.name];
				}
			}
		}
	}
	
	var tmpInputData  = [];
	for (var i = 0; i < inputData.length; i++) {
		var tagId = inputData[i].fromId;
		var oId = inputData[i].toId;
		if(inputData[i].fromId < 200000000000){
			tagId = inputData[i].toId;
			oId = inputData[i].fromId;
		}
		var rs = exRelation[tagId] || [];
		var ex = false;
		for (var j = 0; j < rs.length; j++) {
			if(rs[j] == oId){
				ex = true;
				break;
			}
		}
		if(!ex){
			rs.push(oId);
			exRelation[tagId] = rs;
			tmpInputData.push(inputData[i]);
		}
	}
	inputData = tmpInputData;
	
	if(t == null || refresh){
		var h = $("zoom-chart").height();
		var w = $("zoom-chart").width();
		t = new NetChart({
			container: document.getElementById("zoom-chart"),
			area:{
				height: h,
				width: w
			},
			style:{
				nodeLabel:{
					backgroundStyle: {fillColor:'#FFF'}, 
					textStyle: {font:"15px Microsoft Yahei", fillColor:'black'},
					padding: 0,
					borderRadius: 0
				},
				nodeStyleFunction: nodeStyle,
				linkStyleFunction:linkStyle,
				node: {
					imageCropping: true
				}
			},
			info:{
				enabled: true,
				nodeContentsFunction: function(itemData, item){
					return getNodeContent(itemData, item);
				},
				linkContentsFunction: function(itemData, item){
					return getLinkContent(itemData, item);
				}
			},
			data: {
				preloaded: {
					nodes: nodeData,
					links: inputData
				}
			},
			events:{
				onClick: graphClick,
				onDoubleClick: graphDoubleClick,
				onRightClick: graphRightClick
			},
			layout:{
				nodeSpacing: 30
			},
			localization: localization_zh
		});
	}else{
		t.addData({
			nodes: nodeData,
		    links: inputData
		});
	}			
}

function nodeStyle(node){
	var imgName = "";
	var datalinks = node.dataLinks;
	var lineColor = null;
	var thisId = null;
	var toType = 0;
	var flag = false;
	node.label = removeHTMLTag(node.data.name || node.data.id);
	for(var i=0;i<datalinks.length;i++){
		if(datalinks[i].from == node.data.id){
			if(parseInt(datalinks[i].fromType) == 4){
				imgName = "chart_people.png";
			}else if(parseInt(datalinks[i].fromType) == 5){
				imgName = "chart_company.png";
			}else if(parseInt(datalinks[i].fromType) == 1){
				imgName = "chart_patent.png";
			}else if(parseInt(datalinks[i].fromType) == 2){
				imgName = "chart_type.png";
			}else if(parseInt(datalinks[i].fromType) == 3){
				imgName = "chart_classsify.png";
			}else if(parseInt(datalinks[i].fromType) == 10000){
				imgName = "chart_tag.png";
			}else{
				imgName = "chart_company.png";
			}
			thisId = datalinks[i].fromId;
			toType = datalinks[i].toType;
			var lineColorObj = datalinks[i].lineColor;
			if(lineColorObj){
				for (var j1 = 0; j1 < lineColorObj.length; j1++) {
					if(lineColorObj[j1] == thisId){
						lineColor = "#f00";	
						break;
					}
				}
			}
			flag = true;
		}
		if(datalinks[i].to == node.data.id){
			if(parseInt(datalinks[i].toType) == 4){
				imgName = "chart_people.png";
			}else if(parseInt(datalinks[i].toType) == 5){
				imgName = "chart_company.png";
			}else if(parseInt(datalinks[i].toType) == 1){
				imgName = "chart_patent.png";
			}else if(parseInt(datalinks[i].toType) == 2){
				imgName = "chart_type.png";
			}else if(parseInt(datalinks[i].toType) == 3){
				imgName = "chart_classsify.png";
			}else if(parseInt(datalinks[i].toType) == 10000){
				imgName = "chart_tag.png";
			}else{
				imgName = "chart_company.png";
			}
			thisId = datalinks[i].toId;
			toType = datalinks[i].toType;
			var lineColorObj2 = datalinks[i].lineColor;
			if(lineColorObj2){
				for (var j2 = 0; j2 < lineColorObj2.length; j2++) {
					if(lineColorObj2[j2] == thisId){
						lineColor = "#f00";	
						break;
					}
				}
			}
			flag = true;
		}
		if(flag){
			break;
		}
	}
	imgName = "charts_company.png";
	if(!imgName ){
		if(node.data.classId== 4){
			imgName = "chart_people.png";
		}else if(node.data.classId== 5){
			imgName = "chart_company.png";
		}else if(node.data.classId== 1){
			imgName = "chart_patent.png";
		}else if(node.data.classId== 2){
			imgName = "chart_type.png";
		}else if(node.data.classId== 3){
			imgName = "chart_classsify.png";
		}else if(node.data.classId== 10000){
			imgName = "chart_tag.png";
		}else{
			imgName = "";
		}
	}	
		
	node.radius = node.data.radius;
	node.lineWidth = getNodeLineWidth(node);
	node.image = "images/"+imgName;
	node.imageSlicing = [0,0,170,170];
	node.lineColor = lineColor || getNodeLineColor(node);
}

function getNodeLineWidth(node){
	var datalinks = node.dataLinks;
	
	var focusNodeId = null;
	var flag = false;
	for(var i=0;i<datalinks.length;i++){
		if(datalinks[i].from == node.data.id){
			focusNodeId = datalinks[i].fromId;
			flag = true;
		}
		if(datalinks[i].to == node.data.id){
			focusNodeId = datalinks[i].toId;
			flag = true;
		}
		if(flag){
			break;
		}
	}
	
	return 2;
}

function getNodeLineColor(node){
	var datalinks = node.dataLinks;
	var thisType = null;
	var flag = false;
	for(var i=0;i<datalinks.length;i++){
		if(datalinks[i].from == node.data.id){
			thisType = datalinks[i].fromType;
			flag = true;
		}
		if(datalinks[i].to == node.data.id){
			thisType = datalinks[i].toType;
			thisName = datalinks[i].to;
			flag = true;
		}
		if(flag){
			break;
		}
	}
	if(!thisType){
		thisType = node.data.classId;
	}
	var nodeColor = graphColor[graphColor.length - allNodeNameColorMap[thisType]];
	var es = false;
	for (var i = 0; i < allNodeType.length; i++) {
		if(allNodeType[i] == thisType){
			es = true;
			break;
		}
	}
	if(!es){
		allNodeType.push(thisType);
		if($(".con-color").find(".con-color-list").length > 0){
			$(".con-color").append("<br/>");
		}
		$(".con-color").append('<div class="con-color-list clearfix"><div class="con-color-list-box" style="background-color:'+nodeColor+';"></div><div class="con-color-list-name">'+allNodeNameMap[thisType]+'</div></div>');
	}
	return "#4692c8";//nodeColor;
	
}

function linkStyle(link){
	var specialLinkRadius = 2;
	var linkFillColor = graphColor[allRelationsName[link.data.relation]];
	var es = false;
	for (var i = 0; i < allToType.length; i++) {
		if(allToType[i] == link.data.relation){
			es = true;
			break;
		}
	}
	if(!es){
		allToType.push(link.data.relation);
		if($(".con-line").find(".con-color-list").length > 0){
			$(".con-line").append("<br/>");
		}
		var re = link.data.relation;
		$(".con-line").append('<div class="con-color-list clearfix"><div class="con-color-list-line" style="background-color:'+linkFillColor+';"></div><div class="con-color-list-name">'+re+'</div></div>');
	}
	
	if(allRelationsType[link.data.relation] != 0){
		link.toDecoration = "arrow";
	}
	else{
		link.fromDecoration = "arrow";
	}
	
	link.radius = specialLinkRadius;
	link.fillColor = linkFillColor;
	return;
}

function graphClick(event){
	if (event.clickNode){
		var datalinks = event.clickNode.dataLinks;
		
		var numApplication = "";
		var kgId = "";
		var tag = "";
		
		var flag = false;
		for(var i=0;i<datalinks.length;i++){
			if(datalinks[i].from == event.clickNode.data.id){
				if(datalinks[i].fromType == 10000){
					tag = datalinks[i].fromName;
				}else{
					kgId = datalinks[i].fromId;
					numApplication = datalinks[i].fromNumApplication;	
				}
				flag = true;
			}
			if(datalinks[i].to == event.clickNode.data.id){
				if(datalinks[i].toType == 10000){
					tag = datalinks[i].toName;
				}else{
					kgId = datalinks[i].toId;
					numApplication = datalinks[i].toNumApplication;
				}
				flag = true;
			}
			if(flag){
				break;
			}
		}
		if(kgId || tag){
			if(window.isChart){
				initPatentGraph(numApplication,kgId,tag,false);
			}else{
				goWebPage("chart.html?numApplication="+numApplication+"&kgId="+kgId+"&tag="+tag);
			}
		}
	}
}

function graphDoubleClick(event){
	
}

function graphRightClick(event){
	event.preventDefault();
	$("#pop-rightClick").remove();
	if(event.clickNode && window.isChart){
		var flag = false;
		var id = 0;
		var links = event.clickNode.dataLinks;
		var name = event.clickNode.data.name;
		for (var i = 0; i < links.length; i++) {
			if(links[i].fromName == name){
				if(links[i].fromType == 5){
					id = links[i].fromId;	
				}
				flag = true;
			}else if(links[i].toName == name){
				if(links[i].toType == 5){
					id = links[i].toId;
				}
				flag = true;
			}
			if(flag){
				break;
			}
		}
		if(id > 0){
			var div = $("<div id='pop-rightClick'><ul></ul></div>");
			div.find("ul").append("<li class='rc-item' onclick=\"showEntDetail(this,"+id+",'"+name+"')\">查看企业信息</li>");
			div.css({"top":(event.pageY + 10 )+"px","left":(event.pageX + 10 )+"px"});
			$("body").append(div);
		}
	}
}

function getNodeContent(itemData, item){
	var div_pre = "<div style='font-size:12px;font-family: 微软雅黑;font-weight:bold;font-color:#fff;bockground-color:#008abf;padding:10px 5px 5px 10px;'>";
	var div_after = "</div>";
	var data = item.dataLinks;
	for(var i=0;i<data.length;i++){
		if(itemData.id == data[0].from){
			if(data[0].fromType==1){
			}else if(data[0].fromType==2){
			}else if(data[0].fromType==3){
			}else if(data[0].fromType==4){
			}else if(data[0].fromType==5){
			}
		} 
		if(itemData.id == data[0].to){
			if(data[0].toType==1){
			}else if(data[0].toType==2){
			}else if(data[0].toType==3){
			}else if(data[0].toType==4){
			}else if(data[0].toType==5){
			}
		}
	}
	return "";
}

function getLinkContent(itemData, item){
	var re = item.data.relation;
	var tableHTML = "<div style='font-size:12px;font-family: 微软雅黑;font-weight:bold;font-color:#fff;bockground-color:#008abf;padding:10px 5px 5px 10px;'>" + re + "&nbsp;&nbsp;</div>";				
	return tableHTML;
}
