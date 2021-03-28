from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("🛸 Channel", url="https://t.me/Wandabetaxbot"),
         InlineKeyboardButton(
            "📞 Contact", url="https://t.me/t_r_oy")]
    ])
    welcomed = f"""Hey <b>{message.from_user.first_name}</b>\n
Welcome to @YouTubeX11bot, The Most Advanced YouTube Video and Audio Downloader in Telegram!

Send any YouTube video link to download!"""
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
