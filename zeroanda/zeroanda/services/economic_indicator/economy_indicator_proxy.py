from zeroanda import utils
from zeroanda.models import EconomicIndicatorManagementModel, EconomicIndicatorModel
from zeroanda.services.economic_indicator.economic_indicator_api_services import EconomicIndicatorApiServiceFactory
from zeroanda.classes.utils import timeutils


class EconomicIndicatorProxyModel:
    def get_latest_economic_indicator(self):
        try:
            result = EconomicIndicatorApiServiceFactory.create().get_latest_economic_indicator()
            utils.info(result.get_unique_id())
            model = EconomicIndicatorManagementModel.objects.filter(unique_id=result.get_unique_id())
            if model.count() == 0:
                eim_model = EconomicIndicatorManagementModel(
                    origin      = result.get_origin(),
                    unique_id    = result.get_unique_id(),
                    url         = result.get_url(),
                    filename    = result.get_filename(),
                    created     = timeutils.get_now_with_jst()
                )
                eim_model.save()
                list = result.get_economic_indicator_list()
                for vo in list:
                    eim = EconomicIndicatorModel(
                        management_model= eim_model,
                        raw_date        = vo.raw_date,
                        raw_time        = vo.raw_time,
                        time_zone       = vo.time_zone,
                        currency        = vo.currency,
                        event           = vo.event,
                        importance      = vo.importance,
                        actual          = vo.actual,
                        forecast        = vo.forecast,
                        previous        = vo.previous,
                        date            = vo.date
                        )
                    eim.save()
        except Exception as e:
            utils.info(e)
            return None