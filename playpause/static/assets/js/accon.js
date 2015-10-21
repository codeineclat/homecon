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

function Send_Value_To_server (value,cmd,fun) {
	var siteurl   = window.location.href; 
		var url 	= "";
		var appid   = "0065";
		var type 	= 'POST';
      		data = {
			sPlaypauseValue :value,
			sCommand        :cmd,
			sFunction       :fun,
			sAppID          :appid
	      	};
	
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,
	  		success: function(sLastPingInfo) {
	  			var lastcommunication  = $(sLastPingInfo).find('#lastcommunication').text();
	  			var lastcmdrequest     = $(sLastPingInfo).find('#lastcmdrequest').text();
	  			var lastcmdrequesttime = $(sLastPingInfo).find('#lastcmdrequesttime').text();
	  			var lastcmdaction 	   = $(sLastPingInfo).find('#lastcmdaction').text();
	  			var lastcmdactiontime  = $(sLastPingInfo).find('#lastcmdactiontime').text();
	  			var lastcmdstatus      = $(sLastPingInfo).find('#lastcmdstatus').text();
	  			var lastcmdstatustime  = $(sLastPingInfo).find('#lastcmdstatustime').text();
	  			var lastcmdcmd         = $(sLastPingInfo).find('#lastcmdcmd').text();
	  			var lastfailtime       = $(sLastPingInfo).find('#lastfailtime').text();
	  			var lastfailcmd        = $(sLastPingInfo).find('#lastfailcmd').text();
	  			var lastsong           = $(sLastPingInfo).find('#lastsong').text();

	  			$('#lastcommunication').html(lastcommunication);
	  			$('#lastcmdrequest').html(lastcmdrequest);
	  			$('#lastcmdrequesttime').html(lastcmdrequesttime);
	  			$('#lastcmdaction').html(lastcmdaction);
	  			$('#lastcmdactiontime').html(lastcmdactiontime);
	  			$('#lastcmdstatus').html(lastcmdstatus);
	  			$('#lastcmdstatustime').html(lastcmdstatustime);
	  			$('#lastcmdcmd').html(lastcmdcmd);
	  			$('#lastfailtime').html(lastfailtime);
	  			$('#lastfailcmd').html(lastfailcmd);
	  			$('#lastsong').html(lastsong);

	  			},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
}

function Button_Selected(obj){
	var  sDeviceId = obj.id;
	console.log(sDeviceId)
	return false;
}