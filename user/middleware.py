from django.contrib.messages import get_messages

class DisableCacheMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
        response['Pragma'] = 'no-cache'
        response['Expires'] = '0'
        return response

class ClearMessagesMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Lê todas as mensagens e força a remoção após a leitura
        storage = get_messages(request)
        for _ in storage:
            pass  # Apenas acessando força a remoção

        response = self.get_response(request)
        return response