# Добавить в проект тесты, проверяющие работу команд
# 'd'(удаление из архива) и 'u' (обновление архива).
# Вынести в отдельные переменные пути и папки с файлами,
# с архивами и с распакованными файлами. Выполнить тесты с ключом '-v'.
# Дополнить проект тестами, проверяющими команды вывода списка файлов (l) и разархивирования с путями (x).

from checks import func_search
import pytest

folderin = '/home/yuliya/PycharmProjects/pythonProject/LinuxSeminar2/test'
folderout = '/home/yuliya/PycharmProjects/pythonProject/LinuxSeminar2/out'
folderext = '/home/yuliya/PycharmProjects/pythonProject/LinuxSeminar2/folder'


# def test_step1():
#     # создание архива 'a'
#     assert func_search(f'cd {folderin}; 7z a {folderout}/arh1', 'Everything is Ok'), 'test_step1 FAIL'


# def test_step2():
#     # удаление из архива 'd'
#     assert func_search(f'cd {folderout}; 7z d arh1.7z', 'Everything is Ok'), 'test_step2 FAIL'


# def test_step3():
#     # обновление архива 'u'
#     assert func_search(f'cd {folderext}; 7z u {folderout}/arh1', 'Everything is Ok'), 'test_step3 FAIL'


# def test_step4():
#     # вывод списка содержимого архива 'l'
#     assert func_search(f'cd {folderout}; 7z l arh1.7z', 'file3'), 'test_step4 FAIL'


def test_step5():
    # распаковка файлов из архива со структурой директорий 'x'
    assert func_search(f'cd {folderout}; 7z x arh1.7z', 'file3'), 'test_step5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])