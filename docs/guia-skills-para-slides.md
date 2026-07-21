# Guía de las skills de Claude — material para clase

> Documento base para preparar unas diapositivas.
> Público: personas NO técnicas. Objetivo: explicar para qué sirve cada skill
> y cómo se usan juntas, con palabras sencillas y muchos ejemplos.
>
> Cada apartado `##` está pensado como "una diapositiva o grupo de diapositivas".

---

## 1. Antes de empezar: ¿qué es una "skill"?

Una **skill** es una **receta de trabajo** que le damos a la inteligencia
artificial (Claude). En lugar de improvisar, Claude sigue unos pasos probados,
igual que un cocinero sigue una receta o un mecánico un manual.

- Sin skill: le pides algo y hace lo que buenamente entiende.
- Con skill: sigue un método ordenado, pensado por expertos, que da mejores
  resultados y más predecibles.

**En una frase:** una skill convierte a la IA de "ayudante que improvisa" en
"profesional que sigue un método".

---

## 2. La idea más importante: primero DECIDIR, luego CONSTRUIR

El error más común al hacer algo grande es ponerse a construir antes de tener
claro **qué** se quiere y **cómo** se va a hacer. Estas skills separan esas dos
fases a propósito:

1. **Decidir**: despejar todas las dudas (qué queremos, cómo se llama cada cosa,
   qué herramienta usar, qué aspecto tendrá...).
2. **Construir**: solo cuando ya no queda nada que decidir, se pone uno a trabajar.

**Analogía:** construir una casa. Primero el arquitecto y los planos (decidir);
solo después llegan los albañiles (construir). Nadie levanta paredes sin planos.

---

## 3. Mapa rápido de las 5 skills principales

| Skill | En una frase (sencilla) | Analogía cotidiana |
|---|---|---|
| **`/wayfinder`** | Planifica algo muy grande dividiéndolo en decisiones que se resuelven de una en una. | Organizar una boda: mil decisiones, se toman poco a poco. |
| **`/research`** | Busca información fiable sobre un tema mientras tú sigues con otra cosa. | Mandar a alguien a la biblioteca a buscar datos. |
| **`/to-spec`** | Coge todo lo hablado y lo pasa a limpio en un documento oficial. | El acta de una reunión. |
| **`/to-tickets`** | Trocea ese documento en tareas pequeñas y ordenadas. | Una lista de la compra ordenada por pasos. |
| **`/implement`** | Se arremanga y construye una de esas tareas, comprobando que funciona. | El obrero que ejecuta el plano. |

---

## 4. Las 5 skills, una a una

### 4.1 `/wayfinder` — planificar algo enorme (con niebla)

**En una frase:** cuando el trabajo es tan grande que no cabe en una sola sesión
y encima no ves el camino, wayfinder dibuja un **mapa** y va resolviendo las
dudas una a una hasta que el camino queda claro.

**La clave:** wayfinder **decide, no construye**. Su trabajo es despejar la niebla.

**Analogía:** un explorador que avanza por un bosque con niebla. No ve el final,
pero cada paso que da despeja un poco más el camino y le deja ver el siguiente.

**Cuándo se usa:** proyectos grandes y confusos, donde ni siquiera tienes claro
por dónde empezar.

**Ejemplo:** "Quiero añadir avisos (notificaciones) a mi aplicación."
Suena a una cosa, pero esconde muchas decisiones: ¿avisos por email, por móvil,
o los dos? ¿el usuario puede elegir cuáles recibir? ¿qué aspecto tiene la
pantalla de avisos? Wayfinder pone cada duda como una "tarjeta de decisión" y las
va resolviendo de una en una, sin agobiarse por resolverlo todo de golpe.

---

### 4.2 `/research` — investigar con fuentes fiables

**En una frase:** manda a un ayudante a investigar un tema en **fuentes de
confianza** (documentación oficial, no rumores) mientras tú sigues trabajando, y
te trae un resumen con las fuentes citadas.

