
//$(document).ready(function(){
//    $.getScript("/static/zeroanda/js/logger.js", function(){});
//})

$(function(){
    $("#buyButton").click(function() {
        logger.info($("#id_ordermodel_set-__prefix__-schedule").val());
        $.post(
            "http://" + location.host + "/zeroanda/api/order",
            {
                'schedule_id': $("#id_ordermodel_set-__prefix__-schedule").val()
            },
            function(data) {
                logger.info("success.");
            }
        );
    });
})