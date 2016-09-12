/**
 * Created by wadaakihito on 2/29/16.
 */


$(function(){
    $("#testGetCalender").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/calender",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testGetCsv").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/csv",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})