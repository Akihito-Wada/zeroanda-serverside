/**
 * Created by wadaakihito on 2/24/16.
 */

// test - position

$(function(){
    $("#testPositionsGetButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/positions",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testPositionsDeleteButton").click(function() {
        $.ajax({
            type: "DELETE",
            url: "http://" + location.host + "/zeroanda/test/positions",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})
