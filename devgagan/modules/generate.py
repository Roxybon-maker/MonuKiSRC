from pyrogram import Client, filters
from pyrogram.types import StringSession, Message
from pyrogram.errors import (
    ApiIdInvalid, PhoneNumberInvalid, PhoneCodeInvalid, PhoneCodeExpired,
    SessionPasswordNeeded, PasswordHashInvalid
)
from config import API_ID, API_HASH
from devgagan.core.mongo import db  # ensure this has `set_session`


@app.on_message(filters.command("session") & filters.private)
async def generate_user_session(client, message: Message):
    user_id = message.from_user.id
    await message.reply("📱 Send your phone number with country code (e.g. +911234567890):")

    try:
        phone = await client.listen(user_id, timeout=60)
        phone_number = phone.text.strip()
    except:
        return await message.reply("❌ Timeout. Please try again with /session")

    user_client = Client(
        name="gen",
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=StringSession()
    )

    try:
        await user_client.connect()
        sent_code = await user_client.send_code(phone_number)
        await message.reply("🔐 OTP sent! Now send the OTP code here:")

        otp = await client.listen(user_id, timeout=60)
        code = otp.text.strip()

        try:
            await user_client.sign_in(phone_number, sent_code.phone_code_hash, code)
        except SessionPasswordNeeded:
            await message.reply("🔒 Your account has 2FA enabled. Send your password:")
            pwd = await client.listen(user_id, timeout=60)
            await user_client.check_password(pwd.text.strip())

        string_session = user_client.export_session_string()
        await db.set_session(user_id, string_session)

        await message.reply(
            f"✅ Session generated successfully!\n\n"
            f"`{string_session}`\n\n"
            "⚠️ Save it securely. Do **NOT** share it publicly."
        )

    except ApiIdInvalid:
        await message.reply("❌ Invalid API credentials. Check API_ID/API_HASH.")
    except PhoneNumberInvalid:
        await message.reply("❌ Invalid phone number format.")
    except PhoneCodeInvalid:
        await message.reply("❌ Incorrect OTP. Try again.")
    except PhoneCodeExpired:
        await message.reply("⌛ OTP expired. Start again with /session.")
    except PasswordHashInvalid:
        await message.reply("❌ Incorrect 2FA password.")
    except Exception as e:
        await message.reply(f"⚠️ Error: `{e}`")
    finally:
        await user_client.disconnect()
