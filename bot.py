import asyncio
import os
import yt_dlp
from aiogram import Bot, Dispatcher, F, Router
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import (
    CallbackQuery,
    FSInputFile,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    Message,
)

# === ТВОЙ ТОКЕН ТЕЛЕГРАМ-БОТА ===
TELEGRAM_TOKEN = "9246243317:AAGnAyElVkCuGEQz9_exI7X4g2jVzODMjgo"

router = Router()

# Создаем папку для временных файлов, если её нет
if not os.path.exists("downloads"):
  os.makedirs("downloads")


class BotStates(StatesGroup):
  waiting_for_search_query = State()


# --- Функция поиска и скачивания музыки через YouTube ---
def download_audio_from_web(query: str):
  print(f"🔍 Ищем в интернете: '{query}'...")
  ydl_opts = {
      "format": "bestaudio[ext=m4a]/bestaudio",  # Скачиваем аудио в удобном формате без ffmpeg
      "outtmpl": "downloads/%(id)s.%(ext)s",
      "quiet": True,
      "no_warnings": True,
  }

  try:
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
      # Ищем первый подходящий ролик по запросу
      search_results = ydl.extract_info(f"ytsearch1:{query}", download=True)
      if "entries" in search_results:
        video_info = search_results["entries"][0]
      else:
        video_info = search_results

      video_id = video_info["id"]
      title = video_info.get("title", query)

      # Находим путь к скачанному файлу в папке downloads
      file_path = None
      for file in os.listdir("downloads"):
        if file.startswith(video_id):
          file_path = os.path.join("downloads", file)
          break

      return file_path, title
  except Exception as e:
    print(f"❌ Ошибка скачивания: {e}")
    return None, None


# --- Меню и интерфейс бота ---
def get_main_menu_keyboard():
  return InlineKeyboardMarkup(
      inline_keyboard=[
          [
              InlineKeyboardButton(
                  text="🔍 Найти и скачать музыку", callback_data="menu_search"
              )
          ]
      ]
  )


@router.message(Command("start"))
async def cmd_start(message: Message, state: FSMContext):
  await state.clear()
  await message.answer(
      "🎵 Привет! Я бот для скачивания музыки.\nНажми кнопку ниже и"
      " введи название трека:",
      reply_markup=get_main_menu_keyboard(),
  )


@router.callback_query(F.data == "menu_search")
async def callback_search(callback: CallbackQuery, state: FSMContext):
  await callback.message.edit_text(
      "🔍 Введите название песни или исполнителя:"
  )
  await state.set_state(BotStates.waiting_for_search_query)
  await callback.answer()


@router.message(BotStates.waiting_for_search_query)
async def process_search_input(message: Message, state: FSMContext):
  query = message.text
  await state.clear()

  status_msg = await message.answer(
      f"⏳ Ищу и скачиваю: *{query}*...\nЭто может занять несколько секунд.",
      parse_mode="Markdown",
  )

  # Запускаем скачивание в фоне, чтобы не вешать бота
  loop = asyncio.get_running_loop()
  file_path, title = await loop.run_in_executor(
      None, download_audio_from_web, query
  )

  await status_msg.delete()

  if not file_path or not os.path.exists(file_path):
    await message.answer(
        "❌ К сожалению, не удалось скачать трек. Попробуйте другой запрос.",
        reply_markup=get_main_menu_keyboard(),
    )
    return

  try:
    # Отправляем аудиофайл пользователю
    audio_file = FSInputFile(file_path)
    await message.answer_audio(
        audio=audio_file,
        caption=f"🎵 {title}",
        reply_markup=get_main_menu_keyboard(),
    )
  except Exception as e:
    print(f"Ошибка отправки файла: {e}")
    await message.answer("❌ Ошибка при отправке аудиофайла.")
  finally:
    # Удаляем файл с компьютера, чтобы не забивать диск
    if os.path.exists(file_path):
      try:
        os.remove(file_path)
      except:
        pass


# --- Точка входа ---
async def main():
  bot = Bot(token=TELEGRAM_TOKEN)
  dp = Dispatcher()
  dp.include_router(router)
  print("Бот успешно запущен и готов качать музыку!")
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())