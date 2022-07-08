import octobot.updater.updater_factory as updater_factory


def get_updater():
    return updater_factory.create_updater()
