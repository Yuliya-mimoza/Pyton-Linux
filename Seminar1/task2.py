# выполняется под Linux
# Переписать тест ex1.sh на Python c использованием модуля subprocess.

# Делимся на команды для выполнения следующей задачи:
# Доработать тест из предыдущего задания таким образом,
# чтобы вывод сохранялся построчно в список и в тесте проверялось,
# что в этом списке есть строки VERSION="22.04.1 LTS (Jammy Jellyfish)"
# и VERSION_CODENAME=jammy .
# Проверка должна выполняться только если код возврата равен 0.

import subprocess


if __name__ == '__main__':
    result = subprocess.run('cat /etc/os-release', shell=True,
                            stdout=subprocess.PIPE, encoding='utf-8')
    out = result.stdout

if not result.returncode:
    my_list = out.split('\n')
# print(my_list)

if 'VERSION="22.04.1 LTS (Jammy Jellyfish)"' in my_list and "VERSION_CODENAME=jammy" in my_list:
    print('SUCCESS')
else:
    print("FAIL")
