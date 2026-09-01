# Fase 2 · Construir

La fase más corta de documentar, porque el trabajo ya está decidido. Si aquí hay que
tomar decisiones de producto, es que la fase 1 se quedó a medias.

---

## `implement`

**Cuándo.** Tienes un ticket de `to-tickets` o un plan escrito.

**Qué hace.** Ejecuta la implementación de ese ticket. Uno, no varios.

**Por qué importa.** Mantiene el trabajo acotado a lo que la spec dice, y el diff
revisable.

```
/implement

Ticket #42.
```

---

## Un ticket, una sesión

La tentación es encadenar tickets en la misma conversación. Aguanta lo que aguanta:
según crece el contexto, el modelo empieza a mezclar decisiones de un ticket con las
del siguiente.

Si vas a encadenar, cierra con [`handoff`](05-cerrar-sesion.md) y abre sesión nueva.

---

## Cuando el ticket es de interfaz

No lo implementes a pelo. La fase 3 tiene su propia cadena, y aplicarla después de
haber construido la pantalla entera es rehacerla.

**Anterior:** [01 · Definir](01-definir.md) ·
**Siguiente:** [03 · Interfaz](03-interfaz.md)
