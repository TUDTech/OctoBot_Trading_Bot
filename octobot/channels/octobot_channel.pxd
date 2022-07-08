cimport async_channel.channels as channels
cimport async_channel.consumer as consumers
cimport async_channel.producer as producers


cdef class OctoBotChannel(channels.Channel):
    pass

cdef class OctoBotChannelConsumer(consumers.Consumer):
    pass

cdef class OctoBotChannelProducer(producers.Producer):
    pass
