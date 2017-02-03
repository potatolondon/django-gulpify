import os
from django.conf import settings

NODE_PREFIX = os.environ.get("NODE_PREFIX", settings.NODE_PREFIX)
GULP_CLI_PATH = os.path.join(NODE_PREFIX, "gulp-cli/bin/")
GULP_PATH = os.path.join(NODE_PREFIX, "gulp/bin/")
GULP_CLI_FILE = os.path.join(GULP_CLI_PATH, "gulp.js")
GULP_FILE = os.path.join(GULP_PATH, "gulp.js")
