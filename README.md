
# django-gulpify

This is a fairly barebones Django app which nicely integrates with gulp. It provides the following:

 - An 'gulp' command which lets you run gulp tasks, while forwarding the STATIC_URL setting and whether or not Django is running with DEBUG=True
 - A 'runserver' command which starts/stops gulp by running it in a separate process

It's fairly simple and not much code but it allows you to do stuff like this in your gulpfile.js:


```
    gulp.src(input)
    .pipe(sass(sassOptions).on('error', sass.logError))
    .pipe(rename(dest))
    .pipe(replace("{{STATIC_URL}}", argv.static_url)) // Replace {{STATIC_URL}} in CSS files appropriately
    .pipe(gulp.dest(outputDir));
```

And also things like this:


```
  if(argv.assets_debug) {
    sassOptions.sourceMapEmbed = true;
    sassOptions.outputStyle = 'expanded';
  } else {
    sassOptions.outputStyle = 'compressed';
  }
```

The other useful thing it allows is that you can build assets as part of Django commands:

   call_command('gulp', 'build')

