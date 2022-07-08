cimport octobot.updater.updater as updater_class

cdef class PythonUpdater(updater_class.Updater):
    cdef bint use_git

    cdef str _get_latest_pypi_release_url(self)
    cdef object _get_latest_pypi_version_from_data(self, object pypi_package_data)
    cdef object _run_git_get_latest_tag(self)
    cdef object _run_git_get_last_tag_hash(self)
    cdef object _run_git_remove_local_branch(self, str branch_name)
    cdef object _run_pip_install_package(self, str package_name)
    cdef object _run_pip_update_package(self, str package_name)
    cdef object _run_pip_install_requirements_file(self, str requirement_file)
