from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

STATIC_DIR = './static/'


engine = create_engine(
    "postgresql+psycopg2://izzzy:ooFxfq111@izzzymusic.cpez7q0oykol.us-west-2.rds.amazonaws.com:5432/izzzymusic",
    isolation_level="READ UNCOMMITTED"
)

print("CONNECTING TO DATABASE")
conn = engine.connect()
print("CONNECTED")

metadata = MetaData()
Tracks = Table('music_track', metadata,
     Column('id', Integer, primary_key=True),
     Column('album', String),
     Column('artist', String),
     Column('title', String),
     Column('link', String),
     Column('telegram_id', String),
     Column('duration', Integer),
     Column('user_id', Integer),
 )