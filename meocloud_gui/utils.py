import sys
import os
import math
from meocloud_gui.preferences import Preferences
from meocloud_gui.settings import (CLOUD_HOME_DEFAULT_PATH, UI_CONFIG_PATH)


def create_required_folders():
    prefs = Preferences()
    
    cloud_home = prefs.get('Advanced', 'Folder', CLOUD_HOME_DEFAULT_PATH)

    if not os.path.exists(cloud_home):
        os.makedirs(cloud_home)
    if not os.path.exists(UI_CONFIG_PATH):
        os.makedirs(UI_CONFIG_PATH)


def create_startup_file():
    folder_path = os.path.join(os.path.expanduser('~'),
                               '.config/autostart')
    file_path = os.path.join(folder_path, 'meocloud.desktop')

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    desktop_file = open(file_path, 'w')
    desktop_file.write("[Desktop Entry]\n")
    desktop_file.write("Type=Application\n")
    desktop_file.write("Name=MEO Cloud\n")
    desktop_file.write("Exec=" + os.path.join(os.getcwd(),
                       "meocloud-gui") + "\n")
    desktop_file.close()


def test_already_running(pid_path, proc_name):
    try:
        with open(pid_path) as f:
            pid = int(f.read())
        with open('/proc/{0}/cmdline'.format(pid)) as f:
            if proc_name in f.read():
                assert pid != 0
                return pid
    except Exception:
        # Either the application is not running or we have no way
        # to find it, so assume it is not running.
        pass
    return False


def get_own_dir(own_filename):
    if getattr(sys, "frozen", False):
        own_path = sys.executable
    else:
        own_path = os.path.join(os.getcwd(), own_filename)
    return os.path.dirname(own_path)


def get_proxy(ui_config):
    proxy_url = ui_config.get('Network', 'ProxyURL', None)
    if proxy_url is None:
        proxy_url = os.getenv('http_proxy') or os.getenv('https_proxy')
    return proxy_url


def get_ratelimits(ui_config):
    download_limit = int(ui_config.get('Network', 'ThrottleDownload', 0))
    upload_limit = int(ui_config.get('Network', 'ThrottleUpload', 0))

    return download_limit, upload_limit
    

def convert_size(size):
    if size > 0:
        size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
        i = int(math.floor(math.log(size,1024)))
        p = math.pow(1024,i)
        s = round(size/p,2)
        if (s > 0):
            return '%s %s' % (s,size_name[i])
        else:
            return '0 B'
    else:
        return '0 B'
