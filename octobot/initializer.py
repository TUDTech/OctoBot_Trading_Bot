import octobot_tentacles_manager.api as tentacles_manager_api
import octobot.constants as constants


class Initializer:
    """Initializer class:
    - Initialize services, constants and tools
    """

    def __init__(self, octobot):
        self.octobot = octobot

    async def create(self):
        # initialize tentacle configuration
        tentacles_config_path = self.octobot.get_startup_config(constants.CONFIG_KEY, dict_only=False).\
            get_tentacles_config_path()
        self.octobot.tentacles_setup_config = tentacles_manager_api.get_tentacles_setup_config(tentacles_config_path)

        # create OctoBot channel
        await self.octobot.global_consumer.initialize()
