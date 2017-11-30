from plugins.rogerthat_api.exceptions import ServiceApiException
from plugins.rogerthat_api.plugin_consts import MC_RESERVED_TAG_PREFIX


class InvalidDirtyBehaviorException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 16,
                                     "Invalid dirty_behavior.")


class MessageLockedException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 10,
                                     "Message is already locked.")


class MessageNotFoundException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 9,
                                     "Message not found.")


class CanOnlySendToFriendsException(ServiceApiException):

    def __init__(self, member, app_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 0,
                                     "Member is not in your friends list.", member=member, app_id=app_id)


class CanNotSendToServicesException(ServiceApiException):

    def __init__(self, member, app_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 15,
                                     "Can not send to services.", member=member, app_id=app_id)


class ParentMessageNotFoundException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 1,
                                     "Parent message not found.")


class CanOnlyReplyToMembersException(Exception):
    pass


class DuplicateMembersException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 13,
                                     "Duplicate members.")


class InvalidFlagsException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 3,
                                     "Invalid flags.")


class UnknownMessageAlertFlagException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 17,
                                     "Invalid alert flags.")


class RingAlertFlagsAreNotCombinableException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 18,
                                     "You cannot combine multiple ring flags.")


class IntervalAlertFlagsAreNotCombinableException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 19,
                                     "You cannot combine multiple interval flags.")


class AutoLockCanOnlyHaveOneMemberInMessageException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 11,
                                     "Autoseal flag implies maximum one member.")


class UnDismissableMessagesNeedAnswersException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 12,
                                     "Undismissable messages need at least one answer.")


class InvalidSenderReplyValue(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 2,
                                     "Illegal sender answer.")


class TagTooLargeException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 4,
                                     "Tag too large.")


class UnsupportedActionTypeException(ServiceApiException):

    def __init__(self, scheme):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 6,
                                     "Unsupported answer action type.", scheme=scheme)


class UnknownAnswerWidgetType(ServiceApiException):

    def __init__(self, widget_type):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 5,
                                     "Unknown answer widget type", widget_type=widget_type)


class IncompleteButtonException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 8,
                                     "Incomplete button.")


class BrandingNotFoundException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 7,
                                     "Branding not found.")


class DuplicateButtonIdException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 14,
                                     "Duplicate button ids.")


class InvalidWidgetValueException(ServiceApiException):

    def __init__(self, property_):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 20,
                                     "Invalid value in widget.", property=property_)


class ValueTooLongException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 21,
                                     "Value too long.")


class NoChoicesSpecifiedException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 22,
                                     "No choices specified.")


class DuplicateChoiceLabelException(ServiceApiException):

    def __init__(self, label):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 23,
                                     "Duplicate label in choices.", label=label)


class DuplicateChoiceValueException(ServiceApiException):

    def __init__(self, value):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 24,
                                     "Duplicate value in choices.", value=value)


class DuplicateValueException(ServiceApiException):

    def __init__(self, value):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 25,
                                     "Duplicate value.", value=value)


class ValueNotInChoicesException(ServiceApiException):

    def __init__(self, value):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 26,
                                     "Value not in choices.", value=value)


class ValueNotWithinBoundariesException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 27,
                                     "Value not within boundaries.")


class InvalidBoundariesException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 28,
                                     "Invalid boundaries.")


class InvalidRangeException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 29,
                                     "Invalid values for range.")


class MultipleChoicesNeededException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 30,
                                     "At least 2 choices needed.")


class InvalidUnitException(ServiceApiException):

    def __init__(self, missing_tag):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 31,
                                     "Invalid unit format.", missing_tag=missing_tag)


class SuggestionTooLongException(ServiceApiException):

    def __init__(self, index):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 32,
                                     "Suggestion too long.", index=index)


class MembersDoNotReflectParentMessageException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 33,
                                     "Members do not reflect parent message members.")


class DismissUiFlagWithoutAllowDismissException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 34,
                                     "Undismissable messages can not have dismiss button ui flags.")


class UnknownUiFlagException(ServiceApiException):

    def __init__(self, button):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 35,
                                     "Invalid button ui flags.", button=button)


class UnknownDismissButtonUiFlagException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 36,
                                     "Invalid dismiss button ui flags.")


class InvalidDateSelectModeException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 37,
                                     "Invalid mode for date_select widget.")


class InvalidDateSelectMinuteIntervalException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 38,
                                     "The minimum minute_interval value is 1; the maximum minute_interval value is 30.")


class MinuteIntervalNotEvenlyDividedInto60Exception(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 39,
                                     "The minute_interval value must be a divisor of 60.")


class InvalidStepValue(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 40,
                                     "Step can not be greater than the slider range.")


class InvalidValueInDateSelectWithModeTime(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 41,
                                     "Invalid value in date_select with mode 'time'. The min_date, max_date and date values should be between 0 and 86400.")


class InvalidValueInDateSelectWithModeDate(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 42,
                                     "Invalid value in date_select with mode 'date'. The min_date, max_date and date values should be multiples of 86400.")


class DateSelectValuesShouldBeMultiplesOfMinuteInterval(ServiceApiException):

    def __init__(self, minute_interval):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 43,
                                     "The min_date, max_date and date values should be multiples of minute_interval.", minute_interval=minute_interval)


class ReservedTagException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 44,
                                     "Tag should not start with %s" % MC_RESERVED_TAG_PREFIX)


class InvalidBrandingException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 45,
                                     "This branding can not be used for messages.")


class InvalidFormException(ServiceApiException):

    def __init__(self, message):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 46, message)


class InvalidPhotoUploadQualityException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 47,
                                     "Invalid quality in photo_upload. Values can be 'best', 'user' or the max size in bytes")


class InvalidPhotoUploadSourceException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 48,
                                     "No source to select a picture has been provided.")


class InvalidPhotoUploadRatioException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 49,
                                     "Invalid ratio in photo_upload. (example: 100x100)")


class AttachmentDownloadException(ServiceApiException):

    def __init__(self, reason):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 50,
                                     "Not all attachment download URLs are reachable", reason=reason)


class InvalidAttachmentException(ServiceApiException):

    def __init__(self, reason):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 51,
                                     "Invalid attachment", reason=reason)


class MemberNotFoundException(ServiceApiException):

    def __init__(self, member, app_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 52,
                                     "Member not found", member=member, app_id=app_id)


class InvalidChatMemberStatusException(ServiceApiException):

    def __init__(self, status):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 53,
                                     "Invalid chat status", status=status)


class InvalidPriorityException(ServiceApiException):

    def __init__(self, priority):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 54,
                                     "Invalid priority.", priority=priority)


class InvalidMyDigiPassScopeException(ServiceApiException):

    def __init__(self, scope):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 55,
                                     "Invalid scope.", scope=scope)


class StepIdForbiddenException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 56,
                                     "step_id is only allowed in combination with 1 recipient and flag AUTO_LOCK.")


class MessageFlowValidationException(ServiceApiException):

    def __init__(self, reason):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 57,
                                     "Messageflow invalid.", reason=reason)


class InvalidURLException(ServiceApiException):

    def __init__(self, url):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 58,
                                     "Invalid url.", url=url)


class InvalidColorException(ServiceApiException):

    def __init__(self, color):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE + 59,
                                     "Invalid color.", color=color)
