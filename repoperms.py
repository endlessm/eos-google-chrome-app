#!/usr/bin/env python3

import github
import os

github.enable_console_debug_logging()
gh = github.Github(os.environ['GITHUB_TOKEN'])
repo = gh.get_repo(os.environ['GITHUB_REPOSITORY'])
print(repo.permissions)
