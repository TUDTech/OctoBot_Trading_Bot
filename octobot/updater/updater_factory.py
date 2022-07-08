import octobot_commons.os_util as os_util
import octobot_commons.enums as commons_enums

import octobot.updater.binary_updater as binary_updater
import octobot.updater.python_updater as python_updater


def create_updater():
    bot_type = os_util.get_octobot_type()

    if bot_type == commons_enums.OctoBotTypes.DOCKER.value:
        return None
    if bot_type == commons_enums.OctoBotTypes.BINARY.value:
        return binary_updater.BinaryUpdater()
    if bot_type == commons_enums.OctoBotTypes.PYTHON.value:
        return python_updater.PythonUpdater()
    return None
