# Создать отдельный файл для негативных тестов.
# Функцию проверки вынести в отдельную библиотеку.
# Повредить архив (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки 'e'.

from checks import checkout_negative
import pytest

folderin = '/home/yuliya/PycharmProjects/pythonProject/LinuxSeminar2/test'
folderout = '/home/yuliya/PycharmProjects/pythonProject/LinuxSeminar2/out'
folderext = '/home/yuliya/PycharmProjects/pythonProject/LinuxSeminar2/folder'


def test_step1():
    assert func_search_negative(f'cd {folderout}; 7z e arch1.7z -o{folderext}', 'ERROR'), 'test_step1 FAIL'

#

if __name__ == '__main__':
    pytest.main(['-vv'])