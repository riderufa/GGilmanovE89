import nsq
import pickle
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = os.getenv('DATABASE_URL')

def handler(message):
    engine = create_engine(os.getenv('DATABASE_URI'))
    Session = sessionmaker(bind=engine)
    s = Session()
    unpickled = pickle.loads(message.body)
    s.add(unpickled)
    s.commit()
    s.close()
    # db.session.add(unpickled)
    # db.session.commit()
    return True

r = nsq.Reader(message_handler=handler,
        # nsqd_tcp_addresses=['172.19.0.5:4150'],
        nsqd_tcp_addresses=[os.getenv('TCP_ADDRESSES')],
        topic='results', 
        channel='test3',
        lookupd_poll_interval=15)

if __name__ == '__main__':
    nsq.run()