======================
Django Rest - Back-End
======================
| `Pagina oficial <https://www.django-rest-framework.org/>`_

| Django REST es un framework podersos y flexible con herramientas para la creacion
  APIs web.
| Su funcion es de modelo de comunicación entre el frontend y el backend.

| *Lo importante es que el cliente no recibe HTML para renderizar, sino simplemente 
  los datos que se han generado como respuesta. Es decir, el servidor no escribe 
  HTML, sino únicamente genera los datos para enviarlos al cliente.*

¿Que es REST?
-------------
| REST deriva de "REpresentational State Transfer" (transferencia de representación 
  de estado). Un servicio REST no tiene estado, el servicio pierde todos sus datos 
  entre llamadas. Esto es, que no se puede llamar a un servicio REST y pasarle unos 
  datos (p. ej. un usuario y una contraseña) y esperar que “nos recuerde” en la 
  siguiente petición. 

| De ahí el nombre: el estado lo mantiene el cliente y por lo tanto es el cliente 
  quien debe pasar el estado en cada llamada. Si quiero que un servicio REST me 
  recuerde, debo pasarle quien soy en cada llamada.

¿Porque lo utilizamos?
----------------------
| **Separación cliente/servidor e Independecia de tecnologias**
| Estos se comunican con un lenguaje de intercambio (JSON,XML,...) y podemos hacer 
  varios Front-End (Web, Mobile, etc) con un único Back-End. Todo reciben los
  datos de la misma manera y cada uno decide que hacer con ellos.

Estructura basica
-----------------

| DRF se basa fundamentalmente en 3 componentes: los serializadores, las vistas y 
  los routers.

- | **Los serializadores:** Asociado a los modelos. Nos permiten definir al detalle 
    cómo serán las respuestas que devolverá nuestro API y cómo procesaremos el 
    contenido de las peticiones que nos lleguen.

- | **Los routers:** son una herramienta que nos permiten definir las urls de nuestro
    API de una manera sencilla y ordenada. Nos permiten definir qué método 
    (GET, POST, PUT,...) se ejecutará al llegar una petición HTTP contra un path 
    concreto.
    
- | **Las views:** Extensiones de las class-view de django. Sirva para simplificarnos 
    la union de los routers, los serializadores y los modelos. Como respuesta 
    devuelve json, xml, etc. 

