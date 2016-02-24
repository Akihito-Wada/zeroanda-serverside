/**
 * Created by wadaakihito on 2/24/16.
 */

// test - trade
$(function(){
    $("#testTradesGetButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/trades",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testTradesChangeButton").click(function() {
        $.ajax({
            type: "PATCH",
            url: "http://" + location.host + "/zeroanda/test/trades",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testTradesCloseButton").click(function() {
        $.ajax({
            type: "DELETE",
            url: "http://" + location.host + "/zeroanda/test/trades",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})