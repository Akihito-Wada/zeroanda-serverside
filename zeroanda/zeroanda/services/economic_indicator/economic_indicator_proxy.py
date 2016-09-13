from zeroanda import utils
from zeroanda.models import EconomicIndicatorManagementModel, EconomicIndicatorModel
from zeroanda.services.economic_indicator.economic_indicator_api_services import EconomicIndicatorApiServiceFactory
from zeroanda.classes.utils import timeutils
from zeroanda.classes.utils.csv_utils import CSVFactory


class EconomicIndicatorProxyModel:
    def get_latest_economic_indicator(self):
        try:
            result = EconomicIndicatorApiServiceFactory.create().get_latest_economic_indicator()
            model = EconomicIndicatorManagementModel.objects.filter(unique_id=result.get_unique_id())
            if model.count() == 0:
                self.__save(result)
                # eim_model = EconomicIndicatorManagementModel(
                #     origin      = result.get_origin(),
                #     unique_id    = result.get_unique_id(),
                #     url         = result.get_url(),
                #     filename    = result.get_filename(),
                #     created     = timeutils.get_now_with_jst()
                # )
                # eim_model.save()
                # list = result.get_economic_indicator_list()
                # for vo in list:
                #     eim = EconomicIndicatorModel(
                #         management_model= eim_model,
                #         raw_date        = vo.raw_date,
                #         raw_time        = vo.raw_time,
                #         time_zone       = vo.time_zone,
                #         currency        = vo.currency,
                #         event           = vo.event,
                #         importance      = vo.importance,
                #         actual          = vo.actual,
                #         forecast        = vo.forecast,
                #         previous        = vo.previous,
                #         date            = vo.date
                #         )
                #     eim.save()
            # utils.info(settings.ECONOMIC_INDICATOR_CSV_FILES)
            # utils.info(result.get_csv_path())
            # os.makedirs(result.get_csv_path(), exist_ok=True)
            CSVFactory.create().writer(result)
        except Exception as e:
            utils.info(e)
            return None

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
