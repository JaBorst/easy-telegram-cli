# import requests
import sys
import pathlib
from urllib.parse import quote
import telegram

CONFIG_PATHS = [pathlib.Path.home() / ".tbot.conf",
                pathlib.Path.home() / "tbot.conf",
                pathlib.Path(".") / ".tbot.conf",
                pathlib.Path(".") / "tbot.conf",
                pathlib.Path("/etc/tbot.conf"),
                ]
def get_conf():
    for file in CONFIG_PATHS:
        if file.exists():
            print("Found: %s" % (str(file.absolute()),))

            with open(file, "r") as f: content = f.readlines()
            options = [x.replace("\n", "").replace(" ", "").replace('"', '').split("=") for x in content]
            options = {k: v for k, v in options}
            break
    return options
