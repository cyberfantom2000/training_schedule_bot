from telegram.ext import ConversationHandler

END = str(ConversationHandler.END)

(START_OVER, MENU, CONTROL, LIST, ARCHIVE, *other) = map(str, range(150))
