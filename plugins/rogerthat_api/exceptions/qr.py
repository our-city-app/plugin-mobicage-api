from plugins.rogerthat_api.api import RogerthatApiException


class InvalidQRCodeBodyColorException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_QR + 1, "Invalid QR code color specification.")


class InvalidQRDescriptionException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_QR + 2, "Invalid QR code description.")


class InvalidQRTemplateSizeException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_QR + 3, "Invalid QR code template size.")


class QrTemplateRequiredException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_QR + 4, 'At least one QR template must be set')
