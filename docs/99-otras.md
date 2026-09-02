# Otras

Skills que no encajan en la cadena idea → código, porque resuelven otra cosa.

Viven en [`9-otras/`](../9-otras/).

---

## Aprender

### `teach`

Explicación didáctica de un concepto, una parte del código o una decisión. Para
cuando quieres entender algo, no cambiarlo.

### `muscle-memory`

Gimnasio de katas de Python. Genera ejercicios cortos a partir de tu código reciente,
lleva la cuenta del progreso y te revisa las soluciones.

```
/muscle-memory   ponme ejercicios
/muscle-memory   revisa mi solución
/muscle-memory   cómo voy
```

**Gotcha conocido:** el validador es CPython, no Pyodide. `async` y `asyncio.run`
rompen en el navegador.

---

## Conducir la conversación

### `wait-what`

**Cuándo.** El último mensaje no ha calado. Te has perdido, o la respuesta va por un
sitio que no reconoces.

**Qué hace.** Para y pide que se replantee: con contexto, en frases cortas de una
idea cada una, y usando el vocabulario del proyecto.

**Por qué existe.** Es más barato cortar en cuanto se pierde el hilo que dejar que la
conversación siga tres mensajes construyendo sobre un malentendido.

```
/wait-what
```

No lleva argumentos. Es un freno de mano.

### `to-questionnaire`

**Cuándo.** Hay una decisión que **no puedes responder tú solo**: depende de lo que
sepa un cliente, un comercial, un responsable de producto.

**Qué hace.** Convierte esa decisión en un cuestionario en Markdown, para mandárselo
a esa persona y que lo rellene por su cuenta, o para recorrerlo juntos en una reunión.

**Por qué importa.** Evita el bloqueo de "esto no lo sé", y evita también su
alternativa mala, que es decidirlo tú y descubrir en la demo que estaba mal.

```
/to-questionnaire

Necesito saber cómo factura INNOVA las OT de mantenimiento preventivo.
```

Encaja de forma natural detrás de un ticket de `wayfinder` que se queda bloqueado por
falta de información.

---

## Infraestructura

### `claude-project-setup`

Inicializa y configura un repo para Claude Code: `CLAUDE.md`, reglas, comandos,
skills y agentes. Se usa una vez por proyecto.

### `writing-for-agents`

Cómo escribir documentos que va a consumir un agente. Se usa al crear o editar una
skill, o al modificar `CLAUDE.md` o `AGENTS.md`.

Es la meta-skill: la que se usa para escribir las demás.

**Volver al índice:** [README](../README.md)
