from django.http.response import JsonResponse

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        if request.user.username in ["testman"] and (not request.path.startwith("/admin"))
            return JsonResponse("Error, You are forbidden entering this web!")

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response