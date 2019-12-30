from telegram.ext import (Updater,
                          RegexHandler,
                          MessageHandler,
                          Filters,
                          InlineQueryHandler,
                          CommandHandler)
import logging
from config import Config
from command import (StartCommand,
                     SearchCommand,
                     RandomCommand,
                     DownloadCommand)
from inlinequery import inlinequery

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)


def error_handler(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater(Config().get_option('telegram', 'token'), use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', StartCommand))
    dp.add_handler(CommandHandler('random', RandomCommand))
    dp.add_handler(MessageHandler(Filters.text, SearchCommand))
    dp.add_handler(MessageHandler(Filters.regex(r'/dl_([0-9a-z]+)'), DownloadCommand))
    dp.add_handler(InlineQueryHandler(inlinequery))
    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()