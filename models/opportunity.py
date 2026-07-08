from . import db

class Opportunity(db.Model):

    id = db.Column(db.Integer, primary_key=True)

    title = db.Column(db.String(200), nullable=False)

    company = db.Column(db.String(150), nullable=False)

    category = db.Column(db.String(50), nullable=False)

    description = db.Column(db.Text)

    deadline = db.Column(db.Date)

    link = db.Column(db.String(300))

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )