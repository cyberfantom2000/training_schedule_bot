from telegram.ext import ApplicationBuilder, AIORateLimiter
from repository.utils import create_repository
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
                    level=logging.INFO)
logger = logging.getLogger(__name__)

with open('token.txt', 'r') as file:
    token = file.readline().strip()
    application = ApplicationBuilder().token(token).rate_limiter(AIORateLimiter()).build()
    bot = application.bot
    job_queue = application.job_queue

repository = create_repository('data.db')
