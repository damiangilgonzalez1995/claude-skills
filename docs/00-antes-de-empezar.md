# Fase 0 · Antes de escribir nada

La fase que más se salta y la que más caro sale saltarse. Aquí no se produce
código: se produce **certeza sobre qué hay que construir**.

Señal de que te la has saltado: a mitad de la implementación descubres un requisito
que cambia el diseño entero.

---

## `wayfinder`

**Cuándo.** El trabajo no cabe en una sesión. Hablamos de varios días, varias
personas, o algo que va a atravesar media aplicación.

**Qué hace.** Convierte el esfuerzo en un mapa de tickets de **decisión**, no de
tareas. Cada ticket es una pregunta que hay que cerrar, y se resuelven de uno en
uno. El tracker son GitHub Issues.

**Por qué importa.** Sin esto, a la tercera sesión nadie sabe qué queda pendiente ni
por qué se decidió lo que se decidió. El mapa sobrevive a que se acabe el contexto.

**Cómo se invoca.** Solo con `/wayfinder`. No se auto-invoca a propósito: es una
decisión tuya, no del modelo.

```
/wayfinder

Quiero rehacer el sistema de notificaciones de la aplicación.
```

---

## `grilling`

**Cuándo.** Tienes un plan y te gusta demasiado. O una decisión que llevas
defendiendo un rato sin que nadie la haya atacado en serio.

**Qué hace.** Te interroga sin tregua. No busca ayudarte: busca los agujeros.

**Por qué importa.** Es más barato que se caiga el plan aquí que después de tres
días de implementación.

```
/grilling

Voy a migrar el estado del frontend a un store global. Ponme a prueba.
```

**Variante:** `grill-with-docs` hace lo mismo pero apoyándose en documentación
concreta, cuando la discusión depende de cómo funciona de verdad una herramienta y
no de opiniones.

---

## `research`

**Cuándo.** Necesitas hechos, no opiniones. Cómo funciona de verdad una API, qué
dice la especificación, qué cambió en una versión.

**Qué hace.** Investiga contra fuentes primarias de alta confianza y deja los
hallazgos como un fichero Markdown en el repo. Puede correr en segundo plano
mientras tú sigues con otra cosa.

**Por qué importa.** El hallazgo queda escrito y fechado en el repo. La próxima vez
que surja la duda, la respuesta ya está y no hay que volver a buscarla.

```
/research

Cómo se comporta el rate limiting de la API de Supabase cuando el cliente
usa el pooler en vez de la conexión directa?
```

---

## `domain-modeling`

**Cuándo.** El equipo llama a la misma cosa de tres maneras. O estás a punto de
nombrar una entidad nueva y no tienes claro si ya existe con otro nombre.

**Qué hace.** Construye y afina el modelo de dominio y el lenguaje ubicuo del
proyecto, y registra las decisiones de arquitectura.

**Por qué importa.** Los nombres son la parte del código más cara de cambiar
después. Media hora aquí ahorra un refactor entero.

```
/domain-modeling

En ATI, "incidencia", "parte", "OT" y "tarea" se usan mezclados. Fija el vocabulario.
```

---

## Cómo elegir entre las cuatro

| Tu situación | Skill |
|---|---|
| No sé por dónde empezar, esto es enorme | `wayfinder` |
| Ya tengo un plan y quiero que lo destroces | `grilling` |
| Me falta un dato y no me lo quiero inventar | `research` |
| Tenemos lío con los nombres | `domain-modeling` |

No son excluyentes. Lo normal en algo grande es `wayfinder` primero, y luego
`research` o `grilling` dentro de cada ticket del mapa.

**Siguiente fase:** [01 · Definir](01-definir.md)
