#from facebook_robot.common import postgres
#db = postgres.connect('postgres','postgres','botapi')

from facebook_robot.data.db_context import db
import datetime


class MessageSession(db.Model):
    __tablename__ = 'message_session'

    id = db.Column(db.BigInteger, primary_key=True)
    provider = db.Column(db.String(100))
    channel = db.Column(db.String(100))
    direction = db.Column(db.String(10))
    create_time = db.Column(db.DateTime)
    payload = db.Column(db.JSON)

    def __init__(self, provider, channel, direction, payload):
        self.provider = provider
        self.channel = channel
        self.direction = direction
        self.create_time = datetime.date.today()
        self.payload = payload

    def __repr__(self):
        return '<Message %r>' % (self.channel)
