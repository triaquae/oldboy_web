var mapObj, longititude = 116.29137,latitude = 40.14976;

window.onload = function(){  
    mapObj = new AMap.Map("center_position",{  
		center:new AMap.LngLat(longititude,latitude), 
		level:14,
    });   
	
	AMap.event.addListener(mapObj,'click',function(){  
		window.open("http://www.amap.com");
    });
	if(mapObj)
		openInfo();
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
}  