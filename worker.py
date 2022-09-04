from bot import local_alerts,current_prices , alertdb ,updateLocalAlerts
import asyncio
# from datetime import datetime
from pyrogram.errors import BadRequest



async def alertChecker(client):

    
    
    while True:

        # await asyncio.sleep(5)
        # try:
        #     await client.send_message(chat_id="1212106123", text="test")
        # except BadRequest as br:
        #     if br.ID is "USER_IS_BLOCKED":
        #         print("user blocked you")
        
        # continue


        
 
        if len(local_alerts) > 0:
                for alert in local_alerts:
                    
                    
                    userid = alert["uid"]
                    alertprice = float(alert["alertprice"])
                    types = alert["type"]
                    cur = alert["currency"]
                    coin = alert["coin"].upper()+cur.upper()
                    currentCoinPrice = current_prices[coin]


                    if types == "up":
                            
                        if float(currentCoinPrice) > alertprice:

                            alertmsg  = f""" ⏰ Alert  🔼 \n  <b>{alert["coin"].upper()}</b> \n\n`{currentCoinPrice}` """
                            try:
                                await client.send_message(chat_id=userid, text=alertmsg)
                                await alertdb.delete_one(alert["_id"])
                                await updateLocalAlerts()

                            except BadRequest as br:
                                if br.ID is "USER_IS_BLOCKED":
                                    allAlerts = await alertdb.find({"uid":alert["_id"]})
                                    
                                    try:
                                        await alertdb.delete_one(alert["_id"])

                                        # ? TODO check if delete many is working properly
                                        await alertdb.delete_many(allAlerts)
                                    finally:
                                        await updateLocalAlerts()
                                else:
                                    print(br.ID)

                            except Exception as e:
                                print(e)
                            
                    
                    if types == "down":
                        
                        if float(currentCoinPrice) < alertprice:
                            alertmsg  = f""" ⏰ Alert  🔻 \n  <b>{alert["coin"].upper()}</b> \n\n`{currentCoinPrice}` """
                            try:
                                await client.send_message(chat_id=userid, text=alertmsg)
                                await alertdb.delete_one(alert["_id"])
                                await updateLocalAlerts()
                            except Exception as e:
                                print(e)
                    
                
            
        await asyncio.sleep(5)



if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(alertChecker())

