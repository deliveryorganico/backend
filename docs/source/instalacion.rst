===========
Instalacion
===========

Por el momento la unica forma de instalar este proyecto es por medio de Github.
A su vez, las partes del proyecto (Front-End, Back-End y Mobile), no se encuentran
centradas en un solo repositorio.

| *Le recomendamos el uso de Virtual Environments.*

Instalacion de Front-End
------------------------

`Repositorio de Front End <https://github.com/deliveryorganico/frontend>`_.

Clonar el repositorio::
    
    git clone https://github.com/deliveryorganico/frontend.git

Instalar npm::

    npm install

Ejecutar::
    
    npm run serve

Instalacion de Back-End
------------------------

`Repositorio de Back End <https://github.com/deliveryorganico/backend>`_.

Clonar el repositorio::
    
    git clone https://github.com/deliveryorganico/backend.git

Instalar los requerimientos::

    pip3 install -r requirements.txt

Migrar y crear el superuser::
    
    python3 manage.py migrate
	python3 manage.py createsuperuser

Ejecutar::	

	python3 manage.py runserver

Instalacion de Mobile
------------------------

`Repositorio de Mobile <https://github.com/deliveryorganico/mobile>`_.

| Mobile se encuenta en desarrollo y su por el momento la unica manera de acceder a el es a traves de las herramientas de desarrollador.

Clonar el repositorio::
    
    git clone https://github.com/deliveryorganico/mobile.git

Instalar los expo::
	
	npm install expo

Ejecutar expo::
	
	expo start
