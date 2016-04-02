#!/usr/bin/python
__author__ = 'joaci'

try:
    import time
    from fase import MicroServiceBase
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Pong(MicroServiceBase):
    def __init__(self):
        super(Pong, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')
        self.request_action('ping', {})

    def on_broadcast(self, service, data):
        pass

    def on_new_service(self, service, actions):
        pass

    @MicroServiceBase.action
    def pong(self, service, data):
        print('### service: %s request a pong ###' % service)
        time.sleep(2)
        self.request_action('ping', {})

Pong().execute()
