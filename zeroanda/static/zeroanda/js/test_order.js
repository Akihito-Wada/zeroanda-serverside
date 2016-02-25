/**
 * Created by wadaakihito on 2/24/16.
 */

// test - order
$(function(){
    $("#testOrdersBuyMarketButton").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/test/order/buy_market",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testOrdersGetButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/orders",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testOrdersChangeButton").click(function() {
        $.ajax({
            type: "PATCH",
            url: "http://" + location.host + "/zeroanda/test/orders",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testOrdersCancelButton").click(function() {
        $.ajax({
            type: "DELETE",
            url: "http://" + location.host + "/zeroanda/test/orders",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})
