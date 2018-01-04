$(function(){	
	$("body").on("click",".chart-remove",function(){
		$(this).closest(".chart-item-placeholder").remove();
	});
	
	$("body").on("click",".chart-edit",function(){
		console.log('敬请期待');
	});
	
	$("body").on("mouseenter",".chart-edit,.chart-remove",function(){
		$(this).children().fadeIn(80);
	});
	
	$("body").on("mouseleave",".chart-edit,.chart-remove",function(){
		$(this).children().fadeOut(80);
	});
	
	$(".banner-arrow").on("click",function(){
		var scroll = $("#secondBlock").offset().top;
		$('html,body').animate({scrollTop:scroll},300);
	});
	
	$("body").on("mouseenter",".chart-item-opt",function(){
		$(this).closest(".chart-item").find(".chart-bg").addClass("on");
	});
	
	$("body").on("mouseleave",".chart-item",function(){
		$(this).find(".chart-bg").removeClass("on");
	});
	
	$(".select-box").click(function(event){
		$(this).toggleClass("on");
	});
	$(".select-content").on("click",".select-item",function(){
		$(this).closest(".select-box").find(".show-box").html($(this).html()).attr('data-chart', $(this).attr('data-chart'));
		changeChartType2(this);
	});
	$("body").on("mousedown","",function(event){
		if($(event.target).closest(".select-box").length == 0){
			$(".select-box").removeClass("on");
		}
	});
	initMap('专利热点分析',mapData["2015"]);
	initGrow("2011~2015国内专利授权状况");
	initIpc("国内有效发明专利状况");
	initTop10("创新企业分析");
	initCop("企业合作分析");

    createChart();
});

function createChart() {
    $('#createModalBtn').on('click', function () {

    	var closestRow = $('#lastRow');

    	var showBox = $('#show-box');

        var chartTitle = showBox.text();

        var chartSelect = showBox.attr('data-chart');
        console.log('===>' + chartSelect)

        var date = formatDateTime();

		var chartText = '\
			<div class="row">\
				<div class="col-lg-12 col-xs-12">\
					<div class="chart-item-placeholder">\
						<div class="chart-item chart-7">\
							<div class="chart-item-title">' + chartTitle + '</div>\
							<div class="chart-item-time">' + date + '</div>\
							<div class="chart-item-opt"></div>\
							<div class="chart-item-chart" style="height: 368.333px; -webkit-tap-highlight-color: transparent; user-select: none; position: relative; background-color: transparent;">\
								<div style="position: relative; overflow: hidden; width: 1105px; height: 368px;">\
									<canvas width="1726" height="575" data-zr-dom-id="zr_0" style="position: absolute; left: 0px; top: 0px; width: 1105px; height: 368px; user-select: none; -webkit-tap-highlight-color: rgba(0, 0, 0, 0);"></canvas>\
								</div>\
								<div style="display: none;"></div>\
							</div>\
							<div class="chart-bg">\
								<div class="chart-edit" data-toggle="modal" data-target="#createModal" data-backdrop="false">\
								<div class="chart-edit-on"></div>\
							</div>\
							<div class="chart-remove">\
								<div class="chart-remove-on"></div>\
							</div>\
						</div>\
					</div>\
				</div>\
			</div>\
		</div>';

        closestRow.before(chartText);

        showSelectChart(chartSelect, '.chart-7 .chart-item-chart');
	});
}

//选择准备好的图表
function showSelectChart(chartSelect, clazz) {
    switch (parseInt(chartSelect)) {
        case 1:
            initPatent1(clazz);
            break;
        case 2:
            initPatent2(clazz);
            break;
        case 3:
            initPatent3(clazz);
            break;
        case 4:
            initPatent4(clazz);
            break;
        case 5:
            initPatent5(clazz);
            break;
        case 6:
            initPatent6(clazz);
            break;
        case 7:
            initPatent7(clazz);
            break;
        case 8:
            initPatent8(clazz);
            break;
        default:
            console.log('不存在该类型');
    }
}

function changeChartType2(that){
	$(".form-opt").hide();
	$(".form-opt-"+$(that).attr("op")).show();
}

function changeChartType(that){
	$(".form-opt").hide();
	$(".form-opt-"+that.value).show();
}

