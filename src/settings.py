import os
# Application Settings
APP_NAME = "Yasb"
APP_NAME_FULL = "Yet Another Status Bar"
APP_BAR_TITLE = "YasbBar"
SCRIPT_PATH = os.path.dirname(os.path.abspath(__file__))
GITHUB_URL = "https://github.com/amnweb/yasb"
GITHUB_THEME_URL = "https://github.com/amnweb/yasb-themes"
BUILD_VERSION = "1.7.0"
CLI_VERSION = "1.0.9"
# Development Settings
DEBUG = False
# Configuration Settings
DEFAULT_CONFIG_DIRECTORY = os.getenv('YASB_CONFIG_HOME', ".config\\yasb")
DEFAULT_STYLES_FILENAME = "styles.css"
DEFAULT_CONFIG_FILENAME = "config.yaml"
DEFAULT_LOG_FILENAME = "yasb.log"