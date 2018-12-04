React Native - Mobile
=====================

| `Pagina oficial <https://facebook.github.io/react-native/>`_

| React Native es un framework desarrollado por Facebook que permite construir 
  aplicaciones móviles usando JavaScript. React Native permite que JavaScript 
  se ejecute e interactúe con los sistemas iOS y Android de la misma manera que
  lo hace el código nativo.

| La gran diferencia entre React Native y las WebApps, HTML5 App o aplicaciones 
  hibridas es su rendimiento. Todas están escritas en JavaScript, al igual que 
  React Native, pero no renderizan usando componentes nativos.

| *Crear aplicaciones nativas, nunca fue tan facil.*

JSX
---
| Una sintaxis para incrustar XML dentro de JavaScript. JSX te permite escribir tu 
  lenguaje de marcado dentro del código. Se ve como HTML en la web, excepto que en 
  lugar de cosas de la web como <div> o <span>, usas los componentes React.

| XML sirve para crear lenguaje propio en <tags> y con esto, JSX puede producir 
  componentes de React.

Ejemplo:

::
	
	<View>
		<Text>Hello world!</Text>
	</View>

Components
----------
| Los componentes son los bloques de construcción de cualquier interfaz de usuario. 
  React Native administra que de componentes, de JavaScript, a la Interfaz de 
  Usuario nativa. 

| La UI completa de la aplicacion se especifica mediante la declaracion de los 
  componentes y en que orden se van a representar.
| Los componentes están anidados dentro de otros componentes, formando una 
  estructura en forma de 'arbol'.
  
El componente de nivel superior se conoce como el **componente raíz**. 
Los componentes anidados se denominan **componentes hijos**.

Props
~~~~~
| Muchos componenetes pueden ser customizados cuando son creados con diferentes
  parametros. Los **props** son estos parametros de creacion. Y estan sujetos
  al tiempo de vida del componente.

| Se le pueden pasar las propiedades al ``contructor``. 
| Un elemento padre puede alterar los accesorios de un elemento hijo en cualquier 
  momento.

Ejemplo:

::

	export default class Bananas extends Component {
	  render() {
	    let pic = {
	      uri: 'https://banana.com/galeria/Banana.jpg'
	    };
	    return (
	      <Image source={pic} style={{width: 193, height: 110}}/>
	    );
	  }
	}

| Aca el componente de React Native, ``<Image>`` tiene una prop llamada 
  ``source={}`` que controla que imagen se va a mostrar en ese componente.

| Se pueden crear ``props`` para componentes propios. Permitiendonos usar los 
  componentes ya creados en diferentes lugares de la app, con pocas diferencias
  en cada lugar. 

States
~~~~~~
| Los ``states`` controlan, al igual que los ``props``, los componentes. Los
  states, son para datos que van a cambiar. Cuando se modifica, se 
  re-renderiza solo.

| En general se inicia en el constructor y se llama a ``setState`` para 
  cambiarlo.

::

  constructor(props) {
    super(props);
    this.state = { isShowingText: true };

