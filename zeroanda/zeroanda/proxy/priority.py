class PriorityProxyModel:
    @staticmethod
    def convert_prioriy(origin_priority):
        converted_priority = min(origin_priority * 2, 4)
        return converted_priority
