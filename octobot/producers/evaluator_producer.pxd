cimport octobot.channels as octobot_channel 


cdef class EvaluatorProducer(octobot_channel.OctoBotChannelProducer):
    cdef public object octobot
    cdef public object tentacles_setup_config

    cdef public str matrix_id
