#!/usr/bin/python
__author__ = 'joaci'

try:
    import time
    from fase import MicroService
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Ping(MicroService):
    def __init__(self):
        super(Ping, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')
        self.request_action('pong', {})

    @MicroService.action
    def ping(self, service, data):
        print('### service: %s request a ping ###' % service)
        time.sleep(2)
        self.request_action('pong', {})

Ping().execute()
