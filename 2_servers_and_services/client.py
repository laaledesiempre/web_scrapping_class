import requests

usuarios=requests.get("http://localhost:8001/usuarios")
print(usuarios.text) # tambien podriamos verlo como json con .json

manolin={
    "nombre":"Manolito",
    "apodo":"Manolin"
}
agregando_usuario=requests.post("http://localhost:8001/usuarios",json=manolin)

print("Usuarios luego de agregar a manolin")
print(requests.get("http://localhost:8001/usuarios").text)

manolin["apodo"]="Manolino"
modificando_usuario=requests.put("http://localhost:8001/usuarios",json=manolin)

print("Usuarios luego de modificar a manolin")
print(requests.get("http://localhost:8001/usuarios").text)

borrando_usuario=requests.delete("http://localhost:8001/usuarios",json={"nombre":"Manolito"})

print("Usuarios luego de borrar a manolin")
print(requests.get("http://localhost:8001/usuarios").text)
