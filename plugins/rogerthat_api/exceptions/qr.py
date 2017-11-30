from plugins.rogerthat_api.exceptions import ServiceApiException


class InvalidQRCodeBodyColorException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_QR + 1, "Invalid QR code color specification.")


class InvalidQRDescriptionException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_QR + 2, "Invalid QR code description.")


class InvalidQRTemplateSizeException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_QR + 3, "Invalid QR code template size.")


class QrTemplateRequiredException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_QR + 4, 'At least one QR template must be set')