function initGrow(title){
	var $obj = $('.chart-1 .chart-item-chart');
	var w = $obj.width();
	$obj.height(w);
	var chart = echarts.init($obj[0]);
	var labelRight = {normal: {label : {position: 'right'}}};
	var option = {
		    tooltip : {
		        trigger: 'axis'
		    },
		    toolbox: {
		        show : false,
		        feature : {
		            mark : {show: false},
		            dataView : {show: true, readOnly: false},
		            magicType: {show: true, type: ['line', 'bar']},
		            restore : {show: true},
		            saveAsImage : {show: false }
		        }
		    },
		    calculable : true,
		    legend: {
		        data:[' ',' ',' ']
		    },
		    xAxis : [
		        {
		            type : 'category',
		            data : ['2011','2012','2013','2014','2015']
		        }
		    ],
		    yAxis : [
		        {
		            type : 'value',
		            name : '年授权数量',
		            min: 0,
		            max:  300000,
		            interval:100000,
		            axisLabel : {
		                formatter: '{value}'
		            }
		        },
		        {
		            type : 'value',
		            name : '年授权增量',
		            min: 0,
		            max: 100,
		            interval: 25,
		            axisLabel : {
		                formatter: '{value} %'
		            }
		        }
		    ],
		    series : [

		        {
		            name:'年授权数量',
		            type:'bar',
		            data:[112347, 143847, 143535, 162680, 263436]
		        },
		        {
		            name:'年授权增量',
		            type:'line',
		            yAxisIndex: 1,
		            data:[40.8, 28, -0.2, 13.3, 61.9]
		        }
		    ]
		};
	
	chart.setOption(option);
}

function initTop10(title){
	var $obj = $('.chart-6 .chart-item-chart');
	var w = $obj.width();
	$obj.height(w);
	var chart = echarts.init($obj[0]);
	var labelRight = {normal: {label : {position: 'right'}}};
	var option = {
		    tooltip : {
		        trigger: 'axis'
		    },
		    grid: {
		        left: '3%',
		        right: '4%',
		        bottom: '3%',
		        containLabel: true
		    },
		    xAxis : [
		        {
		            type : 'value',
		            name : '年申请专利数量',
		            min: 0,
		            max:  55000,
		            interval:15000,
		            axisLabel : {
		                formatter: '{value}'
		            }
		        }
		    ],
		    yAxis : [
		        {
		            type : 'category',
		            show : true,
		            data : ['鸿富锦工业', '清华大学', '中国石油', '浙江大学', '松下', '鸿海精密工业', '三星', '中兴', '华为', '国家电网']
		        }
		    ],
		    series : [
		        {
		            name:'2015年',
		            type:'bar',
		            data:[18449,18517,20901,24612,27082,28893,29717,32924,37724,52614]
		        }
		    ]
		};
	chart.setOption(option);
}

function initMap(title, data){
	var $obj = $('.chart-3 .chart-item-chart');
	var w = $obj.width();
	$obj.height(w + 57);
	var max = 0;
	for (var i = 0; i < data.length; i++) {
		if(data[i].value > max){
			max = data[i].value;
		}
	}

	var mapChart = echarts.init($obj[0]);

    mapChart.showLoading();

    $.get('../js/data/geo_xian.json', function (locations) {

        mapChart.hideLoading();

        echarts.registerMap('xian', locations);

        var option = {
            tooltip : {
                trigger: 'item',
                show : true
            },
            visualMap: {
                min: 0,
                max: max,
                left: 'left',
                top: 'top',
                text:['高','低'],
                calculable : true
            },
            toolbox: {
                show: false,
                orient : 'vertical',
                left: 'right',
                top: 'center',
                feature : {
                    mark : {show: true},
                    dataView : {show: true, readOnly: false},
                    restore : {show: true},
                    saveAsImage : {show: true}
                }
            },
            series : [
                {
                    name: '科技资源',
                    type: 'map',
                    mapType: 'xian',
                    roam: true,
					zoom: 1,
                    itemStyle:{
                        normal:{label:{show:true}},
                        emphasis:{label:{show:true}}
                    },
                    data: data
                }
            ]
        };

        mapChart.setOption(option);
    });
}

