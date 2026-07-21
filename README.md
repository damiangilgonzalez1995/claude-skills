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

## Origen

Varias skills de ingeniería están portadas y traducidas al español desde
[`mattpocock/skills`](https://github.com/mattpocock/skills), adaptando sus
referencias cruzadas y el issue tracker al repo de destino.
