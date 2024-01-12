# Seguridad , privacidad e identidad
Dentro de la ciber seguridad existen tres palabras muy utilizadas, que tambien solemos ver todos los dias en lo que a software respeta, y son esas tres, **Seguridad** , **Privacidad** e **Identidad**.

A su vez estas tres entan relacionadas a otros conceptos comunes. para empezar tenemos que entender que significan

### Seguridad:

La seguridad implica una contraparte **Riesgo**. ¿Que tan peligroso es lo que estas haciendo en internet? ¿Que consecuencias reales tiene? ¿Como alguien puede utilizar eso en tu contra, o a tu favor? ¿Cual es el costo y beneficio de ese acto?

Vamos a ver un ejemplo de seguridad que me parece excelente y que viene de Google Developers:

Imaginemos que tenemos una base de datos con la informaciond e nuestros clientes, en ella tenemos su direccion, su codigo postal, su numero de telefono, sus registros bancarios, su numero de documento , sus nombres, direcciones de mail, y contraseñas (encriptadas).

Llamemos a esta base de datos la base A

Ahora imaginemos otra donde solo tenemos la direccion, su numero de telefono, y mail, y sus contraseñas encriptadas.

Llamemos a esta base de datos B

*Si un ciberdelincuente accede a estas bases de datos, ¿cual es mas peligrosa?*

La respuesta es mas que obvia y nos muestra que aveces, la seguridad no viene de saber mas, sino de saber menos.

La seguridad es el costo-recompenza de nuestras acciones.

### Privacidad:

La privacidad es la capacidad de un individuo de poder mantener algo que valora de forma restringida. esta se ve en muchos campos, en la economia un bien privado es un bien que un individuo excluye de los demas para hacerlo propio, o en un ambiente laborar, la privacidad es poder tener un espacio para los empleados y o jefes donde planificar y discutir cosas sin que los otros lo sepan. o en el ambito de la delincuencia, la privacidad es poder mantener oculto algo ilegal.

La privacidad es una pregunta ¿Quienes pueden disponer de esto que valoras?

ya sea esto tus horas de descanzo, las charlas con tus amigos, una carta, o tus datos personales, la privacidad implica que un individuo puede poseer algo y que otros puedan poseerlo con su consentimiento.

Cuando entramos a una pagina web usamos nuestra contraseña, esa contraseña es nuestra y de la pagina web, y confiamos que la pagina web va a guardarla de forma segura sin mostrarsela a nadie, asi como confiamos que el mensaje que enviamos solo lo va a leer la persona a la que se lo enviamos, o que nuestros datos bancarios solo van a ser usados para un pago y nada mas por parte del cajero. 

La privacidad es el poder poseer algo, y que los demas no lo posean.

### Identidad:

La identidad es la capacidad de un individuo de ser diferenciado frente a otros similares, es quienes somos, en donde lo somos, identidad es tu corte de pelo, tus gustos musicales, tu numero de documento, y a su vez, tu identidad es las cosas que hagas, las cosas que digas, y las que no tambien.

la identidad de un individuo puede ser encontrada y accedida de diferentes formas, puede ser interpretada de diferentes formas con los mismos datos, y principalmente da un acceso a algo muy valioso, a vos mismo, a tu persona, a quien seas.

a su vez existe la contraparte de esta, el **Anonimato** seguramente habran visto la pelicula de la purga, o conozcan el concepto, es una noche donde todo el mundo sale a cometer delitos, muchas de esas personas usan mascaras, para ocultar su **Identidad**. 

El anonimato es una herramienta muy poderosa, y **Todo poder conlleva una gran responsabilidad**

```bash
# Mensaje proveniente del programa sudo de Linux
We trust you have received the usual lecture from the local System
Administrator. It usually boils down to these three things:

 #1) Respect the privacy of others.
 #2) Think before you type.
 #3) With great power comes great responsibility.

#Traduccion: Confiamos que tuviste la charla usual 
#con tu administrador de sistemas, usualmente se 
#resume en: Respeta la privacidad de otros, 
#Pensar antes de tipear, Con un gran poder,
#viene una gran responsabilidad
```

---

Entendiendo el significado de cada uno de estos conceptos, entendemos por que son tan importantes en la computacion, porque la computacion y la vida misma son una, suena muy filosofico pero en cada uno de estos ejemplos vimos casos practicos donde el mal uso o desconocimiento de estos conceptos nos lleva a consecuencias terribles, como podria ser amenazas a alguien con su informacion, Publicacion de informacion personal causando problemas en ambitos como el familiar o el laboral, o incluso, que alguien te encuentre y te mate.

