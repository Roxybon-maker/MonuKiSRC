# session.py

from pyrogram import Client, filters
from devgagan import app
from config import API_ID as api_id, API_HASH as api_hash
from devgagan.core.mongo import db
from pyrogram.errors import (
    ApiIdInvalid,
    PhoneNumberInvalid,
    PhoneCodeInvalid,
    PhoneCodeExpired,
    SessionPasswordNeeded,
    PasswordHashInvalid
)
import random
import string

def generate_random_name(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@app.on_message(filters.command("session"))
async def session_generate(_, message):
    user_id = message.chat.id
    await message.reply("📞 Please enter your phone number with the country code. \nExample: +919876543210\n\n⚠️ Use a secondary Telegram account.")
    
    try:
        number = await _.ask(user_id, "Waiting for phone number...", filters=filters.text, timeout=300)
        phone_number = number.text
    except:
        await message.reply("❌ Timeout. Please try again.")
        return

    session_name = f"session_{generate_random_name()}"
    client = Client(session_name, api_id, api_hash)

    await client.connect()

    try:
        code = await client.send_code(phone_number)
    except ApiIdInvalid:
        await message.reply("❌ Invalid API ID or HASH.")
        return
    except PhoneNumberInvalid:
        await message.reply("❌ Invalid phone number.")
        return

    try:
        otp = await _.ask(user_id, "📩 Enter the OTP (Example: 1 2 3 4 5):", filters=filters.text, timeout=300)
        otp_code = otp.text.replace(" ", "")
        await client.sign_in(phone_number, code.phone_code_hash, otp_code)
    except PhoneCodeInvalid:
        await message.reply("❌ Invalid OTP.")
        return
    except PhoneCodeExpired:
        await message.reply("❌ OTP expired.")
        return
    except SessionPasswordNeeded:
        try:
            pw_msg = await _.ask(user_id, "🔐 Two-step verification enabled. Enter your password:", filters=filters.text, timeout=300)
            await client.check_password(password=pw_msg.text)
        except PasswordHashInvalid:
            await message.reply("❌ Incorrect password.")
            return

    string_session = await client.export_session_string()
    await db.set_session(user_id, string_session)
    await client.disconnect()
    
    await message.reply(f"✅ Session Generated!\n\n`{string_session}`\n\n⚠️ **Keep it private!**\n\n__Powered by @xTaR_Force_Sub")
