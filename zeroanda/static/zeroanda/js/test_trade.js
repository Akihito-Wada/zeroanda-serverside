/**
 * Created by wadaakihito on 2/24/16.
 */

// test - trade - option?
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
    $("#testTradesCancelButton").click(function() {
        $.ajax({
            type: "POST",
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
    $("#testTradesDeleteButton").click(function() {
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