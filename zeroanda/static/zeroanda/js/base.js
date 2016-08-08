
//$(document).ready(function(){
//    $.getScript("/static/zeroanda/js/logger.js", function(){});
//})
// $(function(){
//     $("#buyButton").click(function() {
//         $.ajax({
//             type: "POST",
//             url: "http://" + location.host + "/zeroanda/api/order",
//             data: "schedule_id="+$("#scheduleModelId").val(),
//             success: function(msg){
//             },
//             error: function(XMLHttpRequest, textStatus, errorThrown) {
//             }
//         });
//     });
// })

// ifdoco bid and ask.
$(function(){
    $("#ifdocoButton").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/api/order/ifdoco",
            data: "schedule_id="+$("#scheduleModelId").val(),
            success: function(msg){
//                location.href = '/admin/zeroanda/ordermodel/';
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
            }
        });
    });
})

// cancel the order
$(function(){
    $("#cancelButton").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/api/order/cancel",
            data: {"actual_order_id": $("#actual_order_id").val()},
            success: function(msg){
                location.reload();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

// cancel all of the orders
$(function(){
    $("#cancelAllButton").click(function() {
        logger.info('test')
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/api/order/cancelall",
            success: function(msg){
                //location.reload();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

// get prices
$(function(){
    $("#testGetPriceButton").click(function() {
        logger.info('test')
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/api/prices",
            data: {"schedule_id": $("#scheduleModelId").val()},
            success: function(msg){
                //location.reload();
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

// get candles
$(function(){
    $("#testGetCandlesButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/api/candles",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

// get prices
$(function(){
    $("#getTickingPriceButton").click(function() {
        logger.info('test')
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/api/tick",
            data: {"schedule_id": $("#scheduleModelId").val()},
            success: function(msg){},
            error: function(XMLHttpRequest, textStatus, errorThrown) {}
        });
    });
})
