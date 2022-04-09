
from telethon import events 
import time 
import asyncio 
from userbot.events import register

@register(outgoing=True,pattern="^.[Ss]iri")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu siri Yazmak Yerine__ `.owen` __Yazmalısın.__\n \n**Gerekli Açıklama:** t.me/Hiraset/65 \n UserBot Kanalı: @MytUserBot\nPlugin Kanalı: @OwenPlugin")

@register(outgoing=True,pattern="^.[Ee]pic")

async def komut(event):
        await event.edit("**Alışkanlık İşte**\n __Botumuzun İsmi Değişti Unuttun mu Epic Yazmak Yerine__ `.owen` __Yazmalısın.__\n \n**Gerekli Açıklama:** https://t.me/OwenUserBot/80 \n UserBot Kanalı: @OwenUserBot\nPlugin Kanalı: @OwenPlugin")
