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

$('#mp3_prev').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_prev').val();
		console.log(sMP3Value)
		var siteurl   = window.location.href; 
		var url 	= "";
		var type 	= 'POST';
      		data = {
			sPlaypauseValue :sMP3Value
	      	};
		
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,
	  		success: function(response) {
	  			alert("Saved successfully..")
	  			console.log(response);				
   	  		},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
		return false;
});

$('#mp3_pause').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_pause').val();
		console.log(sMP3Value)
		var siteurl   = window.location.href; 
		var url 	= "";
		var type 	= 'POST';
      		data = {
			sPlaypauseValue :sMP3Value
	      	};
		
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,
	  		success: function(response) {
	  			alert("Saved successfully..")
	  			console.log(response);				
   	  		},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
		return false;
});

$('#mp3_stop').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_stop').val();
		console.log(sMP3Value)
		var siteurl   = window.location.href; 
		var url 	= "";
		var type 	= 'POST';
      		data = {
			sPlaypauseValue :sMP3Value
	      	};
		
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,
	  		success: function(response) {
	  			alert("Saved successfully..")
	  			console.log(response);				
   	  		},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
		return false;
});
mp3_next
$('#mp3_next').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_next').val();
		console.log(sMP3Value)
		var siteurl   = window.location.href; 
		var url 	= "";
		var type 	= 'POST';
      		data = {
			sPlaypauseValue :sMP3Value
	      	};
		
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,
	  		success: function(response) {
	  			alert("Saved successfully..")
	  			console.log(response);				
   	  		},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
		return false;
});

$('#mp3_play').click(function() { //on button_download click event print action takes place
		var sMP3Value 	= $('#mp3_play').val();
		console.log(sMP3Value)
		var siteurl   = window.location.href; 
		var url 	= "";
		var type 	= 'POST';
      		data = {
			sPlaypauseValue :sMP3Value
	      	};
		
		$.ajax({
			url: url,
	  		type: type,
	  		data: data,
	  		success: function(response) {
	  			alert("Saved successfully..")
	  			console.log(response);				
   	  		},
   	  		headers:{
   	  			'X-CSRFToken': csrftoken
   	  		}
		});
		return false;
});
