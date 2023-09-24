# Написать функцию на Python, которой передаются в качестве параметров
#  команда и текст.
# Функция должна возвращать True, если команда успешно выполнена и
# текст найден в её выводе и False в противном случае.
# Передаваться должна только одна строка, разбиение вывода использовать не нужно.

import subprocess


def func_search(command: str, text: str) -> None:
    result = subprocess.run(command, shell=True,
                            stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout
    if text in out:
        return print('True')
    else:
        return print('False')


if __name__ == '__main__':
    command = 'cat /etc/os-release'
    text = 'VERSION="22.04.3 LTS (Jammy Jellyfish)"'
    func_search(command, text)
