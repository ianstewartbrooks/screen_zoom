import os
import pyautogui as pag
from configparser import ConfigParser


class ScreenZoom(object):
    def __init__(self):
        self._config = ConfigParser()
        self._config_file_name = "config.ini"
        self._zoom_state = False

    def _disable_zoom(self):
        # Trigger the windows shortcut for disabling zoom
        pag.hotkey('win', 'esc')

    def _enable_zoom(self):
        # Trigger windows shortcut for launching zoom.
        pag.hotkey('win', 'add')

    def _create_config(self):
        # Create a config file to save zoom state value
        self._config.add_section('main')
        self._config.set('main', 'zoom', str(self._zoom_state))

        with open(self._config_file_name, 'w') as f:
            self._config.write(f)

    def _read_config(self):
        # Read last zoom state from the config file
        self._config.read(self._config_file_name)
        self._zoom_state = self._config.getboolean("main", "zoom")

    def _update_config(self):
        # Update the config file with the latest zoom state value
        self._config.set('main', 'zoom', str(self._zoom_state))

        with open(self._config_file_name, 'w') as f:
            self._config.write(f)

    def change_zoom_state(self):
        # Get the stored zoom state, if it exists, and then
        # switch it eg False to True, True to False

        # if the config file doesn't exist then create it
        if not os.path.isfile(self._config_file_name):
            self._create_config()

        self._read_config()

        # Flip zoom state
        self._zoom_state = not self._zoom_state

        if self._zoom_state:
            self._enable_zoom()
        else:
            self._disable_zoom()

        self._update_config()