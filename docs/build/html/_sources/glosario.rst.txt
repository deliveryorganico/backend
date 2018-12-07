========
Glosario 
========

- **Token**: Es una firma cifrda que permite a nuestro API identificar al usuario. 
  Pero este Token no se almacena en el servidor, si no en le cliente, en nuestro 
  caso en localStorage. La API es quien se encarga de decifrar el Token.
  Los token viajan en las cabeceras de las peticiones HTTP.

_____

- **JSON**: Es un formato de texto ligero para el intercambio de datos. Se considera
  un lenguaje independiente. Sera el responsable de transportar todos los datos que
  se envian y reciban de la API al Front-End y Mobile.

_____

- **Peticiones HTTP**: *Hypertext Transefer Protocol* Son un conjunto de metodos de 
  peticion para indicar la accion que se desea realizar para un recurso determinado.

	- *GET*: Solicita una representacion de un recursos especifico. Solo debe recuperar
	  datos.

	- *POST*: Para enviar una entidad o recurso en especifico, causando a menudo un 
	  cambio de estado.

	- *DELETE*: Borra un recursos especifico.

	- *CONNECT*: Establece un tunel hacia un servidor identificado por el recurso.
