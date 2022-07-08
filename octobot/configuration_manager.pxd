cdef class ConfigurationManager:
    cdef dict configuration_elements

    cpdef void add_element(self, str key, object element, bint has_dict=*)
    cpdef object get_edited_config(self, str key, bint dict_only)
    cpdef object get_startup_config(self, str key, bint dict_only)
    cpdef void set_edited_config(self, str config_key, object config)

cdef class ConfigurationElement:
    cdef public object config
    cdef public bint has_dict
    cdef public object startup_config
    cdef public object edited_config

cpdef config_health_check(object config, bint in_backtesting)
cpdef str get_default_tentacles_url(str version=*)
cpdef str get_default_compiled_tentacles_url()
cpdef str get_user_local_config_file()
cpdef void set_default_profile(object config, str from_default_config_file=*)
