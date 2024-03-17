from config import *

def QUERY_nuevoTask(nombreTask):
    # inserta
    new_task = Task(
            name = nombreTask,
            status = False
        )
    db.session.add(new_task)
    db.session.commit()

def QUERY_actualizaTask(id):
    obj = Task.query.get(id)                                                    # trae el registro actual por ID
    if obj:
        obj.status = not obj.status                                             # niega el valor, (alternado/toggle)
        db.session.commit()                                                     # guarda cambios

def QUERY_eliminaTask(id):
    obj = Task.query.get(id)                                                    # trae el registro actual por ID
    if obj:
        db.session.delete(obj)
        db.session.commit()                                                     # guarda cambios        