var gulp = require('gulp');
var minify = require('gulp-minify');
var cleanCss = require('gulp-clean-css');
var rename = require('gulp-rename');
var uncss = require('gulp-uncss');
var concat = require('gulp-concat');
var ignore = require('gulp-ignore');

var js_condition = 'gollahalli_com/static/static_dirs/js/jquery.js';

// JS Files
var fitvids = 'gollahalli_com/static/static_dirs/js/fitvids.js';
var jquery_magnific_popup = 'gollahalli_com/static/static_dirs/js/jquery.magnific-popup.js';
var jquery_shuffle = 'gollahalli_com/static/static_dirs/js/jquery.shuffle.js';
var owl_carousel = 'gollahalli_com/static/static_dirs/js/owl.carousel.js';
var validator = 'gollahalli_com/static/static_dirs/js/validator.js';
var script = 'gollahalli_com/static/static_dirs/js/script.js';

// CSS Files
var bootstrap_location = 'gollahalli_com/static/static_dirs/bootstrap/css/bootstrap.css';
var css_location = 'gollahalli_com/static/static_dirs/css/*.css';

gulp.task('pack-js', function () {
    return gulp.src([fitvids, jquery_magnific_popup, jquery_shuffle, owl_carousel, validator, script])
        .pipe(ignore.exclude(js_condition))
        .pipe(concat('content.js'))
        .pipe(minify({
            ext: {
                src: 'content.js',
                min: '.js'
            },
            noSource: true
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/js'));
});

gulp.task('pack-css', function () {
    return gulp.src([bootstrap_location, css_location])
        .pipe(concat('content.css'))
        .pipe(cleanCss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/css'))
});

gulp.task('default', ['pack-js', 'pack-css']);