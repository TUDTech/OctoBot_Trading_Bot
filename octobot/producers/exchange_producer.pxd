cimport octobot.channels as octobot_channel 


cdef class ExchangeProducer(octobot_channel.OctoBotChannelProducer):
    cdef object octobot
    cdef object backtesting

    cdef bint ignore_config

    cdef public list exchange_manager_ids

    cdef object _init_bot_storage(self) # return object to propagate exceptions
