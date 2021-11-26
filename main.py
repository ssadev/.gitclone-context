import sys
import os
import clipboard


def validate_repo_link(clipbord):
    github_com = clipbord.find('https://github.com/')
    # print(type(github_com), github_com)
    if github_com == 0:
        return True
    return False


def get_repo_link():
    repo = "https://github.com/ssadev/myjsondbs.git"
    repo = clipboard.paste()
    if(validate_repo_link(repo) != True):
        return False
    return repo


def get_repo_folder(repo=None):
    if repo == None:
        return
    repo_folder = repo.split('/')[-1].replace('.git', '')
    return repo_folder


def run_cmd(repo, path):
    cmd = f"git clone {repo} {path}"
    os.system(f"{cmd}")
    return cmd


def main(path):
    repo = get_repo_link()
    if(repo == False):
        print('Invalid Repo Link! Copy repo link in your clipboard.')
        return None
    repo_folder = get_repo_folder(repo)
    path = f"{path}/{repo_folder}"
    try:
        cmd = run_cmd(repo, path)
        print(f'{repo} Cloned Successfully!')
    except:
        print('Error Cloning')


if __name__ == "__main__":
    path = None
    path = sys.argv[1]
    main(path)
