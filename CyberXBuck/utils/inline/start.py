from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from CyberXBuck import app


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="π₯ β£π©πΈDD πE πO πOUΖ¦ πΎΖ¦OUΧ§πͺ π₯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="π₯ βα΄α΄α΄α΄Ι΄α΄Κα΄β π₯",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="π₯ πα΄α΄α΄ΙͺΙ΄Ι’κ± π₯", callback_data="settings_helper"
            ),
        ],
        [
            InlineKeyboardButton(
                text="π₯ πα΄α΄α΄α΄πΌ π₯", url=f"https://t.me/invisiblesecuritycyberbuck"),
            InlineKeyboardButton(
                text="π₯ πα΄α΄α΄α΄Κπ π₯", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="π₯ π©πΈDD πE πO πOUΖ¦ πΎΖ¦OUΧ§πͺ π₯",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            ),
        ],
        [
            InlineKeyboardButton(
                text="π₯ βα΄α΄α΄α΄Ι΄α΄Κα΄β π₯", callback_data="settings_back_helper"
            ),
        ],
        [
            InlineKeyboardButton(text="π₯ πα΄α΄α΄α΄πΌ π₯", url=f"https://t.me/invisiblesecuritycyberbuck"),
            InlineKeyboardButton(
                text="π₯ πα΄α΄α΄α΄Κπ π₯", url=f"{config.SUPPORT_GROUP}"
            ),
        ],
        [
            InlineKeyboardButton(
                    text="πππΌπ»eΝ₯Ρ΅eΝ£lΝ«πΧ§eβπΌππ", url=f"https://t.me/M_r_invisible_official"
                )
        ],
     ]
    return buttons
