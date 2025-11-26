from django.http import JsonResponse

class ApiResponse:

    @staticmethod
    def success(data=None, message='Success', status=200):
        "Standard response object"
        return JsonResponse({
            "success": True,
            "message": message,
            "data": data
        }, status = status)
    
    @staticmethod
    def error(message="Error", data=None, status=400):
        """
        Standard error response wrapper.
        Used by middleware and views.
        """
        return JsonResponse(
            {
                "success": False,
                "message": message,
                "data": data
            },
            status=status
        )