function initIpc(title){
	var $obj = $('.chart-2 .chart-item-chart');
	var w = $obj.width();
	$obj.height(w / 3);
	var mapChart = echarts.init($obj[0]);
	var option = {
		    tooltip : {
		        trigger: 'axis',
		        axisPointer : {            // 坐标轴指示器，坐标轴触发有效
		            type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
		        }
		    },
		    legend: {
		    	data:['申请', '授权','有效']
		    },
		    grid: {
		        left: '3%',
		        right: '4%',
		        bottom: '3%',
		        containLabel: true
		    },
		    xAxis : [
		     
		         {
		            type : 'category',
		            data : ['人类生活必需要','作业、运输','化学、冶金','纺织、造纸','固定建筑物','机械工程','物理','电学']
		        }
		    ],
		    yAxis : [
		        {
		        	min: 0,
			        max:  600000,
			        interval:200000,
					type : 'value'
		        }
		    ],
		    series : [
		             
		        {
		            name:'申请',
		            type:'bar',
		            stack: '总量',
		            itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
		            data:[221642, 205149, 183652, 17837, 43855, 91632, 188623, 160035]
		        },
		        {
		            name:'授权',
		            type:'bar',
		            stack: '总量',
		            itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
		            data:[43825, 68797, 65154, 6350, 15623,30046,62144,67377]
		        },
		        {
		            name:'有效',
		            type:'bar',
		            stack: '总量',
		            itemStyle : { normal: {label : {show: false, position: 'insideRight'}}},
		            data:[177729,225668, 276148, 27082, 45684, 107134,274292, 338637]
		        }
		       
		    ]
		};
	mapChart.setOption(option);
}

function initCreative(title){
	var $obj = $('.chart-4 .chart-item-chart');
	var w = $obj.width();
	$obj.height(w);
	var mapChart = echarts.init($obj[0]);
	var option = {
		    title : {
		        text: title
		    },
		    tooltip : {
		        trigger: 'axis'
		    },
		    legend: {
		        data:['2011年', '2012年']
		    },
		    grid: {
		        left: '3%',
		        right: '4%',
		        bottom: '3%',
		        containLabel: true
		    },
		    xAxis : [
		        {
		            type : 'value',
		            boundaryGap : [0, 0.01]
		        }
		    ],
		    yAxis : [
		        {
		            type : 'category',
		            data : ['巴西','印尼','美国','印度','中国','世界人口(万)']
		        }
		    ],
		    series : [
		        {
		            name:'2011年',
		            type:'bar',
		            data:[18203, 23489, 29034, 104970, 131744, 630230]
		        },
		        {
		            name:'2012年',
		            type:'bar',
		            data:[19325, 23438, 31000, 121594, 134141, 681807]
		        }
		    ]
		};
	mapChart.setOption(option);
}

