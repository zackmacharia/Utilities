"""
This utility automates the steps of setting up a new development virtual environment.
Scenario one
Cloning from remote repository
- clone repository
- cd to repo folder
- initialize virtual environment
- activate virtual environment
- pip install modules from requirements.txt file
- verify installed modules with pip freeze - match against requirements.txt
"""

import os
import argparse
import subprocess
from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='GitHub username')
    parser.add_argument('repo', help='Repository name without the .git extension')
    args = parser.parse_args()
    clone_github_repo(args.username, args.repo)
    if repo_folder_exists(args.repo) is True:
        cd_to_repo_folder(args.repo)
        create_python3_venv()
    else:
        print('try again')


def clone_github_repo(username, repo):
    cmd = subprocess.run(['git', 'clone', f'git@github.com:{username}/{repo}.git'])
    return cmd


def current_path():
    p = Path().cwd()
    return p


def repo_folder_exists(repo):
    repo_path_string = str(current_path()) + '/' + repo
    p = Path(repo_path_string)
    return p.exists()


def cd_to_repo_folder(repo):
    repo_path_string = str(current_path()) + '/' + repo
    return os.chdir(repo_path_string)


def create_python3_venv():
    subprocess.run(['python3', '-m', 'virtualenv', 'venv'])


if __name__ == '__main__':
    main()