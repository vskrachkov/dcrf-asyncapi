from channels.generic.websocket import AsyncJsonWebsocketConsumer
from django.test import SimpleTestCase

from introspect import introspect_application


class ConsumerIntrospectionTestCase(SimpleTestCase):
    class Consumer(AsyncJsonWebsocketConsumer):
        pass

    def test_consumer_without_actions(self) -> None:
        result = introspect_application(self.Consumer)
        self.assertEqual({}, result)
