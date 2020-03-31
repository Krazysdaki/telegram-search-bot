from telegram.ext import CommandHandler
from utils import auto_delete, delete_prev_message, get_bot_user_name


@auto_delete
def get_help(bot, update):
    delete_prev_message(bot, update)
    bot_user_name = get_bot_user_name(bot)
    help_text = '*搜索消息:*\n  `@%s {keyword} {page}`。\n例如: "@%s 复读机 2" 搜索"复读机"并翻到第二页; \n不输入页码默认第一页；\n AT后不输入显示的是全部记录，此时输入 ' \
                r'"\* {page}"进行翻页\n\n' % (
                    bot_user_name, bot_user_name)
    sent_message = bot.send_message(update.message.chat_id, text=help_text, disable_notification=True,
                                    parse_mode='markdown')
    return sent_message


handler = CommandHandler('help', get_help)
