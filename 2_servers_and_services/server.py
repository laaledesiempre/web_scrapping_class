from flask import Flask, request, jsonify

app = Flask(__name__) 

usuarios= {} # nuestros usuarios!, la estructura va a ser ['nombre']":['apodo']"

@app.get("/usuarios")
def traer_usuarios():
    return jsonify(usuarios) #Este metodo de flask devuelve los objetos como json

@app.post("/usuarios") # cambiamos get por post!
def definir_usuarios():
    print(request.get_json()) #Para ver la llamada!
    request_json=request.get_json()
    usuarios[request_json['nombre']]=request_json["apodo"]
    print(usuarios)
    return "hii"
     
@app.put("/usuarios") # cambiamos get por post!
def cambiar_usuarios():
    print(request.get_json()) #Para ver la llamada!
    request_json=request.get_json()
    usuarios[request_json['nombre']]=request_json["apodo"]
    return "Usuario cambiado"
      

@app.delete("/usuarios") # cambiamos get por post!
def borrar_usuarios():
    print(request.get_json()) #Para ver la llamada!
    request_json=request.get_json()
    del usuarios[request_json['nombre']]
    return "usuario borrado"
      
if __name__ == '__main__':
    app.run(port=8001) 

