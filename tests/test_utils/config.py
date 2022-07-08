from octobot_tentacles_manager.api.configurator import get_tentacles_setup_config

TEST_CONFIG_FOLDER = "tests/static"


def load_test_tentacles_config():
    return get_tentacles_setup_config(config_path=f"{TEST_CONFIG_FOLDER}/default_tentacles_config.json")
