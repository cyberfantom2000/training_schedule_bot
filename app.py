from config import application, repository
from handlers.silenthandler import SilentHandler
from handlers.initialhandler import InitialHandler


def main():
    silent_handler = SilentHandler(repository)
    initial_handler = InitialHandler(repository)
    application.add_handler(silent_handler.instance())
    application.add_handler(initial_handler.instance())
    application.run_polling()


if __name__ == '__main__':
    main()
