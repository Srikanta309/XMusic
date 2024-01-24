import time
import random 
from pyrogram import filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message
from youtubesearchpython.__future__ import VideosSearch
import asyncio
import config
from AnonXMusic import app
from AnonXMusic.misc import _boot_
from AnonXMusic.plugins.sudo.sudoers import sudoers_list
from AnonXMusic.zexx import EMOJIOS, STICKER
from AnonXMusic.utils.database import get_served_chats, get_served_users, get_sudoers
from AnonXMusic.utils import bot_sys_stats
from AnonXMusic.utils.database import (
    add_served_chat,
    add_served_user,
    blacklisted_chats,
    get_lang,
    is_banned_user,
    is_on_off,
)
from AnonXMusic.utils.decorators.language import LanguageStart
from AnonXMusic.utils.formatters import get_readable_time
from AnonXMusic.utils.inline import help_pannel, private_panel, start_panel
from config import BANNED_USERS
from strings import get_string



YUMI_PICS = (
"https://telegra.ph/file/a5bab2979b394358a85fb.jpg",
"https://telegra.ph/file/c4d55ee5bf4b897b7c889.jpg",
"https://telegra.ph/file/5cbd0785e1ecc88e76b64.jpg",
"https://telegra.ph/file/891742a91fc82e3e500d1.jpg",
"https://telegra.ph/file/c5211b79c5227cde1dbea.jpg",
"https://telegra.ph/file/ac288f21162efea13e359.jpg",
"https://telegra.ph/file/716647c16254aa77fd189.jpg",
"https://telegra.ph/file/b8c11b32abef6fce3081f.jpg",
"https://telegra.ph/file/93fd70f204ed30e32f220.jpg",
"https://telegra.ph/file/19fa60571da4e42361ce9.jpg",
"https://telegra.ph/file/02dd4f129ba4d7a3f2813.jpg",
"https://telegra.ph/file/57e109386e8a6075eff52.jpg",
has_spoiler=True),



