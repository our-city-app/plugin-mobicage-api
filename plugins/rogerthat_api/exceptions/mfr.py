from plugins.rogerthat_api.exceptions import ServiceApiException


class MessageFlowNotFoundException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 1,
                                     "Message flow definition not found!")


class NonFriendMembersException(ServiceApiException):

    def __init__(self, non_members):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 2,
                                     "Non-friend members supplied!", non_members=non_members)


class MessageFlowNotValidException(ServiceApiException):

    def __init__(self, error):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 3,
                                     "Message flow is not valid and cannot be executed in its current state!", error=error)


class MessageParentKeyCannotBeUsedWithMultipleParents(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 4,
                                     "You can not use the message parent key with multiple members.")


class NoMembersException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 5,
                                     "No members supplied!")


class MessageFlowDesignInUseException(ServiceApiException):

    def __init__(self, reason):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 6,
                                     "Message flow can not be deleted", reason=reason)


class InvalidMessageFlowXmlException(ServiceApiException):

    def __init__(self):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 7,
                                     "The XML is not conform to the message flow design XML schema")


class MessageFlowDesignValidationException(ServiceApiException):

    def __init__(self, message_flow_design):
        self.message_flow_design = message_flow_design
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 8,
                                     "Message flow design is not valid: %s" % message_flow_design.validation_error,
                                     validation_error=message_flow_design.validation_error)


class InvalidMessageFlowLanguageException(ServiceApiException):

    def __init__(self, expected_language, current_language):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 9,
                                     "Unexpected language specified in message flow design XML. Expected language '%s', got language '%s'." % (expected_language, current_language),
                                     expected_language=expected_language, current_language=current_language)


class InvalidMessageAttachmentException(ServiceApiException):

    def __init__(self, reason):
        ServiceApiException.__init__(self, ServiceApiException.BASE_CODE_MESSAGE_FLOW + 10, reason)
