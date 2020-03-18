# easy-telegram-cli

An easy CLI to telegram bot, written in python.

For now it is *only* meant to send messages from the command line, so the only implemented function is to send a message.

# Configuration
Configuration is done by placing a .tbot.conf file in one of the following directories
   * $HOME/.tbot.conf
   * $HOME/tbot.conf
   * ./.tbot.conf
   * ./tbot.conf
   * /etc/tbot.conf

The locations will be checked in the order above, that means a  tbot.conf file in $HOME is preferred over a system wide /etc/tbot.conf.

The file should contain the bot token and chat id like:
```
token="your_token_here" 
chatid="your_chat_here"
```
### Note:
  The path resolution for files has a problem when the current absolute path contains a symlink.
  When in doubt: Use absolute paths specifications to be safe!
