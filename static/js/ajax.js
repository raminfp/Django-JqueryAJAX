$(document).ready(function () {

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    $(".send").click(function () {
        model = {
            fname: $(".fname").val(),
            lname: $(".lname").val()
        }
        $.ajax(
            {
                url: "/ajax",
                type: 'POST',
                dataType: 'json',
                data: model,
                success: function (data) {
                   alert(data.fname);
                },
                error : function(data){
                    alert(data);
                }
            }
        );
    });
});

