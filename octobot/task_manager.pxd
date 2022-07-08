cdef class TaskManager:
    cdef object logger
    cdef public object octobot
    cdef public object async_loop
    cdef public object watcher
    cdef public object tools_task_group
    cdef public object current_loop_thread
    cdef public object bot_main_task
    cdef public object loop_forever_thread
    cdef public object executors

    cdef public bint ready

    cdef void _create_new_asyncio_main_loop(self)
    cdef void _loop_exception_handler(self, object loop, object context)

    cpdef void run_bot_in_thread(self, object coroutine)
    cpdef void run_forever(self, object coroutine)
    cpdef void create_pool_executor(self, int workers=*)
    cpdef void init_async_loop(self)
    cpdef object run_in_main_asyncio_loop(self, object coroutine)
