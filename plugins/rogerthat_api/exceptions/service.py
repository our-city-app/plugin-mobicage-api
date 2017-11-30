from plugins.rogerthat_api.exceptions import ServiceApiException


class TestCallbackFailedException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_TEST + 0, "Test callback failed")


class ServiceIdentityDoesNotExistException(ServiceApiException):

    def __init__(self, service_identity):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 0,
                                     u"Service identity does not exist", service_identity=service_identity)


class InvalidValueException(ServiceApiException):

    def __init__(self, property_, reason):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 1,
                                     u"Invalid value", property=property_, reason=reason)


class InvalidMenuItemCoordinatesException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 2,
                                     u"A menu item has an x, y and page coordinate, with x and y smaller than 4")


class ReservedMenuItemException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 3,
                                     u"This menu item is reserved")


class CanNotDeleteBroadcastTypesException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 4,
                                     u"There are still broadcast settings menu items.")


class InvalidBroadcastTypeException(ServiceApiException):

    def __init__(self, broadcast_type):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 5,
                                     u"Invalid broadcast type", broadcast_type=broadcast_type)


class DuplicateBroadcastTypeException(ServiceApiException):

    def __init__(self, broadcast_type):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 6,
                                     u"Duplicate broadcast type", broadcast_type=broadcast_type)


class CreateServiceDeniedException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 7,
                                     u"No permission to create services")


class InvalidNameException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 8,
                                     u"Invalid name")


class ServiceAlreadyExistsException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 9,
                                     u"Service with that e-mail address already exists")


class UnsupportedLanguageException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 10,
                                     u"This language is not supported")


class FriendNotFoundException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 11,
                                     u"User not in friends list")


class InvalidJsonStringException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 12,
                                     u"Can not parse data as json object")


class AvatarImageNotSquareException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 13,
                                     u"Expected a square input image")


class CategoryNotFoundException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 14,
                                     u"Category not found")


class CallbackNotDefinedException(ServiceApiException):

    def __init__(self, function):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 15,
                                     u"Callback not defined", function=function)


class BeaconAlreadyCoupledException(ServiceApiException):

    def __init__(self, beacon_uuid, beacon_major, beacon_minor):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 16,
                                     u"Beacon already coupled", uuid=beacon_uuid, major=beacon_major,
                                     minor=beacon_minor)


class InvalidAppIdException(ServiceApiException):

    def __init__(self, app_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 17,
                                     u"Invalid app_id", app_id=app_id)


class UnsupportedAppIdException(ServiceApiException):

    def __init__(self, app_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 18,
                                     u"Unsupported app_id", app_id=app_id)


class RoleNotFoundException(ServiceApiException):

    def __init__(self, role_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 19,
                                     u"Role does not exist", role_id=role_id)


class RoleAlreadyExistsException(ServiceApiException):

    def __init__(self, name):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 20,
                                     u"Role with this name already exists", name=name)


class InvalidRoleTypeException(ServiceApiException):

    def __init__(self, type_):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 21,
                                     u"Invalid role type", type=type_)


class DeleteRoleFailedHasMembersException(ServiceApiException):

    def __init__(self, role_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 22,
                                     u"Cannot delete role which is still granted to people.", role_id=role_id)


class DeleteRoleFailedHasSMDException(ServiceApiException):

    def __init__(self, role_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 23,
                                     u"Cannot delete role which is still connected to a service menu item",
                                     role_id=role_id)


class UserWithThisEmailAddressAlreadyExistsException(ServiceApiException):

    def __init__(self, email):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 24,
                                     u"An account with this e-mail address already exists", email=email)


class AppOperationDeniedException(ServiceApiException):

    def __init__(self, app_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 25,
                                     u"No permission to manage app", app_id=app_id)


class ServiceWithEmailDoesNotExistsException(ServiceApiException):

    def __init__(self, service_identity_email):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 26,
                                     u"There is no service with this email",
                                     service_identity_email=service_identity_email)


class NoBeaconRegionFoundException(ServiceApiException):

    def __init__(self, beacon_uuid, beacon_major, beacon_minor):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 27,
                                     u"There is no beacon region for this beacon. Please contact Mobicage for support.",
                                     uuid=beacon_uuid, major=beacon_major, minor=beacon_minor)


class MyDigiPassNotSupportedException(ServiceApiException):

    def __init__(self, unsupported_app_ids):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 28,
                                     u"Not all supported apps of this service implement MYDIGIPASS.",
                                     unsupported_app_ids=unsupported_app_ids)


class AppFailedToResovelUrlException(ServiceApiException):

    def __init__(self, url):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 32,
                                     u"Failed to resolve url", url=url)


class AppFailedToCreateUserProfileWithExistingServiceException(ServiceApiException):

    def __init__(self, email):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 33,
                                     u"Failed to create user profile with the same email as a service account",
                                     email=email)


class InvalidKeyException(ServiceApiException):

    def __init__(self, key):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 34,
                                     u"Invalid key", key=key)


class DuplicateCategoryIdException(ServiceApiException):

    def __init__(self, category_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 35,
                                     u"Duplicate category id", category_id=category_id)


class DuplicateItemIdException(ServiceApiException):

    def __init__(self, category_id, item_id):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 36,
                                     u"Duplicate item id", category_id=category_id, item_id=item_id)


class SigningNotSupportedException(ServiceApiException):

    def __init__(self, unsupported_app_ids):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 37,
                                     u"Not all supported apps of this service implement signing.",
                                     unsupported_app_ids=unsupported_app_ids)


class InvalidSignPayloadException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_SERVICE + 38,
                                     u'Invalid payload. Make sure the payload is base64 encoded properly.')
