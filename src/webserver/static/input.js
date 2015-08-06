var xmlhttp;
var courses;

function loadXMLDoc() {
	var sem = $('#semester').find(":selected").text();
	$.ajax({
		type: 'get',
		url: '/getAvailableCourses/'+sem,
		success: function(data){
			courses = JSON.parse(data);
			if(!courses[sem]) {
				$('#l1').empty()
				$('#l4').empty()
				return;
			}
			$.each(courses[sem], function(key, value) {   
  			    $('#l1').append($("<option></option>").attr("value",key).text(key)); 
  			});

  			$.each(courses[sem], function(key, value) {   
  			    $('#l4').append($("<option></option>").attr("value",key).text(key)); 
  			});
		}
	});
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
			var sem = $('#semester').find(":selected").text();

			$("#l2").empty();
			if(!courses[sem]) return;

			$.each(courses[sem][subject], function(index) {

				$('#l2').append($("<option></option>").attr("value",courses[sem][subject][index]).text(courses[sem][subject][index])); 
			})
		});
	});

	$("#l4").change(function(){
		$("#l4 option:selected").each(function(){
			var subject = $(this).text();
			var sem = $('#semester').find(":selected").text();

			$("#l5").empty();
			if(!courses[sem]) return;

			$.each(courses[sem][subject], function(index) {

				$('#l5').append($("<option></option>").attr("value",courses[sem][subject][index]).text(courses[sem][subject][index])); 
			})
		});
	});

	$('#semester').change(function(){
		loadXMLDoc();
	})
});

function selectAllOptions(selStr)
{
	var selObj = document.getElementById(selStr);
	for (var i=0; i<selObj.options.length; i++) {
		selObj.options[i].selected = true;
	}
}


$(document).ready(function(){
	loadXMLDoc();
});