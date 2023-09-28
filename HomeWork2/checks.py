import subprocess


def func_search(command_1: str, text_1: str) -> None:
    result = subprocess.run(command_1, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text_1 in result.stdout:
        return True
    else:
        return False


def func_search_negative(command_1: str, text_1: str) -> None:
    result = subprocess.run(command_1, shell=True, stdout=subprocess.PIPE, encoding='utf-8', stderr=subprocess.PIPE)
    if text_1 in result.stdout or text in result.stderr:
        return True
    else:
        return False


if __name__ == '__main__':
    command = 'cat /etc/os-release'
    text = 'VERSION="22.04.3 LTS (Jammy Jellyfish)"'
    func_search(command, text)