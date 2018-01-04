$(function () {
	if(isLogin(0)){
		if(getCurrentHtmlName() != 'home'){
			queryMySysInfo(1);
		}
	}
	$("body").on("click",".sweet-alert li",function () {
		$(this).addClass("on").siblings("li").removeClass("on");
		$(".sweet-alert").find(".min-login").find("div").eq($(this).index()).addClass("on").siblings("div").removeClass("on");
	});
	$("body").on("click",".sweet-alert i:eq(0)",function () {
		swal.close();
	});
});
function kgLoader(config){
	var defaults = {type:0,url:'',params:'',success:'',beforeSend:null,that:null,error:null,complete:null,dataFilter:null,processData:true,contentType:'application/x-www-form-urlencoded; charset=UTF-8'};
	var configs = $.extend({},defaults,config);
	var type = configs.type;
	var url = configs.url;
	var params = configs.params;
	var success = configs.success;
	var beforeSend = configs.beforeSend;
	var that = configs.that;
	var error = configs.error;
	var complete = configs.complete;
	var dataFilter = configs.dataFilter;
	var processData = configs.processData;
	var contentType = configs.contentType;

	if(params){
		for(var k in params){
			if(typeof params[k] == "object"){
				params[k] = JSON.stringify(params[k]);
			}
		}
	}
	return $.ajax({
		type: type == 0 ? "GET" : "POST",
		data:params,
		beforeSend:function () {
			if(beforeSend){beforeSend();}
			showAndHideLoading(that,true);
		},
		ifModified: true,
		crossDomain: true,
		statusCode: {404: function() {parent.swal('请求地址不存在');}},
		url: url,
		cache: false,
		timeout:60000,
		processData : processData,
		contentType : contentType,
		dataFilter :function(data, type){
			if(dataFilter){
				return dataFilter(data, type);
			}else{
				data = dealJsonCallback(data);
				data = JSON.stringify(data);
				return data;
			}
		},
		success : function(data,state,XHR){
			var sendData = decodeURIComponent(this.data);
			var jsonSendData = {};
			if(sendData){
				$.extend(jsonSendData,unParam(sendData));
			}
			sendData = "url="+this.url;
			if(sendData.indexOf('?') > -1 ){
				var pre = sendData.substring(0,sendData.indexOf('?'));
				sendData = sendData.substring(sendData.indexOf('?') + 1);
				$.extend(jsonSendData,unParam(pre),unParam(sendData));
			}
			if(success){
				success(data,state,XHR,jsonSendData);
			}
		},
		error:function(data,textStatus){
			if(textStatus == "timeout"){
				parent.swal("超时","与服务器连接超时，请稍后重试!","error");
			}else if(textStatus == "parsererror"){
				parent.swal("失败","数据解析错误!","error");
			}else if(textStatus == "error"){
				parent.swal("错误","网络错误，请重试!","error");
			}
			if(error){
				error();
			}
		},
		complete:function(data){
			showAndHideLoading(that,false);
			if(complete){
				complete(data);
			}
		}
	});

}

function showAndHideLoading(that,flag) {
	if(that){
		if(that.tagName == "INPUT" || that.tagName == "BUTTON"){
			$(that).prop("disabled",flag);
		}else if(that.tagName == "A"){

		}else{
			if(flag){
				$(that).showLoading();
			}else{
				$(that).hideLoading();
			}
		}
	}
}

function dealJsonCallback(data){
	if(data){
		if(typeof(data) == "string"){
			data = JSON.parse(data);
		}
		var code = data.code;
		if(code){
			code = parseInt(code)
			if(code == 200){
				if(!data || !data.data){
					return true;
				}
				return data.data;
			}else if(code == 301 || code == 421|| code == 422|| code == 423){
				parent.swal({title:"提示",text:"请重新登录",type:"warning"},goLogin);
				return false;
			}else if(code == 403){
				parent.swal({
					title:"提示",
					text:"用户已存在，但未激活，是否去激活？",
					type:"warning",
					showCancelButton: true,
					cancelButtonText:"放弃",
					confirmButtonText:"激活"
				},function () {
					var userId = data.data.rsData[0];
					sendEmail(userId,$(".all")[0]);
				});
				return false;
			}else{
				if($.inArray(code,configs.ERROR_CODE) > -1){
					parent.swal("提示",data.msg,"warning");
				}
				return false;
			}
		}else{
			return data;
		}
	}
}

