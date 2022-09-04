from pyrogram import Client, StopPropagation,filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bson.objectid import ObjectId

from bot import current_prices,alertdb
from datetime import datetime
@Client.on_callback_query(filters.regex("^alertoption"))
async def handleAlert(c, m):
    cb_data = m.data

    _id = cb_data.split("||")[-1]


    button = InlineKeyboardMarkup([
        [InlineKeyboardButton("Yes Delete 🗑",callback_data=f"dyes||{_id}")],
        [InlineKeyboardButton("No",callback_data=f"dno||{_id}")]
        ])
    
    try:
        await m.edit_message_text("Delete ?", reply_markup=button)
    except :
        pass



@Client.on_callback_query(filters.regex("^dyes"))
async def yesdeleteAlert(c, m):
        id = m.data.split("||")[-1]
        
        try:
            result  =  await alertdb.delete_one(ObjectId(id))
            print(result.deleted_count,id)
            await m.edit_message_text("Deleted Successfully !!")
        except Exception as e:
            print(e)
            pass

@Client.on_callback_query(filters.regex("^dno"))
async def nodeleteAlert(c, m):
    results  = await alertdb.find({"uid":m.from_user.id})
    
    
    if not results:
        await m.edit_message_text("No Alerts")
        raise StopPropagation
    
    alertsbuttons = []
    for result in results:
            buttonText = result["coin"].upper()+" "+result["alertprice"]+" INR"
            alertsbuttons.append([InlineKeyboardButton(buttonText,callback_data=f"alertoption||{result['_id']}")])
    
    buttons = InlineKeyboardMarkup(alertsbuttons)

    await m.edit_message_text("All Alerts", reply_markup=buttons)