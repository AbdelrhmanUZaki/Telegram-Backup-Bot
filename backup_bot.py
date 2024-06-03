# Importing necessary modules and classes
from pyrogram import filters
from pyrogram.types import Message
from config import app, channel_mappings, logging_channel
from time import sleep

# Initializing variables
username = None
title = None

# Function to handle incoming messages
@app.on_message(filters.chat(list(channel_mappings.keys())))
async def main(client, message: Message):
    try:
        # Try to extract username and title of the chat
        if message.chat.username:
            username = message.chat.username
        if message.chat.title:
            title = message.chat.title
    except Exception as e:
        # Log any errors occurred during extraction
        error = f"""
            Error while getting username and title...\n\nChat id: {message.chat.id}\n\nUsername: @{username}\n\nTitle: {title}\n\n{e}"""
        sleep(3)
        await app.send_message(logging_channel, error)

    # Get source and destination channels
    source_channel = message.chat.id
    destination_channel = channel_mappings.get(source_channel)

    # If the message is forwarded
    if message.forward_from_chat is not None or message.forward_from is not None:
        # Forward the message to destination channel
        try:
            sleep(3)
            await app.forward_messages(chat_id=destination_channel, from_chat_id=source_channel,
                                          message_ids=message.id)
        except Exception as e:
            # Log any errors occurred during forwarding
            error = f"""
            Error occurred while forwarding a message...\n\nChat id: {message.chat.id}\n\nUsername: @{username}\n\nTitle: {title}\n\n{e}"""
            sleep(3)
            await app.send_message(logging_channel, error)

    else:
        # Copy the message to destination channel
        try:
            sleep(3)
            await app.copy_message(chat_id=destination_channel, from_chat_id=source_channel, message_id=message.id)
        except Exception as e:
            # Log any errors occurred during copying
            error = f"""
            Error occurred while copying a message...\n\nChat id: {message.chat.id}\n\nUsername: @{username}\n\nTitle: {title}\n\n{e}"""
            sleep(3)
            await app.send_message(logging_channel, error)

# Main block
if __name__ == "__main__":
    while True:
        try:
            # Run the Pyrogram app instance
            app.run()

        except Exception as e:
            # Catch any exceptions and log them
            error = f"app.run() has an error, bot will be restarted:\n\n{e}"
            sleep(3)
            app.send_message(logging_channel, error)
