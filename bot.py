from pyrogram import Client, idle
#'𓏺 𝘢 𝘍𝘪𝘶𝘯𝘺 .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=22654154,
    api_hash="cf260fa60f76561cb6bf47a12241669b",
    bot_token="5951393602:AAF8T1OcnYQn-AsJmEjcxjpTMTQJXhmORW4",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "T_4IJ"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
