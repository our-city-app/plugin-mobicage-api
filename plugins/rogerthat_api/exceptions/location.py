from plugins.rogerthat_api.api import RogerthatApiException


class CanOnlyTrackServiceSubscriptionsException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_LOCATION + 1,
                                     "Can only track subscribed users.")
