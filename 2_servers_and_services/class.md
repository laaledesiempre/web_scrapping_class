# Internet
## Introduccion y conceptos basicos
**Internet** es un conjunto de redes informaticas alrededor del mundo que se utilizan para permitir la conectividad entre dos usuarios de la misma. no vamos a profundizar en su naturaleza tecnica a mayor detalle, eso se vera posteriormente en nuestro estudio de administracion de sistemas Linux.

![](https://vahid.blog/post/2020-12-15-how-the-internet-works-part-i-infrastructure/featured.jpg)

> Grafico disponible en https://vahid.blog/post/2020-12-15-how-the-internet-works-part-i-infrastructure/featured.jpg

Este grafico es algo complejo por lo que vamos a tratar de simplificarlo lo mas que se pueda, nosotros estamos abajo a la izquierda en el cuadrado amarillo, somos CLIENTES. es decir, somos quienen consumen servicios, el internet esta lleno de servicios, buscadores, redes sociales, sitios de compra, de distribucion multimedia. todos esos son servicios asi como un restaurante o una empresa de gas. nosotros por medio de un switch (que vamos a analizar mas a fondo en la parte de sistemas) nos conectamos con un modem.
> *Muchas veces estan los dos dentro de un mismo dispositivo! a eso le llamamos "Home Router"*

Ese modem se conecta a nuestro Internet Service Provider, nuestro proovedor de internet, que a su vez puede tener servicios o, puede requerirlo de otros proovedores de internet, por hacer un ejemplo, puede ser que la apgina que estemos usando este DENTRO de la red de , por ejemplo, TeleComunicaciones S.A (nuestro ficticio proovedor de internet) o dentro de SistemasInformaticos S.R.L (su competencia), y aun asi podriamos acceder.

En ese momento donde tenemos que acceder cosas fuera de nuestra red, es donde entramos a la interconeccion de redes, o la **internet**. Por lo que:
- Internet es un servicio con multiples proovedores
- Permite la interconeccion de esos proovedores
- Funciona a base de una red de routers

Pero bueno, como es que llega, por ejemplo, este archivo desde mi computadora hasta la de la persona que lee esto? bien, vamos a hacer un analisis corto.

Mi computadora, desde un cliente de internet, un buscador, envia a catgirl.cloud (quien hostea esta pagina!) esto que yo estoy escribiendo, y a su vez, vos al conectarte a ese servidor, se envia desde tu router hasta otro router, hasta otro router. y asi, hasta llegar al router de catgirl.cloud. ¿Como sabe encontrar a catgirl.cloud entre tantos routers? eso funciona con un sistema que se llama DNS. pero eso va a ser para cuando veamos administracion de sistemas. no es urgente ahora.

## Servidores

Como dijimos internet es un conjunto de servicios, como lo es un restaurante, entonces, como es que llega nuestra peticion? bien, tenemos la parte del camino, nuestro router junto a los miles de routers de por ahi llevan mi paquete de datos hasta el router destino, pero, como hace el router destino para saber que hacer con ese paquete? no vamos a ir en detalles a todo lo que implica recibir y decodificar un paquete en una computadora, sino a la parte mas abstracta.

**Un servidor** es una **computadora** (Como la que estas usando ahora). que tiene la particularidad de poder **servir** contenido. es asi de simple, nada mas, tu propia computadora puede ser facilmente un servidor, un *HOST* de un servicio. por ejemplo, una *nube* como catgirl.cloud no es mas que una computadora en un servidor con muchas computadoras que le pertenece/es alquilada por Sophie (https://mastodon.catgirl.cloud/@sophie). una computadora cualquiera, tambien podria ser un celular mismo quien ejecute servicios (eso lo vamos a ver tambien en la parte de sistemas).

Ahora, como una computadora se convierte en un servidor si tecnicamente cualquiera puede serlo? muy facil, cuando esa computadora aparte de hablar, escucha.

Por donde escucha? como? eso funciona con un sistema de puertos, que vamos a ver mas en profundidad en la parte de sistemas, pero ahora te conviene saber que:
- Un puerto es una parte virtual de una computadora
- existen multiples puertos
- un puerto no puede ser tomado por varios programas a la vez.

Por ejemplo, por defecto, las llamadas http se reciben en el puerto 80, cuando veamos herramientas como nginx vas a ver que usan por defecto este puerto. 
En la parte ya de hacking esto de los puertos va a ser muy importante, ya que cuando quieras penetrar en una maquina, sus puertos abiertos y que servicio estan alojando puede ser algo sumamente util ( 3   :) )

Ahora, sabemos que por los puertos pueden llegar datos, pero, quien administra esos datos? quien los interpreta? ese el el trabajo del servicio. vamos a hacer un ejemplo teorico para ejemplificarlo:

> Un servicio http escucha en el puerto 80, cada vez que llega una llamada a ese puerto la analiza y si busca la direccion "/" le devuelve el mensaje "Hola". 

Bien, ya esta bastante clara la parte teorica, ahora, vamos a hacer un servidor http.

## Creando nuestro servidor con flask

> ADVERTENCIA: Este servidor es solo de prueba, Flask debe pasar por un proceso de compilacion para llegar a produccion, es decir, para ser util en el ambito laborar, este servidor que creamos solo sirve para testeo, la proxima lo vamos a hacer con un servicio verdaderamente aplicable. por ahora alcanza con esto para entender.

Para empezar con flask, hay que instalarlo, puede ser que ya lo tengas como que no, para instalarlo usa:

````bash
pip install flask
````

Despues de eso vamos a empezar a hacer nuestro script:

> *main\.py*
````python
from flask import Flask # Requerimos flask

app = Flask(__name__) # Esto es una direccion que usa flask para ubicar el directorio
# Por defecto app.route utiliza el metodo GET
@app.route("/") # Esto de aca es un decorador de python, puede ser que lo veamos despues
def hello_world():
    return "<p>Hola!</p>" #Esto es html!

if __name__ == '__main__':#Esto es una convencion de python
    app.run(port=8001) # Esta funcion ejecuta el servidor en el puerto 8001!
````

Okey, mucho que desempaquetar, aca creamos un archivo y lo comenzamos requiriendo flask, despues declaramos la variable app, que va a contener nuestro server, y va a contener el constructor Flask, que crea un instancia del servidor, recibiendo como arguneto ```__name__``` que es una variable general de python que indica el archivo que esta ejecutando la funcion, despues usamos un decorador para indicarle a la aplicacion que la siguiente funcion va a ser una ruta de app.

> Los decoradores de python son funciones que reciben una funcion y la transforman en otra, internamente flask modifica nuestra funcion para que su retorno sea devuelto como texto por el puerto que le indiquemos!

en este caso le indicamos que la ruta a la que debe responder es "/", que es la ruta por defecto de una aplicacion.

### Como acceder a la pagina: 

Desde nuestro navegador podemos buscar: ```http://localhost:8001``` y nos va a llevar a la ruta "/" de esa pagina con el metodo get, pero, y si queremos utilizar otro metodo? ahora en un toque vamos a hacer una pagina que nos permite hacer llamados http con otros metodos, pero, Flask nos permite hacer servidores con diferentes metodos de la siguiente forma (existen varias pero esta es la ma facil)

````python
from flask import Flask, request

app = Flask(__name__) 

@app.get("/") # cambiamos route por get!
def hello_world():
    print(request) #Para ver la llamada!
    return "<p>Hola!</p>" #Esto es html!

@app.post("/") # cambiamos route por post!
def post_root():
    print(request) #Para ver la llamada!
    return  #Aun no hace nada!

if __name__ == '__main__':
    app.run(port=8001) 
````
 De paso le agregamos un print para ver la llamada que nos devuelve al nosotros acceder a el. 

---

## Como se comunican entre ellos los servidores?

Bien, ya sabemos hacer un servidor http simple, ahora, como se conectan los servidores entre ellos? como recibo yo, al entrar a facebook, una pagina, con una lista de post, o en twitter una pagina con tweets? En los servidores se encuentran varios *Endpoints* para estas tareas, podriamos tener un endpoint que se llame ```/users``` que cuando se le hace una llamada ```GET``` nos devuelva una lista de usuarios, o que, cuando le mandemos una llamada ```POST``` nos guarde en una base de datos el nuevo usuario que le enviamos, o que un ```PUT``` nos modifique un usuario con los datos que le decimos. pero, estas listas o datos, como llegan a nuestros servidores? existen muchisimos protocolos para esto, y aprender los mas basicos podria tomarnos varias clases, pero hay uno que es el standar por defecto, la gran mayoria de estas comunicaciones se hace por el protocolo REST, que es el que usa archivos JSON para comunicarse.
```json
    {
        "ejemplo":"json",
    }
```
Este sistema funciona con un par clave valor, exactamente igual a los diccionarios de Python. la diferencia a javascript es que las claves SIEMPRE son strings, ya que lo que enviamos en un rest, es una pieza de texto. 
```json
    {
        "nombre":"Matilda",
        "caballos":[
            "Pedro",
            "Jose",
            "Martin"
        ],
        "cancionesFavoritas":[
            {
                "nombre": "Psycho",
                "artista": "Red Velvet"
            },
            {
                "nombre": "Los Dinosaurios",
                "artista": "Charly Garcia"
            }
        ]
    }
```
Ahora, como se llama una programa o funcion que permite conectar dos computadoras o procesos? es lo que conocemos como API.

---
### Api

Vamos a ver algunos ejemplos de APIs para entender bien como funciona el concepto.

1. Tenemos una PC corriendo un servidor de un juego, a este se conectan varios clientes, para mandar la informacion del juego a los demas clientes, existe una API que permite acceder a todos esos datos.
2. Tenemos un videojuego que esta siendo desarrollado para una consola, el motor de videojuegos cuenta con una API que permite controlar espectos de la consola como la pantalla, el volumen, los controles, ya que todo eso funciona dentro de la consola, no en el programa en si. 
3. Tenemos un servidor que da una pagina web, esa pagina necesita acceder a una lista de tareas guardadas en una base de datos, en el servidor, existe un endpoint que recibe una peticion de notas, y las envia por medio de una API REST.

Podriamos entonces decir que una API es cualquier programa o proceso que permite conectar a dos procesos independientes por medio de un acuerdo en como se envian y reciben los datos, este "acuerdo de como se hacen las cosas", es lo que conocemos como protocolo. un conjunto de reglas para una tarea.