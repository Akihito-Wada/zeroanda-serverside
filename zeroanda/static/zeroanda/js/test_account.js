/**
 * Created by wadaakihito on 2/29/16.
 */


$(function(){
    $("#testAccountsGetButton").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/accounts",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})