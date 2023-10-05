import pytest
from sshcheckers import ssh_checkout, ssh_getout
import random
import string
import yaml
from datetime import datetime

with open('config.yaml') as f:
    # читаем документ YAML
    data = yaml.safe_load(f)


@pytest.fixture()
def make_folders():
    # создание архива 'a'
    return ssh_checkout(data['ip'], data['user'], data['passwd'],
                        f'mkdir -p {data["folderin"]} {data["folderout"]} {data["folderext"]}', "")


@pytest.fixture()
def clear_folders():
    return ssh_checkout(data['ip'], data['user'], data['passwd'],
                        f'rm -rf {data["folderin"]}/* {data["folderout"]}/* {data["folderext"]}/*', "")


@pytest.fixture()
def make_files1():
    return ssh_checkout(data['ip'], data['user'], data['passwd'],
                        f'cd {data["folderout"]}; touch file1 file2', "")


@pytest.fixture()
def make_files2():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if ssh_checkout(data['ip'], data['user'], data['passwd'],
                        f'cd {data["folderin"]}; dd if=/dev/urandom of={filename} bs={data["bs"]} count=1 iflag=fullblock', ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=5))
    if not ssh_checkout(data['ip'], data['user'], data['passwd'],
                        f'cd {data["folderin"]}; mkdir {subfoldername}', ""):
        return None, None
    if not ssh_checkout(data['ip'], data['user'], data['passwd'],
                        f'cd {data["folderin"]}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs={data["bs"]} count=1 iflag=fullblock', ""):
        return subfoldername, None
    else:
        return subfoldername, testfilename


@pytest.fixture(autouse=True)
def print_time():
    print(f'Start: {datetime.now().strftime("%H:%M:%S.%f")}')
    yield
    print(f'Finish: {datetime.now().strftime("%H:%M:%S.%f")}')


@pytest.fixture()
def make_bad_arx():
    ssh_checkout(data['ip'], data['user'], data['passwd'],
                 f'cd {data["folderin"]}; 7z a {data["folderout"]}/arxbad -t{data["type"]}', "Everything is Ok")
    ssh_checkout(data['ip'], data['user'], data['passwd'],
                 f'truncate -s 1 {data["folderout"]}/arxbad.{data["type"]}', "Everything is Ok")
    yield "arxbad"
    ssh_checkout(data['ip'], data['user'], data['passwd'],
                 f'rm -f {data["folderout"]}/arxbad.{data["type"]}', "")


@pytest.fixture(autouse=True)
def stat():
    yield
    stat = ssh_getout(data['ip'], data['user'], data['passwd'],
                      f"cat /proc/loadavg")
    ssh_checkout(data['ip'], data['user'], data['passwd'],
                 f"echo 'time: {datetime.now().strftime('%H:%M:%S.%f')} count:{data['count']} \
    size: {data['bs']} load: {stat}'>> stat.txt", "")


@pytest.fixture()
def start_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
