import openai

openai.api_key = "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"

def generate_image(prompt, n):
    return openai.Image.create(prompt=prompt, n=n, size="1024x1024", response_format="b64_json")

from telegram.ext import Updater, CommandHandler
import base64

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Send me a string")

def aiart(update, context):
    prompt = update.message.text.split('/aiart ')[1]
    image = generate_image(prompt, 1)
    image_base64 = base64.b64encode(image).decode('utf-8')
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=image_base64)

def main():
    token = '6172086165:AAHVfKrgQhvTn2phxiCZvpOkajZeda90EFA'
    updater = Updater(token=token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("aiart", aiart))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
