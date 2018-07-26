var $ = django.jQuery;
jQuery.noConflict();
$(document).ready(function () {
    $("#id_user_id").change(function () {
        var $self = $(this);
        {% for user in users %}
            if($self.val()==='{{user.id}}'){
                $("#id_first_name").val('{{user.first_name}}');
                $("#id_last_name").val('{{user.last_name}}');
                $("#id_email_id").val('{{user.email}}');
                $("#id_phone_number").val('{{user.phone_number}}');
            }
        {% endfor %}
        else {
            $("#id_first_name").val('First Name');
            $("#id_last_name").val('Last Name');
            $("#id_email_id").val('email ID');
            $("#id_phone_number").val('{{user.phone_number}}');
        }
    })
});
