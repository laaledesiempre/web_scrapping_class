from flask import Flask, request, jsonify

app = Flask(__name__) 

usuarios= {} # nuestros usuarios!, la estructura va a ser "nombre":"apodo"

@app.get("/usuarios")
def traer_usuarios():
    return jsonify(usuarios) #Este metodo de flask devuelve los objetos como json

@app.post("/usuarios") # cambiamos get por post!
def definir_usuarios():
    print(request.get_json()) #Para ver la llamada!
    usuarios[request.nombre]=request.apodo
     

@app.put("/usuarios") # cambiamos get por post!
def definir_usuarios():
    print(request.get_json()) #Para ver la llamada!
    usuarios[request.nombre]=request.apodo
      

@app.delete("/usuarios") # cambiamos get por post!
def definir_usuarios():
    print(request.get_json()) #Para ver la llamada!
    del usuarios[request.nombre]
      

if __name__ == '__main__':
    app.run(port=8001) 