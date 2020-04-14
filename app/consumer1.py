import nsq
import pickle
import os
from app import db

def handler(message):
    unpickled = pickle.loads(message.body)
    db.session.add(unpickled)
    db.session.commit()
    return True

r = nsq.Reader(message_handler=handler,
        nsqd_tcp_addresses=['172.19.0.5:4150'],
        # nsqd_tcp_addresses=[os.getenv('TCP_ADDRESSES')],
        topic='results', 
        channel='test3',
        lookupd_poll_interval=15)

if __name__ == '__main__':
    nsq.run()