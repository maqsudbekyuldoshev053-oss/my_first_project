import asyncio
from aiogram import Bot, Dispatcher, Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import Message, KeyboardButton, BotCommand, BufferedInputFile, InputProfilePhotoStatic, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

bot = Bot('7874681745:AAFb_km4wx4lHNfD-MAYK9OmabOhLdB0ORs')


dp = Dispatcher(storage=MemoryStorage())
router = Router()
dp.include_router(router)


class Setting(StatesGroup):
    set_name = State()
    set_short_description = State()
    set_profile_photo = State()
    set_long_description = State()


@dp.message(Command('start'))
async def handle_start(message: Message):
    rkm = ReplyKeyboardBuilder()
    rkm.add(
        KeyboardButton(text='Set name', style='danger'),
        KeyboardButton(text='Set Short Description', style='primary'),
        KeyboardButton(text='Set Profile Photo', style='success'),
        KeyboardButton(text='Set Long Description', style='danger')
    )
    rkm.adjust(2)
    await message.answer('Xush kelibsiz', reply_markup=rkm.as_markup(resize_keyboard=True))


@dp.message(lambda msg: msg.text == 'Set name')
async def handle_new_name(message: Message, state: FSMContext):
    await message.answer('Yangi nom kiriting: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Setting.set_name)


@dp.message(Setting.set_name)
async def changing_name(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.set_my_name(message.text)

    await message.answer("Botning nomi updated boldi ✅")


@dp.message(lambda msg: msg.text == 'Set Short Description')
async def handle_new_description(message: Message, state: FSMContext):
    await message.answer('Yangi qisqa description kiriting: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Setting.set_short_description)


@dp.message(Setting.set_short_description)
async def changing_description(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.set_my_short_description(message.text)
    await message.answer('Description muvaffaqiyatli ozgartirildi✅')


@dp.message(lambda msg: msg.text == 'Set Profile Photo')
async def handle_new_description(message: Message, state: FSMContext):
    await message.answer('Profil uchun rasm yuboring: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Setting.set_profile_photo)


@dp.message(Setting.set_profile_photo)
async def changing_description(message: Message, bot: Bot, state: FSMContext):
    if not message.photo:
        await message.answer('Rasm yuboring', reply_markup=ReplyKeyboardRemove())
        return

    photo = message.photo[-1]

    file = await bot.get_file(photo.file_id)
    file_bytes = await bot.download_file(file.file_path)

    input_file = BufferedInputFile(
        file_bytes.read(),
        filename="profile.jpg"
    )
    profile_photo_ = InputProfilePhotoStatic(photo=input_file)
    await bot.set_my_profile_photo(photo=profile_photo_)

    await message.answer("Profil rasm muvaffaqiyatli ozgartirildi ✅")
    await state.clear()

@dp.message(lambda msg: msg.text == 'Set Long Description')
async def handle_long_description(message: Message, state: FSMContext):
    await message.answer('Bot uchun uzun description yozing: ', reply_markup=ReplyKeyboardRemove())
    await state.set_state(Setting.set_long_description)

@dp.message(Setting.set_long_description)
async def changing_long_description(message: Message, bot: Bot, state: FSMContext):
    await state.clear()
    await bot.set_my_description(message.text)
    await message.answer('Long description ozgartirildi ✅')


async def startup(bot: Bot):
    await bot.set_my_commands([BotCommand(command='start', description='start')])


async def main() -> None:
    dp.startup.register(startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())