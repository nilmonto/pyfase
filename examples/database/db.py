#!/usr/bin/python
__author__ = 'joaci'

try:
    import os
    from pyfase import MicroService
except Exception as e:
    print('require module exception: %s' % e)
    exit(0)


class Db(MicroService):
    def __init__(self):
        super(Db, self).__init__(self, sender_endpoint='ipc:///tmp/sender', receiver_endpoint='ipc:///tmp/receiver')

    def on_connect(self):
        print('### on_connect ###')
        self.send_broadcast({'message': 'database service is online'})

    def on_new_service(self, service, actions):
        print('### on_new_service ### service: %s - actions: %s' % (service, actions))

    @MicroService.action
    def save_data(self, service, data):
        print('### action::save_data: %s ' % data)
        # save some data on database and respond a status to requester 'service'
        self.response({'save_data_ack': {'status': 'saved'}})

Db().execute()
