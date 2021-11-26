import sys
import os
import clipboard


def get_repo_link():
    repo = "https://github.com/ssadev/myjsondbs.git"
    repo = clipboard.paste()
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
    repo_folder = get_repo_folder(repo)
    path = f"{path}/{repo_folder}"
    try:
        cmd = run_cmd(repo, path)
        print(f'{repo} Cloned Successfully!')
    except:
        print('Error Cloning')


if __name__ == "__main__":
    path = None
    try:
        path = sys.argv[1]
        main(path)
    except:
        pass
