import octobot.constants as constants
import octobot.commands as commands
import octobot.community


class OctoBotAPI:

    def __init__(self, octobot):
        self._octobot = octobot

    def is_initialized(self) -> bool:
        return self._octobot.initialized

    def get_exchange_manager_ids(self) -> list:
        return self._octobot.exchange_producer.exchange_manager_ids

    def get_global_config(self) -> dict:
        return self._octobot.config

    def get_startup_config(self) -> object:
        return self._octobot.get_startup_config(constants.CONFIG_KEY)

    def get_edited_config(self, dict_only=True) -> object:
        return self._octobot.get_edited_config(constants.CONFIG_KEY, dict_only=dict_only)

    def get_startup_tentacles_config(self) -> object:
        return self._octobot.get_startup_config(constants.TENTACLES_SETUP_CONFIG_KEY)

    def get_edited_tentacles_config(self) -> object:
        return self._octobot.get_edited_config(constants.TENTACLES_SETUP_CONFIG_KEY)

    def set_edited_tentacles_config(self, config):
        self._octobot.set_edited_config(constants.TENTACLES_SETUP_CONFIG_KEY, config)

    def get_trading_mode(self) -> object:
        return self._octobot.get_trading_mode()

    def get_tentacles_setup_config(self) -> object:
        return self._octobot.tentacles_setup_config

    def get_start_time(self) -> float:
        return self._octobot.start_time

    def get_bot_id(self) -> str:
        return self._octobot.bot_id

    def get_matrix_id(self) -> str:
        return self._octobot.evaluator_producer.matrix_id

    def get_aiohttp_session(self) -> object:
        return self._octobot.get_aiohttp_session()

    def run_in_main_asyncio_loop(self, coroutine):
        return self._octobot.run_in_main_asyncio_loop(coroutine)

    def run_in_async_executor(self, coroutine):
        return self._octobot.task_manager.run_in_async_executor(coroutine)

    def stop_tasks(self) -> None:
        self._octobot.task_manager.stop_tasks()

    def stop_bot(self) -> None:
        commands.stop_bot(self._octobot)

    @staticmethod
    def restart_bot() -> None:
        commands.restart_bot()

    def update_bot(self) -> None:
        commands.update_bot(self)
