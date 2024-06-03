# Telegram Backup Bot

This bot is designed to relay messages from one channel to another, possibly with some logging functionality.

## Dependencies

- Python 3
- [Pyrofork](https://pyrofork.mayuri.my.id/main/)
- [tgcrypto](https://github.com/pyrogram/tgcrypto)

You can install the dependencies using the following commands:

```bash
pip3 install -U pyrofork tgcrypto
```

## Setup

Before running this script, make sure to obtain the following credentials:

- **API ID and Hash:**
  - Visit [my.telegram.org/auth](https://my.telegram.org/auth) and log in with your Telegram account.
  - Go to 'API development tools' and create a new application.
  - Note down the 'api_id' and 'api_hash' provided for your application.

- **Bot Token:**
  - Create a new bot on Telegram by talking to BotFather ([@BotFather](https://t.me/botfather)).
  - Obtain the token for your bot.

- **Logging Channel ID:**
  - Create a Telegram channel or group where you want to log errors and messages.
  - Obtain the numeric ID of the channel or group.
  - You can get the ID by adding the BotFather to your channel/group and using the `/my_id` command, or use the [@username_to_id_bot](https://t.me/username_to_id_bot) and input the username of your channel/group to get its numeric ID.

Once you have obtained these credentials, replace the placeholder values in the `config.py` file with your actual credentials.

## Usage

- **config.py:** This file contains your Telegram API credentials, bot token, logging channel ID, and channel mappings.
- **backup_bot.py:** This script contains the main functionality of the bot. It relays messages from source channels to destination channels, with optional logging of errors.

## Running the Bot

To run the bot, simply execute the `backup_bot.py` script. It will start listening for messages and relaying them to the configured destination channels.

```bash
python backup_bot.py
```

This will start the bot and prompt you for any required bot authentication.

Once the authentication is completed, you can run the bot in the background using the following command:

```bash
python backup_bot.py &
```
