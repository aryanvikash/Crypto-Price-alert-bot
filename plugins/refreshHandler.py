from pyrogram import Client,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from bot import current_prices
from datetime import datetime
@Client.on_callback_query(filters.regex("^refresh"))
async def handlerefresh(c, m):
    cb_data = m.data

    currencyCode = cb_data.split("||")[-1]

    try:
        Inrprice = float(current_prices[currencyCode.upper()+"INR"] )
        UsdPrice = float(current_prices[currencyCode.upper()+"USDT"]) 
    except ValueError:
        return

    now = datetime.now()
        
    current_time = now.strftime("%I:%M:%S %p")
    msg  = f"<b>{currencyCode.upper()}</b> - {current_time}" + "\n\n"+ f"`{Inrprice}`" + " <b>INR </b> \n\n" +f"`{UsdPrice}`" + " <b>USD</b>"


    button = InlineKeyboardMarkup([[InlineKeyboardButton("Refresh",callback_data=f"refresh||{currencyCode}")]])
    
    try:
        await m.edit_message_text(msg, reply_markup=button)
    except :
        pass