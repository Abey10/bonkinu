#!/bin/bash

screen -XS CSubot1 kill
screen -XS CSubot2 kill
screen -XS CSubot3 kill
screen -XS CSubot4 kill

screen -dmS CSubot1 python3 ubot1.py
screen -dmS CSubot2 python3 ubot2.py
screen -dmS CSubot3 python3 ubot3.py
screen -dmS CSubot4 python3 ubot4.py

echo "!"
