var xmlhttp;
var courses;

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

  			$.each(courses["Fall 2015"], function(key, value) {   
  			    $('#l1').append($("<option></option>").attr("value",key).text(key)); 
  			});

  			$.each(courses["Fall 2015"], function(key, value) {   
  			    $('#l4').append($("<option></option>").attr("value",key).text(key)); 
  			});

  		}
  	}

xmlhttp.open("GET","/getAvailableCourses",true);
xmlhttp.send();
}


$(function () {
	
	$("#b1").click(function() {
		$("#l2 option:selected").each(function(){
			$(this).remove().appendTo("#l3");
			$(this).attr("selected")
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
			$(this).attr("selected")
		});
	});

	$("#b4").click(function() {
		$("#l6 option:selected").each(function(){
			$(this).remove().appendTo("#l5");
		});
	});		

	$("#l1").change(function(){
		$("#l1 option:selected").each(function(){
			var subject = $(this).text();

			$("#l2").empty();

			$.each(courses["Fall 2015"][subject], function(index) {

				$('#l2').append($("<option></option>").attr("value",courses["Fall 2015"][subject][index]).text(courses["Fall 2015"][subject][index])); 
			})
		});
	});

	$("#l4").change(function(){
		$("#l4 option:selected").each(function(){
			var subject = $(this).text();

			$("#l5").empty();

			$.each(courses["Fall 2015"][subject], function(index) {

				$('#l5').append($("<option></option>").attr("value",courses["Fall 2015"][subject][index]).text(courses["Fall 2015"][subject][index])); 
			})
		});
	});
});

function selectAllOptions(selStr)
{
	var selObj = document.getElementById(selStr);
	for (var i=0; i<selObj.options.length; i++) {
		selObj.options[i].selected = true;
	}
}

loadXMLDoc();