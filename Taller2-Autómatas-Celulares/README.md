
<div align="center">

<h1>Taller 1 - Panorama de la IA</h1>

<h2>Profesores: <br>Jose Jesus Fernando Martinez Paez <br> Flavio Augusto Prieto Ortiz <br> Gustavo Perez Hoyos </h2>

<h4>Integrantes del equipo: <br>
    Paula Nicole Quiroga Romero <br>
    Jesus David Sanchez Cobos <br>
    David Steven Pinzón Hernández</h4>
 
---
<div align="left">


## 1. Observe sus comportamientos en la casa, en la universidad y en el medio de transporte que utiliza. Encuentre, para cada uno de estos escenarios sus reglas básicas.  

Reglas:

Casa:
1.	Saludar al llegar a la casa.
2.	Mantener su espacio de trabajo limpio
3.	Despedirse al irse de un grupo.
4.	Cerrar con llave
5.	Golpear antes de entrar en una habitación.
6.	No interrumpir cuando alguien duerme.
7.	No interrumpir cuando alguien está ocupado.
8.	Apagar las luces cuando se sale de un espacio.
9.	No tocar las cosas de otra persona sin autorización.
10.	No comer sobre la cama.
11.	No usar el teléfono mientras que se come.

Universidad:
1.	Saludar al llegar a una reunión
2.	Esperar el turno para hablar en un grupo.
3.	Escuchar al interlocutor.
4.	Ayudar con respeto.
5.	Respetar el ritmo de aprendizaje de cada compañero
6.	Cumplir con las entregas en un trabajo grupal.
7.	Colocar la basura en su lugar.
8.	Ser puntual.
9.	Notificar contratiempos en los objetivos de un equipo. 
10.	No comer en clase.

Medio de transporte:
1.	Dejar salir antes de entrar.
2.	No hacer ruidos incomodos.
3.	No dejar basura.
4.	Ayudar a subir a personas que lo necesitan.
5.	No conducir en estado de ebriedad.
6.	No rayar el medio de transporte.
7.	Ceder el puesto a alguien que necesite.
8.	No obstruir el paso.
9.	No empujar al ingresar al transporte.
10.	Evitar conductas violentas.


## 2. Suponga una enfermedad, o un incendio forestal, o una moda, desarrolle un modelo de difusión usando ACs probabilísticos. O simule un robot con dos ruedas que evite obstáculos.  


### Definición del Espacio y Estados del Sistema

Retículo: Matriz bidimensional de L × L celdas (por ejemplo, 100 × 100 = 10.000 celdas) con condiciones de frontera absorbentes (el fuego se apaga al llegar al límite del bosque).

Vecindad de Moore extendida o estándar: Se utiliza la vecindad de Moore (8 vecinas), ya que las brasas pueden propagarse de forma diagonal debido a las corrientes de aire.

Espacio de Estados ω: Cada celda en el instante t puede estar en uno de los siguientes cuatro estados:
- V (Vegetación/Verde): Celda con material combustible vivo.
- F (Fuego/Incendiada): Celda activa en combustión.
- C (Cenizas/Quemada): Celda sin combustible libre, ya no se puede volver a quemar.
- N (No combustible): Celdas vacías, cuerpos de agua o rocas que actúan como barreras cortafuegos.

### Variables de Control Probabilístico (Parámetros$)
Para que el AC sea realista, la probabilidad de que el fuego salte de una celda incendiada (F) a una verde (V) depende de tres factores:
- $P_{base}$: Probabilidad intrínseca de ignición del tipo de madera/vegetación.
- $P_{viento}$: Factor que aumenta la probabilidad en la dirección hacia donde sopla el viento y la disminuye en la dirección opuesta.
- $P_{humedad}$: Factor inverso; a mayor humedad, menor probabilidad de propagación.
La probabilidad total de contagio de una celda verde está dada por:
- $P_{inf}=f(P_{base},P_{viento},P_{humedad})\times n_{fuego}$

Donde $n_{fuego}$ es el número de vecinas en estado F, ponderadas por la dirección del viento.

### Reglas de Transición Probabilísticas
En cada paso de tiempo $t → t+1$, todas las celdas se evalúan simultáneamente bajo las siguientes reglas probabilísticas y temporales:
- Regla 1: Ignición de Vegetación (V → F)
Si una celda está en estado V y tiene al menos una vecina en estado F, se calcula su probabilidad total de contagio $P_{inf}$. Se genera un número aleatorio $R₁ ~ U(0,1)$:
o	Si $R_1 \le P_{inf}$, la celda se enciende y pasa a ser F en el ciclo t+1.
o	Si $R_1 > P_{inf}$, la celda resiste y permanece como V.

- Regla 2: Combustión Temporal $(F → C)$
El fuego consume el combustible de la celda de forma finita. Una celda en estado F permanece quemándose durante un tiempo determinado τ. Al cumplirse ese tiempo, pasa automáticamente a ser ceniza C.

- Regla 3: Inercia de Estados (C y N)
Las celdas en estado C (cenizas) y N (terreno estéril) son estados estables individuales. Tienen probabilidad de cambio P = 0. No vuelven a quemarse ni a regenerarse en la escala de tiempo del incendio.


## Bibliografía

[1] NVIDIA, “NVIDIA Cosmos: Desarrolle IA física más rápido,” NVIDIA, 2026. [En línea]. Disponible en: https://www.nvidia.com/es-la/ai/cosmos/#nv-accordion-7cc04d1c56-item-cd401cdab4. [Accedido: 07-sep-2026].

[2] NVIDIA, “What is Mixture-of-Transformers (MoT)? Definition & Architecture,” NVIDIA Glossary, 2026. [En línea]. Disponible en: https://www.nvidia.com/en-us/glossary/mixture-of-transformers/?ncid=no-ncid. [Accedido: 07-sep-2026].

[3] Ministerio de Tecnologías de la Información y las Comunicaciones, “Colombia activa modelo de gobernanza de IA y avanza en soberanía tecnológica,” MinTIC: Sala de Prensa, 22-may-2026. [En línea]. Disponible en: https://www.mintic.gov.co/portal/inicio/Sala-de-prensa/Noticias/438177:Colombia-activa-modelo-de-gobernanza-de-IA-y-avanza-en-soberania-tecnologica. [Accedido: 07-sep-2026].

[4] Ministerio de Tecnologías de la Información y las Comunicaciones, “Construcción del Plan TIC Colombia 2026 – 2030,” Plan TIC Colombia, 2026. [En línea]. Disponible en: https://mintic.gov.co/plan-tic-colombia/919/w3-propertyvalue-1044920.html. [Accedido: 07-sep-2026].