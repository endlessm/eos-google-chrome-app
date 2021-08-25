#!/usr/bin/env python3

import github
import os

github.enable_console_debug_logging()
token = os.environ['GITHUB_TOKEN']
repository = os.environ['GITHUB_REPOSITORY']
repo_owner, repo_name = repository.split('/')
print('token prefix:', token[:3])
gh = github.Github(os.environ['GITHUB_TOKEN'])
user = gh.get_user()
try:
    print('user info:', user.id, user.login, user.name, user.type)
except github.GithubException as err:
    if err.status == 403:
        # Not a user, try to be an app
        # app = gh.get_app()
        # print('app info:', app.id, app.name, app.permissions, app.events)
        inst = gh.get_installation(repo_owner, repo_name)
        print('installation info:', inst.id, inst.raw_data['permissions'],
              inst.raw_data['events'])
    else:
        raise
repo = gh.get_repo(repository)
print(repo.permissions)
