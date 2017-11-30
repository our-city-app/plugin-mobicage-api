from plugins.rogerthat_api.exceptions import ServiceApiException


class PersonInvitationOverloadException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 2,
                                     "Person was already invited three times.")


class PersonAlreadyInvitedThisWeekException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 1,
                                     "This person was already invited in the last week.")


class InvalidEmailAddressException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 0,
                                     "Invalid email address.")


class CannotSelfInviteException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 3,
                                     "Can not invite myself.")


class DoesNotWantToBeInvitedViaEmail(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 4,
                                     "This person does not want to be invited anymore via email.")


class CanNotRequestLocationFromServices(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 5,
                                     "Cannot request location from service users.")


class UserNotFoundViaUserCode(ServiceApiException):

    def __init__(self, user_code):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 6,
                                     "User not found via userCode", user_code=user_code)


class CanNotInviteFriendException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 7,
                                     "This person is already your friend")


class CanNotInviteOtherServiceException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_FRIEND + 8,
                                     "Cannot invite services.")