**Analogía:** pedirle a un bibliotecario que te busque datos serios mientras tú
avanzas con otra cosa; luego vuelve con la ficha y te dice de dónde sacó cada dato.

**Cuándo se usa:** cuando una decisión depende de un dato que no sabes y hay que
buscarlo bien (no vale "me suena que...").

**Ejemplo:** antes de decidir "¿qué servicio usamos para enviar los avisos al
móvil?", research compara las opciones oficiales, mira precios y limitaciones, y
te trae un resumen para que decidas con datos en la mano.

---

### 4.3 `/to-spec` — pasar a limpio en un documento

**En una frase:** coge **todo lo que ya se ha hablado** y lo convierte en un
documento claro que explica qué se va a hacer y por qué. **No te vuelve a
preguntar nada**: solo ordena y resume lo decidido.

("Spec" es simplemente ese documento: el "documento oficial" de la tarea.)

**Analogía:** el **acta de una reunión**. Todos hablaron; alguien pone por escrito
lo acordado para que quede claro y nadie lo interprete a su manera.

**Cuándo se usa:** cuando ya has discutido bastante una idea y quieres dejarla
fijada por escrito antes de construir.

**Ejemplo:** después de decidir cómo serán los avisos, to-spec escribe el
documento: "el usuario podrá activar o desactivar cada tipo de aviso desde su
perfil", con la lista completa de lo que debe hacer y lo que queda fuera.

---

### 4.4 `/to-tickets` — trocear en tareas pequeñas y ordenadas

**En una frase:** parte el documento en **tareas pequeñas** ("tickets"), cada una
lo bastante pequeña para hacerse de una vez, y marca **cuál depende de cuál**.

**Idea importante:** cada tarea es una **rebanada completa**, no media cosa. Es
decir, entrega algo que ya se puede ver funcionando, aunque sea pequeño (no "media
pantalla sin botones").

**Analogía:** una receta de cocina. En vez de "haz una tarta", te da los pasos
ordenados: 1) prepara la masa, 2) hornea (necesita el paso 1 hecho), 3) decora
(necesita el paso 2). No puedes decorar antes de hornear.

**Cuándo se usa:** cuando ya tienes el documento y quieres una lista de trabajo
clara y ordenada.

**Ejemplo:** el documento de los avisos se convierte en:
- Tarea 1: guardar las preferencias del usuario (qué avisos quiere).
- Tarea 2: enviar el aviso por email (necesita la 1 hecha).
- Tarea 3: la pantalla donde el usuario activa/desactiva avisos (necesita la 2).

---

### 4.5 `/implement` — construir de verdad

**En una frase:** coge **una** tarea de la lista y la construye, comprobando sobre
la marcha que funciona, y al final pide una **revisión** antes de dar por hecho.

**Analogía:** el obrero que coge un plano concreto, levanta esa parte de la casa,
comprueba que está a plomo, y avisa al aparejador para que la revise.

**Cuándo se usa:** cuando ya tienes las tareas claras y toca ejecutarlas, de una
en una.

**Ejemplo:** implement coge la "Tarea 1: guardar preferencias del usuario", la
programa, comprueba que guarda bien lo que el usuario elige, y luego lanza una
revisión de calidad antes de pasar a la Tarea 2.

---

## 5. Cómo se encadenan: el pipeline

La gracia es que **se usan en cadena**, cada una recoge el trabajo de la anterior:

```
   idea GRANDE y confusa                 idea ya CLARA y pequeña
            |                                     |
            v                                     |
      /wayfinder                                  |
   (dibuja el mapa y                              |
    resuelve las dudas)                           |
            |   ya está claro                     |
            +------------------+------------------+
                               v
                          /to-spec        (pasa a limpio: el documento)
                               v
                         /to-tickets      (trocea en tareas ordenadas)
                               v
                         /implement       (construye tarea a tarea)
```

**Dos formas de entrar:**

