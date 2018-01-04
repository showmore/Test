function updateIframeH(){
	if(parent){
		parent.resizeIframe();
	}
}

String.prototype.replaceAll = function(reallyDo, replaceWith, ignoreCase) {
	if (!RegExp.prototype.isPrototypeOf(reallyDo)) {
		return this.replace(new RegExp(reallyDo, (ignoreCase ? "gi": "g")), replaceWith);
	} else {
		return this.replace(reallyDo, replaceWith);
	}
};

function printPreview(oper) {
	bdhtml=window.document.body.innerHTML;//获取当前页的html代码 
	sprnstr="<!--startprint"+oper+"-->";//设置打印开始区域 
	eprnstr="<!--endprint"+oper+"-->";//设置打印结束区域 
	prnhtml=bdhtml.substring(bdhtml.indexOf(sprnstr)+sprnstr.length); //从开始代码向后取html 
	prnhtml=prnhtml.substring(0,prnhtml.indexOf(eprnstr));//从结束代码向前取html 
	prnhtml=prnhtml.replaceAll('href','aa');
	window.document.body.innerHTML=prnhtml; 
	window.print(); 
	window.document.body.innerHTML=bdhtml; 
}

function resizeIframe(){
	try{
		var iframe = document.getElementById("main-iframe");
//		var pheight = document.body.scrollHeight || document.documentElement.scrollHeight;
//		pheight = pheight - $(iframe).offset().top - $(".footerBox").outerHeight();
		var iHeight = iframe.contentWindow.document.body.scrollHeight || iframe.contentWindow.document.documentElement.scrollHeight;
		var iHeight2 = parseInt($(iframe).css("min-height"));
		iframe.style.height = (iHeight　> iHeight2 ? iHeight : iHeight2) + "px";
	}catch (e) {
	}
}


function removeEmptyElement(array){
	var result = new Array();
	for (var int = 0; int < array.length; int++) {
		if(array[int]){
			result.push(array[int]);
		}
	}
	if(result.length > 0){
		return result;		
	}else{
		return null;		
	}
}

function showTimer(count,dom,jumpHref){
	var jumpCount = count;
	$(dom).text(jumpCount);
	setInterval(function(){
		jumpCount --;
		if( jumpCount == 0){
			goWebPage(jumpHref);
		}
		$(dom).text(jumpCount);
	},1000);
}

function ImgDraw(dom){
	$.each($(dom),function(i,v){
		var src = $(this).attr("src");
		if(src == "" || src == null || src == "null" || src == getAbsoluteLink("") || src == getAbsoluteLink(null) || src == getAbsoluteLink("null")){
			$(this).attr('src',getAbsoluteLink('images/default.jpg'));
		}
	});
}

function formatDateTime(time){
	if(time){
		var dt = null;
		if(typeof(time) == "string"){
			dt = new Date(time);
		}else if(time.time){
			dt = new Date(time.time);
		}else if(typeof(time) == "number"){
			dt = new Date(time);
		}
		if(dt){
			return dateToString(dt);
		}	
	} else {
        return dateToString(new Date());
	}
	return "";
}

function dateToString(dt){
	var month = (dt.getMonth() + 1) + "";
	var date = dt.getDate() + "";
	var hour = dt.getHours() + "";
	var minutes = dt.getMinutes() + "";
	var second = dt.getSeconds() + "";
	return formatDateYear(dt.getFullYear(), month, date, hour, minutes, second);
}

function formatDate(month, date, hour, minutes, second){
	if((""+month).length < 2){
		month = "0" + month;
	}
	if((""+date).length < 2){
		date = "0" + date;
	}
	if((""+hour).length < 2){
		hour = "0" + hour;
	}
	if((""+minutes).length < 2){
		minutes = "0" + minutes;
	}
	if(typeof(second) != "undefined" ){
		if((""+second).length < 2){
			second = "0" + second;
		}
		return month+"-"+date+" "+hour+":"+minutes+":"+second;
	}else{
		return month+"-"+date+" "+hour+":"+minutes;		
	}
}

function formatDateYear(year,month, date, hour, minutes, second){
	if(year.length <2){
	    year = "0"+year;	
	}
	return year+"-"+formatDate(month, date, hour, minutes, second);
}

function judgeDate(time){
	time =  time.replaceAll("-","/");
	var dt = new Date(time);
	return dt;
}

function placeholderBug(){
	if( !('placeholder' in document.createElement('input')) ){   

	    $('input[placeholder],textarea[placeholder]').each(function(){    
	      var that = $(this),    
	      text= that.attr('placeholder');    
	      if(that.val()===""){    
	        that.val(text).addClass('placeholder');    
	      }    
	      that.focus(function(){    
	        if(that.val()===text){    
	          that.val("").removeClass('placeholder');    
	        }    
	      })    
	      .blur(function(){    
	        if(that.val()===""){    
	          that.val(text).addClass('placeholder');    
	        }    
	      })    
	      .closest('form').submit(function(){    
	        if(that.val() === text){    
	          that.val('');    
	        }    
	      });    
	    });    
	  }   
}

function formatPrice(price){
	price = price + "";
	if(price.indexOf(".") > 0){
		var sub = price.split(".")[1];
		if(sub.length == 1){
			return price.split(".")[0] + "." + sub + "0";
		}else if(sub.length == 2){
			return price;
		}else{
			if(sub.charAt(2) > 4){
				var int = price.split(".")[0];
				var ssub = (parseInt(sub.substring(0,2)) + 1) + "";
				if(ssub.length == 1){
					ssub = "0" + ssub;
				}else if(ssub.length == 3){
					ssub = ssub.substring(1);
					int = parseInt(int) + 1;
				}
				return int + "." + ssub;
			}else{
				return price.split(".")[0] + "." + sub.substring(0,2);
			}
		}
	}else if(price == '0' || price == 0){
		return "0";
	}else{
		return price+".00";
	}
}

