from enum import Enum

SIDE = (
    ("sell", "Sell"),
    ("buy", "Buy"),
)

PRIORITY = (
    (0, "Lowest"),
    (1, "Low"),
    (2, "Intermediate"),
    (3, "High"),
    (4, "Highest"),
)

ACCOUNT_STATUS    = (
    (True, "available"),
    (False, "disable"),
)

ORDER_STATUS    = (
    (True, "available"),
    (False, "disable"),
)

ACTUAL_ORDER_STATUS =(
    (0, "Progress"),
    (1, "Finish"),
    (2, "Cancel"),
)

INSTRUMENTS = (
    ("USD_JPY", "USD_JPY"),
    ("EUR_JPY", "EUR_JPY"),
    ("EUR_USD", "EUR_USD"),
    ("EUR_CAD", "EUR_CAD"),
)

TYPE = (
    ("limit", "Limit"),
    ("stop", "Stop"),
    ("marketIfTouched", "MarketIfTouched"),
    ("market", "Market"),
)

SCHEDULE_AVAILABLE = (
    (True, "有効"),
    (False, "無効"),
)

SCHEDULE_STATUS = (
    (0, "has been prepared."),
    (1, "has started."),
    (2, "has finished."),
)

COUNTRY_LIST = (
    # ("USD_JPY", "US"),
    ("0", "Australia",       "AU", "AUD"),
    ("1", "Canada",          "CA", "CAD"),
    ("2", "England",         "GB", "GBP"),
    ("3", "European Union",  "EU", "EUR"),
    ("4", "Japan",           "JP", "JPY"),
    ("5", "New Zealand",     "NZ", "NZD"),
    ("6", "Switzerland",     "CH", "CHF"),
    ("7", "United States",   "US", "USD"),
    ("8", "People's Republic of China",   "CN", "CNY"),
    ("9", "European Central Bank",   "", "ECB"),
)

ERROR_CODE = (
    (0, 'None'),
    (11, 'Order not found'),
)

TRANSACTION_REASON = (
    (0, "UNDEFINED"),
    (1, "CLIENT_REQUEST"),
    (2, "TIME_IN_FORCE_EXPIRED"),
    (3, "ORDER_FILLED"),
    (4, "MIGRATION"),
    (5, "INSUFFICIENT_MARGIN"),
    (6, "BOUNDS_VIOLATION"),
    (7, "UNITS_VIOLATION"),
    (8, "STOP_LOSS_VIOLATION"),
    (9, "TAKE_PROFIT_VIOLATION"),
    (10, "TRAILING_STOP_VIOLATION"),
    (11, "MARKET_HALTED"),
    (12, "ACCOUNT_NON_TRADABLE"),
    (13, "NO_NEW_POSITION_ALLOWED"),
    (14, "INSUFFICIENT_LIQUIDITY"),

    (15, "ADJUSTMENT"),
    (16, "FUNDS"),
    (17, "CURRENSEE_MONTHLY"),
    (18, "CURRENSEE_PERFORMANCE"),
)

TRANSACTION_TYPE = (
    (0, "UNDEFINED"),
    (1, "MARKET_ORDER_CREATE"),
    (2, "STOP_ORDER_CREATE"),
    (3, "LIMIT_ORDER_CREATE"),
    (4, "MARKET_IF_TOUCHED_ORDER_CREATE"),
    (5, "ORDER_UPDATE"),
    (6, "ORDER_CANCEL"),
    (7, "ORDER_FILLED"),
    (8, "TRADE_UPDATE"),
    (9, "TRADE_CLOSE"),
    (10, "MIGRATE_TRADE_OPEN"),
    (11, "MIGRATE_TRADE_CLOSE"),
    (12, "STOP_LOSS_FILLED"),
    (13, "TAKE_PROFIT_FILLED"),
    (14, "TRAILING_STOP_FILLED"),
    (15, "MARGIN_CALL_ENTER"),
    (16, "MARGIN_CALL_EXIT"),
    (17, "MARGIN_CLOSEOUT"),
    (18, "SET_MARGIN_RATE"),
    (19, "TRANSFER_FUNDS"),
    (20, "DAILY_INTEREST"),
    (21, "FEE"),
)

ECONOMIC_INDICATOR_IMPORTANCE = (
    (0, "LOW"),
    (1, "MEDIUM"),
    (2, "HIGH"),
)

class CALENDER_PERIOD(Enum):
    YEAR    =   31536000
    HALF_YEAR   = 15552000
    THREE_MONTH = 7776000
    ONE_MONTH   = 2592000
    ONE_WEEK    = 604800
    ONE_DAY     = 86400
    HALF_DAY    = 43200
    ONE_HOUR    = 3600