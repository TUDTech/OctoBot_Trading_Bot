import pytest

import octobot.api as octobot_api

# All test coroutines will be treated as marked.
pytestmark = pytest.mark.asyncio


async def test_create_updater_from_api():
    updater = octobot_api.get_updater()


async def test_should_update_on_updater_from_api():
    updater = octobot_api.get_updater()
    assert not (await updater.should_be_updated())
