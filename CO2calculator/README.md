
# Proyecto
## Autores

* **Ruben Cherif Narvaez** - 99rubenche@gmail.com - [rabiixx](https://github.com/rabiixx)

* **Josune Sorbet Molina** - [josune](https://github.com/josune99)

* **Xabi Jimenez Cuesta** - [sabi](https://github.com/sabitopito)


## Funcionamiento

El cálculo del consumo de CO2 se realiza mediante un "test": una serie de parámetros de entrada que el usuario debe rellenar. Nos referimos a cada conjunto de parámetros como "tablas". El resultado final del test depende tanto de los valores almacenados en las tablas como de unos parámetros denominados "constantes" (factores de conversión de las tablas a CO2). Tanto las tablas como las constantes se pueden modificar, y los resultados de los test se pueden recalcular con esos datos guardados. El único dato funcional que no se puede modificar es el factor de conversión del consumo de los vehículos, ya que se realiza mediante una API. Se pueden realizar tantos tests como se desee. 

## Diseño

* **Home** - Página principal.
* **Calculadora** - Comienza la realización de un test. Es necesario estar logeado.
* **About** -  Nuestros nombres.
* **Login** -  Iniciar sesión/Crear cuenta.  
* **Logout** - Cerrar sesión.
* **Cuenta** - Muestra un listado con todos los test y un botón para recalcular su valor. Cada test lleva al listado de las tablas que los compone. Cada tabla se puede modificar. Es necesario estar logeado.
* **Constantes** - Muestra la lista de factores de conversión usados para calcular el consumo de CO2 de cada una de las tablas. Todas se pueden modificar. Es necesario estar logeado.
