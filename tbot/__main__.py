from .TBot import get_conf
import telegram
import sys
import argparse

def main():
    parser = argparse.ArgumentParser( description='Easy Telegram', usage="TBot.py [command] options")
    parser.add_argument('command', help="Subcomand to run, for example")
    parser.add_argument('-c', help="Configuration file", default=None, dest="config")
    args = parser.parse_args(sys.argv[1:2])

    if args.config is None:
        options = get_conf()
    else:
        with open(args.config, "r") as f: content= f.readlines()
        options = [x.replace("\n","").replace(" ","").replace('"','').split("=") for x in content]
        options = {k:v for k,v in options}

    tb = telegram.Bot(token=options["token"])
    try:
        if args.command == "sendmessage":
            response = tb.sendMessage(options["chatid"], " ".join(sys.argv[2:]))

        elif args.command == "senddocument":
            tb.sendDocument(options["chatid"], open("".join(sys.argv[2:]), 'rb'))

        elif args.command == "sendimage":
            tb.sendPhoto(options["chatid"], open("".join(sys.argv[2:]), 'rb'))

        else:
            print("command not known")
    except:
        print("Failed...")
        return 0

if __name__ == "__main__":
    main()