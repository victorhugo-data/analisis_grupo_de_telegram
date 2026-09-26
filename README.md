# Análisis de un grupo de Telegram

Tarea escolar de Ciencia de Datos: análisis exploratorio de un chat grupal exportado de
Telegram, desarrollado en una sola libreta Jupyter dentro de un proyecto con estructura
[Cookiecutter Data Science](https://cookiecutter-data-science.drivendata.org/).

## El grupo

Se trata de un grupo público de Telegram en ruso dedicado a la compraventa e intercambio
de cuentas de un videojuego. La exportación abarca aproximadamente de agosto de 2025 a
septiembre de 2026, con alrededor de 35,000 mensajes de más de 1,300 remitentes.
Buena parte del contenido son fotos (capturas de cuentas), anuncios repetidos y jerga
del juego.

## Privacidad

- Los datos crudos (`data/raw/`) y los datos intermedios/procesados **no se suben** al
  repositorio. Por eso la libreta se entrega ya ejecutada, con todas sus salidas visibles.
- Cada remitente se reemplaza por un nombre de superhéroe (por ejemplo, `Batman`,
  `Flash_2`); la tabla de equivalencias no se versiona.
- Las menciones `@usuario` se reemplazan por `@usuario_anon` y se eliminan enlaces y
  números de teléfono.
- Solo se muestran resultados agregados (conteos, promedios, frecuencias), nunca mensajes
  textuales, para que no sea posible identificar a los autores.

## Preguntas de análisis

1. ¿Qué usuario envía más mensajes?
2. Frecuencia promedio de palabras por mensaje de texto de cada usuario.
3. ¿Quién envía más palabras, emojis y stickers?
4. Días de la semana y horas con más y menos mensajes.
5. Palabras más usadas (con y sin *stop words*), en general y por usuario.
6. Adjetivos más usados.
7. Preguntas adicionales propuestas.
8. Conclusiones.

## Estructura del proyecto

```
├── README.md          <- Este archivo
├── environment.yml    <- Entorno conda ("telegram")
├── requirements.txt   <- Mismas dependencias para pip
├── data
│   ├── external       <- Datos de fuentes externas
│   ├── interim        <- Datos intermedios (no se versionan)
│   ├── processed      <- Tabla tidy final (no se versiona)
│   └── raw            <- Exportación HTML original de Telegram (no se versiona)
├── docs               <- Documentación
├── models             <- Modelos (no se usan en esta tarea)
├── notebooks          <- Libreta de análisis: 1.0-analisis-grupo-telegram.ipynb
├── references         <- Material de referencia
├── reports
│   └── figures        <- Gráficas generadas
└── src
    ├── __init__.py
    └── config.py      <- Rutas del proyecto
```

## Entorno

Con Anaconda/Miniconda:

```bash
conda env create -f environment.yml
conda activate telegram
python -m spacy download ru_core_news_sm
```

Alternativa con pip:

```bash
pip install -r requirements.txt
python -m spacy download ru_core_news_sm
```

Después, en VS Code, seleccionar el kernel `telegram` para abrir la libreta.

## Resultados

*Pendiente: se completará al terminar el análisis.*
