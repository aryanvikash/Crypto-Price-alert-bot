from pyrogram import Client, filters



@Client.on_message(filters.command(["start"]))
async def start(_, message):


     await message.reply_text("<b>Set Alert :</b> `/set btc 12345` \n<b>Get Currency Price By sending :</b> `btc`,`ltc`,`doge` ")
