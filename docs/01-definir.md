# Fase 1 · Definir

Convertir lo decidido en algo que se pueda implementar sin volver a decidir. Es la
parte de "spec-driven development": primero el documento, luego el código.

La cadena es corta y no tiene atajos: **spec → tickets → implementar**.

---

## `to-spec`

**Cuándo.** Ya sabes qué quieres construir y por qué. Antes de tocar código.

**Qué hace.** Convierte la idea o la petición en una spec: qué se construye, qué
queda fuera, qué comportamiento se espera y qué decisiones ya están cerradas.

**Por qué importa.** Una spec escrita es lo que permite revisar después si lo
construido es lo pedido. Sin ella, "está terminado" es una opinión.

```
/to-spec

Los técnicos tienen que poder anotar la solución desde el móvil, con foto,
y que eso cierre la incidencia.
```

**Sale de aquí:** un fichero de spec en el repo, no un mensaje en el chat.

---

## `to-tickets`

**Cuándo.** Justo después de `to-spec`. Siempre.

**Qué hace.** Descompone la spec en tickets accionables, cada uno lo bastante
pequeño como para resolverse de una sentada y revisarse de un vistazo.

**Por qué importa.** Es lo que evita el PR de cuarenta ficheros que nadie puede
revisar de verdad. Un ticket, una rama, un PR.

```
/to-tickets

Descompón la spec de anotar solución desde móvil.
```

---

## `prototype`

**Cuándo.** Hay una duda de diseño que no se resuelve discutiendo. "¿Este modelo de
estados se siente bien?" "¿Cómo debería verse esta pantalla?"

**Qué hace.** Construye un prototipo **desechable** para responder esa pregunta
concreta. No es el código final y no se queda.

**Por qué importa.** Discutir sobre cómo se sentirá algo es más caro y menos fiable
que construirlo en veinte minutos y tocarlo.

```
/prototype

Necesito ver si el selector de estado de incidencia funciona mejor como
desplegable o como pastillas en línea.
```

**Ojo:** es desechable de verdad. Si el prototipo acaba en producción, el prototipo
no era un prototipo.

---

## El orden importa

`to-spec` antes que `to-tickets`, y los dos antes que `implement`. El error caro es
saltar directo a implementar con la idea en la cabeza: funciona en tareas de media
hora y se desmorona en todo lo demás.

`prototype` va en paralelo, cuando la spec depende de una duda que solo se resuelve
viendo la cosa.

**Anterior:** [00 · Antes de empezar](00-antes-de-empezar.md) ·
**Siguiente:** [02 · Construir](02-construir.md)
