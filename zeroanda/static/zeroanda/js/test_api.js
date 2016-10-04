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
            url: "http://" + location.host + "/zeroanda/test/csv/add",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})

$(function(){
    $("#testUpdateCsv").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/csv/update",
            success: function(msg){
                // alert(msg);
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
                alert("error")
            }
        });
    });
})