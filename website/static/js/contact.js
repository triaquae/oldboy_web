﻿var mapObj, longititude = 116.291424,latitude = 40.149607116;

window.onload = function(){  
try{
    mapObj = new AMap.Map("center_position",{  
		center:new AMap.LngLat(longititude,latitude), 
		level:17,
    });   
	
	if(mapObj)
		openInfo();
}catch(ex){
	$("#center_position").html("<img src='/static/assets/map.png' >");
	console.log("mmap can not be loaded cu");
}
};  
function openInfo(){  
    var info = [];   
    info.push("<div><div><img style=\"float:left;\" src=\" http://webapi.amap.com/images/autonavi.png \"/></div> ");   
    info.push("<div style=\"padding:0px 0px 0px 4px;\"><b>老男孩培训</b>");    
    info.push("电话: 010-60747396 18911718229  18600338340");    
    info.push("地址:北京市昌平区沙河青年创业大厦15层</div></div>");    
        
    inforWindow = new AMap.InfoWindow({    
        content:info.join("<br/>")
    });   
    inforWindow.open(mapObj,new AMap.LngLat(longititude,latitude)); 

    AMap.event.addListener(inforWindow,'click',function(){
                window.open("http://www.amap.com");
    }); 
}  
