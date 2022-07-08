cimport octobot.updater.updater as updater_class

cdef class BinaryUpdater(updater_class.Updater):
    cdef str _get_latest_release_url(self)
    cdef object _parse_latest_version(self, object latest_release_data)
    cdef str _create_release_asset_name(self, object platform)
    cdef void _give_execution_rights(self, str new_binary_file)
