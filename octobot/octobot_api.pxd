cdef class OctoBotAPI:

    cdef object _octobot

    cpdef bint is_initialized(self)
    cpdef list get_exchange_manager_ids(self)
    cpdef dict get_global_config(self)
    cpdef object get_startup_tentacles_config(self)
    cpdef object get_edited_tentacles_config(self)
    cpdef void set_edited_tentacles_config(self, object config)
    cpdef object get_startup_config(self)
    cpdef object get_edited_config(self, bint dict_only=*)
    cpdef void set_edited_tentacles_config(self, object config)
    cpdef object get_trading_mode(self)
    cpdef double get_start_time(self)
    cpdef str get_bot_id(self)
    cpdef str get_matrix_id(self)
    cpdef object get_aiohttp_session(self)
    cpdef object run_in_main_asyncio_loop(self, object coroutine)
    cpdef void stop_tasks(self)
    cpdef void stop_bot(self)
    cpdef void update_bot(self)
