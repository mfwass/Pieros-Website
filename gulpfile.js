var gulp = require('gulp');
var rename = require('gulp-rename');
var autoprefixer = require('gulp-autoprefixer');
var nano = require('gulp-cssnano');

gulp.task('default', function() {
  return gulp.src('./assets/css/style.css')
    .pipe(rename('style.min.css'))
    .pipe(nano())
    .pipe(autoprefixer({
      browsers: ['> 5%'],
      cascade: false
    }))
    .pipe(gulp.dest('./assets/css'));
});
