import pytest
import time

import octobot.community as community


ERROR_TITLE = "An error happened"
ERROR_METRICS_ID = "1254xyz"
ERROR_TIME = time.time()
UPLOADER_URL = "http://upload_url"


@pytest.fixture
def basic_error():
    return community.Error(
        None,
        ERROR_TITLE,
        ERROR_TIME,
        ERROR_METRICS_ID
    )


@pytest.fixture
def exception_error():
    # generated exception with traceback
    return community.Error(
        _get_exception(),
        ERROR_TITLE,
        ERROR_TIME,
        ERROR_METRICS_ID
    )


@pytest.fixture
def error_uploader():
    return community.ErrorsUploader(UPLOADER_URL)


def _get_exception():
    def fake3():
        1/0

    def fake2():
        fake3()

    def fake_func():
        fake2()
    try:
        fake_func()
    except ZeroDivisionError as err:
        return err
