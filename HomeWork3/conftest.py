import pytest
from checks import checkout, checkout_negative, getout
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
    return checkout(f'mkdir -p {data["folderin"]} {data["folderout"]} {data["folderext"]}', "")


@pytest.fixture()
def clear_folders():
    return checkout(f'rm -rf {data["folderin"]}/* {data["folderout"]}/* {data["folderext"]}/*', "")


@pytest.fixture()
def make_files1():
    return checkout(f'cd {data["folderout"]}; touch file1 file2', "")


@pytest.fixture()
def make_files2():
    list_off_files = []
    for i in range(data["count"]):
        filename = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
        if checkout(f'cd {data["folderin"]}; dd if=/dev/urandom of={filename} bs={data["bs"]} count=1 iflag=fullblock', ""):
            list_off_files.append(filename)
    return list_off_files


@pytest.fixture()
def make_subfolder():
    testfilename = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=5))
    subfoldername = ''.join(random.choices(
        string.ascii_uppercase + string.digits, k=5))
    if not checkout(f'cd {data["folderin"]}; mkdir {subfoldername}', ""):
        return None, None
    if not checkout(
            f'cd {data["folderin"]}/{subfoldername}; dd if=/dev/urandom of={testfilename} bs=1M count=1 iflag=fullblock', ""):
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
    checkout(f'cd {data["folderin"]}; 7z a {data["folderout"]}/arxbad -t{data["type"]}', "Everything is Ok")
    checkout(f'truncate -s 1 {data["folderout"]}/arxbad.{data["type"]}', "Everything is Ok")
    yield "arxbad"
    checkout(f'rm -f {data["folderout"]}/arxbad.{data["type"]}', "")


@pytest.fixture(autouse=True)
def stat():
    yield
    stat = getout("cat /proc/loadavg")
    checkout(f"echo 'time: {datetime.now().strftime('%H:%M:%S.%f')} count:{data['count']} \
    size: {data['bs']} load: {stat}'>> stat.txt", "")
