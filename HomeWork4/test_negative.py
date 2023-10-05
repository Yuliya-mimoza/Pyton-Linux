# Создать отдельный файл для негативных тестов.
# Функцию проверки вынести в отдельную библиотеку.
# Повредить архив (например, отредактировав его в текстовом редакторе).
# Написать негативные тесты работы архиватора с командами распаковки 'e'.

from sshcheckers import ssh_checkout_negative
from checks import getout
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

class TestNegative:

    def save_log(self, starttime, name):
        with open(name, 'w') as f:
            f.write(getout(f"journalctl --since '{starttime}'"))

    def test_step1_negative(self, start_time):
        self.save_log(start_time, "log1_negative.txt")
        assert ssh_checkout_negative(data['ip'], data['user'], data['passwd'],
                                     f"cd {data['folderout']}; 7z e ar2.7z -o{data['folderext']}",
                                     'ERROR'), 'test_step1_negative FAIL'

#

# if __name__ == '__main__':
#     pytest.main(['-vv'])