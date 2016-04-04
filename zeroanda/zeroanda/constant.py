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

ACCOUNT_STATUS    = (
    (True, "available"),
    (False, "disable"),
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

EXPIRY_MINITES = 5

IFDOCO_ENTRY_POINT = 0

DURATION_GET_ACCOUNT_EXCUTE_TIME= -60  # seconds

DURATION_GET_PRICE_EXCUTE_TIME  = -10 # seconds

DURATION_IFDOCO_EXCUTE_TIME     = -3  # seconds