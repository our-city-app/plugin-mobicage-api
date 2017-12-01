from plugins.rogerthat_api.api import RogerthatApiException


class TestCallbackFailedException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_TEST + 0, "Test callback failed")


class ServiceIdentityDoesNotExistException(RogerthatApiException):

    def __init__(self, service_identity):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 0,
                                     u"Service identity does not exist", service_identity=service_identity)


class InvalidValueException(RogerthatApiException):

    def __init__(self, property_, reason):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 1,
                                     u"Invalid value", property=property_, reason=reason)


class InvalidMenuItemCoordinatesException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 2,
                                     u"A menu item has an x, y and page coordinate, with x and y smaller than 4")


class ReservedMenuItemException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 3,
                                     u"This menu item is reserved")


class CanNotDeleteBroadcastTypesException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 4,
                                     u"There are still broadcast settings menu items.")


class InvalidBroadcastTypeException(RogerthatApiException):

    def __init__(self, broadcast_type):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 5,
                                     u"Invalid broadcast type", broadcast_type=broadcast_type)


class DuplicateBroadcastTypeException(RogerthatApiException):

    def __init__(self, broadcast_type):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 6,
                                     u"Duplicate broadcast type", broadcast_type=broadcast_type)


class CreateServiceDeniedException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 7,
                                     u"No permission to create services")


class InvalidNameException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 8,
                                     u"Invalid name")


class ServiceAlreadyExistsException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 9,
                                     u"Service with that e-mail address already exists")


class UnsupportedLanguageException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 10,
                                     u"This language is not supported")


class FriendNotFoundException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 11,
                                     u"User not in friends list")


class InvalidJsonStringException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 12,
                                     u"Can not parse data as json object")


class AvatarImageNotSquareException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 13,
                                     u"Expected a square input image")


class CategoryNotFoundException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 14,
                                     u"Category not found")


class CallbackNotDefinedException(RogerthatApiException):

    def __init__(self, function):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 15,
                                     u"Callback not defined", function=function)


class BeaconAlreadyCoupledException(RogerthatApiException):

    def __init__(self, beacon_uuid, beacon_major, beacon_minor):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 16,
                                     u"Beacon already coupled", uuid=beacon_uuid, major=beacon_major,
                                     minor=beacon_minor)


class InvalidAppIdException(RogerthatApiException):

    def __init__(self, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 17,
                                     u"Invalid app_id", app_id=app_id)


class UnsupportedAppIdException(RogerthatApiException):

    def __init__(self, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 18,
                                     u"Unsupported app_id", app_id=app_id)


class RoleNotFoundException(RogerthatApiException):

    def __init__(self, role_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 19,
                                     u"Role does not exist", role_id=role_id)


class RoleAlreadyExistsException(RogerthatApiException):

    def __init__(self, name):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 20,
                                     u"Role with this name already exists", name=name)


class InvalidRoleTypeException(RogerthatApiException):

    def __init__(self, type_):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 21,
                                     u"Invalid role type", type=type_)


class DeleteRoleFailedHasMembersException(RogerthatApiException):

    def __init__(self, role_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 22,
                                     u"Cannot delete role which is still granted to people.", role_id=role_id)


class DeleteRoleFailedHasSMDException(RogerthatApiException):

    def __init__(self, role_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 23,
                                     u"Cannot delete role which is still connected to a service menu item",
                                     role_id=role_id)


class UserWithThisEmailAddressAlreadyExistsException(RogerthatApiException):

    def __init__(self, email):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 24,
                                     u"An account with this e-mail address already exists", email=email)


class AppOperationDeniedException(RogerthatApiException):

    def __init__(self, app_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 25,
                                     u"No permission to manage app", app_id=app_id)


class ServiceWithEmailDoesNotExistsException(RogerthatApiException):

    def __init__(self, service_identity_email):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 26,
                                     u"There is no service with this email",
                                     service_identity_email=service_identity_email)


class NoBeaconRegionFoundException(RogerthatApiException):

    def __init__(self, beacon_uuid, beacon_major, beacon_minor):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 27,
                                     u"There is no beacon region for this beacon. Please contact Mobicage for support.",
                                     uuid=beacon_uuid, major=beacon_major, minor=beacon_minor)


class MyDigiPassNotSupportedException(RogerthatApiException):

    def __init__(self, unsupported_app_ids):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 28,
                                     u"Not all supported apps of this service implement MYDIGIPASS.",
                                     unsupported_app_ids=unsupported_app_ids)


class AppFailedToResovelUrlException(RogerthatApiException):

    def __init__(self, url):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 32,
                                     u"Failed to resolve url", url=url)


class AppFailedToCreateUserProfileWithExistingServiceException(RogerthatApiException):

    def __init__(self, email):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 33,
                                     u"Failed to create user profile with the same email as a service account",
                                     email=email)


class InvalidKeyException(RogerthatApiException):

    def __init__(self, key):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 34,
                                     u"Invalid key", key=key)


class DuplicateCategoryIdException(RogerthatApiException):

    def __init__(self, category_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 35,
                                     u"Duplicate category id", category_id=category_id)


class DuplicateItemIdException(RogerthatApiException):

    def __init__(self, category_id, item_id):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 36,
                                     u"Duplicate item id", category_id=category_id, item_id=item_id)


class SigningNotSupportedException(RogerthatApiException):

    def __init__(self, unsupported_app_ids):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 37,
                                     u"Not all supported apps of this service implement signing.",
                                     unsupported_app_ids=unsupported_app_ids)


class InvalidSignPayloadException(RogerthatApiException):

    def __init__(self):
        RogerthatApiException.__init__(self, RogerthatApiException.BASE_CODE_SERVICE + 38,
                                     u'Invalid payload. Make sure the payload is base64 encoded properly.')
