from plugins.rogerthat_api.api import RogerthatApiException


class PersonInvitationOverloadException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 2,
                                     "Person was already invited three times.")


class PersonAlreadyInvitedThisWeekException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 1,
                                     "This person was already invited in the last week.")


class InvalidEmailAddressException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 0,
                                     "Invalid email address.")


class CannotSelfInviteException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 3,
                                     "Can not invite myself.")


class DoesNotWantToBeInvitedViaEmail(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 4,
                                     "This person does not want to be invited anymore via email.")


class CanNotRequestLocationFromServices(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 5,
                                     "Cannot request location from service users.")


class UserNotFoundViaUserCode(RogerthatApiException):

    def __init__(self, user_code):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 6,
                                     "User not found via userCode", user_code=user_code)


class CanNotInviteFriendException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 7,
                                     "This person is already your friend")


class CanNotInviteOtherServiceException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_FRIEND + 8,
                                     "Cannot invite services.")
