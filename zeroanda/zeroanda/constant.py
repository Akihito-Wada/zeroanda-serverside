from enum import Enum

SIDE = (
    ("sell", "Sell"),
    ("buy", "Buy"),
)

PRIORITY = (
    (1, "Lowest"),
    (2, "Low"),
    (3, "Intermediate"),
    (4, "High"),
    (5, "Highest"),
)

ORDER_STATUS    = (
    (True, "available"),
    (False, "disable"),
)

ACTUAL_ORDER_STATUS =(
    (1, "Progress"),
    (2, "Finish"),
    (3, "Cancel"),
)

INSTRUMENTS = (
    ("USD_JPY", "us_jp"),
    ("EUR_JPY", "eu_jp"),
    ("EUR_USD", "eu_us"),
    ("EUR_CAD", "eu_ca"),
)

TYPE = (
    ("limit", "Limit"),
    ("stop", "Stop"),
    ("marketIfTouched", "MarketIfTouched"),
    ("market", "Market"),
)

SCHEDULE_STATUS = (
    (True, "有効"),
    (False, "無効"),
)

COUNTRY_LIST = (
    ("USD_JPY", "US"),
)

ERROR_CODE = (
    (0, 'None'),
    (11, 'Order not found'),
)