#!/bin/bash
result=$(cat /etc/os-release)
if [[ $result == *"22.04.1"* && $result == *"jammy"* && $? == 0 ]];
then echo "SUCCESS"
else echo "FAIL"
fi