function clearLoginStatus() {
	var ddomain = document.domain;
	var domain = getDomain(ddomain);
	$.removeCookie("kc_accessToken",{domain:domain==".kechuang.cn"?domain:ddomain});
	$.removeCookie("kc_userId",{domain:domain==".kechuang.cn"?domain:ddomain});
	$.removeCookie("login_user",{domain:domain==".kechuang.cn"?domain:ddomain});
	$.removeCookie("nickName",{domain:domain==".kechuang.cn"?domain:ddomain});
	$.removeCookie("userSig",{domain:domain==".kechuang.cn"?domain:ddomain});
	$.removeCookie("mark");
	$.removeCookie("token");
	$.removeCookie("_cusRole");
	$.removeCookie("homelink");
}

function goLogin(){
	clearLoginStatus();
	top.location.href = "login.html";
}

function setLoginStatus(data){
	var ddomain = document.domain;
	var domain = getDomain(ddomain);
	$.cookie("kc_userId",data.id,{expires:365,domain:domain==".kechuang.cn"?domain:ddomain});
	$.cookie("login_user",data.userName,{expires:365,domain:domain==".kechuang.cn"?domain:ddomain});
	$.cookie("nickName",data.nickName,{expires:365,domain:domain==".kechuang.cn"?domain:ddomain});
	$.cookie("kc_accessToken",data.accessToken,{expires:365,domain:domain==".kechuang.cn"?domain:ddomain});
	$.cookie("userSig",data.userSig,{expires:365,domain:domain==".kechuang.cn"?domain:ddomain});
	$.cookie("homelink","userinfo.html");
}

function linkTa(that){
	if(isLogin()){
		window.open("chat.html?id="+$(that).attr("uid")+"&_cname="+encodeURIComponent($(that).attr("nname")),"_blank");
	}
}

function isLogin(isShowLogin){
	if($.cookie("kc_accessToken")){
		return true;
	}else{
		if(isShowLogin==0){
			return false;
		}else{
			showLoginView();
		}
	}
}

function showLoginView(){
	parent.swal({
		title:'',
		text: "<iframe id='min-iframe' src='min-login.html' frameborder='0' scrolling='no' height='310' width='320'></iframe>",
		html:true,
		customClass:'min-login',
		animation:'slide-from-top',
		showConfirmButton:false
	});
	if(!$(".min-login").find("i").length){
		$(".min-login").prepend("<i class='fa fa-close fa-2x' style='position: absolute;top:3px;right: 7px; cursor: pointer;'></i>")
	}
}

function exit(){
	var params = setCommonParam();
	kgLoader({
		type:0,
		url: configs.RESTFUL_URL+"/user/logout?"+$.param(params),
		success:function(data,status,XHR,params) {
			if (data) {
				clearLoginStatus();
				top.location.href = "index.html";
			}
		}
	});
}


function setCommonParam(config){
	var param = {};
	param.userId = $.cookie("kc_userId");
	param.accessToken = $.cookie("kc_accessToken");
	param.tt = new Date().getTime();
	param.region = '310000';
	if(config){
		param.pageNo = config.pageNo;
		param.pageSize = config.pageSize;
	}
	return param;
}


function getMobileCode(mobile){
	var params = setCommonParam();
	params.mobile = mobile;
	kgLoader({
		type:0,
		url:configs.RESTFUL_URL+"/common/get/mcode?"+$.param(params),
		success: function(data,status,XHR,params) {
		}
	});
}

function getCheckCode(callback){
	var oReq = new XMLHttpRequest();
	if(getCurrentHtmlName() == "min-login"){
		oReq.open("GET", configs.RESTFUL_URL+"/common/get/captcha?width=80&height=30", true);
	}else{
		oReq.open("GET", configs.RESTFUL_URL+"/common/get/captcha", true);
	}
	oReq.responseType = "blob";
	oReq.onreadystatechange = function () {
		if (oReq.readyState == oReq.DONE) {
			var blob = oReq.response;
			var obj = {};
			obj.capatchaId = oReq.getResponseHeader("capatchaId");
			obj.imgSrc = URL.createObjectURL(blob);
			callback(obj.capatchaId,obj.imgSrc);
		}
	}
	oReq.send();
}


function showPage(selector,current,pageCount,callback) {
	if(current == 1){
		$(selector).createPage({
			pageCount:pageCount,
			current:parseInt(current),
			backFn:function(p){
				callback(p);
			}
		});
	}
}

/*
 * 系统消息提示
 */
