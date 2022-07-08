cimport async_channel.channels as channels

cdef class OctoBotChannelGlobalConsumer:
    cdef object octobot
    cdef object logger

    cdef list octobot_channel_consumers

    cdef channels.Channel octobot_channel
