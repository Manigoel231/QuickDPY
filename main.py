# GrowBot created by JordanIsADev
# (C) 2024 JordanIsADev
# MIT LICENSE

# Importing necessary modules
import os
import json
from src.handler.event_handler import create_bot
from src.handler.event_handler import main
import asyncio

# Banner
banner = r'''
   ____        _      _    _____  _______     __
  / __ \      (_)    | |  |  __ \|  __ \ \   / /
 | |  | |_   _ _  ___| | _| |  | | |__) \ \_/ / 
 | |  | | | | | |/ __| |/ / |  | |  ___/ \   /  
 | |__| | |_| | | (__|   <| |__| | |      | |   
  \___\_\\__,_|_|\___|_|\_\_____/|_|      |_|   
                                                
[#] QuickDPY - DiscordPY Bot
[!] Github: https://github.com/jordanisadev
'''

# Functions to load config files
def load_config():
    with open('config/config.json') as config_file:
        return json.load(config_file)
config = load_config()

if __name__ == '__main__':
    print(banner)
    asyncio.run(main())