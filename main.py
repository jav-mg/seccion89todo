from config import *
from rutas import *

#inicia server
if __name__ == "__main__":
    app.run(debug=True, port=5020, host="0.0.0.0")
