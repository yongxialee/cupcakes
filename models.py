"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

DEFAULT_IMAGE= "https://cookienameddesire.com/wp-content/uploads/2020/12/gingerbread-cupcakes-4-320x320.jpg"
def connect_db(app):
    db.app=app
    db.init_app(app)
    
    
## Models go below this line
class Cupcake(db.Model):
    """cupcake model"""
    __tablename__="cupcakes"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    flavor = db.Column(db.Text, nullable=False)
    size = db.Column(db.Text,nullable = False,default="medium")
    rating = db.Column(db.Float,nullable = False)
    image = db.Column(db.Text,nullable = False, default =DEFAULT_IMAGE)
    
    def serialize_cupcake(self):
        """serialize cupcake to a dict of cupcake infor"""
        return {
            "id" : self.id,
            "flavor":self.flavor,
            "rating": self.rating,
            "image":self.image
        }