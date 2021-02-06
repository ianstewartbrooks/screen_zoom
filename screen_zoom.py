import os
import pyautogui as pag
from configparser import ConfigParser


class ScreenZoom(object):
    def __init__(self):
        self.config = ConfigParser()
        self.config_file_name = "config.ini"
        self.zoom_state = False

    def disable_zoom(self):
        # Trigger the windows shortcut for disabling zoom
        pag.hotkey('win', 'esc')

    def enable_zoom(self):
        # Trigger windows shortcut for launching zoom.
        pag.hotkey('win', 'add')

    def create_config(self):
        # Create a config file to save zoom state value
        self.config.add_section('main')
        self.config.set('main', 'zoom', str(self.zoom_state))

        with open(self.config_file_name, 'w') as f:
            self.config.write(f)

    def read_config(self):
        # Read last zoom state from the config file
        self.config.read(self.config_file_name)
        self.zoom_state = self.config.getboolean("main", "zoom")

    def update_config(self):
        # Update the config file with the latest zoom state value
        self.config.set('main', 'zoom', str(self.zoom_state))

        with open(self.config_file_name, 'w') as f:
            self.config.write(f)

    def change_zoom_state(self):
        # Get the stored zoom state, if it exists, and then
        # switch it eg False to True, True to False

        # if the config file doesn't exist then create it
        if not os.path.isfile(self.config_file_name):
            self.create_config()

        self.read_config()

        # Flip zoom state
        self.zoom_state = not self.zoom_state

        if self.zoom_state:
            self.enable_zoom()
        else:
            self.disable_zoom()

        self.update_config()