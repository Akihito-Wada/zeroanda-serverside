/**
 * Created by wadaakihito on 3/8/16.
 */

$(function(){
    $("#testCallActionButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/call/action",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})
