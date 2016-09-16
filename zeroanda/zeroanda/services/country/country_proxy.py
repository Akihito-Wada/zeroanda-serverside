from zeroanda.constant import COUNTRY_LIST
from zeroanda.services.country.country_value_object import CountryVO
from zeroanda import utils

class CountryProxyModel:
    __country_list  = []
    def __init__(self):
        for item in COUNTRY_LIST:
            vo = CountryVO(item[0], item[1], item[2], item[3])
            self.__country_list.append(vo)

    def country_list(self):
        _list = []
        for item in self.__country_list:
            _list.append((item.index, item.country_name))
        return tuple(_list)

    def get_index(self, currency):
        for item in self.__country_list:
            if item.currency == currency:
                return item.index
        raise Exception("This currency:{currency} is not defined in country_list.".format(currency=currency))

