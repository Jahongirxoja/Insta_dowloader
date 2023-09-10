from aiogram import types
from loader import dp, bot
from aiogram.dispatcher.filters import Command, Text
from insta import instadonwload


@dp.message_handler(Text(startswith='https://www.instagram.com/'))
async def send_media(message: types.Message):
    link = message.text
    data = instadonwload(link=link)
    if data == 'Bad':
        await message.answer('Bu Url yoq')
    else:
        if data['type'] == 'image':
            await message.answer_photo(photo=data['media'])
        elif data['type'] == 'video':
            await message.answer_video(video=data['media'])
        elif data['type'] == 'carousel':
            for i in data['media']:
                await message.answer_document(document=i)
        else:
            await message.answer('Bu Url yoq')
