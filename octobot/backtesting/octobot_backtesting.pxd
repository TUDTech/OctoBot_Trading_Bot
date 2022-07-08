cdef class OctoBotBacktesting:
    cdef public dict backtesting_config
    cdef public object tentacles_setup_config

    cdef object logger

    cdef public str matrix_id
    cdef public str bot_id
    cdef public list exchange_manager_ids
    cdef public dict symbols_to_create_exchange_classes
    cdef public list evaluators
    cdef public list service_feeds
    cdef public dict fees_config
    cdef public list backtesting_files
    cdef public object backtesting
    cdef public bint run_on_common_part_only
    cdef public object start_timestamp
    cdef public object end_timestamp
    cdef public bint enable_logs
    cdef public bint is_future
    cdef public object futures_contract_type

    cpdef object memory_leak_checkup(self, list to_check_elements)
    cpdef object check_remaining_objects(self)

cdef str _get_remaining_object_error(object obj, int expected, tuple actual)
