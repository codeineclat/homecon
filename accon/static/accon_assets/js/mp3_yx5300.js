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

$('#get_info').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#get_info').val();
		var sCMDValue   = '0';
		var sFun 	    = '0';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

function songselected(obj){
	var sMP3Value  = obj.id;
	var sCMDValue  = obj.value;
	var sFun       = '01';
	Send_Value_To_server(sMP3Value,sCMDValue,sFun);
	return false;
}

$('#mp3_prev').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_prev').val();
		var sCMDValue   = '0002';
		var sFun 	    = '0A';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});


$('#mp3_pause').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_pause').val();
		var sCMDValue 	= '000E';
		var sFun        = '0A';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#mp3_stop').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_stop').val();
		var sCMDValue 	= '0016';
		var sFun        = '0A';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#mp3_next').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_next').val();
		var sCMDValue 	= '0001';
		var sFun        = '0A';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#mp3_play').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_play').val();
		var sCMDValue 	= '000C';
		var sFun        = '0A';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#volume').click(function() { //on button_download click event print action takes place

	var x = document.getElementById("volumerange").value;
   	var volume =Math.round( x/6.66);
		var sMP3Value 	= "volume";
		var sCMDValue 	= volume;
		var sFun        = '00';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#fmvolume').click(function() { //on button_download click event print action takes place

	var x = document.getElementById("fmvolumerange").value;
   	var volume =Math.round( x/6.66);
		var sMP3Value 	= "fmvolume";
		var sCMDValue 	= volume;
		var sFun        = '00';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#fm_stop').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#fm_stop').val();
		var sCMDValue 	= 0;
		var sFun        = '00';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#fm0927').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#fm0927').val();
		var sCMDValue   = '039F';
		var sFun 	    = '06';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#fm0935').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#fm0935').val();
		var sCMDValue   = '03A7';
		var sFun 	    = '06';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#fm1006').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#fm1006').val();
		var sCMDValue   = '03EE';
		var sFun 	    = '06';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});

$('#fm1052').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#fm1052').val();
		var sCMDValue   = '041C';
		var sFun 	    = '06';
		Send_Value_To_server(sMP3Value,sCMDValue,sFun);
		return false;
});
