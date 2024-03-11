#!/bin/bash

file=$(mktemp)
python .make/switch_device.py $file
device=$(cat $file)

sed -i.backup -E -e "s/^\s*(DEVICE_FLASH\=)stm8\w+\s*\$/\1${device}/" .make/Makefile-sdcc
echo Switched to $device.
