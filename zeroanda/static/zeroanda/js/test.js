/**
 * Created by wadaakihito on 2/24/16.
 */


$(function(){
    $("#testBuyMarketButton").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/test/buy_market",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})


$(function(){
    $("#testCancelButton").click(function() {
        $.ajax({
            type: "POST",
            url: "http://" + location.host + "/zeroanda/test/cancel",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})