Fue esto toda una charla sobre que hay que saber lo que se esta haciendo antes de emprender el camino de la ciberseguridad? es verdaderamente reelevante esto?

Si, atras de las maquinas hay personas, personas con vidas, personas con informacion, con su identidad llena de gustos de comida, musica, y demas, e incluso detras de una maquina *estas vos*

Por lo que ahora vamos a ver, por encima algunos conceptos que despues vamos a abordar en nuestro camino hacia la ciber seguridad. 

## Seguridad, Como protejerse.

El salir a internet es como salir a la calle, vas por la vereda, esperas el semaforo, existen reglas y formas de hacer las cosas, pero en la computacion, para poder cuidarnos, cuidar, e incluso atacar, tenemos que conocer la calle, la vereda, el asfalto, los postes de luz. Esto implica:
- Conocimientos en hardware, como se compone una computadora y como funciona
- Conocimientos en redes, como llega una informacion a otra computadora
- Sistemas operativos, como un monton de cables y metal pueden hacer cosas
- Administracion de datos, como se pueden almacenar, como se evita que cualquiera los acceda.
- Proteccion de sistemas, como blindarce ante posibles atacante que te quieran "atropellar"

Esta rama implica desde entender la PC, hasta saber de sistemas de proteccion electrica, de datos, y demas.
Un ejemplo simple son los sitemas linux y sus administradores de usuarios, donde no cualquiera puede hacer cualquier cosa, y al administrar o auditar una red, saber quien puede hacer que y como es la diferencia entre no poder hacer nada y poder hacer todo. y saber las debilidades de un sistema te abre la puerta a poder acceder dentro de el. mientras mas conozcas a tu enemigo, menos seguro está.
## Privacidad, Datos para todos.
Vivimos en una era donde la informacion es poder, dinero, y mucho mas, por lo que dentro de la seguridad tenemos el recavamiento de informacion y a su vez la manipulacion de la misma, si un admin de una paginaweb puede  acceder a las contraseñas, como esos datos son privados? que metodos existen? Esta rama contempla:
- Proteccion de datos, que nadie pueda acceder a ellos
- Ofuscacion, hacer los datos dificiles de encontrar.
- Acceso de datos, que alguien con mi permiso pueda recibirlos.
- Confianza de servicios, Es la persona a la que le doy mis daots confiable?


Un ejemplo de esta rama es el encriptado, seguramente oyeron hablar sobre la criptografia, pero que es? por que es tan segura? un ejemplo claro son las claves asimetricas, donde se utiliza matematicas para poder ocultar informacion y que solo quien tenga su clave privada para desbloquear esa informacion, pueda accederla, mientras confies en el receptor, la informacion entre los dos nadie mas la puede tener.

## Identidad, quien soy?

En la Ciberseguridad la identidad es, probablemente, la mas importante de todas estas ramas, ya antes hicimos el ejemplo de la calle, tanto si caminamos por el asfalto como por la vereda, alguien nos puede atropellar, ¿Quien?.
- Entrender las formas de indetificar individuos
- Recoleccion de caracteristicas de identidades digitales
- Herramientas de extraccion de informacion personal
- Herramientas de ocultacion y anonimicidad.

Esta es la parte mas poderosa y riesgosa de este campo, porque , en especial cuando trabajamos en ocultarnos, un individuo anonimo puede hacer lo que sea sin consecuencias, si no tuvieras consecuencias ¿Que harias? Yo en mi caso, elijo enseñarte ciberseguridad, por lo que implica una enorme responsabilidad el que hacemos con este poder, y como lo empleamos. porque ahi atras esta gente que puede ser mas mala que uno, o como decian nuestros abuelos "No te hagas el guapo porque siempre hay uno mas guapo".

Dentro de la informatica existe una red muy famosa, Tor, que te permite "acceder a una internet profunda". donde es mas dificil rastrearse, aunque no imposible, y donde las consecuencias de tus actos se mitigan.

Podes usarla para que personas accedan a informacion censurada, como para hacer daño al mundo, quien seas implica mucho.

----
Esta fue una introduccion a los conceptos mas reelevantes de la ciberseguridad, y es necesario entenderlos para poder saber a donde vamos, que queremos y que vamos a hacer con esta informacion. porque

# Un gran poder conlleva una gran responsabilidad