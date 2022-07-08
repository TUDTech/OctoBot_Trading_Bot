import octobot_backtesting.api as backtesting_api
import octobot_commons.configuration as configuration
import octobot_backtesting.constants as constants

import octobot.api.backtesting as octobot_backtesting_api
import octobot.octobot as octobot_class


class OctoBotBacktestingFactory(octobot_class.OctoBot):
    def __init__(self, config: configuration.Configuration,
                 log_report=True,
                 run_on_common_part_only=True,
                 enable_join_timeout=True,
                 enable_logs=True):
        super().__init__(config)
        self.independent_backtesting = None
        self.log_report = log_report
        self.run_on_common_part_only = run_on_common_part_only
        self.enable_join_timeout = enable_join_timeout
        self.enable_logs = enable_logs

    async def initialize(self):
        try:
            await self.initializer.create()
            join_backtesting_timeout = constants.BACKTESTING_DEFAULT_JOIN_TIMEOUT if self.enable_join_timeout else None
            self.independent_backtesting = octobot_backtesting_api.create_independent_backtesting(
                self.config,
                self.tentacles_setup_config,
                backtesting_api.get_backtesting_data_files(self.config),
                run_on_common_part_only=self.run_on_common_part_only,
                join_backtesting_timeout=join_backtesting_timeout,
                enable_logs=self.enable_logs)
            await octobot_backtesting_api.initialize_and_run_independent_backtesting(self.independent_backtesting,
                                                                                     log_errors=False)
            await octobot_backtesting_api.join_independent_backtesting(self.independent_backtesting,
                                                                       timeout=join_backtesting_timeout)
            if self.log_report:
                octobot_backtesting_api.log_independent_backtesting_report(self.independent_backtesting)
            await octobot_backtesting_api.stop_independent_backtesting(self.independent_backtesting, memory_check=False)
        except Exception as e:
            self.logger.exception(e, True, f"Error when starting backtesting: {e.__class__.__name__}")
        finally:
            self.task_manager.stop_tasks(stop_octobot=False)
