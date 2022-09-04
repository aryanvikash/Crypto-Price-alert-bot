from pyrogram import Client, ContinuePropagation 

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import current_prices

from datetime import datetime

@Client.on_message()
async def onMessage(_, message):
    if(message.text.startswith("/")):
        raise ContinuePropagation

    try:
        Inrprice = float(current_prices[message.text.upper()+"INR"] )
        UsdPrice = float(current_prices[message.text.upper()+"USDT"]) 

        now = datetime.now()
        
        current_time = now.strftime("%I:%M:%S %p")
        msg  = f"<b>{message.text.upper()}</b> - {current_time}" + "\n\n"+ f"`{Inrprice}`" + " <b>INR </b> \n\n" +f"`{UsdPrice}`" + " <b>USD</b>"
     
        button = InlineKeyboardMarkup([[InlineKeyboardButton("Refresh",callback_data=f"refresh||{message.text}")]])
      
        await message.reply_text(msg,reply_markup=button)
        
    except KeyError:
        await message.reply_text("Currency Not Found")
