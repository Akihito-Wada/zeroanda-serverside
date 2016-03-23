/**
 * Created by wadaakihito on 2/24/16.
 */

// test - trade
$(function(){
    $("#testGetEvents").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/events",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})