function initCop(title){
	var $obj = $('.chart-5 .chart-item-chart');
	var w = $obj.width();
	$obj.height(w /2 -45);
	var data = {"attributeList":[{"classId":1,"id":1,"name":"公司"}],"entityList":[{"classId":1,"id":2,"name":"中兴通讯股份有限公司","radius":50},{"classId":1,"id":11065320,"name":"中国移动通信集团重庆有限公司","radius":25},{"classId":1,"id":24741261,"name":"深圳市瑞光电子自动化技术有限公司","radius":25},{"classId":1,"id":14590669,"name":"珠海市润星泰电器有限公司","radius":25},{"classId":1,"id":10007119,"name":"中国移动通信集团江苏有限公司","radius":25},{"classId":1,"id":10004943,"name":"中国科学技术大学","radius":25},{"classId":1,"id":10462815,"name":"中兴通讯美国公司","radius":25},{"classId":1,"id":11305552,"name":"东方有线网络有限公司","radius":25},{"classId":1,"id":14690946,"name":"中兴新能源汽车有限责任公司","radius":25},{"classId":1,"id":10010894,"name":"中国科学院声学研究所","radius":25},{"classId":1,"id":10637359,"name":"南京中兴软件有限责任公司","radius":25},{"classId":1,"id":10310484,"name":"中国移动通信集团广西有限公司","radius":25},{"classId":1,"id":3,"name":"华为技术有限公司","radius":50},{"classId":1,"id":12012687,"name":"安费诺商用电子产品(成都)有限公司","radius":25},{"classId":1,"id":10347309,"name":"光红建圣股份有限公司","radius":25},{"classId":1,"id":10009649,"name":"暨南大学","radius":25},{"classId":1,"id":10037722,"name":"北京大学深圳研究生院","radius":25},{"classId":1,"id":10006065,"name":"菲尼克斯电气（南京）研发工程中心有限公司","radius":25},{"classId":1,"id":10006064,"name":"菲尼克斯亚太电气(南京)有限公司","radius":25},{"classId":1,"id":10004943,"name":"中国科学技术大学","radius":25},{"classId":1,"id":10019852,"name":"中国科学院苏州纳米技术与纳米仿生研究所","radius":25},{"classId":1,"id":10073504,"name":"重庆邮电大学","radius":25},{"classId":1,"id":13772151,"name":"德国福朗霍夫研究所","radius":25},{"classId":1,"id":10075455,"name":"中国移动通信集团安徽有限公司","radius":25},{"classId":1,"id":4,"name":"海尔集团公司","radius":50},{"classId":1,"id":10255487,"name":"合肥海尔电冰箱有限公司","radius":25},{"classId":1,"id":19304540,"name":"佛山市顺德海尔电器有限公司","radius":25},{"classId":1,"id":11038942,"name":"青岛海尔卫浴设施有限公司","radius":25},{"classId":1,"id":20645839,"name":"青岛乐家电器有限公司","radius":25},{"classId":1,"id":10027575,"name":"青岛经济技术开发区海尔热水器有限公司","radius":25},{"classId":1,"id":13704232,"name":"三菱重工海尔(青岛)空调机有限公司","radius":25},{"classId":1,"id":25499559,"name":"青岛海尔空调有限总公司","radius":25},{"classId":1,"id":10978691,"name":"青岛海日高科模型有限公司","radius":25},{"classId":1,"id":10839878,"name":"青岛海尔特种电冰箱有限公司","radius":25},{"classId":1,"id":25357446,"name":"中国华北电力集团公司","radius":25},{"classId":1,"id":17610471,"name":"纳讯（青岛）通信有限公司","radius":25},{"classId":1,"id":5,"name":"百度在线网络技术（北京）有限公司","radius":50},{"classId":1,"id":10002068,"name":"清华大学","radius":25},{"classId":1,"id":10010793,"name":"南开大学","radius":25},{"classId":1,"id":6,"name":"腾讯科技（深圳）有限公司","radius":50},{"classId":1,"id":10020526,"name":"深圳大学","radius":25},{"classId":1,"id":10037722,"name":"北京大学深圳研究生院","radius":25},{"classId":1,"id":10037035,"name":"华北科技学院","radius":25},{"classId":1,"id":10501528,"name":"四川工程职业技术学院","radius":25},{"classId":1,"id":10003926,"name":"中国科学院深圳先进技术研究院","radius":25},{"classId":1,"id":10073504,"name":"重庆邮电大学","radius":25},{"classId":1,"id":10001219,"name":"北京大学","radius":25},{"classId":1,"id":10002068,"name":"清华大学","radius":25},{"classId":1,"id":10027645,"name":"中国石油大学（华东）","radius":25},{"classId":1,"id":10005369,"name":"西安交通大学","radius":25},{"classId":1,"id":10000826,"name":"上海交通大学","radius":25},{"classId":1,"id":7,"name":"阿里巴巴集团控股有限公司","radius":50}],"relationList":[{"attId":1,"fromId":2,"id":"3eaaade7183546f28bac96f12fcaf6ff","toId":11065320},{"attId":1,"fromId":2,"id":"7a67a2098be74b9d803832f586744385","toId":24741261},{"attId":1,"fromId":2,"id":"d2f3079400814756b87fbf1151829c04","toId":14590669},{"attId":1,"fromId":2,"id":"a5d73a90e2654088bb17b538e6a0426e","toId":10007119},{"attId":1,"fromId":2,"id":"d6165578d46a4aa49ded1b77b10c4004","toId":10004943},{"attId":1,"fromId":2,"id":"2340db63525f45c297663e8372c627d3","toId":10462815},{"attId":1,"fromId":2,"id":"47330d90e5eb4a7fa18378857ad7162f","toId":11305552},{"attId":1,"fromId":2,"id":"3fb4bf2ecf154357a42f79e6bb73f2b7","toId":14690946},{"attId":1,"fromId":2,"id":"b7bfdf17b3e94320a380ff16f4175a30","toId":10010894},{"attId":1,"fromId":2,"id":"fed63e9dec2240208047b5198b82e65b","toId":10637359},{"attId":1,"fromId":2,"id":"1912f92952d54aaaa03a37bde7548a71","toId":10310484},{"attId":1,"fromId":3,"id":"4dffddf73c594988b6a4dee3ce3087ab","toId":12012687},{"attId":1,"fromId":3,"id":"bb90200af5d44e879baa20fa17c4fdb7","toId":10347309},{"attId":1,"fromId":3,"id":"8f1481dfd0a84f3dac16ce1469463c21","toId":10009649},{"attId":1,"fromId":3,"id":"e1239404437b449294e2b64df2ff0227","toId":10037722},{"attId":1,"fromId":3,"id":"41636ccc75004c9f9c3d4d37ef7a353f","toId":10006065},{"attId":1,"fromId":3,"id":"298b40b160be48afb0d255cd0f051d9c","toId":10006064},{"attId":1,"fromId":3,"id":"07d6f93b981849f19acb19a2db63f922","toId":10004943},{"attId":1,"fromId":3,"id":"7a3ba43ef7054b14a2db3c2ad07e307e","toId":10019852},{"attId":1,"fromId":3,"id":"c4e845b98b424e318f04634114e8fa0e","toId":10073504},{"attId":1,"fromId":3,"id":"ecff2b4658bf42d38d63600afcaa0684","toId":13772151},{"attId":1,"fromId":3,"id":"5599cd00eba7460a91b06ffbacff25c0","toId":10075455},{"attId":1,"fromId":4,"id":"f443f15244f542af83c2af124e538556","toId":10255487},{"attId":1,"fromId":4,"id":"ab8becb6fa734ffabc692062c98670a2","toId":19304540},{"attId":1,"fromId":4,"id":"1db66730892b460bae00901fce28380c","toId":11038942},{"attId":1,"fromId":4,"id":"41836ab187b747208e938b20d02ea4d2","toId":20645839},{"attId":1,"fromId":4,"id":"ca501895f9554624b5b83fe32a531eaa","toId":10027575},{"attId":1,"fromId":4,"id":"0e59740f79d24f40aff728e331e9390e","toId":13704232},{"attId":1,"fromId":4,"id":"75e932a889124d82ac26aa923cdd2a43","toId":25499559},{"attId":1,"fromId":4,"id":"169d14871891496099bc8374e91fbf3b","toId":10978691},{"attId":1,"fromId":4,"id":"9a9a3179abc1429a94bbad1022bd111a","toId":10839878},{"attId":1,"fromId":4,"id":"dad4072318a2407d8180feafd830ddda","toId":25357446},{"attId":1,"fromId":4,"id":"3ac2cb4eef3c40168c7e91a823f554ca","toId":17610471},{"attId":1,"fromId":5,"id":"67b0659b0b9e4bc69c7f93c26e7db263","toId":10002068},{"attId":1,"fromId":5,"id":"ac57c9f0d1e2443b8a5bf86935eadeac","toId":10010793},{"attId":1,"fromId":6,"id":"cb4509db61284405a0c1920aaa2a932e","toId":10020526},{"attId":1,"fromId":6,"id":"15bb9397b96048feb5c5bcf17f27ddf6","toId":10037722},{"attId":1,"fromId":6,"id":"3e9ac68298cf4097b97775888451359f","toId":10037035},{"attId":1,"fromId":6,"id":"e88b80570cfa4f4590b80f7e2c5bb362","toId":10501528},{"attId":1,"fromId":6,"id":"813a0d320766490281fb286558c6cf12","toId":10003926},{"attId":1,"fromId":6,"id":"15ea837ae08a45f886aac954f0a0f3de","toId":10073504},{"attId":1,"fromId":6,"id":"cc1523fab6c1435095028ae58118176b","toId":10001219},{"attId":1,"fromId":6,"id":"a131d3ad1b6b4dd88a47677e5e92f057","toId":10002068},{"attId":1,"fromId":6,"id":"082ce5e0d0ef458d91403b5472cb7fa2","toId":10027645},{"attId":1,"fromId":6,"id":"70e9466f0d8d4904aa6dc2feae98dc37","toId":10005369},{"attId":1,"fromId":6,"id":"aee2e81623b5466791e5f39b14c2beb8","toId":10000826}]};
	var relation = dataChanger(data);
	draw_graph_basic(data.entityList,relation,true);	
}

