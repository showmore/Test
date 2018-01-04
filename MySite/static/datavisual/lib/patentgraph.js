window.isChart = false;

function dataChanger(data){
	if(data.attributeList){
		for (var i = 0; i < data.attributeList.length; i++) {
			data.attributeList[i].id = eidMapping(data.attributeList[i].id);
		}
	}
	if(data.entityList){
		for (var i = 0; i < data.entityList.length; i++) {
			data.entityList[i].classId = classIdMapping(data.entityList[i].classId);
		}	
	}
	if(data.relationList){
		for (var i = 0; i < data.relationList.length; i++) {
			data.relationList[i].attId = eidMapping(data.relationList[i].attId);
			data.relationList[i].fromType = classIdMapping(data.relationList[i].fromType);
			data.relationList[i].toType = classIdMapping(data.relationList[i].toType);
		}	
	}
	if(data.searchEntityList){
		//console.log("toMapping...");
	}
	if(data.relationList){
		var newData = new Array();
		for (var i = 0; i < data.relationList.length; i++) {
			var newDataObj = data.relationList[i];
			newDataObj.name = idToAttr(data.attributeList,newDataObj.attId,"name");
			newDataObj.from = newDataObj.fromId;
			newDataObj.fromName = idToAttr(data.entityList,newDataObj.fromId,"name");
			newDataObj.fromType = idToAttr(data.entityList,newDataObj.fromId,"classId");
			newDataObj.to = newDataObj.toId;
			newDataObj.toName = idToAttr(data.entityList,newDataObj.toId,"name");
			newDataObj.toType = idToAttr(data.entityList,newDataObj.toId,"classId");
			newDataObj.relation = newDataObj.name;
			newData.push(newDataObj);
		}
		return newData;
	}else{
		return data;
	}
	
	function idToAttr(list,id,attr){
		for (var j = 0; j < list.length; j++) {
			if(list[j].id == id){
				return list[j][attr];
			}
		}
		return "";
	}
}

function eidMapping(k){
	switch (parseInt(k)) {
	case 304:
		k = 101;
		break;
	case 305:
		k = 102;
		break;
	case 309:
		k = 103;
		break;
	case 308:
		k = 111;
		break;
	case 312:
		k = 112;
		break;
	case 313:
		k = 113;
		break;
	case 303:
		k = 114;
		break;
	case 315:
		k = 115;
		break;
	case 316:
		k = 116;
		break;
	case 306:
		k = 117;
		break;
	case 302:
		k = 118;
		break;
	case 319:
		k = 119;
		break;
	case 320:
		k = 120;
		break;
	case 321:
		k = 121;
		break;
	case 322:
		k = 122;
		break;
	case 323:
		k = 123;
		break;
	case 111:
		k = 832;
		break;
	case 158:
		k = 833;
		break;
	default:
		break;
	}
	return k;
}
function classIdMapping(k){
	switch (parseInt(k)) {
	case 3:
		k = 1;
		break;
	case 33:
		k = 2;
		break;
	case 30:
		k = 3;
		break;
	case 2:
		k = 4;
		break;
	case 1:
		k = 5;
		break;
	default:
		break;
	}
	return k;
}
