import os
from zeroanda.constant import ECONOMIC_INDICATOR_IMPORTANCE

from zeroanda import utils
from zeroanda.models import EconomicIndicatorManagementModel, EconomicIndicatorModel
from zeroanda.services.economic_indicator.economic_indicator_api_services import EconomicIndicatorApiServiceFactory
from zeroanda.classes.utils import timeutils
from zeroanda.classes.utils.csv_utils import CSVFactory


class EconomicIndicatorProxyModel:
    def get_new_economic_indicator(self):
        try:
            result = EconomicIndicatorApiServiceFactory.create().get_next_week_economic_indicator()
            models = EconomicIndicatorManagementModel.objects.filter(unique_id=result.get_unique_id())
            if models.count() == 0:
                model = self.__save(result)
                result.set_management_id(model.id)
                return result
            else:
                return None
        except Exception as e:
            utils.info(e)
            return None

    def get_latest_economic_indicator(self):
        try:
            result = EconomicIndicatorApiServiceFactory.create().get_latest_economic_indicator()
            models = EconomicIndicatorManagementModel.objects.filter(unique_id=result.get_unique_id())
            if models.count() == 0:
                model = self.__save(result)
                result.set_management_id(model.id)
            else:
                result.set_management_id(models[0].id)
            return result
        except Exception as e:
            utils.info(e)
            return None

    def save_as_csv(self, dto):
        csv = CSVFactory.create()
        latest_file_path = dto.get_csv_path()
        backup_path = dto.get_backup_csv_path()
        body = []
        for vo in dto.get_economic_indicator_list():
            if vo.date == None or vo.event == None: continue
            row = []
            row.append(vo.event)
            row.append(csv.format_date(vo.date))
            row.append(csv.format_time(vo.date))
            row.append(csv.format_date(vo.date))
            row.append(csv.format_time(vo.date))
            row.append("False")
            row.append(vo)
            row.append("")
            row.append("True")
            row.append(vo.currency)
            row.append(vo.get_importance())
            body.append(row)

        csv.writer(backup_path, body, dto.get_unique_id())

        csv.writer(latest_file_path, body)

    def __save(self, dto):
        eim_model = EconomicIndicatorManagementModel(
            origin=dto.get_origin(),
            unique_id=dto.get_unique_id(),
            url=dto.get_url(),
            filename=dto.get_filename(),
            created=timeutils.get_now_with_jst()
        )
        eim_model.save()
        list = dto.get_economic_indicator_list()
        for vo in list:
            eim = EconomicIndicatorModel(
                management_model=eim_model,
                raw_date=vo.raw_date,
                raw_time=vo.raw_time,
                time_zone=vo.time_zone,
                currency=vo.currency,
                event=vo.event,
                importance=vo.importance,
                actual=vo.actual,
                forecast=vo.forecast,
                previous=vo.previous,
                date=vo.date
            )
            eim.save()
        return eim_model

    def get_unique_economic_indicator_model_list(self, dto):
        models = EconomicIndicatorModel.objects.filter(management_model=dto.get_management_id()).order_by('date', '-importance')

        target_model = None
        _list = []
        for model in models:
            if model.date == None:
                continue
            if target_model == None:
                target_model = model
            elif target_model.date == model.date:
                continue
            _list.append(model)
            target_model = model
        return _list

    def get_importance(self, value):

        for item in ECONOMIC_INDICATOR_IMPORTANCE:
            if item[0] == value:
                return item[1]