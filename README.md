
## Parte Conceptual

## Latch vs. Flip-Flop
1. Latch: Es un dispositivo asíncrono y sensible al nivel. Esto significa que su salida cambia en cualquier momento en que la entrada de habilitación (Enable) esté activa.
2. Flip-Flop: Es un dispositivo síncrono y sensible al flanco (de subida o bajada) de una señal de reloj (Clock). Solo cambia su estado en el instante preciso del pulso.

## Tipos y Características:

1. SR (Set-Reset): El más básico; permite establecer (1) o restablecer (0) el estado. Tiene una condición "prohibida" cuando ambas entradas son 1.
2. D (Data): Evita la condición prohibida del SR; la salida simplemente sigue a la entrada D cuando hay pulso de reloj.
3. JK: Es una versión mejorada del SR que permite el modo "Toggle" (conmutación) cuando ambas entradas son 1.
4. T (Toggle): Cambia el estado de la salida en cada pulso de reloj si la entrada T está en 1.

## Multiplexor vs. Demultiplexor
1. Multiplexor: Actúa como un selector. Tiene muchas entradas y una sola salida. Selecciona una de las entradas de datos para enviarla a la salida basándose en líneas de selección.
   MUX 8 a 1: Tiene 8 entradas de datos ($D_0$ a $D_7$) y 3 líneas de selección ($2^3 = 8$). Según el valor binario en las líneas de selección, una de las 8 entradas se refleja en la salida única.
   
3. Demultiplexor (DEMUX): Hace lo opuesto. Tiene una entrada y muchas salidas. Dirige el dato de la entrada única hacia una de las múltiples salidas.
   DEMUX 1 a 8: Tiene una entrada de datos, 3 líneas de selección y 8 salidas ($S_0$ a $S_7$). El dato de entrada aparecerá únicamente en la salida seleccionada por el código binario.

## Sumadores y Circuitos Secuenciales
1. Semisumador (Half Adder): Suma dos bits individuales y produce un resultado (Suma) y un acarreo (Carry). No tiene entrada para un acarreo previo.
2. Sumador Completo (Full Adder): Suma tres bits (dos bits de entrada y el acarreo de una etapa anterior). Es esencial para sumar números de varios bits en cascada.
3. Circuitos Secuenciales: Son aquellos cuya salida no solo depende de las entradas actuales, sino también de la historia pasada (estados anteriores). Tienen memoria, a diferencia de los combinacionales. Ejemplos: contadores y registros.

## Mapas de Karnaugh
1. ¿Qué es? Es una herramienta gráfica que representa la tabla de verdad de una función lógica.
2. ¿Para qué sirve? Se utiliza para simplificar funciones booleanas de manera visual y eficiente. Permite reducir el número de compuertas lógicas necesarias en un diseño, minimizando expresiones complejas sin tener que usar álgebra booleana abstracta extensivamente. Es ideal para funciones de 2 a 5 variables.

