"""Flask app for Cupcakes"""

from flask import Flask,request ,render_template,jsonify
from models import db, connect_db,Cupcake


app = Flask(__name__)
# i need you to talk to postgresql using database movies_example
app.config['SQLALCHEMY_DATABASE_URI']='postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "ThisisHappyyuy3693"
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS']=False
# debug = DebugToolbarExtension(app)
# app.debug = True
app.app_context().push()
# call connect_db
connect_db(app)



##### root route
@app.route('/')
def index():
    return render_template('index.html')

######GET /api/cupcakes
@app.route('/api/cupcakes')
def list_all_cupcakes():
    cupcakes = Cupcake.query.all()
    serialized = [cupcake.serialize_cupcake() for cupcake in cupcakes]
    return jsonify(cupcakes = serialized)

#####GET /api/cupcakes/[cupcake-id]
@app.route('/api/cupcakes/<int:id>')
def show_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    return jsonify(cupcake=cupcake.serialize_cupcake())
   
######POST /api/cupcakes
@app.route('/api/cupcakes' , methods = ["POST"])
def create_cupcake():
    flavor =request.json["flavor"]
    size =request.json["size"]
    print(size)
    rating =request.json["rating"]
    image =request.json["image"]
    new_cupcake =Cupcake(flavor=flavor,size=size,rating=rating,image=image)
    db.session.add(new_cupcake)
    db.session.commit()
    res_json = jsonify(cupcake = new_cupcake.serialize_cupcake())
    return (res_json,201)
#     # data = request.json

    # cupcake = Cupcake(
    #     flavor=data['flavor'],
    #     rating=data['rating'],
    #     size=data['size'],
    #     image=data['image'] or None)

    # db.session.add(cupcake)
    # db.session.commit()

    # # POST requests should return HTTP status of 201 CREATED
    # return (jsonify(cupcake=cupcake.serialize_cupcake()), 201)
    
######### PATCH /api/cupcakes/[cupcake-id]
@app.route('/api/cupcakes/<int:id>', methods=["PATCH"])
def update_cupcake(id):
    cupcake = Cupcake.query.get_or_404(id)
    cupcake.flavor=request.json.get('flavor',cupcake.flavor)
    cupcake.size = request.json.get("size",cupcake.size)
    cupcake.rating = request.json.get("rating",cupcake.rating)
    cupcake.image = request.json.get("image",cupcake.image)
    db.session.commit()
    return jsonify(cupcake=cupcake.serialize_cupcake())

@app.route('/api/cupcakes/<int:id>',methods=["DELETE"])
def delete_cupcake(id):
    cupcake=Cupcake.query.get_or_404(id)
    db.session.delete(cupcake)
    db.session.commit()
    return jsonify(message="Delete")