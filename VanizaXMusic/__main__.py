import asyncio
import importlib

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from VanizaXMusic import LOGGER, app, userbot
from VanizaXMusic.core.call import Hotty
from VanizaXMusic.misc import sudo
from VanizaXMusic.plugins import ALL_MODULES
from VanizaXMusic.utils.database import get_banned_users, get_gbanned
from config import BANNED_USERS


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER(__name__).error("Assistant client variables not defined, exiting...")
        exit()
    await sudo()
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("VanizaXMusic.plugins" + all_module)
    LOGGER("VanizaXMusic.plugins").info("Successfully Imported Modules...")
    await userbot.start()
    await Hotty.start()
    try:
        await Hotty.stream_call("https://graph.org/file/e999c40cb700e7c684b75.mp4")
    except NoActiveGroupCall:
        LOGGER("VanizaXMusic").error(
            "Please turn on the videochat of your log group\channel.\n\nStopping Bot..."
        )
        exit()
    except:
        pass
    await Hotty.decorators()
    LOGGER("VanizaXMusic").info(
        "ᴅʀᴏᴘ ʏᴏᴜʀ ɢɪʀʟꜰʀɪᴇɴᴅ'ꜱ ɴᴜᴍʙᴇʀ ᴀᴛ @ᴠᴀɴɪᴢᴀ_ ᴊᴏɪɴ @ᴠᴀɴɪᴢᴀ_ʙᴏᴛ , @ᴠᴀɴɪᴢᴀ_ᴡᴏʀʟᴅ ꜰᴏʀ ᴀɴʏ ɪꜱꜱᴜᴇꜱ"
    )
    await idle()
    await app.stop()
    await userbot.stop()
    LOGGER("VanizaXMusic").info("Stopping Vaniza Music Bot...")


if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(init())
