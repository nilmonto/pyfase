#!/usr/bin/python
__author__ = 'joaci'

try:
    import os
    from fase import MicroServiceBase
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Client(MicroServiceBase):
    def __init__(self):
        super(Client, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('hello i\'m Client and i want coffee')
        self.request_action('make_coffee', {'type': 'brazilian'})

    def on_broadcast(self, service, data):
        print('### on_broadcast ### service: %s - data: %s' % (service, data))

    def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    @MicroServiceBase.action
    def drink_coffee(self, service, data):
        print('### drinking coffee... %s!!! thank you: %s ' % (data['coffee'], service))

Client().execute()
