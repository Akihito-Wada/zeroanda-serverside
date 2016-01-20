
//$(document).ready(function(){
//    $.getScript("/static/zeroanda/js/logger.js", function(){});
//})

$(function(){
    $("#buyButton").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/api/order",
            data: "schedule_id="+$("#scheduleModelId").val(),
            success: function(msg){
//                alert( "Data Saved: " + msg );
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
//                alert("some error");
            }
        });
    });
})

$(function(){
    $("#getOrdersButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/api/order",
//            data: "schedule_id="+$("#id_ordermodel_set-__prefix__-schedule").val(),
            success: function(msg){
//                alert( "Data Saved: " + msg );
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
//                alert("some error");
            }
        });
    });
})
