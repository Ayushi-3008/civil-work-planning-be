class CustomException(Exception):
    """
    Custom exception for business-level validation or domain errors.
    These errors are expected and should return a clean message to the user,
    not a stack trace.
    """

    def __init__(self, message, data=None, status=400):
        """
        :param message: Human readable message explaining the issue
        :param error_code: Internal application error code (string/int)
        :param status_code: HTTP status code (default 400)
        """
        self.message = message
        self.data = data or "BUSINESS_ERROR"
        self.status = status
        super().__init__(message)

    def __str__(self):
        return f"{self.data}: {self.message}"
