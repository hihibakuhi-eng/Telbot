import os
import telebot
from telebot import types

# قراءة التوكن بأمان من إعدادات السيرفر
TOKEN = os.environ.get("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def send_welcome(message):
  markup = types.InlineKeyboardMarkup(row_width=2)
  btn1 = types.InlineKeyboardButton(
      "🎮 لعبة خفيفة", callback_data="play_game"
  )
  btn2 = types.InlineKeyboardButton(
      "ℹ️ معلومات عن البوت", callback_data="info"
  )
  markup.add(btn1, btn2)

  first_name = message.from_user.first_name
  bot.send_message(
      message.chat.id,
      f"أهلاً بك يا {first_name} في البوت التفاعلي! 🚀\nاختر أحد الخيارات من الأسفل:",
      reply_markup=markup,
  )


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
  if call.data == "play_game":
    bot.answer_callback_query(call.id, "جاري تحميل اللعبة...")
    bot.send_message(
        call.message.chat.id,
        "خمن الرقم من 1 إلى 5! ارسل رقمك الآن في المحادثة 🎲",
    )
  elif call.data == "info":
    bot.send_message(
        call.message.chat.id,
        "هذا البوت تم إنشاؤه لتجربة برمجة بوتات تلجرام التفاعلية باستخدام بايثون.",
    )


bot.infinity_polling()
