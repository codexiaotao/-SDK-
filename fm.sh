#!/bin/bash
source /etc/profile
source /home/pi/.bashrc
cd /home/pi/myDocument/kdxf/bin
python3 /home/pi/myPySpace/QHDWeather.py | xargs ./tts_sample
cp -l weather.wav /home/pi/fm/fm_transmitter
cd /home/pi/fm/fm_transmitter
sox weather.wav -r 22050 -c 1 -b 16 -t wav - | sudo ./fm_transmitter -f 100.6 -
