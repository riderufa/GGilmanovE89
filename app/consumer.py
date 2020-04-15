import nsq
import pickle
import os
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
# from models import Results
# from app import db

# DATABASE_URL = os.getenv('DATABASE_URL')

Base = declarative_base()

class Results(Base):
    __tablename__ = "results"
    id = sa.Column(sa.INTEGER, primary_key=True)
    address = sa.Column(sa.TEXT)
    words_count = sa.Column(sa.INTEGER)
    http_status_code = sa.Column(sa.INTEGER)

def handler(message):
    engine = sa.create_engine(os.getenv('DATABASE_URI'))
    Session = sessionmaker(bind=engine)
    s = Session()
    unpickled = pickle.loads(message.body)
    result = Results(address=unpickled['address'], words_count=unpickled['words_count'], http_status_code=unpickled['http_status_code'])
    s.add(result)
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