function queryMySysInfo(page){
	var params = setCommonParam({pageNo:page,pageSize:1});
	params.isRead = 0;
	kgLoader({
		type:0,
		url: configs.RESTFUL_URL+"/user/query/msg/system?"+$.param(params),
		success:function(data,state,XHR,params) {
			if (data && data.rsData && data.rsData.length) {
				$(".reglog .msg-length").addClass("on");
				$(".reglog .msg-length",parent.document).addClass("on");
				// $(".list-set-read-btn").show();
			}
			queryMyPushMsg(1);
		}
	});
}
function queryMyPushMsg(page){
	var params = setCommonParam({pageNo:page,pageSize:1});
	params.isRead = 0;
	kgLoader({
		type:0,
		url:configs.RESTFUL_URL+"/user/query/msg/push?"+$.param(params),
		success:function(data,state,XHR,params){
			if(data && data.rsData && data.rsData.length){
				$(".head-mail .msg-length").addClass("on");
				$(".head-mail .msg-length",parent.document).addClass("on");
				// $(".list-set-read-btn").show();
			}
		}
	});
}

function uploadSuccess(selector) {	
	$(selector).hideLoading();
}

function submitAddvice(that){
	var t = $(that).closest(".advice-box").find("input").val();
	var c = $(that).closest(".advice-box").find("textarea").val();
	if($.trim(t) && $.trim(c)){
		var params = setCommonParam();
		var params2 = {};
		params2.bean = {title:t,content:c};
		kgLoader({
			type:1,
			url: configs.RESTFUL_URL+"/common/add/advice?"+$.param(params),
			params:params2, 
			success:function(data,state,XHR,params) {
				if (data) {
					closeThisSysDialog(that);
					parent.swal("提示","感谢你的建议，我们将尽快为您处理！","success");
				}
			}
		});
	}
}

function sendEmail(userId,that){
	var params = setCommonParam();
	params.userId = userId;
	kgLoader({
		type:0,
		that:that,
		url:configs.RESTFUL_URL+"/user/send/active/email?"+$.param(params),
		success: function(data,status,XHR,params) {
			if(data){
				swal("提示","邮件发送成功，请前往邮箱激活","success");
			}
		}
	});
}

function renderLocation(str){
	if(str){
		var arr = str.split(",");
		for (var i = 0; i < provinceList.length; i++) {
			if(provinceList[i].id == arr[0]){
				str = provinceList[i].province;
			}
		}
		for (var i = 0; i < cityList.length; i++) {
			if(cityList[i].id == arr[1]){
				str += " " + cityList[i].city;
			}
		}
	}
	return str;
}

function validateMobileCode(mobile,mCode,callback){
	if(!$.trim(mCode)){
		parent.swal("提示","手机校验码不能为空","warning");
		return;
	}
	var param = setCommonParam();
	param.mobile = mobile;
	param.code = mCode;
	kgLoader({
		type:0,
		url: configs.RESTFUL_URL+"/common/check/mcode?"+$.param(param),
		success:function(data,state,XHR,params) {
			if (data) {
				callback?callback(data.rsData[0]):'';
			}
		}
	});
}

function uploadFile(config) {
	var defaults = {selector:'',url:configs.UPLOAD_URL,auto:true,name:"fileData",submit:null,complete:null,that:null};
	var con = $.extend({},defaults,config);
	var that = con.that;
	var sub = con.submit;
	var complete = con.complete;
	$(con.selector).zinoUpload({
		method: "POST",
		url: con.url,
		name: con.name,
		autoSubmit:con.auto,
		label:"",
		submit:function (event, ui) {
			var file = ui.file[0].files[0];
			var size = file.size;
			if(size > 4*1024*1024){
				$(this).data("result", false);
				$(this).find(".zui-upload-file").val('');
				parent.swal("提示","上传文件过大，限制大小4MB","error");
			}else{
				that?$(that).showLoading({'indicatorZIndex': 99999,'overlayZIndex': 99999}):'';
				sub?sub(file):'';
			}
		},
		complete: function (event, ui) {
			var code = ui.response.code;
			if(code == 200){
				var data = ui.response.data.rsData[0];
				complete?complete(data,event):'';
			}else if(code == 301 || code == 421|| code == 422|| code == 423){
				parent.swal({title:"提示",text:"请重新登录",type:"warning"},goLogin);
			}
			$(this).find(".zui-upload-file").val('');
			that?$(that).hideLoading():'';
		}
	});
}