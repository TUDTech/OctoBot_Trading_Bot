import traceback


class Error:
    """
    Error is the error data wrapper use to upload errors to the error server
    """

    def __init__(self, error: Exception, title: str, timestamp: float, metrics_id: str):
        self.error: Exception = error
        self.title: str = str(title)
        self.first_timestamp: float = timestamp
        self.last_timestamp: float = timestamp
        self.count: int = 1
        self.metrics_id: str = metrics_id
        self.type: str = self.error.__class__.__name__ if self.error else ""
        self.stacktrace: list = traceback.format_exception(
            etype=type(self.error), value=self.error, tb=self.error.__traceback__
        )[1:] if self.error and isinstance(self.error, Exception) else []

    def to_dict(self) -> dict:
        """
        Return the dict serialization of self
        """
        return {
            "title": self.title,
            "type": self.type,
            "stacktrace": self.stacktrace,
            "firsttimestamp": self.first_timestamp,
            "lasttimestamp": self.last_timestamp,
            "count": self.count,
            "metricsid": self.metrics_id,
        }

    def is_equivalent(self, other) -> bool:
        return (self.error is other.error or
                (type(self.error) is type(other.error)
                 and self.error.args == other.error.args)) and \
               self.title == other.title and \
               self.metrics_id == other.metrics_id and \
               self.type == other.type and \
               self.stacktrace == other.stacktrace

    def merge_equivalent(self, other):
        self.count += other.count
        if other.last_timestamp > self.last_timestamp:
            self.last_timestamp = other.last_timestamp
