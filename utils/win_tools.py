import os 

def get_desktop_path():
    return os.path.join(os.environ["USERPROFILE"], "Desktop")

