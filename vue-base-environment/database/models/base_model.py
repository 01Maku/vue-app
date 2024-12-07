from app import db

class BaseSampleTableModel(db.Model):
    __tablename__ = 'sample_tbl'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    string_data = db.Column(db.String(100), nullable=False)
    integer_data = db.Column(db.Integer, nullable=False)
    float_data = db.Column(db.Float, nullable=False)
    boolean_data = db.Column(db.Boolean, default=True)
    text_data = db.Column(db.Text, nullable=True)
    date_data = db.Column(db.Date, nullable=True)

    def __repr__(self):
        return f"<Sample {self.name}>"
