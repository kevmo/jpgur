from app import db


class Link(db.Model):
    __tablename__ = 'links'

    id = db.Column(db.Integer, primary_key=True)
    url= db.Column(db.String, nullable=False)

    def __init__(self, url):
        self.url = url

    def __repr__(self):
        return '<Link {} {}>'.format(self.id, self.url)
