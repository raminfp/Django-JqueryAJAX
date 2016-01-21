
var jsonitem = []
  
item = {};
item ["one"] = $(".one").val();
item ["two"] = $(".two").val();
item ["three"] = $(".three").val();
item ["four"] = $(".four").val();
jsonitem.push(item);

// Send with JQuery - AJAX

 model = jsonitem;
    $.ajax({
        url: "/sendjsonlistmodel",
        datatype: 'json',
        type: 'POST',
        data: {'model[]': JSON.stringify(model)},
        success: function (data) {
            $(".seccuess").html(data).show();
           
        },
        
// Get List of Django on view.py

listmode = request.POST.getlist('model[]')
  
