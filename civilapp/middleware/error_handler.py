import traceback
from django.core.exceptions import PermissionDenied, ValidationError
from civilapp.common.response import ApiResponse
from civilapp.common.logger import logger
from civilapp.common.exceptions import CustomException

class GlobalExceptionMiddleware:
    """
    Centralized error-handling middleware.
    Catches all exceptions and ensures consistent JSON output.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            return self.get_response(request)
    
        except PermissionDenied as ex:
            logger.warning(f"Permission Denied: {ex}")
            return ApiResponse.error(
                message="You do not permissions to perform this activity",
                status=403,
                data=str(ex)
            )
        
        except ValidationError as ex:
            logger.warning(f"Validation Error: {ex}")
            return ApiResponse.error(
                message= "Validation error",
                data= str(ex),
                status=400
            )
        
        except Exception as ex:
            logger.warning(f"Exception Occured: {ex}")
            return ApiResponse.error(
                message="Internal Server Error",
                data=str(ex),
                status=500
            )
        
        except CustomException as ex:
            logger.warning(f"Custom Error: {ex}")
            return ApiResponse.error(
                message=ex.message,
                data=ex.data,
                status=ex.status
            )