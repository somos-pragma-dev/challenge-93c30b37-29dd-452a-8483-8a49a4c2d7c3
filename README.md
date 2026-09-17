# Desarrollo de una API REST para gestión de cuentas bancarias

El equipo de desarrollo de una institución financiera necesita una API REST para gestionar cuentas bancarias. La API debe permitir la creación, lectura, actualización y eliminación de cuentas, así como la autenticación de usuarios mediante JWT. Los clientes de la API son aplicaciones móviles y web de la institución. La API debe manejar un volumen de 10 000 solicitudes por segundo en hora pico con un tiempo de respuesta promedio de 200 ms. Las cuentas tienen atributos como número de cuenta, saldo, tipo de cuenta (ahorros, corriente), fecha de apertura y estado (activa, inactiva). La API debe validar que el saldo no sea negativo y que el número de cuenta sea único. En caso de error, debe devolver un mensaje descriptivo y un código de error específico.

## Informacion General

| Campo | Valor |
|-------|-------|
| **Tema** | API REST en entorno bancario |
| **Nivel** | junior-l2 |
| **Tipo** | practical |
| **Tiempo estimado** | 8 horas |

## Fases del Reto

### Fase 0: Configuración del Proyecto

**Objetivo:** Obtener el proyecto base funcional enviando el Código Base a un asistente de IA, que lo analizará, corregirá errores y generará un ZIP listo para usar.

**Tiempo estimado:** 15-30 minutos

**Instrucciones:**

- Asegúrate de tener instalado para ejecutar el proyecto: Python 3.10+, pip, VS Code o similar.
- Copia todo el contenido del campo **Código Base** de este reto — incluyendo el texto de instrucciones que aparece al inicio.
- Abre un asistente de IA (Claude en claude.ai, ChatGPT o Gemini — se recomienda Claude), pega el contenido copiado en el chat y envíalo.
- El asistente analizará los archivos, corregirá errores y generará un archivo ZIP descargable. Descárgalo y extráelo en la carpeta donde quieras trabajar.
- Ejecuta `pip install -r requirements.txt` y luego arranca el proyecto. Si no hay errores, estás listo.

**Entregable:** El proyecto compila/arranca sin errores.

<details>
<summary>Pistas de conocimiento</summary>

- Copia el Código Base completo incluyendo el texto de instrucciones al inicio — esas instrucciones le indican al asistente exactamente qué hacer con los archivos.
- Si el asistente no genera el ZIP automáticamente al terminar el análisis, escríbele: "genera el ZIP ahora".
- Si el proyecto tiene errores al arrancar, comparte el mensaje de error con el mismo asistente para que lo corrija.

</details>

### Fase 1: Definición del modelo de datos y autenticación

**Objetivo:** Definir el modelo de datos para las cuentas bancarias y configurar la autenticación JWT.

**Tiempo estimado:** 2 horas

**Instrucciones:**

- Identificar los atributos necesarios para una cuenta bancaria.
- Definir las reglas de validación para el saldo y el número de cuenta.
- Configurar la autenticación JWT para asegurar que solo usuarios autorizados puedan acceder a la API.

**Entregable:** Modelo de datos para cuentas bancarias y configuración de autenticación JWT.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo representar los diferentes tipos de cuentas y sus atributos.
- Piensa en cómo manejar la unicidad del número de cuenta y la validación del saldo.

</details>

### Fase 2: Implementación de endpoints CRUD

**Objetivo:** Implementar los endpoints para crear, leer, actualizar y eliminar cuentas bancarias.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Crear los endpoints para las operaciones CRUD de cuentas bancarias.
- Asegurar que los endpoints manejen las validaciones definidas en la fase anterior.
- Implementar la lógica para manejar errores y devolver mensajes descriptivos.

**Entregable:** Endpoints CRUD para cuentas bancarias con validaciones y manejo de errores.

<details>
<summary>Pistas de conocimiento</summary>

- Considera cómo estructurar los endpoints para seguir los principios REST.
- Piensa en cómo manejar las relaciones entre cuentas y usuarios en la autenticación.

</details>

### Fase 3: Optimización y escalabilidad

**Objetivo:** Optimizar la API para manejar el volumen de solicitudes y asegurar la escalabilidad.

**Tiempo estimado:** 3 horas

**Instrucciones:**

- Identificar posibles cuellos de botella en la API.
- Implementar estrategias para mejorar el rendimiento y la escalabilidad.
- Asegurar que la API maneje el volumen de solicitudes especificado con un tiempo de respuesta promedio de 200 ms.

**Entregable:** API optimizada y escalable para manejar 10 000 solicitudes por segundo con un tiempo de respuesta promedio de 200 ms.

<details>
<summary>Pistas de conocimiento</summary>

- Considera el uso de caché para reducir la carga en la base de datos.
- Piensa en cómo distribuir la carga entre múltiples instancias de la API.

</details>

## Dimensiones Evaluadas

- **queEs**: ¿Qué es una cuenta bancaria y cuáles son sus atributos principales?
- **paraQueSirve**: ¿Para qué sirve la autenticación JWT en este contexto?
- **comoSeUsa**: ¿Cómo se usan los endpoints CRUD para gestionar cuentas bancarias?
- **erroresComunes**: ¿Cuáles son los errores comunes al implementar una API REST y cómo se pueden evitar?
- **queDecisionesImplica**: ¿Qué decisiones implica la optimización y escalabilidad de una API REST?

## Criterios de Evaluacion

- Definición correcta del modelo de datos para cuentas bancarias.
- Configuración adecuada de la autenticación JWT.
- Implementación de endpoints CRUD con validaciones y manejo de errores.
- Optimización y escalabilidad de la API para manejar el volumen de solicitudes especificado.

## Como trabajar con un asistente de IA

Hay dos caminos, elegi uno:

- **AGENTS.md** (recomendado) — instrucciones nativas del repo. Abri esta carpeta con tu agente local (Claude Code, Cursor, Codex, Copilot, Gemini) y las carga solo. Sabe que archivos faltan y con que comando se verifica, y completa el scaffold escribiendo en disco.
- **PROMPT_MEJORA.md** — para copiar y pegar en un chat (claude.ai, ChatGPT). Devuelve un ZIP con el proyecto. Sirve si no tenes un agente en el IDE.

Ninguno de los dos resuelve las fases del reto: eso es tu trabajo.

## Verificacion

El proyecto esta listo para trabajar cuando este comando corre sin errores:

```bash
el comando de build o arranque canonico del stack elegido
```

---

*Reto generado automaticamente por Challenge Generator - Pragma*
