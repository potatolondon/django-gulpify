import os
from subprocess import check_call

from django.core.management.base import BaseCommand

from gulpify import config


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("command", type=str)

    def handle(self, *args, **options):
        env = os.environ.copy()
        env["NODE_PATH"] = config.NODE_PREFIX

        check_call(
            config.generate_gulp_args(options["command"]),
            env=env,
            cwd=config.GULP_CLI_PATH
        )
