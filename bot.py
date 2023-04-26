from pyrogram import Client, idle
#'𓏺 𝘢 𝘍𝘪𝘶𝘯𝘺 .'#
from pyromod import listen



bot = Client(
    "mo",
    api_id=8186557,
    api_hash="efd77b34c69c164ce158037ff5a0d117",
    bot_token="6117543347:AAGDn6t7Bxz1QKojYmlI8a4_mf0s6b1LDWI",#توكن المصنع
    plugins=dict(root="MHelal")
    )

async def start_helalbot():
    print("تم تشغيل الصانع بنجاح..💗")
    await bot.start()
    hh = "LLL7P"#يوزر المطور المصنع
    try:
        await bot.send_message(hh, "**تم تشغيل الصانع بنجاح ...🥀**")
    except:
        pass
    await idle()