function formatNumber(num){
	num = num + "";
	if(num.indexOf(".") > 0){
		var sub = num.split(".")[1];
		if(sub.length == 1){
			return num;
		}else{
			if(sub.charAt(1) > 4){
				return num.split(".")[0] + 1;
			}else{
				return num.split(".")[0] + "." + sub.substring(0,1);
			}
		}
	}else{
		return num;
	}
}

function showToast(msg,auto,event,hideico) {
	var did = null;
	if(parent){
		did = parent.addAlertDialog(msg, event);
	}else{
		did = addAlertDialog(msg, event);
	}
	if(auto){
		setTimeout(function(){closeSysDialog(did);},2000);
	}
}

function getSysDialogOffsetTop(dlgh,height){
	var scrollTop = document.body.scrollTop || document.documentElement.scrollTop;
	if(dlgh > height){
		return height * 0.05 + scrollTop;
	}else{
		return height * 0.5 - dlgh / 2 + scrollTop;
	}
}

$(window).scroll(function(event){
	var height = document.body.scrollTop || document.documentElement.scrollTop;
	if(height > 500){
		$(".go-top").css("visibility","visible");
	}else{
		$(".go-top").css("visibility","hidden");
	}
});

$(window).resize(function(event){
	height = document.body.clientHeight || document.documentElement.clientHeight;
	if($(".sys-dialog").length){
		if($(".sys-dialog").offset().top < height * 0.05){
			$(".sys-dialog").css({"top":"5%","margin-top":"0"});
		}	
	}
	if($("#sys-mask").length){
		$("#sys-mask").height(height);
	}
});

function showSysDialog(did,ifParent){
	var domDiv = "";
	var domMask = "";
	var height ="";
	if(ifParent){
		domDiv = $("#"+did,parent.document);
		domMask = $("#sys-mask",parent.document);
		height = parent.document.body.clientHeight || parent.document.documentElement.clientHeight;
	}else{
		domDiv = $("#"+did);
		domMask = $("#sys-mask");
		height = document.body.clientHeight || document.documentElement.clientHeight;
	}
	var dlgh = domDiv.height();
	domDiv.css({"top":getSysDialogOffsetTop(dlgh,height) + "px"});
	var wHeight = $(window).height();
	if(dlgh > wHeight * 0.9){
		var h = wHeight*0.9 - 100;
		domDiv.find(".sys-dialog-body").css({"height":(h > 300 ? h : 300) +"px","overflow":"auto"});	
	}
	domDiv.show();
	if(ifParent){
		height = parent.document.body.scrollHeight || parent.document.documentElement.scrollHeight;
	}else{
		height = document.body.scrollHeight || document.documentElement.scrollHeight;
	}
	if(domMask.length  == 0){
		domMask = $('<div id="sys-mask"></div>');
	}
	domMask.height(height).show();
	domDiv.before(domMask);

}

/**
 * 修改obj hide时出现多余dialog的情况
 * */
function addSysDialog(param,ifParent){
	$("body").css("overflow","hidden");
	var params = {
		obj:null,
		content:"",
		width:400,
		footStyle:"",
		foot:"",
		buttons:[],
		hide:false,
		title:"",
		auto:true,
		reset:false
	};
	var events ={};
	$.extend(params,param);
	var did = "sd"+new Date().getTime();
	var bodyDom ='';
	if(ifParent){
		bodyDom = $('body',parent.document);
	}else{
		bodyDom = $('body');
	}
	
	if(params.obj){
		if($(params.obj).closest(".sys-dialog").length > 0){
			did = $(params.obj).closest(".sys-dialog").attr("id");
			if(params.reset){
				$(params.obj).closest(".sys-dialog").remove();
				params.obj = bodyDom.data(did);
			}
		}else{
			bodyDom.data(did,params.obj.clone());			
		}
	}
//	if(params.obj && $(params.obj).closest(".sys-dialog").length > 0){
//		
//	}else{
		var existdlg = bodyDom.find(".sys-dialog");
		var ex = false;
		for (var i = 0; i < existdlg.length; i++) {
			var dlg = $(existdlg[i]);
			if(dlg.find(".sys-dialog-body").html() == params.content){
				did = dlg.attr("id");
				ex == true;
			}
		}
		if(!ex){
			var style = "";
			if(params.width){
				if(typeof(params.width) == "string" && params.width.indexOf("%") > 0){
					style = "style=\"width:"+params.width + ";margin-left:-"+parseFloat(params.width) / 2 + "%;\"";
				}else{
					style = "style=\"width:"+params.width + "px;margin-left:-"+params.width / 2 + "px;\"";	
				}
			}
			var foot = "";
			var footStyle = "";
			if(params.footStyle){
				footStyle = "style='"+params.footStyle+"'";
			}
			if(params.foot){
				foot = '<div class="sys-dialog-foot" '+footStyle+'>'+params.foot+'</div>';
			}else{
				if(params.buttons.length){
					foot = '<div class="sys-dialog-foot" '+footStyle+'>';
					for (var i = 0; i < params.buttons.length; i++) {
						var btn = params.buttons[i];
						var event = btn.event || "closeSysDialog('"+did+"',"+params.hide+","+ifParent+")";
						var id = did + i;
						events[id] = event;
						var text = btn.text || "确定";
						var cls = btn.cls || "btn-primary";
						foot += '<input type="button" class="btn ' + cls + '" value="'+text+'" id="'+id+'"/>';
						if(i != params.buttons.length - 1){
							foot += '&nbsp;&nbsp;&nbsp;&nbsp;';
						}
					}
					foot += '</div>';
				}
			}
			var head = "";
			if(params.title){
				head = '<div class="sys-dialog-head">'+params.title+'<div class="sys-dialog-close" onclick="closeSysDialog(\''+did+'\','+params.hide+')"></div></div>';
			}
//			bodyDom.find("#sys-mask").remove();
//			bodyDom.append('<div id="sys-mask"></div>');	
//			if($("#sys-mask").length == 0){
//				bodyDom.append('<div id="sys-mask"></div>');	
//			}	
			bodyDom.append('<div id="'+did+'" class="sys-dialog" '+style+'>'+head+
				'<div class="sys-dialog-content"><div class="sys-dialog-body clearfix">'+params.content+		
				'</div>'+foot+'</div></div>');
			for ( var eid in events) {
				bodyDom.find("#"+eid).on("click",function(event){
					var eid = $(this).attr("id");
					if(typeof(events[eid]) == "string"){
						eval(events[eid]);
					}else{
						events[eid](this,$(this).closest(".sys-dialog"));
					}
				})
			}
			if(params.obj){
				bodyDom.find("#"+did+" .sys-dialog-body").append(params.obj);
			}
		}
//	}
	if(params.auto){
		showSysDialog(did,ifParent);
	}
	return did;
}

