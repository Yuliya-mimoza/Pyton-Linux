import subprocess


def checkout(command: str, text: str) -> None:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8')
    if text in result.stdout:
        return True
    else:
        return False


def checkout_negative(command: str, text: str) -> None:
    result = subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8', stderr=subprocess.PIPE)
    if text in result.stdout or text in result.stderr:
        return True
    else:
        return False


def getout(command):
    return subprocess.run(command, shell=True, stdout=subprocess.PIPE, encoding='utf-8').stdout


if __name__ == '__main__':
    command = 'cat /etc/os-release'
    text = 'VERSION="22.04.3 LTS (Jammy Jellyfish)"'
    checkout(command, text)
