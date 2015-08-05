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
  			courses = JSON.parse(xmlhttp.responseText);

  			for (var subject in courses[""]) {
  				
				console.log(subject);

  				$.each([subject], function(key, value) {   
  				    $('#l1').append($("<option></option>").attr("value",key).text(value)); 
  				});

  				$.each([subject], function(key, value) {   
  				    $('#l4').append($("<option></option>").attr("value",key).text(value)); 
  				});

  				console.log(courses[""][subject]);

  				$.each(courses[""][subject], function(index) { 
  				    $('#l2').append($("<option></option>").attr("value",courses[""][subject][index]).text(courses[""][subject][index])); 
  					//console.log(index);
  				});

  				$.each(courses[""][subject], function(index) {   
  				    $('#l5').append($("<option></option>").attr("value",courses[""][subject][index]).text(courses[""][subject][index])); 
  				});
  			}
      	}
  	}

xmlhttp.open("GET","/getAvailableCourses",true);
xmlhttp.send();
}

$(function () {
	
	$("#b1").click(function() {
		$("#l2 option:selected").each(function(){
			$(this).remove().appendTo("#l3");
		});
	});

	$("#b2").click(function() {
		$("#l3 option:selected").each(function(){
			$(this).remove().appendTo("#l2");
		});
	});

	$("#b3").click(function() {
		$("#l5 option:selected").each(function(){
			$(this).remove().appendTo("#l6");
		});
	});

	$("#b4").click(function() {
		$("#l6 option:selected").each(function(){
			$(this).remove().appendTo("#l5");
		});
	});		

});

loadXMLDoc();