/**
 * Created by wadaakihito on 3/1/16.
 */

$(function(){
    $("#testProcessConuntButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/process",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})