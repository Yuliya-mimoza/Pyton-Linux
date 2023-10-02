# Добавить в проект тесты, проверяющие работу команд
# 'd'(удаление из архива) и 'u' (обновление архива).
# Вынести в отдельные переменные пути и папки с файлами,
# с архивами и с распакованными файлами. Выполнить тесты с ключом '-v'.
import pytest
import yaml
from checks import checkout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:

    def test_step1(self, make_folders):
        # создание архива 'a'
        assert checkout(f"cd {data['folderin']}; 7z a {data['folderout']}/arh1", 'Everything is Ok'), 'test_step1 FAIL'


    # def test_step2(self):
    #     # удаление из архива 'd'
    #     assert checkout(f'cd {data["folderout"]}; 7z d arh1.7z', 'Everything is Ok'), 'test_step2 FAIL'

    #
    # def test_step3(self):
    #     # обновление архива 'u'
    #     assert checkout(f'cd {data["folderext"]}; 7z u {data["folderout"]}/arh1', 'Everything is Ok'), 'test_step3 FAIL'
    #
    #
    # def test_step4(self):
    #     # вывод списка содержимого архива 'l'
    #     assert checkout(f'cd {data["folderout"]}; 7z l arh1.7z', ''), 'test_step4 FAIL'
    #
    #
    # def test_step5(self):
    #     # распаковка файлов из архива со структурой директорий 'x'
    #     assert checkout(f'cd {data["folderout"]}; 7z x arh1.7z', ''), 'test_step5 FAIL'


if __name__ == '__main__':
    pytest.main(['-vv'])
