# Django Gulpify

Really *REALLY* lightweight connector between Django and Gulp. Does only the following:

1. Provides a runserver command which starts gulp automatically
2. Adds a 'gulp' management command which allows you to run gulp tasks but automatically passes down the static URL and debug flags for the active Django settings

