from bot import updateLocalAlerts,current_prices
from pyrogram import Client, StopPropagation, filters
from utils import isvalidAlert
from config import API_URL
from bot import alertdb
@Client.on_message(filters.command(["set"]))
async def alert(_, message):

        if not isvalidAlert(message):
                await message.reply_text("InValid format use `\set btc 1234`")
                return


        coin = message.command[-2]
        alertPrice = message.command[-1] 



        try:
                current_prices[coin.upper()+"INR"]
        except KeyError:
                await message.reply_text("No Currency Found For this Keyword")
                return


        
        types = None
        alertPrice =   float(alertPrice)
        currentPrice = float(current_prices[coin.upper()+"INR"])

        

#  Here < working reverse don't know why
        if alertPrice < currentPrice:
               
                types = "down"
        
        if alertPrice > currentPrice:
              
                types = "up"
        
        

        currency  = "INR"

        res = await alertdb.insert({"alertprice": str(alertPrice),"currency": currency, "type": types,"coin":coin ,"uid":message.from_user.id})

        result  = await alertdb.find_one({"_id":res.inserted_id})

        emoji  = "🔻" if types == "down" else "🔼"

        
        try:    
                alertText = f"""{emoji} 🔔 Alert Added ✅ \n 
Price: <b>{result['currency']}</b> `{currentPrice}`\n
Alert Price: <b>{result['currency']} </b> `{result['alertprice']}`

"""
                await message.reply_text(alertText)
                await updateLocalAlerts()
        except Exception as e:
                await message.reply_text(f"<b> Failed To add  Alert </b> \n`{e}`")








