from zeroanda   import utils
from django.conf import settings

class SettingProxy:

    def __init__(self):return

    @staticmethod
    def get_expire_time(priority):
        return TIME_MAP[priority]["EXPIRE_SECONDS"]

    @staticmethod
    def get_ifdo_expire_time(priority):
        return SettingProxy.get_expire_time(priority) - settings.DURATION_IFDOCO_EXCUTE_TIME

    @staticmethod
    def get_close_all_trades_excute_time(priority):
        return SettingProxy.get_expire_time(priority) + settings.CLOSE_ALL_TRADES_EXCUTE_TIME

    @staticmethod
    def get_transaction_excute_time(priority):
        return SettingProxy.get_close_all_trades_excute_time(priority) + settings.GET_TRANSACTION_EXCUTE_TIME

    @staticmethod
    def get_account_info_excute_time(priority):
        return SettingProxy.get_transaction_excute_time(priority) + settings.DURATION_GET_ACCOUNT_INFO_EXCUTE_TIME


TIME_MAP = (
    {
        "EXPIRE_SECONDS": 5,
    },
    {
        "EXPIRE_SECONDS": 5,
    },
    {
        "EXPIRE_SECONDS": 5,
    },
    {
        "EXPIRE_SECONDS": 5,
    },
    {
        "EXPIRE_SECONDS": 10,
    },
)