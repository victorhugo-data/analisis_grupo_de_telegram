# Diccionario de datos

Tabla tidy `df` que se construye en la sección 2 de la libreta
[`1.0-vh-analisis-grupo-telegram.ipynb`](../notebooks/1.0-vh-analisis-grupo-telegram.ipynb).
Cada fila es un mensaje de usuario del grupo (34,868 en total); los avisos del sistema no se incluyen. La tabla se guarda en `data/processed/mensajes_tidy.pkl`, que no se versiona.

| Columna | Tipo | Descripción |
|---|---|---|
| `id_mensaje` | entero | Número del mensaje dentro de la exportación de Telegram. |
| `timestamp` | fecha y hora | Fecha y hora de envío en hora de Moscú (`Europe/Moscow`, UTC+3). La exportación venía en UTC-07:00 y se convirtió sumando 10 horas. Usar Moscú es un supuesto: algunos miembros pueden vivir en otras zonas horarias. |
| `usuario` | texto | Remitente anonimizado con un nombre de superhéroe (con sufijo numérico a partir del usuario 51, p. ej. `Flash_2`), o "Cuenta eliminada" para todas las cuentas borradas. |
| `texto` | texto | Texto del mensaje sin correos, enlaces, tarjetas ni teléfonos, y con las menciones cambiadas por `@usuario_anon`. Vacío si el mensaje solo tenía multimedia. |
| `tipo_contenido` | texto | `texto`, `foto`, `sticker`, `gif`, `video` (archivo de video o video mensaje), `voz` u `otro` (audio, archivo, encuesta o mensaje que solo tenía un enlace). Si una foto trae texto, su tipo es `foto`. |
| `reenviado` | booleano | Si el mensaje se reenvió desde otro chat. |
| `es_respuesta` | booleano | Si el mensaje responde a otro mensaje. |
| `responde_a_id` | entero (con nulos) | `id_mensaje` del mensaje al que responde. |
| `sticker_emoji` | texto | Emoji asociado al sticker; solo en los stickers. |
| `n_reacciones` | entero | Número de reacciones que recibió el mensaje. |
| `via_bot` | booleano | Si el mensaje se envió a través de un bot. |
| `es_repetido` | booleano | Si su texto aparece idéntico más de 3 veces en el grupo (normalmente anuncios). |
| `n_palabras` | entero | Palabras del texto: secuencias de letras latinas o cirílicas, con guion opcional ("что-то"). No cuentan números, emojis ni menciones. |
| `n_emojis` | entero | Emojis del texto, contados con la librería `emoji`. |
