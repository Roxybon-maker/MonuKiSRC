# devgagan
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

# VPS --- FILL COOKIES 🍪 in """ ... """ 

INST_COOKIES = """
# wtite up here insta cookies
"""

YTUB_COOKIES = """
# # Netscape HTTP Cookie File
# http://curl.haxx.se/rfc/cookie_spec.html
# This is a generated file!  Do not edit.

.youtube.com	TRUE	/	TRUE	1753371966	GPS	1
.youtube.com	TRUE	/	FALSE	1787930311	HSID	AJmgJFat6cEQLmnFv
.youtube.com	TRUE	/	TRUE	1787930311	SSID	A9Tx518EbjTtK_eDY
.youtube.com	TRUE	/	FALSE	1787930311	APISID	cFL3juUwF9GUEDSA/AP5-2du1McR7XI2Z-
.youtube.com	TRUE	/	TRUE	1787930311	SAPISID	yEaAivY2Myi5ky_4/A9qzmYa-m3WogKqiI
.youtube.com	TRUE	/	TRUE	1787930311	__Secure-1PAPISID	yEaAivY2Myi5ky_4/A9qzmYa-m3WogKqiI
.youtube.com	TRUE	/	TRUE	1787930311	__Secure-3PAPISID	yEaAivY2Myi5ky_4/A9qzmYa-m3WogKqiI
.youtube.com	TRUE	/	FALSE	1787930311	SID	g.a000zQgjOLuju9MoyTdrq9Zcn2SBZYZUWxRUilg6IkOVduIaoyX5Hf2T5xpwTzAAPkS1yTiMKwACgYKAVcSARMSFQHGX2MisCKnI5XpTgWYArd2gz8AEhoVAUF8yKpW-MhQgcy7hRfcNnRvP_EU0076
.youtube.com	TRUE	/	TRUE	1787930311	__Secure-1PSID	g.a000zQgjOLuju9MoyTdrq9Zcn2SBZYZUWxRUilg6IkOVduIaoyX5LLbD141L_j0MA7e8miOL9gACgYKAZoSARMSFQHGX2Mi560QUiKZjsNoQzC6MjUGCRoVAUF8yKoinFBnV8ZCLTlH1CjgYvez0076
.youtube.com	TRUE	/	TRUE	1787930311	__Secure-3PSID	g.a000zQgjOLuju9MoyTdrq9Zcn2SBZYZUWxRUilg6IkOVduIaoyX5faG7Sm4SDrUHMOTgAR7Y1gACgYKAY8SARMSFQHGX2MiO5YGGWJDh47b9cNIwAvs1RoVAUF8yKqcrTj-qjNsPsXUtrypDgVp0076
.youtube.com	TRUE	/	TRUE	1787930533	PREF	tz=Asia.Calcutta&f4=4000000
.youtube.com	TRUE	/	TRUE	1787930481	LOGIN_INFO	AFmmF2swRQIhAJiB3kxWDnr40rEGXoumj3YVzJMxH7YWX39VxlsCKalAAiAJqcfz6tLzXqoei2Y4rTrnT-7fMP7qC8Wfm5u5rU7s3Q:QUQ3MjNmeVFqMlFWd0xEcUw1UnAzS2hkMnNtQ2JpSG9QV0tya1Y1el91elQ0M2pkUzEyY2I2TE1sZHhWLTVwcHFJNHNKVXlnSTRZQnU5c2xkZlI2NVlKS3dLVWlONVowTDlQTFdacm1LeHN5Sk1ESFpkS1FRMnpWenFzOFdJZllJRUFSUXZ6d3VHcWhJSjdBZDJUVURpaWtSaHpJOVBzOHNB
.youtube.com	TRUE	/	TRUE	1784906498	__Secure-1PSIDTS	sidts-CjEB5H03P27jsKfnZFFwl_mOTTE6yh6vt80942SdbGyKiCfyv4YZhHkDzJA25tHirObREAA
.youtube.com	TRUE	/	TRUE	1784906498	__Secure-3PSIDTS	sidts-CjEB5H03P27jsKfnZFFwl_mOTTE6yh6vt80942SdbGyKiCfyv4YZhHkDzJA25tHirObREAA
.youtube.com	TRUE	/	FALSE	1784906538	SIDCC	AKEyXzXeoKglvRWa5gYX7hgHSwEIFZJznHXnFR1t6QLF9ZzQ1jf2eXT9DBcj3G6CWQ6fi-NV
.youtube.com	TRUE	/	TRUE	1784906538	__Secure-1PSIDCC	AKEyXzUvbgNrzUvySNF5CuVaDGN1hD8MmJh-p3dmdp5vmihNdjro9Ha2n9Q_qvMPWLjcSDkAOg
.youtube.com	TRUE	/	TRUE	1784906538	__Secure-3PSIDCC	AKEyXzWWgRakce4b0vZHhOvz6Gw2UjFwplUB79_TKND0H7YIAiULIMDFezd7EkHHvDAz_vlA
"""

API_ID = int(getenv("API_ID", ""))
API_HASH = getenv("API_HASH", "")
BOT_TOKEN = getenv("BOT_TOKEN", "")
OWNER_ID = list(map(int, getenv("OWNER_ID", "7114926879").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "-1002250829565")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1002250829565"))
FREEMIUM_LIMIT = int(getenv("FREEMIUM_LIMIT", "5000"))
PREMIUM_LIMIT = int(getenv("PREMIUM_LIMIT", "5000"))
WEBSITE_URL = getenv("WEBSITE_URL", "upshrink.com")
AD_API = getenv("AD_API", "52b4a2cf4687d81e7d3f8f2b7bc2943f618e78cb")
STRING = getenv("STRING", None)
YT_COOKIES = getenv("YT_COOKIES", YTUB_COOKIES)
INSTA_COOKIES = getenv("INSTA_COOKIES", INST_COOKIES)
