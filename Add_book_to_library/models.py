from app import db


class Academic(db.Model):
    __tablename__ = "academics"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)

    def __repr__(self):
        return "<Academic: {}>".format(self.name)


class Biography(db.Model):
    """"""
    __tablename__ = "biography"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    release_date = db.Column(db.String)
    publisher = db.Column(db.String)
    media_type = db.Column(db.String)

    academics_id = db.Column(db.Integer, db.ForeignKey("academics.id"))
    academics = db.relationship("Academic", backref=db.backref(
        "biography", order_by=id), lazy=True)