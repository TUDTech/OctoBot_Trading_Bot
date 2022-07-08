import packaging.version as packaging_version

import octobot.constants as constants
import octobot.configuration_manager as configuration_manager
import octobot.commands as commands
import octobot_commons.logging as logging


class Updater:
    def __init__(self):
        self.logger = logging.get_logger(self.__class__.__name__)

    async def should_be_updated(self):
        """
        :return: True if the updater version is greater than current bot version
        """
        try:
            return packaging_version.parse(await self.get_latest_version()) > packaging_version.parse(constants.VERSION)
        except TypeError as e:
            self.logger.debug(f"Error when comparing latest with current OctoBot version: {e}")

    async def get_latest_version(self):
        raise NotImplementedError("get_latest_version is not implemented")

    async def update_impl(self) -> bool:
        raise NotImplementedError("update_impl is not implemented")

    async def update_tentacles(self):
        await commands.install_all_tentacles(
            tentacles_url=configuration_manager.get_default_tentacles_url(version=await self.get_latest_version()))

    async def post_update(self):
        await self.update_tentacles()
        commands.restart_bot()

    async def update(self):
        """
        Call updater update_impl and updates tentacles on update success
        """
        if await self.update_impl():
            await self.post_update()
