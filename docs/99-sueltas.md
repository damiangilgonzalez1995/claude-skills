# Fuera del flujo

Skills que no encajan en la cadena idea → código, porque resuelven otra cosa.

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

## Utilidades de diseño

### `vocabulario-animacion`

Le describes un efecto sin saber cómo se llama ("eso que rebota al abrirse un
popover", "el scroll elástico de iOS") y te da el término exacto, en inglés, que es
el vocabulario con el que se le pide a una IA o a un diseñador.

No diseña ni construye: nombra.

### `video-a-superprompt`

Le pasas la grabación de una web que te gusta y te devuelve un prompt de recreación
detallado: anatomía sección a sección, sistema de movimiento, mapa de assets,
comportamiento en móvil y con movimiento reducido.

**Necesita `ffmpeg`** en el PATH: `winget install Gyan.FFmpeg`.

---

## Infraestructura

### `claude-project-setup`

Inicializa y configura un repo para Claude Code: `CLAUDE.md`, reglas, comandos,
skills y agentes. Se usa una vez por proyecto.

### `writing-for-agents`

Cómo escribir documentos que va a consumir un agente. Se usa al crear o editar una
skill, o al modificar `CLAUDE.md` o `AGENTS.md`.

Es la meta-skill: la que se usa para escribir las demás.

---

## Sin clasificar

`wait-what`, `to-questionnaire` y `grill-me` están en el repo sin documentar aquí.
Si alguna de las tres se usa de verdad, merece su hueco en el flujo; si no, tocaría
borrarla.

**Volver al índice:** [README](../README.md)
