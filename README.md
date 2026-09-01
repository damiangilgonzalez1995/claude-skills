# claude-skills

Biblioteca personal de skills de Claude Code de Damián. Fuente de verdad global,
clonada/ubicada en `~/.claude/skills/` para estar disponible en todos los
proyectos. Las skills que además se usan en un proyecto concreto (p. ej.
`ATI_PLATFORM`) se copian a su `.claude/skills/` local.

## Skills

| Skill | Qué hace |
|---|---|
| `wayfinder` | Planifica un esfuerzo enorme (más de una sesión) como un mapa de tickets de decisión que se resuelven de uno en uno. Solo `/wayfinder` (no auto-invocable). |
| `code-review` | Revisa cambios desde un punto fijo en dos ejes independientes: Estándares y Spec, en subagentes paralelos. |
| `to-spec` | Convierte una idea/petición en una spec. |
| `to-tickets` | Descompone una spec en tickets accionables. |
| `implement` | Ejecuta la implementación de un ticket/plan. |
| `grilling` | Interroga sin tregua un plan, decisión o idea. |
| `grill-with-docs` | Grilling apoyado en documentación. |
| `domain-modeling` | Construye y afina el modelo de dominio / lenguaje ubicuo. |
| `prototype` | Prototipo desechable para responder una pregunta de diseño. |
| `handoff` | Compacta la conversación en un documento de traspaso. |
| `teach` | Explicación didáctica. |
| `muscle-memory` | Gimnasio de katas de práctica en Python. |
| `claude-project-setup` | Inicializa/configura un repo para Claude Code. |

## Skills de diseño

Portadas y traducidas al español desde los repos públicos que recopila el
documento de AI Labs. Los `SKILL.md` están en español; los ficheros de
`references/` y los `scripts/` se conservan en inglés a propósito, porque son
catálogos técnicos y código que los propios `SKILL.md` citan por ruta.

| Skill | Qué hace | Origen |
|---|---|---|
| `animar` | Construye una animación decidiendo en orden: debe animarse, con qué propósito, herramienta, propiedades, curva y duración. | Emil Kowalski |
| `diseno-apple` | Movimiento fluido y físico de Apple traducido a la web: muelles, interrumpibilidad, traspaso de velocidad, materiales, tipografía. | Emil Kowalski |
| `ingenieria-de-diseno` | Filosofía de acabado de UI y los detalles invisibles que se acumulan. Revisa en tabla Antes/Después/Por qué. | Emil Kowalski |
| `vocabulario-animacion` | Glosario inverso: convierte "eso que rebota al abrirse" en el término exacto. | Emil Kowalski |
| `ingeniero-diseno-web` | Construye artefactos visuales pulidos en HTML/CSS/JS/React, con 25 recetas de estilo ancladas y modo crítica de 5 dimensiones. | Garden (ConardLi) |
| `diseno-landing` | Sistema completo de landing: estrategia y estructura (Parte A) más el sistema visual innegociable (Parte B). | Elaya |
| `video-a-superprompt` | Convierte un vídeo de referencia en un prompt de recreación detallado. Usa `ffprobe`/`ffmpeg`. | Meng To |
| `sitios-calidad-premio` | Sitios distintivos y ricos en movimiento: GSAP, un único motor de scroll suave, Three.js solo con propósito, assets honestos. | Meng To |
| `revision-interfaz` | Orquesta las seis `mejor-*` en una revisión consolidada con severidad, tope y veredicto. | Jakub Krehel |
| `revision-de-cambios` | Revisa un cambio (rama, PR, rango), lee las líneas eliminadas y clasifica cada hallazgo. Solo `/revision-de-cambios`. | Jakub Krehel |
| `mejor-layout` | Agrupación, alineación, orden de lectura, breakpoints, crecimiento de textos traducidos, RTL. | Jakub Krehel |
| `mejor-tipografia` | Escala, espaciado, fuentes variables, OpenType, wrapping, truncado, puntuación. | Jakub Krehel |
| `mejor-colores` | Rampas, tokens semánticos, contraste medido, modo oscuro, espacios de interpolación. | Jakub Krehel |
| `mejor-accesibilidad` | Nativo antes que ARIA, foco, teclado, áreas de pulsación, formularios, regiones vivas. | Jakub Krehel |
| `mejor-ui` | Radios concéntricos, alineación óptica, superficies, transiciones de iconos, escala al pulsar. | Jakub Krehel |
| `mejor-redaccion` | Voz y tono, botones con verbo, errores que dicen cómo arreglarlo, estados vacíos. | Jakub Krehel |
| `tastemaker` | Genera UI con gusto en vez de bazofia genérica: extrae color de píxeles reales, genera paletas, diversifica estructura y recuerda decisiones. | codeswithroh |
| `leyes-de-percepcion` | Gestalt aplicada a interfaz: proximidad, similitud, región común, cierre, continuidad, figura-fondo, Von Restorff, jerarquía. | Owl-Listener |
| `leyes-de-retencion` | Por qué la gente abandona un flujo: Hick, Fitts, Miller, Jakob, Doherty, Zeigarnik, posición serial, pico-final, Tesler. | Owl-Listener |

Banco de pruebas con demos antes/después y los prompts de cada una:
`ui-mejora`, en `~/Documents/GitHub/ui-mejora`.