function closeThisSysDialog(that,hide,ifParent){
	var did = $(that).closest(".sys-dialog").attr("id");
	closeSysDialog(did, hide, ifParent);
}

function closeSysDialog(did,hide,ifParent){
	$("body").css("overflow","auto");
	var domDiv = "";
	var domMask = "";
	var domSys ="";
	
	if(hide){
		if(ifParent){
			domDiv = $("#"+did,parent.document);
			domMask = $("#sys-mask",parent.document);
		}else{
			domDiv = $("#"+did);
			domMask = $("#sys-mask");
		}
		domDiv.hide();
	}else{
		if(ifParent){
			domDiv = $("#"+did,parent.document);
			domMask = $("#sys-mask",parent.document);
		}else{
			domDiv = $("#"+did);
			domMask = $("#sys-mask");
		}
		domDiv.remove();
	}
	if($(".sys-dialog:visible").length == 0){
		domMask.remove();	
	}else{
		$(".sys-dialog:visible").last().before(domMask);
	}
}

function addAlertDialog(msg,event,hideico){
	if(!event && msg == $(".sys-dialog:visible").find(".sys-dialog-body").text()){
		return;
	}
	var ico = '<i class="fa fa-exclamation-triangle fa-2x" style="vertical-align: -4px;margin-right: 10px;color: #FC0;"></i>';
	if(hideico){
		ico = "";
	}
	var params = {};
	params.title = "提 示";
	params.width = 400;
	params.buttons = new Array();
	var btn = {};
	if(event){
		btn.event = event;		
	}
	btn.cls = "btn-primary";
	btn.text = " 确 定 ";
	params.buttons.push(btn);
	params.content = '<div style="text-align: center;padding: 40px 0 10px;">'+ico + msg+'</div>';
	params.auto = true;
	return addSysDialog(params);
}

function addSuccDialog(msg,event,hideico){
	if(!event && msg == $(".sys-dialog:visible").find(".sys-dialog-body").text()){
		return;
	}
	var ico = '<i class="fa fa-check-circle-o fa-2x" style="vertical-align: -4px;margin-right: 10px;color: #3C8DBC;"></i>';
	if(hideico){
		ico = "";
	}
	var params = {};
	params.title = "提 示";
	params.width = 400;
	params.buttons = new Array();
	var btn = {};
	if(event){
		btn.event = event;		
	}
	btn.cls = "btn-primary";
	btn.text = " 确 定 ";
	params.buttons.push(btn);
	params.content = '<div style="text-align: center;padding: 40px 0 10px;">'+ico + msg+'</div>';
	params.auto = true;
	return addSysDialog(params);
}

function addDeleteDialog(event){
	return addConfirmDialog('确认删除？', event);
}

function addDetailDialog(title,data,callback,width,ifParent){
	var html = $("<div><table class='virtue-box' width='100%'></table></div>");
	for ( var key in data) {
		var tr = $("<tr><td>"+key+"</td><td></td></tr>");
		tr.find("td:eq(1)").text(data[key]);
		html.children("table").append(tr);
	}
	html = html.html();
	var params = {};
	params.title = title;
	params.width = width || 600;
	params.buttons = new Array();
	var btn = {};
	if(callback){
		btn.event = callback;	
	}
	btn.cls = "btn-primary";
	btn.text = " 确 定 ";
	params.buttons.push(btn);
	params.content = '<div style="text-align: left;padding: 20px 0 10px;">'+html+'</div>';
	params.auto = true;
	return addSysDialog(params,ifParent);
}

function addConfirmDialog(title,event,ifParent){
	var params = {};
	params.title = "提 示";
	params.width = 400;
	params.buttons = new Array();
	var btn2 = {};
	btn2.cls = "btn-cancel";
	btn2.text = " 取 消 ";
	params.buttons.push(btn2);
	var btn = {};
	btn.event = event;
	btn.cls = "btn-primary";
	btn.text = " 确 定 ";
	params.buttons.push(btn);
	params.content = '<div style="text-align: center;padding: 40px 0 10px;">'+title+'</div>';
	params.auto = true;
	return addSysDialog(params,ifParent);
}

function addSuperConfirmDialog(title,event,tip,ifParent){
	tip = tip || title;
	var params = {};
	params.title = title;
	params.width = 400;
	params.buttons = new Array();
	var btn2 = {};
	btn2.cls = "btn-cancel";
	btn2.text = " 取 消 ";
	params.buttons.push(btn2);
	var btn = {};
	btn.event = event;
	btn.cls = "btn-primary";
	btn.text = " 确 定 ";
	params.buttons.push(btn);
	params.content = '<div style="padding: 30px 0 10px;"><div>请输入"'+tip+'"确认进行'+title+'操作</div><div><input id="super-confirm-input" class="super-confirm-input"></div></div>';
	params.auto = true;
	return addSysDialog(params,ifParent);
}

