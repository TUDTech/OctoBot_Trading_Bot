def activate_tentacles_loading_logger():
    import logging
    console = logging.StreamHandler()
    console.setLevel(logging.DEBUG)
    # add the handler to the TentacleLoader logger
    logging.getLogger('TentacleLoader').addHandler(console)
