from telethon import TelegramClient
API_KEY="2930013"
API_HASH="7cab92dcd979add511b79d693775e17d"
#my.telegram.org adresinden alın
bot = TelegramClient('userbot',API_KEY,API_HASH)
bot.start()

#Bu komut dosyası botunuzu çalıştırmaz, sadece bir oturum oluşturur.
