$(function () {
    "use strict";

    $('#contact-me').on('click', function () {
        $('#footer').html(
            '<footer class="footer">\
              <div class="container-fluid">\
                Place sticky footer content here.\
              </div>\
            </footer>'
        );
    });

    $('#about-me').on('click', function () {
        $('#footer').html(
            '<footer class="footer">\
              <div class="container-fluid">\
                Place sticky footer content here.\
              </div>\
            </footer>'
        );
    });

    $('#portfolio-me').on('click', function () {
        $('#footer').html(
            '<footer class="footer">\
              <div class="container-fluid">\
                Place sticky footer content here.\
              </div>\
            </footer>'
        );
    });

    $('#resume-me').on('click', function () {
        $('#footer').html(
            '<footer class="footer">\
              <div class="container-fluid">\
                Place sticky footer content here.\
              </div>\
            </footer>'
        );
    });

    $('#blog-me').on('click', function () {
        $('#footer').html(
            '<footer class="footer">\
              <div class="container-fluid">\
                Place sticky footer content here.\
              </div>\
            </footer>'
        );
    });


    $('#home-me').on('click', function () {
        $('#footer').html('');
    });
});