var mapData = {
		"2011":[
			{name: '北京',value: 15880},
			{name: '天津',value: 2528},
			{name: '上海',value: 9160},
			{name: '重庆',value: 1865},
			{name: '河北',value: 1469},
			{name: '河南',value: 2462},
			{name: '云南',value: 1006},
			{name: '辽宁',value: 3164},
			{name: '黑龙江',value: 1953},
			{name: '湖南',value: 2606},
			{name: '安徽',value: 2026},
			{name: '山东',value: 5856},
			{name: '新疆',value: 302},
			{name: '江苏',value: 11043},
			{name: '浙江',value: 9135},
			{name: '江西',value: 679},
			{name: '湖北',value: 3160},
			{name: '广西',value: 634},
			{name: '甘肃',value: 552},
			{name: '山西',value: 1114},
			{name: '内蒙古',value: 364},
			{name: '陕西',value: 3139},
			{name: '吉林',value: 1202},
			{name: '福建',value: 1945},
			{name: '贵州',value: 596},
			{name: '广东',value: 18242},
			{name: '青海',value: 70},
			{name: '西藏',value: 27},
			{name: '四川',value: 3270},
			{name: '宁夏',value: 103},
			{name: '海南',value: 272},
			{name: '台湾',value: 6154},
			{name: '香港',value: 360},
			{name: '澳门',value: 9}
		],
		"2012":[
			 {name: '北京',value: 20140},
			 {name: '天津',value: 3326},
			 {name: '上海',value: 11379},
			 {name: '重庆',value: 2426},
			 {name: '河北',value: 1933},
			 {name: '河南',value: 3182},
			 {name: '云南',value: 1301},
			 {name: '辽宁',value: 3973},
			 {name: '黑龙江',value: 2418},
			 {name: '湖南',value: 3353},
			 {name: '安徽',value: 3066},
			 {name: '山东',value: 7453},
			 {name: '新疆',value: 456},
			 {name: '江苏',value: 16242},
			 {name: '浙江',value: 11571},
			 {name: '江西',value: 893},
			 {name: '湖北',value: 4050},
			 {name: '广西',value: 1297},
			 {name: '甘肃',value: 704},
			 {name: '山西',value: 1297},
			 {name: '内蒙古',value: 569},
			 {name: '陕西',value: 4018},
			 {name: '吉林',value: 1583},
			 {name: '福建',value: 2977},
			 {name: '贵州',value: 635},
			 {name: '广东',value: 22153},
			 {name: '青海',value: 101},
			 {name: '西藏',value: 57},
			 {name: '四川',value: 4460},
			 {name: '宁夏',value: 140},
			 {name: '海南',value: 396},
			 {name: '台湾',value: 6211},
			 {name: '香港',value: 476},
			 {name: '澳门',value: 7}
		 ],
		"2013":[
			 {name: '北京',value: 20695},
			 {name: '天津',value: 3141},
			 {name: '上海',value: 10644},
			 {name: '重庆',value: 2360},
			 {name: '河北',value: 2008},
			 {name: '河南',value: 3173},
			 {name: '云南',value: 1312},
			 {name: '辽宁',value: 3830},
			 {name: '黑龙江',value: 2238},
			 {name: '湖南',value: 3613},
			 {name: '安徽',value: 4241},
			 {name: '山东',value: 8913},
			 {name: '新疆',value: 540},
			 {name: '江苏',value: 16790},
			 {name: '浙江',value: 11139},
			 {name: '江西',value: 923},
			 {name: '湖北',value: 4052},
			 {name: '广西',value: 1295},
			 {name: '甘肃',value: 785},
			 {name: '山西',value: 1332},
			 {name: '内蒙古',value: 549},
			 {name: '陕西',value: 4133},
			 {name: '吉林',value: 1496},
			 {name: '福建',value: 2941},
			 {name: '贵州',value: 776},
			 {name: '广东',value: 20084},
			 {name: '青海',value: 91},
			 {name: '西藏',value: 44},
			 {name: '四川',value: 4566},
			 {name: '宁夏',value: 184},
			 {name: '海南',value: 449},
			 {name: '台湾',value: 4806},
			 {name: '香港',value: 374},
			 {name: '澳门',value: 18}
		 ],
		"2014":[
			 {name: '北京',value: 23237},
			 {name: '天津',value: 3279},
			 {name: '上海',value: 11614},
			 {name: '重庆',value: 2321},
			 {name: '河北',value: 2286},
			 {name: '河南',value: 3493},
			 {name: '云南',value: 1423},
			 {name: '辽宁',value: 3975},
			 {name: '黑龙江',value: 2454},
			 {name: '湖南',value: 4160},
			 {name: '安徽',value: 5184},
			 {name: '山东',value: 10538},
			 {name: '新疆',value: 605},
			 {name: '江苏',value: 19671},
			 {name: '浙江',value: 13372},
			 {name: '江西',value: 1033},
			 {name: '湖北',value: 4855},
			 {name: '广西',value: 1933},
			 {name: '甘肃',value: 812},
			 {name: '山西',value: 1559},
			 {name: '内蒙古',value: 458},
			 {name: '陕西',value: 4885},
			 {name: '吉林',value: 1434},
			 {name: '福建',value: 3426},
			 {name: '贵州',value: 1047},
			 {name: '广东',value: 22276},
			 {name: '青海',value: 110},
			 {name: '西藏',value: 50},
			 {name: '四川',value: 5682},
			 {name: '宁夏',value: 243},
			 {name: '海南',value: 380},
			 {name: '台湾',value: 4405},
			 {name: '香港',value: 466},
			 {name: '澳门',value: 14}
		],
		"2015":[
			 {name: '灞桥',value: 35308},
			 {name: '碑林',value: 4624},
			 {name: '长安',value: 17601},
			 {name: '高陵',value: 3964},
			 {name: '户县',value: 3840},
			 {name: '蓝田',value: 5384},
			 {name: '莲湖',value: 2079},
			 {name: '临潼',value: 6569},
			 {name: '未央',value: 4024},
			 {name: '新城',value: 6776},
			 {name: '阎良',value: 11180},
			 {name: '雁塔',value: 16881},
			 {name: '周至',value: 950}
		 ]};