function goWebPage(page,isTop){
	if(isTop){
		top.location.href = getAbsoluteLink(page);
	} else{
		window.location.href = getAbsoluteLink(page);
	}
}

function goNewWebPage(page){
	 window.open(getAbsoluteLink(page));	
}

function getWebRoot(){
	var href = window.location.href;
	var defaultAppName  = configs.PROJECT_NAME;
	if(href.indexOf("/" + defaultAppName, 8) > 0 ){
		return href.substring(0, href.indexOf("/" + defaultAppName, 8) + defaultAppName.length + (defaultAppName?2:1));
	}else{
		return href.substring(0, href.indexOf("/", 8) + 1);
	}
}

function getAbsoluteLink(str){
	if(str && str != null){
		if(str.indexOf("http://") == 0){
			return str;
		}
		return getWebRoot() + str; 		
	}else{
		return str;
	}
}

function getTopJsonNode(nodes,nodeid){
	var findedId = nodeid;
	while (true && nodes.length > 0) {
		for(var i = 0;i < nodes.length;i++){
			if(nodes[i].id == findedId){
				findedId = nodes[i].pid;
				if(findedId == 0){
					return nodes[i];
				}
			}
		}
	}
}

function getParentJsonNode(nodes,nodeid){
	for(var i = 0;i < nodes.length;i++){
		if(nodes[i].id == nodeid){
			nodeid = nodes[i].pid;
			for(var i = 0;i < nodes.length;i++){
				if(nodes[i].id == nodeid){
					return nodes[i];
				}
			}
		}
	}
}

function getJsonNode(nodes,nodeid){
	for(var i = 0;i < nodes.length;i++){
		if(nodes[i].id == nodeid){
			return nodes[i];
		}
	}
}

function getChildrenJsonNodes(nodes,nodeid){
	var chilrenNode = new Array();
	for(var i = 0;i < nodes.length;i++){
		if(nodes[i].pid == nodeid){
			chilrenNode.push(nodes[i]);
		}
	}
	return chilrenNode;
}

function resetUrlParm(k,v,link){
	if(!link){
		link = window.location.href;		
	}
	if(typeof(k) == "string"){
		var s = "&"+k+"=";
		var ss = "?"+k+"=";
		var c = "";
		if(link.indexOf("#") > 0){
			c = "#"+link.split("#")[1];
			link = link.split("#")[0];
		}
		if(link.indexOf(s) > 0){
			var b = link.split(s)[0];
			
			var a = "";
			if(link.split(s)[1].indexOf("&") > 0){
				var at = link.split(s)[1];
				a = at.substring(at.indexOf("&"));
			}
			if(v == null){
				return b + a + c;
			}else{
				return b + s + v + a + c;
			}
		}else if(link.indexOf(ss) > 0){
			var b = link.split(ss)[0];
			var a = "";
			if(link.split(ss)[1].indexOf("&") > 0){
				var at = link.split(ss)[1];
				a = at.substring(at.indexOf("&"));
			}
			if(v == null){
				return b + a.replace("&", "?") + c;
			}else{
				return b + ss + v + a + c;
			}
		}else{
			if(v == null){
				return link + c;
			}else{
				if(link.indexOf("?") > 0){
					return link + s + v + c;						
				}else{
					return link + ss + v + c;						
				}
			}	
		}
	}else if(typeof(k) == "object"){
		for ( var p in k ){ // 方法 
		   link = resetUrlParm(p,k[p],link);
		}
		return link;
	}
}

function getDecodeSearchParm(name) {
	var r = getSearchParm(name);
	if(r != null){
		try{
			r = decodeURIComponent(escape(r));			
		}catch (e) {
			
		}
	}
	return r;
}


//js获取url参数
function getUrlParam(name){
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
	var r = window.location.search.substr(1).match(reg);
	if (r != null)
		return decodeURIComponent(r[2]);
	return null;
}

function getSearchParm(name) {
	var reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)");
	var r = window.location.search.substr(1).match(reg);
	if (r != null)
		return unescape(r[2]);
	return null;
}

