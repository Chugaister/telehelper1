import configparser, logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, ChatJoinRequest

logging.basicConfig(level=logging.INFO)

config = configparser.ConfigParser()
config.read('config.ini')
channels = [int(id) for id in config["CHANNEL"].values()]
admins = [int(id) for id in config["ADMIN"].values()]

bot = Bot(config["BOT"]["token"])
dp = Dispatcher(bot)

@dp.message_handler(commands=["start"])
async def sendWelcome(msg: Message):
    await msg.answer("Greetings!")

@dp.chat_join_request_handler(lambda req: req.chat.id in channels)
async def handleJoinRequest(req: ChatJoinRequest):
    await bot.approve_chat_join_request(
        req.chat.id,
        req.from_user.id)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