function reloadMap(that){
	var y = $(that).text();
	$(that).addClass("on").siblings().removeClass("on");
	initMap("", mapData[y]);
}

//2016年西安市（区）专利申请量
function  initPatent1(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['专利申请量']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            min: 0,
            max: 25000,
            interval: 5000,
            boundaryGap: [0, 0.01],
            data: ['申请量']
        },
        yAxis: {
            type: 'category',
            data: ['其他区','西安经开','西安高新']
        },
        series: [
            {
                "name": "申请量",
                "type": "bar",
                "stack": "分布" ,
                "data": [17976,6213,21228]
            }


        ]
    };

    mapChart.setOption(option);
}

//2016年西安市（区）专利申请人类型构成
function initPatent2(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['申请人类型构成']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            min: 0,
            max: 20000,
            interval: 2000,
            boundaryGap: [0, 0.01],
            data: ['西安高新','西安经开','其他区']
        },
        yAxis: {
            type: 'category',
            data: ['机关团体','企业','科研机构','高等学校','个人'],
            axisLabel: {
                interval: 0
            },
        },
        series: [
            {   "barWidth": 50,
                "name": "西安高新",
                "type": "bar",
                "stack": "分布" ,
                "data": [17,8932,1370,5629,5284]
            },
            {
                "name": "西安经开",
                "type": "bar",
                "stack": "分布" ,
                "data": [13,3949,153,1684,420]
            },
            {
                "name": "其他区",
                "type": "bar",
                "stack": "分布",
                "data": [585,5058,1303,7909,3121]
            }

        ]
    };

    mapChart.setOption(option);
}

