from pybot.bot import respond_to
from pybot.bot import listen_to
import re


@respond_to('hello$', re.IGNORECASE)
def hello_reply(message):
    message.reply('hello sender!')


@respond_to('hello_formatting')
def hello_reply_formatting(message):
    # Format message with italic style
    message.reply('_hello_ sender!')

@respond_to('deploy')
def hello_reply_deploy(message):
    # Format message with italic style
    message.reply('deploy ansible file')

@listen_to('hello$')
def hello_send(message):
    message.send('hello channel!')

@listen_to('hello_decorators')
@respond_to('hello_decorators')
def hello_decorators(message):
    message.send('hello!')
