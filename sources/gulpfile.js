//Projektordner-Struktur
var scssSrc = "sass/style.scss";
var scssDest = "../deploy/static/css";

//var jsSrc = "../static/js/app.js";
//var jsDest = "../static/compiled/js";

//var imgSrc = "../static/img/*.*";
//var imgDest = "../static/compiled/img";

//var iconsSrc = "icons/*.*";
//var iconsDest = "../deploy/static/icons";


//Gulp Module
var gulp = require('gulp'),                         //GULP  -- Gulp selbst
    rename = require('gulp-rename'),                //GULP  -- Benennt Dateien
    util = require('gulp-util'),                    //GULP  -- Generiert CLI-Log
    plumber = require('gulp-plumber'),              //GULP  -- Verhindert Pipe-Stop welche von Plugins verursacht werden
    color = require('gulp-color'),                  //GULP   -- CLI-Log Farben
    autoprefixer = require('gulp-autoprefixer'),   //CSS   -- Autoprefixer um alle Vendor Prefixes zu überprüfen
    minifyCSS = require('gulp-minify-css'),       //CSS   -- Minifizierung
    cleanCSS = require('gulp-clean-css'),           //CSS   -- Säubern mit clean-css
    sass = require('gulp-sass'),                    //CSS   -- Konvertierung der Sass-Datei in eine CSS-Datei
    concat = require('gulp-concat'),               //JS    -- Zusammenfassen
    uglify = require('gulp-uglify'),               //JS    -- Minifizierung
    imagemin = require('gulp-imagemin');          //IMG   -- Verlustlose Kompression aller Bilder und Vektoren


//Uhrzeit
date = new Date();
hour = date.getHours();
minute = date.getMinutes();
second = date.getSeconds();
currentTime = hour + ':' + minute + ':' + second;


//Gulp Tasks
gulp.task('sass', function(done) {
    util.log(color('Generate CSS File at ' + currentTime, 'YELLOW'));
    return gulp.src(scssSrc)
        .pipe(plumber())
        .pipe(sass().on('error', sass.logError))
        .pipe(autoprefixer())
        .pipe(rename({suffix: '.min'}))
        .pipe(cleanCSS())
        .pipe(minifyCSS())
        .pipe(gulp.dest(scssDest));
        done();
});

/*
gulp.task('js', function(done) {
    util.log(color('Generate JS File at ' + currentTime, 'YELLOW'));
    return gulp.src(jsSrc)
                .pipe(concat('app.min.js'))
				.pipe(uglify().on('error', util.log))
				//.pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(jsDest))
        done();
 });
*/

/*
gulp.task('imagemin', function(done) {
    util.log(color('Generate IMG Files at ' + currentTime, 'YELLOW'));
        return gulp.src(imgSrc)
        .pipe(imagemin({ progressive: true }))
        //.pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(imgDest));
        done();
});
*/

/*
gulp.task('iconmin', function(done) {
    util.log(color('Generate IMG Files at ' + currentTime, 'YELLOW'));
        return gulp.src(iconsSrc)
        .pipe(imagemin({ progressive: true }))
        //.pipe(rename({suffix: '.min'}))
        .pipe(gulp.dest(iconsDest));
        done();
});
*/

gulp.task('watch', function(done) {
    util.log(color('Watching SCSS/JS/IMG files for modifications', 'YELLOW'));
    gulp.watch(scssSrc, gulp.series('sass')).on('error', util.log);
    //gulp.watch(jsSrc, gulp.series('js')).on('error', util.log);
    //gulp.watch(iconsSrc, gulp.series('iconmin')).on('error', util.log);
    //gulp.watch(imgSrc, gulp.series('imagemin')).on('error', util.log);
    done();
});


gulp.task('default', gulp.series('watch'));
