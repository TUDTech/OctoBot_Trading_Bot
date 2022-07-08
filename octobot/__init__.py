from __future__ import print_function
import os
import sys


# binary tentacle importation
sys.path.append(os.path.dirname(sys.executable))

bot_instance = None
global_config = None


def __init__(bot, config):
    global bot_instance
    bot_instance = bot

    global global_config
    global_config = config


# TODO: find a better way to keep track of the bot instance in octobot module
def set_bot(bot):
    global bot_instance
    bot_instance = bot


def get_bot():
    return bot_instance


def get_config():
    return global_config
