#!/usr/bin/python
__author__ = 'joaci'

try:
    import time
    from fase import MicroServiceBase
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Ping(MicroServiceBase):
    def __init__(self):
        super(Ping, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')
        self.request_action('pong', {})

    @MicroServiceBase.action
    def ping(self, service, data):
        print('### service: %s request a ping ###' % service)
        time.sleep(2)
        self.request_action('pong', {})

Ping().execute()
