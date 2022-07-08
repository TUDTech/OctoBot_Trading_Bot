cimport octobot.octobot  as octobot_class


cdef class OctoBotBacktestingFactory(octobot_class.OctoBot):
    cdef object independent_backtesting
    cdef bint log_report
    cdef bint run_on_common_part_only
    cdef bint enable_join_timeout
    cdef bint enable_logs
