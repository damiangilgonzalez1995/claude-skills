# Fase 4 · Revisar

Tres skills de revisión que miran cosas distintas. Se pueden pasar las tres sobre el
mismo trabajo sin que se pisen.

---

## `code-review`

**Qué mira.** El código, en dos ejes independientes que corren en subagentes
paralelos:

- **Estándares** — ¿sigue las convenciones documentadas del repo?
- **Spec** — ¿hace lo que pedía el issue o la spec de origen?

**Por qué los dos ejes.** Un código impecable que resuelve otra cosa pasa cualquier
revisión de estilo. El segundo eje es el que lo caza, y es el que se olvida.

```
/code-review

Desde main.
```

Acepta un punto fijo: un commit, una rama, un tag o un merge-base.

---

## `revision-interfaz`

**Qué mira.** La pantalla. Enruta a las seis `mejor-*` en orden (accesibilidad,
layout, redacción, tipografía, color, acabado), consolida en **una** tabla ordenada
por severidad y emite un veredicto.

**Cuándo.** Cuando el trabajo toca interfaz. Es la forma correcta de usar las seis:
a mano y una a una salen seis informes inconexos.

**Lo que la hace fiable.** Tiene disparadores de escalado que son ALTA a la vista, sin
promediar: un control sin nombre accesible, foco invisible, movimiento que ignora
`prefers-reduced-motion`, contenido recortado a 320px, significado transmitido solo
por color.

```
/revision-interfaz

Revisa la pantalla de reserva.
```

---

## `revision-de-cambios`

**Qué mira.** El **cambio**, no la pantalla. Resuelve el alcance contra el
merge-base, expande los ficheros tocados a las superficies donde se renderizan, y
clasifica cada hallazgo:

- `Introducido` — lo creó este cambio
- `Regresión` — debilitó algo que antes funcionaba
- `Preexistente` — ya estaba, no es culpa de este cambio

**Por qué esa clasificación importa.** Es la diferencia entre "has roto esto" y "esto
ya estaba roto". Sin ella, tocar un fichero heredado se convierte en una auditoría
completa que nadie pidió.

**Lo que hace y nadie más hace:** leer el lado `-` del diff. Las regresiones son
invisibles mirando solo el estado final.

```
/revision-de-cambios pr 482
```

Sin argumentos revisa lo que tengas sin commitear. Es de solo lectura: nunca hace
checkout de nada.

---

## Cuál usar

| Qué revisas | Skill |
|---|---|
| Un PR o una rama, sea de lo que sea | `code-review` |
| Una pantalla concreta | `revision-interfaz` |
| Un cambio que toca interfaz, antes de abrir el PR | `revision-de-cambios` |

Lo normal antes de un PR de front: `revision-de-cambios` primero (¿he roto algo?) y
`code-review` después (¿hace lo que pedía la spec?).

**Anterior:** [03 · Interfaz](03-interfaz.md) ·
**Siguiente:** [05 · Cerrar sesión](05-cerrar-sesion.md)