function isEmail(str){
	var reg = /^([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+@([a-zA-Z0-9]+[_|\_|\.]?)*[a-zA-Z0-9]+\.[a-zA-Z]{2,3}$/;
	return reg.test(str);
}

function isMobile(tel){
	var reg = /^1[3-9]\d{9}$/;
	return reg.test(tel);
}

function isIdCard(str){
	var reg = /^[1-9]\d{5}[1-9]\d{3}((0\d)|(1[0-2]))(([0|1|2]\d)|3[0-1])((\d{4})|\d{3}[A-Z])$/;
	return reg.test(str);
}

function checkPwdLevel(val){ 
	var lv = 0; 
	if(val.match(/[a-z]/g)){lv++;} 
	if(val.match(/[0-9]/g)){lv++;} 
	if(val.match(/(.[^a-z0-9])/g)){lv++;} 
	if(val.length < 6){lv=0;} 
	if(lv > 3){lv=3;} 
	return lv;
} 

function md5(sMessage) {
	function RotateLeft(lValue, iShiftBits) {
		return (lValue << iShiftBits) | (lValue >>> (32 - iShiftBits));
	}

	function AddUnsigned(lX, lY) {
		var lX4, lY4, lX8, lY8, lResult;
		lX8 = (lX & 0x80000000);
		lY8 = (lY & 0x80000000);
		lX4 = (lX & 0x40000000);
		lY4 = (lY & 0x40000000);
		lResult = (lX & 0x3FFFFFFF) + (lY & 0x3FFFFFFF);
		if (lX4 & lY4)
			return (lResult ^ 0x80000000 ^ lX8 ^ lY8);
		if (lX4 | lY4) {
			if (lResult & 0x40000000)
				return (lResult ^ 0xC0000000 ^ lX8 ^ lY8);
			else
				return (lResult ^ 0x40000000 ^ lX8 ^ lY8);
		} else
			return (lResult ^ lX8 ^ lY8);
	}

	function F(x, y, z) {
		return (x & y) | ((~x) & z);
	}

	function G(x, y, z) {
		return (x & z) | (y & (~z));
	}

	function H(x, y, z) {
		return (x ^ y ^ z);
	}

	function I(x, y, z) {
		return (y ^ (x | (~z)));
	}

	function FF(a, b, c, d, x, s, ac) {
		a = AddUnsigned(a, AddUnsigned(AddUnsigned(F(b, c, d), x), ac));
		return AddUnsigned(RotateLeft(a, s), b);
	}

	function GG(a, b, c, d, x, s, ac) {
		a = AddUnsigned(a, AddUnsigned(AddUnsigned(G(b, c, d), x), ac));
		return AddUnsigned(RotateLeft(a, s), b);
	}

	function HH(a, b, c, d, x, s, ac) {
		a = AddUnsigned(a, AddUnsigned(AddUnsigned(H(b, c, d), x), ac));
		return AddUnsigned(RotateLeft(a, s), b);
	}

	function II(a, b, c, d, x, s, ac) {
		a = AddUnsigned(a, AddUnsigned(AddUnsigned(I(b, c, d), x), ac));
		return AddUnsigned(RotateLeft(a, s), b);
	}

	function ConvertToWordArray(sMessage) {
		var lWordCount;
		var lMessageLength = sMessage.length;
		var lNumberOfWords_temp1 = lMessageLength + 8;
		var lNumberOfWords_temp2 = (lNumberOfWords_temp1 - (lNumberOfWords_temp1 % 64)) / 64;
		var lNumberOfWords = (lNumberOfWords_temp2 + 1) * 16;
		var lWordArray = Array(lNumberOfWords - 1);
		var lBytePosition = 0;
		var lByteCount = 0;
		while (lByteCount < lMessageLength) {
			lWordCount = (lByteCount - (lByteCount % 4)) / 4;
			lBytePosition = (lByteCount % 4) * 8;
			lWordArray[lWordCount] = (lWordArray[lWordCount] | (sMessage
					.charCodeAt(lByteCount) << lBytePosition));
			lByteCount++;
		}
		lWordCount = (lByteCount - (lByteCount % 4)) / 4;
		lBytePosition = (lByteCount % 4) * 8;
		lWordArray[lWordCount] = lWordArray[lWordCount]
				| (0x80 << lBytePosition);
		lWordArray[lNumberOfWords - 2] = lMessageLength << 3;
		lWordArray[lNumberOfWords - 1] = lMessageLength >>> 29;
		return lWordArray;
	}

	function WordToHex(lValue) {
		var WordToHexValue = "", WordToHexValue_temp = "", lByte, lCount;
		for (lCount = 0; lCount <= 3; lCount++) {
			lByte = (lValue >>> (lCount * 8)) & 255;
			WordToHexValue_temp = "0" + lByte.toString(16);
			WordToHexValue = WordToHexValue
					+ WordToHexValue_temp.substr(
							WordToHexValue_temp.length - 2, 2);
		}
		return WordToHexValue;
	}
	var x = Array();
	var k, AA, BB, CC, DD, a, b, c, d;
	var S11 = 7, S12 = 12, S13 = 17, S14 = 22;
	var S21 = 5, S22 = 9, S23 = 14, S24 = 20;
	var S31 = 4, S32 = 11, S33 = 16, S34 = 23;
	var S41 = 6, S42 = 10, S43 = 15, S44 = 21;
	x = ConvertToWordArray(sMessage);
	a = 0x67452301;
	b = 0xEFCDAB89;
	c = 0x98BADCFE;
	d = 0x10325476;
	for (k = 0; k < x.length; k += 16) {
		AA = a;
		BB = b;
		CC = c;
		DD = d;
		a = FF(a, b, c, d, x[k + 0], S11, 0xD76AA478);
		d = FF(d, a, b, c, x[k + 1], S12, 0xE8C7B756);
		c = FF(c, d, a, b, x[k + 2], S13, 0x242070DB);
		b = FF(b, c, d, a, x[k + 3], S14, 0xC1BDCEEE);
		a = FF(a, b, c, d, x[k + 4], S11, 0xF57C0FAF);
		d = FF(d, a, b, c, x[k + 5], S12, 0x4787C62A);
		c = FF(c, d, a, b, x[k + 6], S13, 0xA8304613);
		b = FF(b, c, d, a, x[k + 7], S14, 0xFD469501);
		a = FF(a, b, c, d, x[k + 8], S11, 0x698098D8);
		d = FF(d, a, b, c, x[k + 9], S12, 0x8B44F7AF);
		c = FF(c, d, a, b, x[k + 10], S13, 0xFFFF5BB1);
		b = FF(b, c, d, a, x[k + 11], S14, 0x895CD7BE);
		a = FF(a, b, c, d, x[k + 12], S11, 0x6B901122);
		d = FF(d, a, b, c, x[k + 13], S12, 0xFD987193);
		c = FF(c, d, a, b, x[k + 14], S13, 0xA679438E);
		b = FF(b, c, d, a, x[k + 15], S14, 0x49B40821);
		a = GG(a, b, c, d, x[k + 1], S21, 0xF61E2562);
		d = GG(d, a, b, c, x[k + 6], S22, 0xC040B340);
		c = GG(c, d, a, b, x[k + 11], S23, 0x265E5A51);
		b = GG(b, c, d, a, x[k + 0], S24, 0xE9B6C7AA);
		a = GG(a, b, c, d, x[k + 5], S21, 0xD62F105D);
		d = GG(d, a, b, c, x[k + 10], S22, 0x2441453);
		c = GG(c, d, a, b, x[k + 15], S23, 0xD8A1E681);
		b = GG(b, c, d, a, x[k + 4], S24, 0xE7D3FBC8);
		a = GG(a, b, c, d, x[k + 9], S21, 0x21E1CDE6);
		d = GG(d, a, b, c, x[k + 14], S22, 0xC33707D6);
		c = GG(c, d, a, b, x[k + 3], S23, 0xF4D50D87);
		b = GG(b, c, d, a, x[k + 8], S24, 0x455A14ED);
		a = GG(a, b, c, d, x[k + 13], S21, 0xA9E3E905);
		d = GG(d, a, b, c, x[k + 2], S22, 0xFCEFA3F8);
		c = GG(c, d, a, b, x[k + 7], S23, 0x676F02D9);
		b = GG(b, c, d, a, x[k + 12], S24, 0x8D2A4C8A);
		a = HH(a, b, c, d, x[k + 5], S31, 0xFFFA3942);
		d = HH(d, a, b, c, x[k + 8], S32, 0x8771F681);
		c = HH(c, d, a, b, x[k + 11], S33, 0x6D9D6122);
		b = HH(b, c, d, a, x[k + 14], S34, 0xFDE5380C);
		a = HH(a, b, c, d, x[k + 1], S31, 0xA4BEEA44);
		d = HH(d, a, b, c, x[k + 4], S32, 0x4BDECFA9);
		c = HH(c, d, a, b, x[k + 7], S33, 0xF6BB4B60);
		b = HH(b, c, d, a, x[k + 10], S34, 0xBEBFBC70);
		a = HH(a, b, c, d, x[k + 13], S31, 0x289B7EC6);
		d = HH(d, a, b, c, x[k + 0], S32, 0xEAA127FA);
		c = HH(c, d, a, b, x[k + 3], S33, 0xD4EF3085);
		b = HH(b, c, d, a, x[k + 6], S34, 0x4881D05);
		a = HH(a, b, c, d, x[k + 9], S31, 0xD9D4D039);
		d = HH(d, a, b, c, x[k + 12], S32, 0xE6DB99E5);
		c = HH(c, d, a, b, x[k + 15], S33, 0x1FA27CF8);
		b = HH(b, c, d, a, x[k + 2], S34, 0xC4AC5665);
		a = II(a, b, c, d, x[k + 0], S41, 0xF4292244);
		d = II(d, a, b, c, x[k + 7], S42, 0x432AFF97);
		c = II(c, d, a, b, x[k + 14], S43, 0xAB9423A7);
		b = II(b, c, d, a, x[k + 5], S44, 0xFC93A039);
		a = II(a, b, c, d, x[k + 12], S41, 0x655B59C3);
		d = II(d, a, b, c, x[k + 3], S42, 0x8F0CCC92);
		c = II(c, d, a, b, x[k + 10], S43, 0xFFEFF47D);
		b = II(b, c, d, a, x[k + 1], S44, 0x85845DD1);
		a = II(a, b, c, d, x[k + 8], S41, 0x6FA87E4F);
		d = II(d, a, b, c, x[k + 15], S42, 0xFE2CE6E0);
		c = II(c, d, a, b, x[k + 6], S43, 0xA3014314);
		b = II(b, c, d, a, x[k + 13], S44, 0x4E0811A1);
		a = II(a, b, c, d, x[k + 4], S41, 0xF7537E82);
		d = II(d, a, b, c, x[k + 11], S42, 0xBD3AF235);
		c = II(c, d, a, b, x[k + 2], S43, 0x2AD7D2BB);
		b = II(b, c, d, a, x[k + 9], S44, 0xEB86D391);
		a = AddUnsigned(a, AA);
		b = AddUnsigned(b, BB);
		c = AddUnsigned(c, CC);
		d = AddUnsigned(d, DD);
	}
	var temp = WordToHex(a) + WordToHex(b) + WordToHex(c) + WordToHex(d);
	return temp.toLowerCase();
}

function removeHTMLTag(str) {
    str = str.replace(/<\/?[^>]*>/g,''); //去除HTML tag
    str = str.replace(/[ | ]*\n/g,'\n'); //去除行尾空白
    //str = str.replace(/\n[\s| | ]*\r/g,'\n'); //去除多余空行
    str=str.replace(/&nbsp;/ig,'');//去掉&nbsp;
    return str;
}

function removeHTMLTagWithoutImg(str){
	if(str.indexOf("<img ") != 0){
		str = removeHTMLTag(str);
	}
	return str;
}

//图片延迟加载js;
function lazyload(option) {
	var settings = {
	   defObj: null,
	   defHeight: 0
	};
	settings = $.extend(settings, option || {});
	//var defHeight = settings.defHeight, defObj = (typeof settings.defObj == "object") ? settings.defObj.find("img") : $(settings.defObj).find("img");
	var pageTop = function () {
	   return document.documentElement.clientHeight + Math.max(document.documentElement.scrollTop, document.body.scrollTop) - settings.defHeight;
	};
	var imgLoad = function () {
	   defObj.each(function () {
		   if ($(this).offset().top <= pageTop()) {
			   var src2 = $(this).attr("src2");
			   if (src2) {
				   $(this).attr("src", src2).removeAttr("src2");
			   }
		   }
	   });
	};
	imgLoad();
	$(window).bind("scroll", function () {
	   imgLoad();
	});
}

function filterNull(str){
	if(str == null){
		return "";
	}
	return str;
}

function filterZero(str){
	if(str == null || str == ""){
		return 0;
	}
	return str;
}

function limitWords(text,num){
	if(text.length >= num){
		return text.substring(0,num) + '  ...';
	}else{
		return text;
	}
}

function html_encode(str){
	if (typeof(str) != "string" || str.length == 0) return "";
	return str.replace(/&/g, '&amp;').replace(/\"/g, '&quot;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
}

function html_decode(str){
	if (typeof(str) != "string" || str.length == 0) return "";
	return str.replace(/&amp;/g, '&').replace(/&quot;/g, '\"').replace(/&lt;/g, '<').replace(/&gt;/g, '>');
}

function unParam(str){
	var rs = {};
	str.split('&').forEach(function(param){
		if(param.indexOf("[") > 0 && param.indexOf("[") < param.indexOf("=")){
			var keyFalse = param.substring(0,param.indexOf("="));
			var keyTrue = param.substring(0,param.indexOf("["));
			var val = param.substring(param.indexOf("=") + 1);
			dealParam(keyFalse,keyTrue,val,rs);
		}else{
			param = param.split('=');
			rs[param[0]] = param[1];	
		}
	});
	return rs;
}

function dealParam(str2,key,val,rs){
	var k = key;
	var t = rs;
	var a = str2.substring(str2.indexOf("[") + 1,str2.indexOf("]"));
	var r = str2.substring(str2.indexOf("]") + 1);
	if(a && !$.isNumeric(a)){
		if($.isArray(rs)){
			if(rs.length <= key){
				rs.push({});	
			}
			k = a;
			t = rs[key];
		}else{
			if(!rs[key]){
				rs[key] = {};	
			}
			k = a;
			t = rs[key];
		}
	}else{
		if($.isArray(rs)){
			if(!rs[key]){
				rs[key] = [];	
			}
			k = a;
			t = rs[key];
		}else{
			if(!rs[key]){
				rs[key] = [];
			}
			k = a;
			t = rs[key]; 
		}
	}
	if(r.indexOf("[") == 0){
		dealParam(r,k,val,t);
	}else{
		if(a && !$.isNumeric(a)){
			t[a] = val;
		}else{
			if(!a){
				t.push(val);
			}else{
				t[a] = val;	
			}
		}
	}
}

function deapMerge(a,b,arr){
	if($.isPlainObject(a)){
		for ( var k in a) {
			if(b[k]){
				deapMerge(a[k], b[k]);
			}else{
				arr.push(b);
			}
		}
	}else if($.isArray(a)){
		var len = a.length;
		for (var i = 0; i < len; i++) {
			for (var j = 0; j < b.length; j++) {
				if(($.isPlainObject(a[i]) && $.isPlainObject(b[j]))||($.isArray(a[i]) && $.isArray(b[j]))){
					deapMerge(a[i], b[j], a);	
				}else{
					a.push(b[j]);
				}
			}
		}
	}else{
		$.merge(a, b); 
	}
}

function cutstr(str,length){
	if(str == null || '') return;
	return str.length > length?(str.substring(0,length)+"..."):str;
}

function base64_encode(str){
    var c1, c2, c3;
    var base64EncodeChars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/";                
    var i = 0, len= str.length, string = '';
    while (i < len){
            c1 = str.charCodeAt(i++) & 0xff;
            if (i == len){
                    string += base64EncodeChars.charAt(c1 >> 2);
                    string += base64EncodeChars.charAt((c1 & 0x3) << 4);
                    string += "==";
                    break;
            }
            c2 = str.charCodeAt(i++);
            if (i == len){
                    string += base64EncodeChars.charAt(c1 >> 2);
                    string += base64EncodeChars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
                    string += base64EncodeChars.charAt((c2 & 0xF) << 2);
                    string += "=";
                    break;
            }
            c3 = str.charCodeAt(i++);
            string += base64EncodeChars.charAt(c1 >> 2);
            string += base64EncodeChars.charAt(((c1 & 0x3) << 4) | ((c2 & 0xF0) >> 4));
            string += base64EncodeChars.charAt(((c2 & 0xF) << 2) | ((c3 & 0xC0) >> 6));
            string += base64EncodeChars.charAt(c3 & 0x3F)
    }
    return string
}

function base64_decode(str){
    var c1, c2, c3, c4;
    var base64DecodeChars = new Array(
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1, -1, -1, 62, -1, -1, -1, 63, 52, 53, 54, 55, 56, 57,
            58, 59, 60, 61, -1, -1, -1, -1, -1, -1, -1, 0,  1,  2,  3,  4,  5,  6,
            7,  8,  9,  10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24,
            25, -1, -1, -1, -1, -1, -1, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36,
            37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, -1, -1, -1,
            -1, -1
    );
    var i=0, len = str.length, string = '';
    while (i < len){
            do{
                    c1 = base64DecodeChars[str.charCodeAt(i++) & 0xff]
            } while (
                    i < len && c1 == -1
            );

            if (c1 == -1) break;

            do{
                    c2 = base64DecodeChars[str.charCodeAt(i++) & 0xff]
            } while (
                    i < len && c2 == -1
            );

            if (c2 == -1) break;

            string += String.fromCharCode((c1 << 2) | ((c2 & 0x30) >> 4));

            do{
                    c3 = str.charCodeAt(i++) & 0xff;
                    if (c3 == 61)
                            return string;

                    c3 = base64DecodeChars[c3]
            } while (
                    i < len && c3 == -1
            );

            if (c3 == -1) break;

            string += String.fromCharCode(((c2 & 0XF) << 4) | ((c3 & 0x3C) >> 2));

            do{
                    c4 = str.charCodeAt(i++) & 0xff;
                    if (c4 == 61) return string;
                    c4 = base64DecodeChars[c4]
            } while (
                    i < len && c4 == -1
            );

            if (c4 == -1) break;

            string += String.fromCharCode(((c3 & 0x03) << 6) | c4)
    }
    return string;
}

function isImage(fileName){
    var sufi = fileName.substring(fileName.lastIndexOf('.')).toLowerCase();
    var flag = false;
    if(/\.(png|jpg|jpeg)$/.test(sufi)){
        flag = true;
    }
    return flag;
}

function getCurrentHtmlName(){
	var pn = window.location.pathname;
	var s1 = pn.lastIndexOf("/");
	var s2 = pn.lastIndexOf(".");
	return pn.substring(s1+1,s2);
}

function dealNull(obj){
    if(!obj)return;
	var o;
	if(obj.length){
		o = [];
		for (var i = 0; i < obj.length; i++) {
            var oob = dealObjectNull(obj[i]);
			o.push(oob);
		}
	}else{
        o = dealObjectNull(obj);
	}
	return o;
}

function dealObjectNull(obj){
    if(!obj)return;
    o = {};
    for(var k in obj){
        o[k] = obj[k] == null?"":obj[k];
    }
    return o;
}

function reload(){
    window.location.reload();
}

function setData(cfg){
    if(!cfg)return;
    var obj = cfg.selector;
    var data = cfg.data;
    var type = cfg.type;//0:表单，1:span
    if(type == 1){
        for(var k in data){
            $(obj).find("[name='"+k+"']").text(data[k]);
        }
    }else{
        var inputs = $(obj).find("input[name],select[name],textarea[name]");
        $.each(inputs,function(i,v){
			var input_type = $(v).attr("type");
            var name = data[$(v).attr("name")];
            if(input_type == "radio"){
                if(name == $(v).val()){
                    $(v).prop("checked",true);
                }else{
                    $(v).prop("checked",false);
                }
            }else if(input_type == "checkbox"){
                if(name){
                    var temp = name.split(/,|，/);
                    if($.inArray($(v).val(),temp) > -1){
                        $(v).prop("checked",true);
                    }else{
                        $(v).prop("checked",false);
                    }
                }else{
                    $(v).prop("checked",false);
                }
            }else if(input_type == "button"){

            }else{
                $(v).val(data[$(v).attr("name")]);
            }
        });
    }
}

function getData(select,that){
    var mdata = {};
    var inputs = $(that).closest(select).find("input[name],select[name],textarea[name]");
    $.each(inputs,function(i,v){
        var input_type = $(v).attr("type");
        if(input_type == "radio" && !v.checked){
        }else if(input_type  == "checkbox"){
            if(v.checked){
                if(!mdata[$(v).attr("name")]){
                    mdata[$(v).attr("name")] = [];
                }
                mdata[$(v).attr("name")].push($(v).val());
            }
        }else if(input_type == "buttton"){

        }else{
            mdata[$(v).attr("name")] = $(v).val();
        }
    });
    return mdata;
}

function getDataChange(odata,ndata){
    var obj = {};
    for(var k in ndata){
        if(ndata[k] != odata[k]){
            obj[k] = ndata[k];
        }
    }
    return obj;
}

function goToMail(email){
    var hash = {
        'qq.com': 'http://mail.qq.com',
        'gmail.com': 'http://mail.google.com',
        'sina.com': 'http://mail.sina.com.cn',
        '163.com': 'http://mail.163.com',
        '126.com': 'http://mail.126.com',
        'yeah.net': 'http://www.yeah.net/',
        'sohu.com': 'http://mail.sohu.com/',
        'tom.com': 'http://mail.tom.com/',
        'sogou.com': 'http://mail.sogou.com/',
        '139.com': 'http://mail.10086.cn/',
        'hotmail.com': 'http://www.hotmail.com',
        'live.com': 'http://login.live.com/',
        'live.cn': 'http://login.live.cn/',
        'live.com.cn': 'http://login.live.com.cn',
        '189.com': 'http://webmail16.189.cn/webmail/',
        'yahoo.com.cn': 'http://mail.cn.yahoo.com/',
        'yahoo.cn': 'http://mail.cn.yahoo.com/',
        'eyou.com': 'http://www.eyou.com/',
        '21cn.com': 'http://mail.21cn.com/',
        '188.com': 'http://www.188.com/',
        'foxmail.com': 'http://www.foxmail.com',
        'outlook.com': 'http://www.outlook.com'
    }

    var _mail = email.split('@')[1];
	var mail = null;
    for (var j in hash){
        if(j == _mail){
			mail = hash[_mail];
            break;
        }
    }
    return mail;
}

function removeInArray(obj,arr) {
	if(arr.length){
		var pos = $.inArray(obj,arr);
		if(pos > - 1){
			arr.splice(pos,1);
		}
	}
}

function equals(that,obj){
	if(that == obj)
		return true;
	if(typeof(obj)=="undefined"||obj==null||typeof(obj)!="object")
		return false;
	var length = 0; var length1 = 0;
	for(var ele in that) {
		length++;
	}
	for(var ele in obj) {
		length1++;
	}
	if(length != length1)
		return false;
	if(obj.constructor==that.constructor){
		for(var ele in that){
			if(typeof(that[ele])=="object") {
				if(!that[ele].equals(obj[ele]))
					return false;
			}
			else if(typeof(that[ele])=="function"){
				if(!that[ele].toString().equals(obj[ele].toString()))
					return false;
			}
			else if(that[ele]!=obj[ele])
				return false;
		}
		return true;
	}
	return false;
}

$.extend({
	includePath: '',
	include: function(file)	{
		var files = typeof file == "string" ? [file] : file;
		for (var i = 0; i < files.length; i++){
			var name = files[i].replace(/^\s|\s$/g, "");
			var att = name.split('.');
			var ext = att[att.length - 1].toLowerCase();
			var isCSS = ext == "css";
			var tag = isCSS ? "link" : "script";
			var attr = isCSS ? " type='text/css' rel='stylesheet' " : " type='text/javascript' ";
			var link = (isCSS ? "href" : "src") + "='" + $.includePath + name + "'";
			if ($(tag + "[" + link + "]").length == 0) $("head").append("<" + tag + attr + link + "></" + tag + ">");
		}
	}
});

function getDomain(domain) {
	return domain.substring(domain.indexOf("."));
}

function isCellphone(){
	var userAgentInfo = navigator.userAgent;
	var Agents = new Array("Android", "iPhone", "SymbianOS", "Windows Phone", "iPad", "iPod");
	var flag = false;
	for (var v = 0; v < Agents.length; v++) {
		if (userAgentInfo.indexOf(Agents[v]) > 0) {
			flag = true;
			break;
		}
	}
	return flag;
}