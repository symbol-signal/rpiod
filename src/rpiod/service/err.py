class ServiceException(Exception):
    pass


class APINotStarted(ServiceException):
    pass


class ServiceNotStarted(ServiceException):
    pass


class ErrorDuringShutdown(ServiceException):
    pass


class ServiceAlreadyRunning(ServiceException):
    pass
