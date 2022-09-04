
from bot import updateLocalAlerts, priceworker
import config
from pyrogram import Client, idle
from worker import alertChecker
import  asyncio
plugins = dict(
    root="plugins",
)

app = Client(
    "CrptoBot",
    bot_token=config.BOT_TOKEN,
    api_id=config.APP_ID,
    api_hash=config.API_HASH,
    plugins=plugins,
    workers=20
).start()


loop = asyncio.get_event_loop()
# asyncio.set_event_loop(loop)
FirstRunTask = loop.create_task(updateLocalAlerts())
priceTask = loop.create_task(priceworker())
alertTask = loop.create_task(alertChecker(app))

all_task = asyncio.gather(priceTask,alertTask,FirstRunTask)

try:
    loop.run_until_complete(all_task)
except asyncio.CancelledError:
    pass


idle()
app.stop()


# signal.signal(signal.SIGINT,sys.exit(0) )