//2016年西安市（区）专利授权类型构成
function  initPatent3(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['专利授权类型构成']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            min: 0,
            max: 20000,
            interval: 2000,
            boundaryGap: [0, 0.01],
            data: ['西安高新','西安经开','其他区']
        },
        yAxis: {
            type: 'category',
            data: ['外观设计','实用新型','发明']
        },
        series: [
            {
                "name": "西安高新",
                "type": "bar",
                "stack": "分布" ,
                "data": [16843,4344,3569]
            },
            {
                "name": "西安经开",
                "type": "bar",
                "stack": "分布" ,
                "data": [319,1949,943]
            },
            {
                "name": "其他区",
                "type": "bar",
                "stack": "分布",
                "data": [1982,5742,2053]
            }

        ]
    };

    mapChart.setOption(option);
}

//2016年西安市（区）专利授权量
function initPatent4(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['专利授权量']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            min: 0,
            max: 30000,
            interval: 5000,
            boundaryGap: [0, 0.01],
            data: ['授权量']
        },
        yAxis: {
            type: 'category',
            data: ['其他区','西安经开','西安高新']
        },
        series: [
            {
                "name": "授权量",
                "type": "bar",
                "data": [9777,3211,24756]
            }


        ]
    };

    mapChart.setOption(option);
}

//2016年西安市（区）专利授权人类型构成
function initPatent5(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['授权人类型构成']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            min: 0,
            max: 20000,
            interval: 2000,
            boundaryGap: [0, 0.01],
            data: ['西安高新','西安经开','其他区']
        },
        yAxis: {
            type: 'category',
            data: ['机关团体','企业','科研机构','高等学校','个人']
        },
        series: [
            {
                "name": "西安高新",
                "type": "bar",
                "stack": "分布" ,
                "data": [150,5700,500,3000,15700]
            },
            {
                "name": "西安经开",
                "type": "bar",
                "stack": "分布" ,
                "data": [13,2000,80,800,250,420]
            },
            {
                "name": "其他区",
                "type": "bar",
                "stack": "分布",
                "data": [150,2250,500,5000,2000]
            }

        ]
    };

    mapChart.setOption(option);
}

