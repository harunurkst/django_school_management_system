$(document).ready(function(){
    $('.btn_class').on('click', function(){
        var btn_proparty = $(this)
        var row = $(this).closest("tr");
        var roll = row.find(".cls_roll").text();
        var cls = row.find(".cls_class").text();
        
        var api_url = 'http://localhost:8000/api/attendance/'+ cls + '/' + roll 
        
        $.ajax({
            url: api_url,
            method: 'get',
            success: function(data){
                btn_proparty.addClass('btn btn-success');

                
            },
            error: function(err){
                alert(err.status)
            }
        });
    })
    
})