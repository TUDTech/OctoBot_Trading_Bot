import time

import octobot.community.errors_upload.errors_uploader as errors_uploader
import octobot.community.errors_upload.error_model as error_model
import octobot_commons.logging as logging
import octobot.constants as constants


class _UploadWrapper:
    def __init__(self, upload_url, config):
        self._config = config
        self._metrics_id = self._get_metrics_id()
        self._uploader = errors_uploader.ErrorsUploader(
            upload_url
        )

    def upload_if_necessary(self, exception, error_message):
        if constants.UPLOAD_ERRORS and self._config.get_metrics_enabled():
            self._uploader.schedule_error_upload(
                error_model.Error(
                    exception, error_message, time.time(), self._metrics_id
                )
            )

    def _get_metrics_id(self):
        try:
            return self._config.get_metrics_id()
        except KeyError:
            return constants.DEFAULT_METRICS_ID


def register_error_uploader(upload_url, config):
    upload_wrapper = _UploadWrapper(upload_url, config)
    logging.BotLogger.register_error_callback(upload_wrapper.upload_if_necessary)
