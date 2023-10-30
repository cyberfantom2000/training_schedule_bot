from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ConversationHandler, ContextTypes, CommandHandler, CallbackQueryHandler
from handlers.defines import *
from repository.sql import SqlRepository


class InitialHandler:
    """ Show initial bot menu """
    def __init__(self, repo: SqlRepository) -> None:
        self.repo = repo

    # TODO pass the dict with other handlers and unpack it into states?
    def instance(self) -> ConversationHandler:
        return ConversationHandler(
            entry_points=[CommandHandler('start', self.init_conversation)],
            states={
                # TODO
                MENU: []
            },
            fallbacks=[CallbackQueryHandler(self.stop_conversation, pattern='^{}$'.format(END)),
                       CommandHandler('stop', self.stop_conversation)]
        )

    async def init_conversation(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
        keyboard = self._create_keyboard()
        text = self._get_hello_text()
        self._make_reply(update, context, keyboard, text)
        return MENU

    async def stop_conversation(self):
        # TODO close and delete msg
        pass

    @staticmethod
    def _create_keyboard() -> InlineKeyboardMarkup:
        buttons = [
            [InlineKeyboardButton(text='Управление', callback_data=CONTROL)],
            [InlineKeyboardButton(text='Мероприятия', callback_data=LIST)],
            [InlineKeyboardButton(text='Архив', callback_data=ARCHIVE)],
            [InlineKeyboardButton(text='Закрыть сообщение', callback_data=END)]
        ]
        return InlineKeyboardMarkup(buttons)

    @staticmethod
    def _get_hello_text() -> str:
        return "Hello dynamic schedule bot! Choose your action..."

    @staticmethod
    def _make_reply(update, context, keyboard, text) -> None:
        if context.user_data.get(START_OVER):
            update.callback_query.answer()
            update.callback_query.edit_message_text(text=text, reply_markup=keyboard)
        else:
            context.user_data[START_OVER] = True
            update.message.reply_text(text=text, reply_markup=keyboard)
