var gulp = require('gulp');
var minify = require('gulp-minify');
var cleanCss = require('gulp-clean-css');
var rename = require('gulp-rename');
var uncss = require('gulp-uncss');
var concat = require('gulp-concat');

// JS
var fitvids_js = 'gollahalli_com/static/static_dirs/js/fitvids.js';
var script_js = 'gollahalli_com/static/static_dirs/js/script.js';
var prism_js = 'gollahalli_com/static/static_dirs/external/prism.js';

// CSS
var gollahalli_css = 'gollahalli_com/static/static_dirs/css/gollahalli.css';
var magnific_popup_css = 'gollahalli_com/static/static_dirs/css/magnific-popup.css';
var style_css = 'gollahalli_com/static/static_dirs/css/style.css';
var owl_carousel_css = 'gollahalli_com/static/static_dirs/css/owl.carousel.css';
var linea_css = 'gollahalli_com/static/static_dirs/css/linea.css';
var ionicons_css = 'gollahalli_com/static/static_dirs/css/ionicons.css';
var bootstrap_css = 'gollahalli_com/static/static_dirs/bootstrap/css/bootstrap.css';

// External
// CSS
var prism_css = 'gollahalli_com/static/static_dirs/external/prism.css';

// Mini stuff
// JS
var fitvids_js_mini = 'gollahalli_com/static/static_dirs/js/fitvids.js';
var script_js_mini = 'gollahalli_com/static/static_dirs/js/script.js';
var jquery_magnific_popup_mini = 'gollahalli_com/static/static_dirs/js/jquery.magnific-popup.min.js';
var jquery_js_mini = 'gollahalli_com/static/static_dirs/js/jquery.min.js';
var jquery_shuffle_js_mini = 'gollahalli_com/static/static_dirs/js/jquery.shuffle.min.js';
var owl_carousel_js_mini = 'gollahalli_com/static/static_dirs/js/owl.carousel.min.js';
var validator_js_mini = 'gollahalli_com/static/static_dirs/js/validator.min.js';

// CSS
var gollahalli_css_mini = 'gollahalli_com/static/static_dirs/css/gollahalli.css';
var magnific_popup_css_mini = 'gollahalli_com/static/static_dirs/css/magnific-popup.css';
var style_css_mini = 'gollahalli_com/static/static_dirs/css/style.css';
var owl_carousel_css_mini = 'gollahalli_com/static/static_dirs/css/owl.carousel.css';
var linea_css_mini = 'gollahalli_com/static/static_dirs/css/linea.css';
var ionicons_css_mini = 'gollahalli_com/static/static_dirs/css/ionicons.css';
var bootstrap_css_mini = 'gollahalli_com/static/static_dirs/bootstrap/css/bootstrap.css';

gulp.task('pack-js', function () {
    return gulp.src([fitvids_js, script_js])
        .pipe(minify({
            ext: {
                min: '.js'
            },
            noSource: true
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/js'));
});

gulp.task('pack-js-external', function () {
    return gulp.src([
        prism_js
    ])
        .pipe(minify({
            ext: {
                min: '.js'
            },
            noSource: true
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/external'));
});

gulp.task('pack-css', function () {
    return gulp.src([
        gollahalli_css, magnific_popup_css, style_css, owl_carousel_css, linea_css
    ])
        .pipe(cleanCss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/css'));
});

gulp.task('pack-css-external', function () {
    return gulp.src([
        prism_css
    ])
        .pipe(cleanCss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/external'));
});

// gulp.task('uncss-bootstrap', function () {
//     return gulp.src(bootstrap_css)
//         .pipe(uncss({
//             html: [
//                 'https://www.gollahalli.com'
//             ],
//             timeout: 1000
//         }))
//         .pipe(cleanCss())
//         .pipe(rename({suffix: '.min'}))
//         .pipe(gulp.dest('gollahalli_com/static/static_dirs/bootstrap/css'));
// });
//
// gulp.task('uncss-all', function () {
//     return gulp.src([gollahalli_css, ionicons_css])
//         .pipe(uncss({
//             html: [
//                 'https://www.gollahalli.com'
//             ],
//             timeout: 1000
//         }))
//         .pipe(cleanCss())
//         .pipe(rename({suffix: '.min'}))
//         .pipe(gulp.dest('gollahalli_com/static/static_dirs/css'));
// });

gulp.task('concat-all-css', function () {
    return gulp.src([gollahalli_css_mini, ionicons_css_mini, linea_css_mini, magnific_popup_css_mini, owl_carousel_css_mini, style_css_mini, bootstrap_css_mini])
        .pipe(concat('content.css'))
        .pipe(cleanCss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/css'))
});

gulp.task('concat-all-js', function () {
    return gulp.src([jquery_js_mini, fitvids_js_mini, jquery_magnific_popup_mini, jquery_shuffle_js_mini, owl_carousel_js_mini, script_js_mini, validator_js_mini])
        .pipe(concat('content.js'))
        .pipe(minify({
            ext: {
                src: 'content.js',
                min: '.js'
            },
            noSource: true
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_com/static/static_dirs/js'))
});

gulp.task('default', ['pack-js', 'pack-css', 'pack-js-external', 'pack-css-external', 'concat-all-css', 'concat-all-js']);