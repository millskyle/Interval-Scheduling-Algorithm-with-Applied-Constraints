var xmlhttp;
var courses;

function clear_hash() {
   var vposition = document.body.scrollTop;
   window.location.hash = "";
   document.body.scrollTop = vposition;
}

function loadXMLDoc() {
    $('#l2').empty();
    $('#l3').empty();
    $('#l5').empty();
    $('#l6').empty();


    //parse the url hash to get selected courses:
    hash = window.location.hash.replace("#-","").split("-");
    if (hash.length > 1) { 
        $.each(hash,function(key,value) {
            var thiscourse = $('#l3').append($("<option></option>").attr("value",value).text(value));
//            thiscourse.attr("selected");
        });
    }
    ///////

    var sem = $('#semester').find(":selected").val();
    $.ajax({
        type: 'get',
        url: '/getAvailableCourses/'+sem,
        success: function(data){
            courses = JSON.parse(data);
            $('#l1').empty();
            if(!courses){
                $('#l4').empty();
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

    $("#b0").click(function() {
        clear_hash();
        $('#l3').empty();
    });
    
    $("#b1").click(function() {
        $("#l2 option:selected").each(function(){
            $(this).clone().appendTo("#l3");
            window.location.hash=window.location.hash + '-' + $(this).val();
        });
    });

    $("#b2").click(function() {
        $("#l3 option:selected").each(function(){
            $(this).remove();
            var vposition = document.body.scrollTop;
            window.location.hash = window.location.hash.replace('-'+$(this).val(),'');
            document.body.scrollTop = vposition;
            //$(this).remove().appendTo("#l2");
        });
    });

//    $("#b3").click(function() {
//        $("#l5 option:selected").each(function(){
//            $(this).remove().appendTo("#l6");
//            $(this).attr("selected")
//        });
//    });

//    $("#b4").click(function() {
//        $("#l6 option:selected").each(function(){
//            $(this).remove().appendTo("#l5");
//        });
//    });        

    $("#l1").change(function(){
        $("#l1 option:selected").each(function(){
            var subject = $(this).text();
            var sem = $('#semester').find(":selected").val();

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
        clear_hash();
        loadXMLDoc();
    })
});



function selectAllOptions(selStr)
{
//    var selObj = document.getElementById(selStr);
    
    $('#l3 option').each(function() {
        $(this).attr("selected",'selected');
    });
    
//    for (var i=0; i<selObj.options.length; i++) {
//        selObj.options[i].selected = true;
//    }

}


$(document).ready(function(){
    loadXMLDoc();
});
