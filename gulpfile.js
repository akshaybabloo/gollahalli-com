var gulp = require('gulp');
var minify = require('gulp-minify');
var cleanCss = require('gulp-clean-css');
var rename = require('gulp-rename');

gulp.task('pack-js', function () {
    return gulp.src([
        'gollahalli_me/static/static_dirs/js/fitvids.js',
        'gollahalli_me/static/static_dirs/js/script.js'
    ])
        .pipe(minify({
            ext: {
                min: '.js'
            },
            noSource: true
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_me/static/static_dirs/js'));
});

gulp.task('pack-js-external', function () {
    return gulp.src([
        'gollahalli_me/static/static_dirs/external/prism.js'
    ])
        .pipe(minify({
            ext: {
                min: '.js'
            },
            noSource: true
        }))
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_me/static/static_dirs/external'));
});

gulp.task('pack-css', function () {
    return gulp.src([
        'gollahalli_me/static/static_dirs/css/gollahalli.css',
        'gollahalli_me/static/static_dirs/css/magnific-popup.css',
        'gollahalli_me/static/static_dirs/css/style.css',
        'gollahalli_me/static/static_dirs/css/owl.carousel.css',
        'gollahalli_me/static/static_dirs/css/linea.css'
    ])
        .pipe(cleanCss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_me/static/static_dirs/css'));
});

gulp.task('pack-css-external', function () {
    return gulp.src([
        'gollahalli_me/static/static_dirs/external/prism.css'
    ])
        .pipe(cleanCss())
        .pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest('gollahalli_me/static/static_dirs/external'));
});

gulp.task('default', ['pack-js', 'pack-css', 'pack-js-external', 'pack-css-external']);