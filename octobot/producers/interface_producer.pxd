cimport octobot.channels as octobot_channels


cdef class InterfaceProducer(octobot_channels.OctoBotChannelProducer):
    cdef public object octobot

    cdef public list interfaces
    cdef public list notifiers

    cdef int to_create_notifiers_count

    # Cython bug with all()
    # cdef bint _is_interface_relevant(self, object interface_class, bint backtesting_enabled)
    # cdef bint _is_notifier_relevant(self, object notifier_class, bint backtesting_enabled)
