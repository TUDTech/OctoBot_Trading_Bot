cimport octobot.channels as octobot_channels


cdef class ServiceFeedProducer(octobot_channels.OctoBotChannelProducer):
    cdef public object octobot
    cdef public bint started

    cdef public list service_feeds
