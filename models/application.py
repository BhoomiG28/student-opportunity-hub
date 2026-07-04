from . import db

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    status = db.Column(db.String(50), nullable=False)

    notes = db.Column(db.Text)

    applied_date = db.Column(db.Date)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user.id"),
        nullable=False
    )

    opportunity_id = db.Column(
        db.Integer,
        db.ForeignKey("opportunity.id"),
        nullable=False
    )