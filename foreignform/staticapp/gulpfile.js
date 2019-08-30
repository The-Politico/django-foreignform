const gulp = require('./gulp')([
  'dev',
  'build',
]);

gulp.task('default', gulp.series('dev'));
