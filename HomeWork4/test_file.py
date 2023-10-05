# Добавить в проект тесты, проверяющие работу команд
# 'd'(удаление из архива) и 'u' (обновление архива).
# Вынести в отдельные переменные пути и папки с файлами,
# с архивами и с распакованными файлами. Выполнить тесты с ключом '-v'.

import yaml
from sshcheckers import ssh_checkout, ssh_getout, upload_files
from checks import getout

with open('config.yaml') as f:
    data = yaml.safe_load(f)


class TestPositive:

    def save_log(self, starttime, name):
        with open(name, 'w') as f:
            f.write(getout(f"journalctl --since '{starttime}'"))


    # def test_step0(self, start_time):
    #     res = []
    #     upload_files(data['ip'], data['user'], data['passwd'], data['pkgname']+'.deb',
    #                  "/home/{data['user']}/{data['pkgname']}.deb")
    #     res.append(ssh_checkout(data['ip'], data['user'], data['passwd'],
    #                f"echo '{data['passwd']}' | sudo -S dpkg -i '/home/{data['user']}/{data['pkgname']}.deb",
    #                             "Настраивается пакет"))
    #     # print(res[0])
    #     res.append(ssh_checkout(data['ip'], data['user'], data['passwd'],
    #                             f"echo '{data['passwd']}' | sudo -S dpkg -s {data['pkgname']}",
    #                             "Status: install ok installed"))
    #     self.save_log(start_time, "log1.txt")
    #     # print(res[1])
    #     assert all(res), "test0 FAIL"

    def test_step1(self, make_folders, start_time):
        # создание архива 'a'
        res1 = ssh_checkout(data['ip'], data['user'], data['passwd'],
                            f"cd {data['folderin']}; 7z a {data['folderout']}/arx2", "Everything is Ok")
        res2 = ssh_checkout(data['ip'], data['user'], data['passwd'],
                            f"ls {data['folderout']}", "arx2.7z")
        self.save_log(start_time, "log1.txt")
        assert res1 and res2, "test_step1 FAIL"


    def test_step2(self, start_time):
        # удаление из архива 'd'
        self.save_log(start_time, "log2.txt")
        assert ssh_checkout(data['ip'], data['user'], data['passwd'],
                            f'cd {data["folderout"]}; 7z d arx2.7z', 'Everything is Ok'), 'test_step2 FAIL'


    def test_step3(self, start_time):
        # обновление архива 'u'
        self.save_log(start_time, "log3.txt")
        assert ssh_checkout(data['ip'], data['user'], data['passwd'],
                            f'cd {data["folderin"]}; 7z u arx2.7z', 'Everything is Ok'), 'test_step3 FAIL'


    def test_step4(self, start_time):
        # вывод списка содержимого архива 'l'
        self.save_log(start_time, "log4.txt")
        assert ssh_checkout(data['ip'], data['user'], data['passwd'],
                            f'cd {data["folderout"]}; 7z l arx2.7z', ''), 'test_step4 FAIL'


    def test_step5(self, start_time):
        # распаковка файлов из архива со структурой директорий 'x'
        self.save_log(start_time, "log5.txt")
        assert ssh_checkout(data['ip'], data['user'], data['passwd'],
                            f'cd {data["folderout"]}; 7z x arx2.7z', ''), 'test_step5 FAIL'


# if __name__ == '__main__':
#     pytest.main(['-vv'])
