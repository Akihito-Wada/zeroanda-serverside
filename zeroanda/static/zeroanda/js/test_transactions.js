/**
 * Created by wadaakihito on 2/24/16.
 */

// test - trade
$(function(){
    $("#testGetTransactions").click(function() {
        $.ajax({
            type: "GET",
            url: "http://" + location.host + "/zeroanda/test/transactions",
            success: function(msg){
            },
            error: function(XMLHttpRequest, textStatus, errorThrown) {
            }
        });
    });
})
