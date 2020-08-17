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
import sys
import time
import argparse
import subprocess

from pathlib import Path


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('username', help='GitHub username')
    parser.add_argument('repo', help='Repository name without the .git extension')
    args = parser.parse_args()
    setup_github_repo(args.username, args.repo)
    # if repo_folder_exists(args.repo) is True:
    #     cd_to_repo_folder(args.repo)
    #     create_python3_venv()
    #     TODO: 'initialize virtualenv'
    #     TODO: 'check if requirements.txt exists if True pip install -r requirements.txt'
    # else:
    #     print('try again')
    # #     TODO: 'gracefully handle failures'


def setup_github_repo(username, repo):
    try:
        cmd = subprocess.run(['git', 'clone', f'git@github.com:{username}/{repo}.git'], capture_output=True)
        return cmd.check_returncode()  # check for any errors after command is run
    except subprocess.CalledProcessError as e:  # use print(sys.exc_info()) to determine exception type
        print(f'Git clone for {repo} failed!')
        create_new_repo(repo)


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
    cmd = subprocess.call(['python3', '-m', 'virtualenv', 'venv'])
    return cmd


def git_init():
    cmd = subprocess.call(['git', 'init'])
    return cmd


def make_new_dir(repo):
    if repo_folder_exists(repo) is True:
        print(f'A folder with the same name exists: {repo}')
    else:
        subprocess.call(['mkdir', repo])


def create_new_repo(repo):
    print(f'\nCreating a new {repo} directory...\n')
    make_new_dir(repo)
    if repo_folder_exists(repo) is True:
        cd_to_repo_folder(repo)
        git_init()
        create_python3_venv()
    else:
        print('Unable to create directory. Exiting...')
        sys.exit()


if __name__ == '__main__':
    main()
