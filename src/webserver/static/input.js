var xmlhttp;

function loadXMLDoc() {

	if (window.XMLHttpRequest) {
		xmlhttp=new XMLHttpRequest();
  	}
	else {
  		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  	}

	xmlhttp.onreadystatechange=function() {
  		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
    		alert(xmlhttp.responseText);
    	}
  	}

xmlhttp.open("GET","/getAvailableCourses",true);
xmlhttp.send();
}

$(function () {
	
	$("#b1").click(function() {
		$("#l1 option:selected").each(function(){
			$(this).remove().appendTo("#l2");
		});
	});

	$("#b2").click(function() {
		$("#l2 option:selected").each(function(){
			$(this).remove().appendTo("#l1");
		});
	});

	$("#b3").click(function() {
		$("#l3 option:selected").each(function(){
			$(this).remove().appendTo("#l4");
		});
	});

	$("#b4").click(function() {
		$("#l4 option:selected").each(function(){
			$(this).remove().appendTo("#l3");
		});
	});		

});

loadXMLDoc();