function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function Send_Value_To_server (DeviceId,Value,Speed) {
	var siteurl   = window.location.href; 
		var url 	= "";
		var appid   = "0066";
		var type 	= 'POST';
      		data = {
			sDeviceId : DeviceId,
			sValue    : Value,
			sSpeed    : Speed,
			sAppID    : appid
	      	};
		
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,

	  		success: function(sAcconDetail) {
	  			var baseurl = document.getElementById("baseurl").value;
	  			var returnedData = JSON.parse(sAcconDetail);

	  			var acconfailtime     = returnedData.saccondetail.acconfailtime;
	  			acconfailtime = "CMD failed at: " . concat(acconfailtime)
	  			acconfailtime = acconfailtime . concat(" ago")

				var acconfailinfo     = returnedData.saccondetail.acconfailinfo;
				acconfailinfo = "CMD failed   :" . concat(acconfailinfo)

				var acconfailvalue    = returnedData.saccondetail.acconfailvalue;
				acconfailvalue = "CMD value: " . concat(acconfailvalue)

				var acconactiontime   = returnedData.saccondetail.acconactiontime;
				acconactiontime = "CMD taken at: " . concat(acconactiontime)
	  			acconactiontime = acconactiontime . concat(" ago")

				var acconactioninfo   = returnedData.saccondetail.acconactioninfo;
				acconactioninfo = "CMD taken  :" . concat(acconactioninfo)

				var acconactionvalue  = returnedData.saccondetail.acconactionvalue;
				acconactionvalue = "CMD value: " . concat(acconactionvalue)

				var acconsucesstime   = returnedData.saccondetail.acconsucesstime;
				acconsucesstime = "CMD status at: " . concat(acconsucesstime)
	  			acconsucesstime = acconsucesstime . concat(" ago")

				var acconsucessinfo   = returnedData.saccondetail.acconsucessinfo;
				acconsucessinfo = "CMD info :" . concat(acconsucessinfo)

				var acconsucessstatus = returnedData.saccondetail.acconsucessstatus;
				acconsucessstatus = "CMD status :" . concat(acconsucessstatus)

				var acconappliedtime     = returnedData.saccondetail.acconappliedtime;
	  			acconappliedtime = "CMD applied at: " . concat(acconappliedtime)
	  			acconappliedtime = acconappliedtime . concat(" ago")

				var acconappliedinfo     = returnedData.saccondetail.acconappliedinfo;
				acconappliedinfo = "CMD applied   :" . concat(acconappliedinfo)

				var acconappliedvalue    = returnedData.saccondetail.acconappliedvalue;
				
				acconappliedvalue = "CMD value: " . concat(acconappliedvalue)


				$('#acconfailtime').html(acconfailtime);
	  			$('#acconfailinfo').html(acconfailinfo);
	  			$('#acconfailvalue').html(acconfailvalue);

	  			$('#acconactiontime').html(acconactiontime);
	  			$('#acconactioninfo').html(acconactioninfo);
	  			$('#acconactionvalue').html(acconactionvalue);

	  			$('#acconsucesstime').html(acconsucesstime);
	  			$('#acconsucessinfo').html(acconsucessinfo);
	  			$('#acconsucessstatus').html(acconsucessstatus);

	  			$('#acconappliedtime').html(acconappliedtime);
	  			$('#acconappliedinfo').html(acconappliedinfo);
	  			$('#acconappliedvalue').html(acconappliedvalue);

	  			var currentvalue = returnedData.saccondetail.devicecurrentvalue;
	  			if (currentvalue == 0){
	  				var img = returnedData.saccondetail.deviceimgoff;	
	  			}
	  			else{
	  				var img = returnedData.saccondetail.deviceimgon;
	  			}

	  			var imgsrc = baseurl . concat(img);
	  			var imgid  = returnedData.saccondetail.deviceplace;
	  			imgid  = "device_img_" . concat(imgid);
	  			document.getElementById(imgid).src=imgsrc;
	  			},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
}

function Button_Selected(obj){
	var sDeviceId = obj.id;
	var sValue = obj.value
	var sSpeed = 0
	
	if (sValue == "02"){
		var sElementID = "Range".concat(sDeviceId)
		var x = document.getElementById(sElementID).value;
   		sSpeed =Math.round( x/10);
	}

	Send_Value_To_server(sDeviceId,sValue,sSpeed);

	return false;
}

