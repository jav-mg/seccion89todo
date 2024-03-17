from config import *
from consultasAlchemy import *           # se desactiva consulta directa a SQLite

# ~~~ rutas ~~~
@app.route("/")
def home():
    result = db.session.execute(db.select(Task).order_by(Task.id))    
    all_tasks = result.scalars()                                                # Use .scalars() to get the elements rather than entire rows from the database
    return render_template("index.html", tasks=all_tasks)

@app.route("/saveTask", methods=["POST"])
def saveTask():
    task = request.form['task']
    QUERY_nuevoTask(task)
    return redirect(url_for("home"))

@app.route("/updateTask/<id>", methods=["GET"])
def updateTask(id):    
    QUERY_actualizaTask(id)        
    return redirect(url_for("home"))

@app.route("/eliminarTask", methods=["POST"])
def eliminarTask():    
    id = request.form['id']    
    QUERY_eliminaTask(id)        
    return redirect(url_for("home"))
    