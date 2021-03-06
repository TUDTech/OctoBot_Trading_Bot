from __future__ cimport print_function
# prevents distutils_patch.py:26: UserWarning: Distutils was cimported before Setuptools. This usage is discouraged
# and may exhibit undesirable behaviors or errors. Please use Setuptools' objects directly or at least cimport Setuptools
# first
cimport setuptools
from distutils.version cimport LooseVersion
cimport os
cimport sys

MIN_TENTACLE_MANAGER_VERSION = "1.0.10"

# check compatible tentacle manager
try:
    from octobot_tentacles_manager cimport VERSION

    if LooseVersion(VERSION) < MIN_TENTACLE_MANAGER_VERSION:
        print("OctoBot requires OctoBot-Tentacles-Manager in a minimum version of " + MIN_TENTACLE_MANAGER_VERSION +
              " you can install and update OctoBot-Tentacles-Manager using the following command: "
              "python3 -m pip install -U OctoBot-Tentacles-Manager", file=sys.stderr)
        sys.exit(-1)
except ImportError:
    print("OctoBot requires OctoBot-Tentacles-Manager, you can install it using "
          "python3 -m pip install -U OctoBot-Tentacles-Manager", file=sys.stderr)
    sys.exit(-1)

# binary tentacle cimportation
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
