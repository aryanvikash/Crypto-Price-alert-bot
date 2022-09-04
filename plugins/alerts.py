from pyrogram import Client, StopPropagation,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot import alertdb
@Client.on_message(filters.command(["alerts"]))
async def alert(_, message):
    results  = await alertdb.find({"uid":message.from_user.id})
    
    
    if not results:
        await message.reply_text("No Alerts")
        raise StopPropagation
    
    alertsbuttons = []
    for result in results:
            buttonText = result["coin"].upper()+" "+result["alertprice"]+" INR"
            alertsbuttons.append([InlineKeyboardButton(buttonText,callback_data=f"alertoption||{result['_id']}")])
    
    buttons = InlineKeyboardMarkup(alertsbuttons)

    await message.reply_text("All Alerts", reply_markup=buttons)