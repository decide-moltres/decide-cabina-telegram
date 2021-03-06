import logging
from configurations import config
from utilities import parser
from telegram import (ReplyKeyboardMarkup, ReplyKeyboardRemove)
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters,
                          ConversationHandler)
from bot import (llamadas)
from utilities import (global_vars)
import json


LOGIN, STORE, VOTINGS, VOTING, SAVE_VOTE  = range(5)
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def votings(update, context):
    response = llamadas.get_user(global_vars.token)
    usuario = json.loads(response.text)

    response2 = llamadas.get_votings(usuario["id"])

    vots = json.loads(response2.text)
    votaciones = parser.parseVotings(vots)
    global_vars.user_votings = votaciones
    reply_keyboard = parser.createKeybVoting(votaciones)
    update.message.reply_text(update.message.text, reply_markup=ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True))
    logger.info("Listing votings")
    return VOTING
