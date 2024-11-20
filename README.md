# Team Challenge: Hundir la flota


### ¡Bienvenido a Hundir la flota!
El team Yamato ha creado un codigo para jugar al juego de hundir la flota.


  - [**Descripción**](#descripción)
    - [Instalaciones](#instalaciones)
    - [Reglas del juego](#reglas-del-juego)
  - [**Tableros**](#comentarios-y-aclaraciones)
    - [Cada jugador tendrá dos tableros](#Cada-jugador-tendrá-dos-tableros)
  - [**Flujo del Juego**](#flujo-del-juego)
  - [**Comentarios y Aclaraciones**](#comentarios-y-aclaraciones)


## Descripción

El objetivo del juego es hundir la flota, es decir, todos los barcos del otro jugador.

#### Instalaciones
- Python
- Librería de Numpy

#### Reglas del juego

1. Hay dos jugadores: tú y la máquina
2. Un tablero de 10 x 10 posiciones donde irán los barcos
3. Las posiciones de los barcos y su tamaño: los barcos se colocan de manera aleatoria

    * 4 barcos de 1 posición de eslora
    * 3 barcos de 2 posiciones de eslora
    * 2 barcos de 3 posiciones de eslora
    * 1 barco de 4 posiciones de eslora

4. Tanto tú, como la máquina tenéis un tablero con barcos, y se trata de ir "disparando" y hundiendo los del adversario hasta que un jugador se queda sin barcos, y por tanto, pierde.

5. Funciona por turnos y empiezas tú.

## Tableros

El tablero de 10 x 10 posiciones donde irán los barcos

## Flujo del Juego

**Inicialización:**
Se crean dos tableros: uno para el jugador y otro para la máquina.
Los barcos se colocan en posiciones válidas de forma aleatoria.

Puedes elegir el nivel de dificultad del juego:
- Facil (1) - Un disparo
- Normal (2) - dos disparos
- Dificil (3) - tres disparos

**Turnos:**

Jugador:
- Introduce las coordenadas de disparo.
- El programa valida si el disparo impacta o falla.
- Si impacta, el jugador vuelve a disparar. Si falla, es turno de la máquina.
- Cuando es el turno del jugador, puede elegir salir del juego y se mostrará el tablero como queda.

Máquina:
- Genera un disparo aleatorio y verifica su efecto.
- Similar al jugador, repite si impacta y cede el turno si falla.
  
**Visualización:**
Se actualizan y muestran los tableros después de cada turno:
 - El jugador ve su tablero con los disparos recibidos y el tablero visible del oponente.

**Fin del juego:**
Cuando un jugador pierde todos sus barcos, el programa anuncia el ganador.

#### Cada jugador tendrá dos tableros
1. Un tablero donde se ven los barcos colocados
2. Otro trablero en blanco, que sería el del oponente, que se irán visualizando los disparos, si se ha acertado o no.


## Comentarios y Aclaraciones
Para la ejecución de este programa está guardado el código en varios scripts:

1. main.py
2. funciones.py
3. variables.py
4. tablero.py

## Equipo
- [antoniiio2000](https://github.com/antoniiio2000)
- [cmonzon-94](https://github.com/cmonzon-94)
- [FuaElKiks](https://github.com/FuaElkiks)
- [patrigal2](https://github.com/patrigal2)
- [AlbrtttoTorres](https://github.com/AlbertttoTorres)
