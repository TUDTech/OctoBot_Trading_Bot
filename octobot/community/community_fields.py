import enum 


class CommunityFields(enum.Enum):
    ID = "_id"
    CURRENT_SESSION = "currentsession"
    STARTED_AT = "startedat"
    UP_TIME = "uptime"
    VERSION = "version"
    SIMULATOR = "simulator"
    TRADER = "trader"
    EVAL_CONFIG = "evalconfig"
    PAIRS = "pairs"
    EXCHANGES = "exchanges"
    NOTIFICATIONS = "notifications"
    TYPE = "type"
    PLATFORM = "platform"
    REFERENCE_MARKET = "referencemarket"
    PORTFOLIO_VALUE = "portfoliovalue"
    PROFITABILITY = "profitability"
    TRADED_VOLUMES = "tradedvolumes"
    SUPPORTS = "supports"
    ROLES = "roles"
    DONATIONS = "donations"
