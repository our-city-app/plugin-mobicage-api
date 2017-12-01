from plugins.rogerthat_api.api import RogerthatApiException


class AppDoesNotExistException(RogerthatApiException):

    def __init__(self, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_APP + 0,
                                     u"App does not exist", app_id=app_id)


class AppAlreadyExistsException(RogerthatApiException):

    def __init__(self, app_id):
        message = u"App %(app_id)s already exists" % dict(app_id=app_id)
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_APP + 1, message, app_id=app_id)
