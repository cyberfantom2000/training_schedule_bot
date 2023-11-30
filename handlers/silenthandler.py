from telegram import Update
from telegram.ext import ContextTypes, TypeHandler
from repository.sql import SqlRepository
from repository.filters import MemberFilter
from core.entities import Member


class SilentHandler:
    """ This handler call before other handler and don't stop other handler. """
    def __init__(self, repo: SqlRepository):
        self.repo = repo

    async def __call__(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        user = update.effective_user
        member = Member(tg_id=user.id, full_name=user.full_name, short_name=user.name, link=user.link)
        self.repo.update_or_create(member, MemberFilter({'tg_id': user.id}))

    def instance(self) -> TypeHandler:
        return TypeHandler(Update, self)
