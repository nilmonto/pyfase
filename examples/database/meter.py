#!/usr/bin/python
__author__ = 'joaci'

try:
    import os
    from pyfase import MicroService
    import time
    import random
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Meter(MicroService):
    def __init__(self):
        super(Meter, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')

    def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    def on_response(self, service, data):
        print('### on_response ### service: %s respond an status of the action save_data previous resquested: %s' % (service, data))

    @MicroService.task
    def meter_proccess(self):
        while True:
            sensor_data = random.randrange(10, 50, 1)
            self.request_action('save_data', {'sensor': sensor_data})
            time.sleep(2)

Meter().execute(enable_tasks=True)

