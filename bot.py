from telegram.ext import Updater, RegexHandler, MessageHandler, Filters, InlineQueryHandler, CommandHandler, \
    CallbackQueryHandler
import logging
import config
from cmd import cmd_find, cmd_dl, cmd_start, cmd_random
from inlinequery import inlinequery

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error_handler(bot, update, error):
    logger.warning('Update {0} caused error {1}'.format(update, error))


def main():
    updater = Updater(config.telegram['access_token'])

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', cmd_start))
    dp.add_handler(CommandHandler('random', cmd_random))
    dp.add_handler(MessageHandler(Filters.text, cmd_find))
    dp.add_handler(RegexHandler(r'/dl_([0-9a-z]+)', cmd_dl, pass_groups=True))
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_error_handler(error_handler)

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()