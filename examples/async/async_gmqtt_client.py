#!/usr/bin/python
__author__ = 'joaci'

try:
    import os
    import asyncio
    import uvloop
    import time
    from pyfase import MicroService
    from gmqtt import Client as MQTTClient
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Asyncgmqttclient(MicroService):
    def __init__(self):
        super(Asyncgmqttclient, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')
        self.mqtt_client = None
        self.stop = asyncio.Event()

    def on_connect(self):
        print('### on_connect ###')
        self.send_broadcast({'message': 'hello i am Cafe Shop'})

    def on_broadcast(self, service, data):
        print('### on_broadcast ### service: %s - data: %s' % (service, data))

    def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    @MicroService.async_action
    def make_coffee(self, service, data):
        print('### making some %s coffee to %s ' % (data['type'], service))
        self.request_action('drink_coffee', {'coffee': 'this is awesome coffee'})

    def mqtt_on_connect(self, client, flags, rc, properties):
        print('### mqtt_on_connect ###')
        client.subscribe('TEST/#', qos=0)

    def mqtt_on_message(self, client, topic, payload, qos, properties):
        print('### mqtt_on_message ###: %s', payload)

    def mqtt_on_disconnect(self, client, packet, exc=None):
        print('### mqtt_on_disconnect ###')

    def mqtt_on_subscribe(self, client, mid, qos):
        print('### mqtt_on_subscribe ###')

    async def mqtt_task(self):
        self.mqtt_client = MQTTClient("client-id")

        self.mqtt_client.on_connect = self.mqtt_on_connect
        self.mqtt_client.on_message = self.mqtt_on_message
        self.mqtt_client.on_disconnect = self.mqtt_on_disconnect
        self.mqtt_client.on_subscribe = self.mqtt_on_subscribe

        try:
            await self.mqtt_client.connect('192.168.1.45', 1883)
            self.mqtt_client.publish('TEST/TIME', str(time.time()), qos=1)
        except Exception as e:
            print(e)

        await self.stop.wait()
        await self.mqtt_client.disconnect()


Ac = Asyncgmqttclient()
loop = asyncio.get_event_loop()
asyncio.ensure_future(Ac.async_execute())
loop.run_until_complete(Ac.mqtt_task())
loop.run_until_complete(Ac.async_execute())


