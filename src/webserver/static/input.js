function loadXMLDoc() {

	var xmlhttp;

	if (window.XMLHttpRequest) {
		xmlhttp=new XMLHttpRequest();
  	}
	else {
  		xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  	}

	xmlhttp.onreadystatechange=function() {
  		if (xmlhttp.readyState==4 && xmlhttp.status==200) {
    		document.getElementById("myDiv").innerHTML=xmlhttp.responseText;
    	}
  	}

xmlhttp.open("POST",".asp",true);
xmlhttp.send();

}

$(function () {
	
	$("#b1").click(function() {
		$("#l1 option:selected").each(function(){
			$(this).remove().appendTo("l2");
		});
	});

	$("#b2").click(function() {
		$("#l2 option:selected").each(function(){
			$(this).remove().appendTo("l1");
		});
	});	

});