//2016年西安市（区）专利申请类型构成
function initPatent6(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: 'axis',
            axisPointer: {
                type: 'shadow'
            }
        },
        legend: {
            data: ['专利申请类型构成']
        },
        grid: {
            left: '3%',
            right: '4%',
            bottom: '3%',
            containLabel: true
        },
        xAxis: {
            type: 'value',
            min: 0,
            max: 20000,
            interval: 2000,
            boundaryGap: [0, 0.01],
            data: ['西安高新','西安经开','其他区']
        },
        yAxis: {
            type: 'category',
            data: ['外观设计','实用新型','发明']
        },
        series: [
            {
                "name": "西安高新",
                "type": "bar",
                "stack": "分布" ,
                "data": [6591,5010,9627]
            },
            {
                "name": "西安经开",
                "type": "bar",
                "stack": "分布" ,
                "data": [478,3443,2292]
            },
            {
                "name": "其他区",
                "type": "bar",
                "stack": "分布",
                "data": [1979,9634,6363]
            }

        ]
    };

    mapChart.setOption(option);
}

//西安市雁塔区11-15年输出吸纳情况
function initPatent7(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

	var option = {
		tooltip: {
			trigger: "axis"
		},
		toolbox: {
			feature: {
				dataView: {show: !0, readOnly: !1},
				magicType: {show: !0, type: ["line", "bar"]},
				restore: {show: !0},
				saveAsImage: {show: !0}
			}
		},
		legend: {
			data: ["输出金额", "吸纳金额", "输出项", "吸纳项"]
		},
		xAxis: [
            {
                type: "category",
                data: [2011, 2012, 2013, 2014,2015]
            }
        ],
		yAxis: [
            {
                type: "value",
                name: "亿元",
                min: 0,
                max: 350,
                interval: 50,
                axisLabel: {
                    formatter: "{value}"
                }
            },
            {
                type: "value",
                name: "项",
                min: 0,
                max: 7000,
                interval: 1000,
                axisLabel: {
                    formatter: "{value}"
                }
            }
        ],
		series: [
            {
                name: "输出金额",
                type: "bar",
                data: [60, 20, 30, 10, 210]
            },
            {
                name: "吸纳金额",
                type: "bar",
                data:[10, 130, 110, 140, 20]
            },
            {
                name: "输出项",
                type: "line",
                yAxisIndex: 1,
                data: [3300, 5900, 1000, 4000, 5800]
            },
            {
                name: "吸纳项",
                type: "line",
                yAxisIndex: 1,
                data: [600, 1200, 2400, 1100, 900]
            }
        ]
	};

    mapChart.setOption(option);
}

//2016年西安市技术合同技术领域成交构成
function initPatent8(clazz) {
    var $obj = $(clazz);
    var w = $obj.width();
    $obj.height(w / 3);
    var mapChart = echarts.init($obj[0]);

    var option = {
        tooltip: {
            trigger: "axis"
        },
        toolbox: {
            feature: {
                dataView: {show: !0, readOnly: !1},
                magicType: {show: !0, type: ["line", "bar"]},
                restore: {show: !0},
                saveAsImage: {show: !0}
            }
        },
        legend: {
            data: ["2015年合同数", "2016年合同数", "2015年成交数", "2016年成交数"]
        },
        xAxis: [
            {
                type: "category",
                data: ["电子信息技术","航空航天技术","先进制造技术","生物、医药和医疗器械技术","新材料及其应用","新能源与高效节能","环境保护与资源综合利用技术","核应用技术","农业技术","现代交通","城市建设与社会发展"]
            }
        ],
        yAxis: [
            {
                type: "value",
                name: "亿元",
                min: 0,
                max: 350,
                interval: 50,
                axisLabel: {
                    formatter: "{value}"
                }
            },
            {
                type: "value",
                name: "份数",
                min: 0,
                max: 7000,
                interval: 1000,
                axisLabel: {
                    formatter: "{value}"
                }
            }
        ],
        series: [
            {
                name: "2015年合同数",
                type: "bar",
                label: {
                    normal: {
                        show: true,
                        formatter: "{b}: {c}"
                    }
                },
                data: [165, 65, 86, 23, 15, 120, 35, 7, 5, 140, 90]
            },
            {
                name: "2016年合同数",
                type: "bar",
                data:[170, 72, 74, 11, 8, 230, 22, 5, 4, 92, 130]
            },
            {
                name: "2015年成交数",
                type: "line",
                yAxisIndex: 1,
                data: [5300, 900, 1000, 400, 580, 1900, 700, 100, 100, 1000, 4800]
            },
            {
                name: "2016年成交数",
                type: "line",
                yAxisIndex: 1,
                data: [5400, 1100, 800, 400, 660, 1100, 500, 100, 110, 700, 4200]
            }
        ]
    };

    mapChart.setOption(option);
}