from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID", 27806628))
API_HASH = getenv("API_HASH", "8577192556:AAGvn0FXD2md_f9nFPYf0Ljn7oRGP_UuBdI")

BOT_TOKEN = getenv("BOT_TOKEN", "8577192556:AAGvn0FXD2md_f9nFPYf0Ljn7oRGP_UuBdI")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID", 7931898805))

PING_IMG = getenv("PING_IMG", "https://te.legra.ph/file/6f99c49bdb4679acad717.jpg")
START_IMG = getenv("START_IMG", "https://te.legra.ph/file/f8ba75bdbb9931cbc8229.jpg")

SESSION = getenv("SESSION", "BAFwyZ4AbxB_LuVHkowYZgZuhN_-OjnZQInGa4U2bTcQ9bVaTjUnAx1ox5zA2YDO-RUAzJZaFAzULKkGaY4mxLpWlJvJtgMN9d7oGrHo5wgS-CMKEtIqj6oPNPlDjOrtFFk-lKpQXccM8rZU5npHJrtyzqV4cUQoesbnwin4WCiX68_1y9GaZ2PTSk0UhUqaSsQK3kMwMLdYnE5D-zjFK7IRu01RgICcHdwerk39IHa7I1SQi0Wk3oKbo76EXCM1Q_HRkBUDmeWdD_l5L0z4m9mB4o1Pf-9YRlqGLHD7ohNSvpoe-MnBRkSoK3TAxcqvHbgagxC9mI0KKzTqr5g2MUJntall0QAAAAH244hdAA")

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/DevilsHeavenMF")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/FallenAssociation")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7931898805").split()))


FAILED = "https://te.legra.ph/file/4c896584b592593c00aa8.jpg"
