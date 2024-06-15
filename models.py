from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Market(db.Model):
    __tablename__ = 'markets'

    fm_id = db.Column(db.BigInteger, primary_key=True)
    market_name = db.Column(db.String(255), nullable=True)
    website = db.Column(db.String(255), nullable=True)
    street = db.Column(db.String(255), nullable=True)
    city = db.Column(db.String(255), nullable=True)
    county = db.Column(db.String(255), nullable=True)
    state = db.Column(db.String(255), nullable=True)
    zip = db.Column(db.String(10), nullable=True)
    rating = db.Column(db.Numeric, default=1.0, nullable=True)

    reviews = db.relationship('Review', backref='market', lazy=True, cascade="all, delete-orphan")

    __table_args__ = (
        db.CheckConstraint('rating >= 1.0 AND rating <= 5.0', name='markets_rating_check'),
    )


class Review(db.Model):
    __tablename__ = 'reviews'

    review_id = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    fm_id = db.Column(db.BigInteger, db.ForeignKey('markets.fm_id'), nullable=False)
    user_nickname = db.Column(db.String(255), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    text = db.Column(db.String(1000), nullable=True)

    __table_args__ = (
        db.CheckConstraint('rating >= 1 AND rating <= 5', name='reviews_rating_check'),
    )