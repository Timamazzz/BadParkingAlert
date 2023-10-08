import asyncio
import logging

from aiogram.filters.command import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types

logging.basicConfig(level=logging.INFO)
bot = Bot(token="6675710046:AAGD0IDmfKwW9sgEice0WfriTd7Q0sEafLI")
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: types.Message):
    photo_url = 'https://th.bing.com/th/id/OIG.p_m8isM9CWKncEanVuiI?pid=ImgGn'

    await message.answer_photo(photo_url,
                               caption="Здарова трудяга, здесь типа приветственное сообщение с картинкой, "
                                       "удачи тебе в жизни!")

    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Поделиться номером телефона",
        callback_data="share_contact",
        request_contact=True),
    )

    await message.answer(
        "Мобилу дай, э",
        reply_markup=builder.as_markup()
    )


'''@dp.callback_query(F.data == "share_contact")
async def share_contact(callback: types.CallbackQuery):
    user = callback.from_user
    print("phone", callback.message.contact)
    await bot.send_message(user.id, f"Вы: {user}")'''


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
