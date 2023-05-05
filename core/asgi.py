
import os

from channels.security.websocket import AllowedHostsOriginValidator
from django.core.asgi import get_asgi_application

from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

import room.routing
from room.consumers import ChatConsumer


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": AllowedHostsOriginValidator(
            AuthMiddlewareStack(URLRouter([path('ws/<str:room_name>/', ChatConsumer.as_asgi())]))
        ),
    }
)


