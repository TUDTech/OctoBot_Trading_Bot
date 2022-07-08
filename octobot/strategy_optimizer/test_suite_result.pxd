cdef class TestSuiteResult:
    cdef public list run_profitabilities
    cdef public list trades_counts
    cdef public double risk
    cdef public list time_frames
    cdef public object min_time_frame
    cdef public list evaluators
    cdef public str strategy

    cpdef double get_average_score(self)
    cpdef double get_average_trades_count(self)
    cpdef list get_evaluators_without_strategy(self)
    cpdef TestSuiteResultSummary get_config_summary(self)
    cpdef str get_result_string(self, bint details=*)
    cpdef dict get_result_dict(self, int index=*)

cdef class TestSuiteResultSummary:
    cdef public list evaluators
    cdef public double risk

    cpdef str get_result_string(self)
