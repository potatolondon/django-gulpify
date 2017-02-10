import os
from django.conf import settings
from django.core.exceptions import ImproperlyConfigured

NODE_PREFIX = os.environ.get("NODE_PREFIX", settings.NODE_PREFIX)
NODE_PATH = os.environ.get("NODE_PATH", os.path.join(NODE_PREFIX, "node_modules"))
GULP_CLI_PATH = os.path.join(NODE_PATH, "gulp-cli/bin/")
GULP_PATH = os.path.join(NODE_PATH, "gulp/bin/")
GULP_CLI_FILE = os.path.join(GULP_CLI_PATH, "gulp.js")
GULP_FILE = os.path.join(GULP_PATH, "gulp.js")


def generate_gulp_args(task=None):
    if not os.path.exists(NODE_PATH):
        raise ImproperlyConfigured(
            "Unable to find node_modules at: {}".format(NODE_PATH)
        )

    if not os.path.exists(GULP_CLI_FILE):
        raise ImproperlyConfigured(
            "Unable to find gulp-cli at: {}".format(GULP_CLI_FILE)
        )

    args = [GULP_CLI_FILE]
    if task:
        args.append(task)
    args.append("--static_url={}".format(settings.STATIC_URL))
    if settings.DEBUG:
        args.append("--assets_debug=1")
    return args
