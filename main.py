import logging
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from aiogram.enums import ParseMode
from aiogram.types import FSInputFile
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.client.default import DefaultBotProperties
from PIL import Image
import io

TOKEN = '8437894095:AAEr0NYMmxdSV1PYaRG8zeQ2bYa4_Z_Saos'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

@dp.message(F.photo)
async def get_photo_info(message: Message):
    photo = message.photo[-1]  # eng sifatli rasm
    file = await bot.get_file(photo.file_id)
    file_path = file.file_path
    file_data = await bot.download_file(file_path)

    image = Image.open(io.BytesIO(file_data.read()))
    width, height = image.size
    pixel_count = width * height

    await message.answer(f"📸 Rasm o‘lchami: {width} × {height} piksel\n🧮 Jami: {pixel_count:,} piksel")

@dp.message()
async def echo_text(message: Message):
    await message.answer("Rasm yuboring, men sizga undagi piksel sonini aytaman!")

if __name__ == '__main__':
    import asyncio
    asyncio.run(dp.start_polling(bot))