@app.on_message(filters.command(["start"]) & filters.private & ~BANNED_USERS)
@LanguageStart
async def start_pm(client, message: Message, _):
    await add_served_user(message.from_user.id)
    if len(message.text.split()) > 1:
        name = message.text.split(None, 1)[1]
        if name[0:4] == "help":
            keyboard = help_pannel(_)
            accha = await message.reply_text(
            text=random.choice(EMOJIOS),
            )
            await asyncio.sleep(1.3)
            await accha.edit("ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg.....")
            await asyncio.sleep(0.2)
            await accha.edit("ᴅιиg ᴅσиg ꨄ sтαятιиg.........")
            await asyncio.sleep(0.2)
            await accha.edit("ᴅιиg ᴅσиg ꨄ︎ sтαятιиg.....")
            await asyncio.sleep(0.2)
            await accha.delete()
            umm = await message.reply_sticker(sticker=random.choice(STICKER))
            await asyncio.sleep(2)
            await umm.delete()
            return await message.reply_photo(
                random.choice(YUMI_PICS),
                caption=_["help_1"].format(config.SUPPORT_CHAT),
                reply_markup=keyboard,
            )
        if name[0:3] == "sud":
            await sudoers_list(client=client, message=message, _=_)
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>sᴜᴅᴏʟɪsᴛ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
            return
        if name == "verify":
            await message.reply_text(f"ʜᴇʏ {message.from_user.first_name},\nᴛʜᴀɴᴋs ғᴏʀ ᴠᴇʀɪғʏɪɴɢ ʏᴏᴜʀsᴇʟғ ɪɴ ˹𝐓𝐚𝐫𝐠𝐞𝐭 ✘ 𝐇𝐢𝐭˼, ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ɢᴏ ʙᴀᴄᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴜsɪɴɢ ᴍᴇ.")
            if await is_on_off(2):
                sender_id = message.from_user.id
                sender_name = message.from_user.first_name
                return await bot.send_message(
                    config.LOG_GROUP_ID,
                    f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ <code>ᴠᴇʀɪғʏ ʜɪᴍsᴇʟғ</code>\n\n**ᴜsᴇʀ ɪᴅ:** {sender_id}\n**ᴜsᴇʀɴᴀᴍᴇ:** {sender_name}",
                )
            return    
        if name[0:3] == "inf":
            m = await message.reply_text("🔎")
            query = (str(name)).replace("info_", "", 1)
            query = f"https://www.youtube.com/watch?v={query}"
            results = VideosSearch(query, limit=1)
            for result in (await results.next())["result"]:
                title = result["title"]
                duration = result["duration"]
                views = result["viewCount"]["short"]
                thumbnail = result["thumbnails"][0]["url"].split("?")[0]
                channellink = result["channel"]["link"]
                channel = result["channel"]["name"]
                link = result["link"]
                published = result["publishedTime"]
            searched_text = _["start_6"].format(
                title, duration, views, published, channellink, channel, app.mention
            )
            key = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text=_["S_B_8"], url=link),
                        InlineKeyboardButton(text=_["S_B_9"], url=config.SUPPORT_CHAT),
                    ],
                ]
            )
            await m.delete()
            await app.send_photo(
                chat_id=message.chat.id,
                photo=thumbnail,
                caption=searched_text,
                reply_markup=key,
            )
            if await is_on_off(2):
                return await app.send_message(
                    chat_id=config.LOGGER_ID,
                    text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ ᴛᴏ ᴄʜᴇᴄᴋ <b>ᴛʀᴀᴄᴋ ɪɴғᴏʀᴍᴀᴛɪᴏɴ</b>.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
                )
    else:
        out = private_panel(_)
        served_chats = len(await get_served_chats())
        served_users = len(await get_served_users())
        UP, CPU, RAM, DISK = await bot_sys_stats()
        accha = await message.reply_text(
            text=random.choice(EMOJIOS),
        )
        await asyncio.sleep(1.3)
        await accha.edit("ᴅιиg ᴅσиg ꨄ︎ ѕтαятιиg........")
        await asyncio.sleep(0.2)
        await accha.edit("ᴅιиg ᴅσиg ꨄ sтαятιиg........")
        await asyncio.sleep(0.2)
        await accha.edit("ᴅιиg ᴅσиg ꨄ︎ sтαятιиg......")
        await asyncio.sleep(0.2)
        await accha.delete()
        umm = await message.reply_sticker(sticker=random.choice(STICKER))
        await asyncio.sleep(2)
        await umm.delete()
        await message.reply_photo(
            random.choice(YUMI_PICS),
            caption=_["start_2"].format(message.from_user.mention, app.mention, UP, DISK, CPU, RAM,served_users,served_chats),
            reply_markup=InlineKeyboardMarkup(out),
        )
        if await is_on_off(2):
            return await app.send_message(
                chat_id=config.LOGGER_ID,
                text=f"{message.from_user.mention} ᴊᴜsᴛ sᴛᴀʀᴛᴇᴅ ᴛʜᴇ ʙᴏᴛ.\n\n<b>ᴜsᴇʀ ɪᴅ :</b> <code>{message.from_user.id}</code>\n<b>ᴜsᴇʀɴᴀᴍᴇ :</b> @{message.from_user.username}",
            )


@app.on_message(filters.command(["start"]) & filters.group & ~BANNED_USERS)
@LanguageStart
async def start_gp(client, message: Message, _):
    out = start_panel(_)
    uptime = int(time.time() - _boot_)
    await message.reply_photo(
        random.choice(YUMI_PICS),
        caption=_["start_1"].format(app.mention, get_readable_time(uptime)),
        reply_markup=InlineKeyboardMarkup(out),
    )
    return await add_served_chat(message.chat.id)


@app.on_message(filters.new_chat_members, group=-1)
async def welcome(client, message: Message):
    for member in message.new_chat_members:
        try:
            language = await get_lang(message.chat.id)
            _ = get_string(language)
            if await is_banned_user(member.id):
                try:
                    await message.chat.ban_member(member.id)
                except:
                    pass
            if member.id == app.id:
                if message.chat.type != ChatType.SUPERGROUP:
                    await message.reply_text(_["start_4"])
                    return await app.leave_chat(message.chat.id)
                if message.chat.id in await blacklisted_chats():
                    await message.reply_text(
                        _["start_5"].format(
                            app.mention,
                            f"https://t.me/{app.username}?start=sudolist",
                            config.SUPPORT_CHAT,
                        ),
                        disable_web_page_preview=True,
                    )
                    return await app.leave_chat(message.chat.id)

                out = start_panel(_)
                await message.reply_photo(
                    random.choice(YUMI_PICS),
                    caption=_["start_3"].format(
                        message.from_user.mention,
                        app.mention,
                        message.chat.title,
                        app.mention,
                    ),
                    reply_markup=InlineKeyboardMarkup(out),
                )
                await add_served_chat(message.chat.id)
                await message.stop_propagation()
        except Exception as ex:
            print(ex)
