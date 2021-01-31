# Screen Zoom
# Python 3.8.5
# This small script turns on Windows Magnifier or closes it.
# The script is bound to the middle mouse button on my mouse meaning I can quickly switch between magnifier mode or normal mode
# quickly

# TODO: Turn it into a class

import os
import pyautogui as pag
from configparser import ConfigParser

# Globals
config = ConfigParser()
config_file_name = "config.ini"
zoom_state = False


def disable_zoom():
    # Trigger the windows shortcut for disabling zoom
    pag.hotkey('win', 'esc')


def enable_zoom():
    # Trigger windows shortcut for launching zoom.
    pag.hotkey('win', 'add')


def create_config():
    global configp, zoom_state, config_file_name

    # config.read(config_file_name)
    config.add_section('main')
    config.set('main', 'zoom', str(zoom_state))

    with open(config_file_name, 'w') as f:
        config.write(f)


def read_config():
    global config, zoom_state, config_file_name

    config.read(config_file_name)
    zoom_state = config.getboolean("main", "zoom")


def update_config():
    global configp, zoom_state, config_file_name

    # config.read(config_file_name)
    config.set('main', 'zoom', str(zoom_state))

    with open(config_file_name, 'w') as f:
        config.write(f)


# if the config file doesn't exist then create it
if not os.path.isfile(config_file_name):
    create_config()

read_config()

# Flip zoom state
zoom_state = not zoom_state

if zoom_state:
    enable_zoom()
else:
    disable_zoom()

update_config()
