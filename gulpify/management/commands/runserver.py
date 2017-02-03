import os
import subprocess

from django.core.management import load_command_class
from django.conf import settings
from gulp import config


def locate_runserver():
    """
        Lots of apps override the runserver command, what we want to do is
        subclass whichever one had precedence before the gulpify app and subclass that
    """

    index = settings.INSTALLED_APPS.index('gulp')
    for i in xrange(index + 1, len(settings.INSTALLED_APPS)):
        app_label = settings.INSTALLED_APPS[i]
        command = load_command_class(app_label, 'runserver')
        if command:
            return command.__class__
    else:
        raise ImportError("Unable to locate a base runserver Command to subclass")


BaseCommand = locate_runserver()


class Command(BaseCommand):
    def __init__(self, *args, **kwargs):
        self._process = None
        super(Command, self).__init__(*args, **kwargs)

    def run(self, *args, **kwargs):
        try:
            self._start_gulp()
            super(Command, self).run(*args, **kwargs)
        finally:
            self._stop_gulp()

    def _generate_gulp_args(self, task=None):
        args = [config.GULP_CLI_FILE]
        if task:
            args.append(task)
        args.append("--static_url={}".format(settings.STATIC_URL))
        if settings.DEBUG:
            args.append("--assets_debug=1")
        return args

    def _start_gulp(self):
        env = os.environ.copy()
        env["NODE_PREFIX"] = config.NODE_PREFIX

        self._process = subprocess.Popen(
            self._generate_gulp_args(),
            env=env,
            cwd=config.GULP_CLI_PATH
        )

    def _stop_gulp(self):
        if self._process:
            self._process.kill()
            self._process = None
