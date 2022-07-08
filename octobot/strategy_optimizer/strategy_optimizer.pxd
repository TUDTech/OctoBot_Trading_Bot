cdef class StrategyOptimizer:
    cdef object logger
    cdef dict config
    cdef object tentacles_setup_config
    cdef dict sorted_results_by_time_frame
    cdef list sorted_results_through_all_time_frame
    cdef object current_test_suite
    cdef set errors
    cdef int run_id
    cdef bint keep_running
    cdef total_nb_runs

    cdef public bint is_properly_initialized
    cdef public object trading_mode
    cdef public object strategy_class
    cdef public list all_time_frames
    cdef public list all_TAs
    cdef public list risks
    cdef public bint is_computing
    cdef public bint is_finished
    cdef public list run_results

    cpdef void find_optimal_configuration(self, list TAs=*, list time_frames=*, list risks=*)
    cpdef void print_report(self)
    cpdef int get_current_test_suite_progress(self)
    cpdef list get_report(self)
    cpdef object get_errors_description(self)

    cdef void _run_test_suite(self, dict config, dict evaluators)
    cdef void _adapt_tentacles_config(self, dict activated_evaluators)
    cdef void _find_optimal_configuration_using_results(self)
    cdef void _iterate_on_configs(self, int nb_TAs, int nb_TFs)
    cdef void _run_on_config(self, object risk, object current_forced_time_frame, int nb_time_frames,
                            list time_frames_conf_history, dict activated_evaluators)
    cdef list _get_all_TA(self)
