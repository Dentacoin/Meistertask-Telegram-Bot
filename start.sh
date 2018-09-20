#!/bin/sh

byobu new-session -d -s $USER

# bot window
byobu rename-window -t $USER:0 'Meistertask-Telegram-Bot'
#byobu new-window -t $USER:0 'Meistertask-Telegram-Bot'
byobu send-keys "python3.7 /home/bot/bot_meistertask/bot.py" C-m
#byobu attach-session -t $USER