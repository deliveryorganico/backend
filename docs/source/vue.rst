Vue.js 
======
| *Front-End*
| `Pagina oficial <https://vuejs.org/>`_

| Vue.js es un framework progresivo de JavaScript para crear interfaces de usuario. 
  Tiene un rendimiento y experiencia de desarrollo muy buena.
| Con un nivel medio de HTML, CSS y JavaScript ya se puede emepzar con Vue.js

| Vue te permite tomar una pagina web y dividirla en componentes reusables cada uno 
  con su propio HTML, CSS y JavaScript necesarios para generar esa parte de la 
  pagina.

| Hay varias formas de usar Vue.js, CLI, NPM o Script en HTML. 
| Nosotros elegimos llamándolo desde un <script> tag in un archivo HTML


Estructura
----------

| Los archivos .vue son interesantes, en ellos se observa una estrucutra de HTML con 
  *<tags>* propios, *<scripts>* de JavaScript y <style> de CSS. Se lo conoce como un
   componente de archivo simple (single-file component).
| Usaremos el archivo Base.vue como ejemplo:

::

	<template>
	  <div id="base">
	    <Toolbar/>
	    <Producto/>
	    <router-view/>
	    <Pie/>
	  </div>
	</template>

	<script>
	  import Pie from './Base/Pie'
	  import Toolbar from './Base/Toolbar'
	  import Producto from './Formulario/Producto'
	  export default {
	    name: 'Base',
	    components: {
	      Pie,
	      Toolbar,
	      Producto
	    }
	  }
	</script>

- En la sección <template> estamos definiendo el código HTML que queremos usar en nuestra página.
- En el código podemos ver un div con un id="app". En este div es donde vamos a ver todo el código que Vue JS va a generar.
- Cada <tag>, debajo de template, es un componente creado anteriormente. 
- En <script> se importa los diferentes componentes.
- Cuando se exporta *default* son llamados los componentes que formaran parte de 'Base'.