import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/efe1fe3be3414134a448e.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm URANIUM ROBOT.** \n\n"
  TEXT += "♨️ **I'ᴍ Wᴏʀᴋɪɴɢ Pʀᴏᴘᴇʀʟʏ** \n\n"
  TEXT += f"♨️ **Mʏ Mᴀsᴛᴇʀ : [ᴜʀᴀɴɪᴜᴍ](https://t.me/THE_URANIUM)** \n\n"
  TEXT += f"♨️ **Lɪʙʀᴀʀʏ Vᴇʀsɪᴏɴ :** `{telever}` \n\n"
  TEXT += f"♨️ **Tᴇʟᴇᴛʜᴏɴ Vᴇʀsɪᴏɴ :** `{tlhver}` \n\n"
  TEXT += f"♨️ **Pʏʀᴏɢʀᴀᴍ Vᴇʀsɪᴏɴ :** `{pyrover}` \n\n"
  TEXT += "**Tʜᴀɴᴋs Fᴏʀ Aᴅᴅɪɴɢ Mᴇ Hᴇʀᴇ ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/URANIUMxROBOT?start=help"), Button.url("Support", "https://t.me/URANIUMXSUPPORT")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
