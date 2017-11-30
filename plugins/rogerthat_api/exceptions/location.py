from plugins.rogerthat_api.exceptions import ServiceApiException


class CanOnlyTrackServiceSubscriptionsException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_LOCATION + 1,
                                     "Can only track subscribed users.")
