# PARCIAL

## Parte Conceptual

## Latch vs. Flip-Flop
1. Latch: Es un dispositivo asíncrono y sensible al nivel. Esto significa que su salida cambia en cualquier momento en que la entrada de habilitación esté activa.
2. Flip-Flop: Es un dispositivo síncrono y sensible al costado de una señal de reloj. Solo cambia su estado en el instante preciso del pulso.

## Tipos y Características:

1. SR: El más básico; permite establecer o restablecer el estado. Tiene una condición prohibida cuando ambas entradas son 1.
2. D: Evita la condición prohibida del SR; la salida simplemente sigue a la entrada D cuando hay pulso de reloj.
3. JK: Es una versión mejorada del SR que permite el modo Toggle cuando ambas entradas son 1.
4. T: Cambia el estado de la salida en cada pulso de reloj si la entrada T está en 1.

   <img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/9917c60f-1cd1-4eee-836e-f73e5c20faf7" />




## Multiplexor vs. Demultiplexor
1. Multiplexor: Actúa como un selector. Tiene muchas entradas y una sola salida. Selecciona una de las entradas de datos para enviarla a la salida basándose en líneas de selección.


MUX 8 a 1: Tiene 8 entradas de datos ($D_0$ a $D_7$) y 3 líneas de selección ($2^3 = 8$). Según el valor binario en las líneas de selección, una de las 8 entradas se refleja en la salida única.
   
3. Demultiplexor: Hace lo opuesto. Tiene una entrada y muchas salidas. Dirige el dato de la entrada única hacia una de las múltiples salidas.

   
DEMUX 1 a 8: Tiene una entrada de datos, 3 líneas de selección y 8 salidas ($S_0$ a $S_7$). El dato de entrada aparecerá únicamente en la salida seleccionada por el código binario.

<img width="600" height="400" alt="image" src="https://github.com/user-attachments/assets/b2a9c3c6-c314-42c2-8f1d-130321cc33e4" />



## Sumadores y Circuitos Secuenciales
1. Semisumador: Suma dos bits individuales y produce un resultado y un acarreo. No tiene entrada para un acarreo previo.
2. Sumador Completo: Suma tres bits (dos bits de entrada y el acarreo de una etapa anterior). Es esencial para sumar números de varios bits en cascada.
3. Circuitos Secuenciales: Son aquellos cuya salida no solo depende de las entradas actuales, sino también de la historia pasada. Tienen memoria, a diferencia de los combinacionales. Ejemplos: contadores y registros.

## Mapas de Karnaugh
1. ¿Qué es? Es una herramienta gráfica que representa la tabla de verdad de una función lógica.
2. ¿Para qué sirve? Se utiliza para simplificar funciones booleanas de manera visual y eficiente. Permite reducir el número de compuertas lógicas necesarias en un diseño, minimizando expresiones complejas sin tener que usar álgebra booleana abstracta extensivamente. Es ideal para funciones de 2 a 5 variables.
3. 

## Parte de diseño 
<img width="280" height="42" alt="image" src="https://github.com/user-attachments/assets/176be7ad-dbf4-40e1-915a-74442f634919" />

## Circuito
<img width="700" height="300" alt="image" src="https://github.com/user-attachments/assets/a48feb79-73cc-44ed-8f39-43aba8cc3ba8" />

## Tabla de verdad 
<img width="700" height="200" alt="image" src="https://github.com/user-attachments/assets/181ce8b0-7bf1-4a56-bdc1-389ee9eeb1b1" />


<img width="280" height="42" alt="image" src="https://github.com/user-attachments/assets/4f304613-c7bb-47eb-a272-db2b6945d82d" />

## Circuito
<img width="700" height="300" alt="image" src="https://github.com/user-attachments/assets/5149aafe-d119-4d69-bf85-6fc2d7c65ae4" />

## Tabla de Verdad
<img width="372" height="407" alt="image" src="https://github.com/user-attachments/assets/21397570-3682-4e06-8ac3-079f04ff63d2" />


## CHATBOT

Se agrega como archivo https://github.com/NicolQuintero777/Parcial-/blob/main/ChatBot.py

