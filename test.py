# from database import Database
# import aiohttp

# import config,aiohttp

# import asyncio


# current_prices ={}

# import threading

# alertdb = Database(db="bot",col="alerts")






# #  Worker Here
# async def priceworker():
#     async with aiohttp.ClientSession() as session:

#         while True:    
#             try:
#                 async with session.get(config.API_URL) as response:
#                     data  = await response.json()
#                     current_prices.update(data)
                    
#             except Exception as e:
#                 print(e)

#             await asyncio.sleep(2)
           


# async def main():
#     loop = asyncio.get_running_loop()
#     task = loop.create_task(priceworker())
#     while not task.done():
#         await asyncio.sleep(1)
#         print(current_prices)

# asyncio.run(main())