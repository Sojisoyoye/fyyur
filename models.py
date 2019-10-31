from app import app, db
from flask_migrate import Migrate

migrate = Migrate(app, db)
String = db.String

shows = db.Table('show',
    db.Column('venue_id', db.Integer, db.ForeignKey('venue.id'), primary_key=True),
    db.Column('artist_id', db.Integer, db.ForeignKey('artist.id'), primary_key=True)
)
class Venue(db.Model):
    __tablename__ = 'venue'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.PickleType, nullable=True)
    address = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_talent = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    past_shows = db.Column(db.ARRAY(String))
    upcoming_shows = db.Column(db.ARRAY(String))
    past_shows_count = db.Column(db.Integer)
    upcoming_shows_count = db.Column(db.Integer)
    artists = db.relationship('Artist', secondary=shows,
        backref=db.backref('venues', lazy=True))

    def __ref__(self):
        return f'<Venue {self.name} {self.city}>'


class Artist(db.Model):
    __tablename__ = 'artist'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    genres = db.Column(db.PickleType, nullable=True)
    city = db.Column(db.String(120))
    state = db.Column(db.String(120))
    phone = db.Column(db.String(120))
    website = db.Column(db.String(120))
    facebook_link = db.Column(db.String(120))
    seeking_venue = db.Column(db.Boolean, default=False)
    seeking_description = db.Column(db.String(120))
    image_link = db.Column(db.String(500))
    past_shows = db.Column(db.ARRAY(String))
    upcoming_shows = db.Column(db.ARRAY(String))
    past_shows_count = db.Column(db.Integer)
    upcoming_shows_count = db.Column(db.Integer)

    def __ref__(self):
        return f'<Artist {self.name} {self.city}>'