#!/usr/bin/python
__author__ = 'joaci'

try:
    import os
    from pyfase import MicroService
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Cafe(MicroService):
    def __init__(self):
        super(Cafe, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')
        self.send_broadcast({'message': 'hello i am Cafe Shop'})

    def on_broadcast(self, service, data):
        print('### on_broadcast ### service: %s - data: %s' % (service, data))

    def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    @MicroService.action
    def make_coffee(self, service, data):
        print('### making some %s coffee to %s ' % (data['type'], service))
        self.request_action('drink_coffee', {'coffee': 'this is awesome coffee'})

Cafe().execute()
