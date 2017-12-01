from plugins.rogerthat_api.api import RogerthatApiException
from plugins.rogerthat_api.consts import MC_RESERVED_TAG_PREFIX


class InvalidDirtyBehaviorException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 16,
                                     "Invalid dirty_behavior.")


class MessageLockedException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 10,
                                     "Message is already locked.")


class MessageNotFoundException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 9,
                                     "Message not found.")


class CanOnlySendToFriendsException(RogerthatApiException):

    def __init__(self, member, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 0,
                                     "Member is not in your friends list.", member=member, app_id=app_id)


class CanNotSendToServicesException(RogerthatApiException):

    def __init__(self, member, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 15,
                                     "Can not send to services.", member=member, app_id=app_id)


class ParentMessageNotFoundException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 1,
                                     "Parent message not found.")


class CanOnlyReplyToMembersException(Exception):
    pass


class DuplicateMembersException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 13,
                                     "Duplicate members.")


class InvalidFlagsException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 3,
                                     "Invalid flags.")


class UnknownMessageAlertFlagException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 17,
                                     "Invalid alert flags.")


class RingAlertFlagsAreNotCombinableException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 18,
                                     "You cannot combine multiple ring flags.")


class IntervalAlertFlagsAreNotCombinableException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 19,
                                     "You cannot combine multiple interval flags.")


class AutoLockCanOnlyHaveOneMemberInMessageException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 11,
                                     "Autoseal flag implies maximum one member.")


class UnDismissableMessagesNeedAnswersException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 12,
                                     "Undismissable messages need at least one answer.")


class InvalidSenderReplyValue(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 2,
                                     "Illegal sender answer.")


class TagTooLargeException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 4,
                                     "Tag too large.")


class UnsupportedActionTypeException(RogerthatApiException):

    def __init__(self, scheme):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 6,
                                     "Unsupported answer action type.", scheme=scheme)


class UnknownAnswerWidgetType(RogerthatApiException):

    def __init__(self, widget_type):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 5,
                                     "Unknown answer widget type", widget_type=widget_type)


class IncompleteButtonException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 8,
                                     "Incomplete button.")


class BrandingNotFoundException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 7,
                                     "Branding not found.")


class DuplicateButtonIdException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 14,
                                     "Duplicate button ids.")


class InvalidWidgetValueException(RogerthatApiException):

    def __init__(self, property_):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 20,
                                     "Invalid value in widget.", property=property_)


class ValueTooLongException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 21,
                                     "Value too long.")


class NoChoicesSpecifiedException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 22,
                                     "No choices specified.")


class DuplicateChoiceLabelException(RogerthatApiException):

    def __init__(self, label):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 23,
                                     "Duplicate label in choices.", label=label)


class DuplicateChoiceValueException(RogerthatApiException):

    def __init__(self, value):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 24,
                                     "Duplicate value in choices.", value=value)


class DuplicateValueException(RogerthatApiException):

    def __init__(self, value):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 25,
                                     "Duplicate value.", value=value)


class ValueNotInChoicesException(RogerthatApiException):

    def __init__(self, value):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 26,
                                     "Value not in choices.", value=value)


class ValueNotWithinBoundariesException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 27,
                                     "Value not within boundaries.")


class InvalidBoundariesException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 28,
                                     "Invalid boundaries.")


class InvalidRangeException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 29,
                                     "Invalid values for range.")


class MultipleChoicesNeededException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 30,
                                     "At least 2 choices needed.")


class InvalidUnitException(RogerthatApiException):

    def __init__(self, missing_tag):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 31,
                                     "Invalid unit format.", missing_tag=missing_tag)


class SuggestionTooLongException(RogerthatApiException):

    def __init__(self, index):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 32,
                                     "Suggestion too long.", index=index)


class MembersDoNotReflectParentMessageException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 33,
                                     "Members do not reflect parent message members.")


class DismissUiFlagWithoutAllowDismissException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 34,
                                     "Undismissable messages can not have dismiss button ui flags.")


class UnknownUiFlagException(RogerthatApiException):

    def __init__(self, button):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 35,
                                     "Invalid button ui flags.", button=button)


class UnknownDismissButtonUiFlagException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 36,
                                     "Invalid dismiss button ui flags.")


class InvalidDateSelectModeException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 37,
                                     "Invalid mode for date_select widget.")


class InvalidDateSelectMinuteIntervalException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 38,
                                     "The minimum minute_interval value is 1; the maximum minute_interval value is 30.")


class MinuteIntervalNotEvenlyDividedInto60Exception(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 39,
                                     "The minute_interval value must be a divisor of 60.")


class InvalidStepValue(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 40,
                                     "Step can not be greater than the slider range.")


class InvalidValueInDateSelectWithModeTime(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 41,
                                     "Invalid value in date_select with mode 'time'. The min_date, max_date and date values should be between 0 and 86400.")


class InvalidValueInDateSelectWithModeDate(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 42,
                                     "Invalid value in date_select with mode 'date'. The min_date, max_date and date values should be multiples of 86400.")


class DateSelectValuesShouldBeMultiplesOfMinuteInterval(RogerthatApiException):

    def __init__(self, minute_interval):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 43,
                                     "The min_date, max_date and date values should be multiples of minute_interval.", minute_interval=minute_interval)


class ReservedTagException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 44,
                                     "Tag should not start with %s" % MC_RESERVED_TAG_PREFIX)


class InvalidBrandingException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 45,
                                     "This branding can not be used for messages.")


class InvalidFormException(RogerthatApiException):

    def __init__(self, message):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 46, message)


class InvalidPhotoUploadQualityException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 47,
                                     "Invalid quality in photo_upload. Values can be 'best', 'user' or the max size in bytes")


class InvalidPhotoUploadSourceException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 48,
                                     "No source to select a picture has been provided.")


class InvalidPhotoUploadRatioException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 49,
                                     "Invalid ratio in photo_upload. (example: 100x100)")


class AttachmentDownloadException(RogerthatApiException):

    def __init__(self, reason):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 50,
                                     "Not all attachment download URLs are reachable", reason=reason)


class InvalidAttachmentException(RogerthatApiException):

    def __init__(self, reason):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 51,
                                     "Invalid attachment", reason=reason)


class MemberNotFoundException(RogerthatApiException):

    def __init__(self, member, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 52,
                                     "Member not found", member=member, app_id=app_id)


class InvalidChatMemberStatusException(RogerthatApiException):

    def __init__(self, status):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 53,
                                     "Invalid chat status", status=status)


class InvalidPriorityException(RogerthatApiException):

    def __init__(self, priority):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 54,
                                     "Invalid priority.", priority=priority)


class InvalidMyDigiPassScopeException(RogerthatApiException):

    def __init__(self, scope):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 55,
                                     "Invalid scope.", scope=scope)


class StepIdForbiddenException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 56,
                                     "step_id is only allowed in combination with 1 recipient and flag AUTO_LOCK.")


class MessageFlowValidationException(RogerthatApiException):

    def __init__(self, reason):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 57,
                                     "Messageflow invalid.", reason=reason)


class InvalidURLException(RogerthatApiException):

    def __init__(self, url):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 58,
                                     "Invalid url.", url=url)


class InvalidColorException(RogerthatApiException):

    def __init__(self, color):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_MESSAGE + 59,
                                     "Invalid color.", color=color)
