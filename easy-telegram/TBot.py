import requests
import sys
import pathlib

CONFIG_PATHS = [pathlib.Path.home() / ".tbot.conf",
                pathlib.Path.home() / "tbot.conf",
                pathlib.Path(".") / ".tbot.conf",
                pathlib.Path(".") / "tbot.conf",
                pathlib.Path("/etc/tbot.conf"),
                ]


class Tbot:
    def __init__(self, token, chatid):
        self.token = token
        self.chatid = chatid

    def sendtext(self, bot_message):
        send_text = 'https://api.telegram.org/bot' + self.token + '/sendMessage?chat_id=' + self.chatid + '&parse_mode=Markdown&text=' + bot_message
        response = requests.get(send_text)
        return response.json()



import argparse
def main():
    parser = argparse.ArgumentParser( description='Easy Telegram', usage="TBot.py [command] options")
    parser.add_argument('command', help="Subcomand to run, for example")
    args = parser.parse_args(sys.argv[1:2])

    for file in CONFIG_PATHS:
        if file.exists():
            print("Found: %s" % (str(file.absolute()),))

            with open(file, "r") as f: content= f.readlines()
            options = [x.replace("\n","").replace(" ","").replace('"','').split("=") for x in content]
            options = {k:v for k,v in options}
            break

    tb = Tbot(**options)

    if args.command == "sendtext":
        response = tb.sendtext(" ".join(sys.argv[2:]))
        if not response["ok"]:
            print("Message could not be sent.")
            print(response)
    else:
        print("command not known")

if __name__ == "__main__":
    main()