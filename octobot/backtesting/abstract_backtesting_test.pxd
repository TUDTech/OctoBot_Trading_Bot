cdef class AbstractBacktestingTest:
    cdef dict config
    cdef object tentacles_setup_config
    cdef object strategy_evaluator_class
    cdef object logger

    cpdef void initialize_with_strategy(self,
                                        object strategy_evaluator_class,
                                        object tentacles_setup_config,
                                        dict config)

    cdef void _register_only_strategy(self, object strategy_evaluator_class)