- Si la idea es **grande y confusa** → empieza por `/wayfinder`.
- Si la idea ya está **clara y es pequeña** → sáltate wayfinder y ve directo a
  `/to-spec → /to-tickets → /implement`.

**Regla de oro que comparten todas:** trabajar **de una en una**. Una decisión
cada vez, una tarea cada vez. Nada de hacerlo todo a la vez y liarse.

---

## 6. Ejemplo completo, de principio a fin

Idea inicial: **"Quiero añadir avisos a mi aplicación."**

1. **`/wayfinder`** — Es grande y confuso, así que primero dibujamos el mapa de
   dudas y las resolvemos una a una:
   - ¿Qué servicio usamos para enviar avisos? → lo mira **`/research`**.
   - ¿El usuario podrá elegir qué avisos recibir? → se decide preguntando.
   - ¿Qué aspecto tiene la pantalla de avisos? → se hace una maqueta rápida.
2. **`/to-spec`** — Con las dudas resueltas, se escribe el documento oficial:
   qué avisos habrá, quién los recibe, qué puede configurar el usuario.
3. **`/to-tickets`** — El documento se trocea en tareas ordenadas (guardar
   preferencias → enviar email → pantalla de configuración).
4. **`/implement`** — Se construye tarea a tarea, comprobando que cada una
   funciona antes de pasar a la siguiente.

Resultado: se pasó de una frase difusa a algo construido y comprobado, **sin
atascos**, porque cada paso preparó el terreno al siguiente.

---

## 7. Otras skills de apoyo (más breve)

Estas no son las 5 protagonistas, pero ayudan en el camino:

| Skill | Para qué sirve (sencillo) | Analogía |
|---|---|---|
| **`/grilling`** | Te hace preguntas difíciles para que no se te escape nada. | Un entrevistador exigente. |
| **`/domain-modeling`** | Pone de acuerdo a todos en cómo se llama cada cosa. | Un diccionario común del equipo. |
| **`/prototype`** | Hace una maqueta rápida y tosca para ver si la idea "se siente bien". | Una maqueta de cartón. |
| **`/code-review`** | Revisa el trabajo terminado en dos preguntas: ¿está bien hecho? ¿hace lo que se pedía? | Un corrector de exámenes. |
| **`/handoff`** | Resume todo para que otra persona (u otra sesión) continúe el trabajo. | Pasar el testigo en una carrera de relevos. |
| **`/teach`** | Explica un tema de forma didáctica, paso a paso. | Un profesor particular. |
| **`/muscle-memory`** | Gimnasio de ejercicios de práctica para no perder la forma. | Ir al gimnasio a entrenar. |

---

## 8. Resumen: una frase por skill (para una diapositiva final)

- **`/wayfinder`**: planifica lo enorme resolviendo dudas una a una.
- **`/research`**: busca datos fiables mientras tú sigues.
- **`/to-spec`**: pasa a limpio lo hablado en un documento.
- **`/to-tickets`**: trocea el documento en tareas ordenadas.
- **`/implement`**: construye tarea a tarea y lo revisa.
- Apoyo: **grilling** (pregunta), **domain-modeling** (nombres), **prototype**
  (maqueta), **code-review** (revisa), **handoff** (pasa el testigo).

---

## 9. Ideas para montar las diapositivas (opcional)

Un posible guion de slides, una idea por diapositiva:

1. Portada: "Cómo trabaja la IA con un método: las skills".
2. ¿Qué es una skill? (la receta).
3. La idea grande: primero decidir, luego construir (la casa y los planos).
4. Las 5 protagonistas (la tabla del apartado 3).
5–9. Una diapositiva por skill (frase + analogía + ejemplo).
10. El pipeline (el dibujo del apartado 5).
11. Ejemplo completo de los avisos (apartado 6).
12. Skills de apoyo (tabla del apartado 7).
13. Cierre: una frase por skill (apartado 8).

**Consejo para clase:** en cada skill, cuenta primero la analogía cotidiana y
solo después el ejemplo. La analogía "engancha" y el ejemplo "aterriza".
