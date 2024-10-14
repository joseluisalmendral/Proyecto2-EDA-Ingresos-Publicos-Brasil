
# Proyecto de Análisis de Datos de Ingresos Gubernamentales de Brazil

## Descripción del Proyecto

Este proyecto se centra en el análisis de las diferencias entre los ingresos **previstos** y **realizados** por diversas categorías económicas dentro de un contexto gubernamental. A través de varias fases de análisis, visualización de datos y propuestas de mejora, se identifican tendencias clave en la ejecución de ingresos y se formulan recomendaciones para mejorar la precisión en la planificación y recolección de ingresos.

## Estructura del Proyecto

El proyecto está organizado de la siguiente manera:

```
- datos/             # Carpeta que contiene los archivos de datos utilizados para el análisis.
- imagenes/          # Carpeta con imagenes redundates.
- notebooks/         # Contiene los Jupyter Notebooks con las distintas fases del proyecto.
- src/               # Librería personal con funciones personalizadas.
```

### Notebooks incluidos:

1. **fase1_fase2.ipynb**:
   - Se realiza la limpieza inicial de los datos (reducción de nulos/duplicados) y un análisis exploratorio básico (EDA). Aquí se transforman las columnas y se identifican las categorías económicas presentes en el dataset.

2. **fase3.ipynb**:
   - Este notebook está dedicado al análisis exploratorio más detallado, donde se comienzan a identificar discrepancias entre ingresos previstos y realizados. También se generan las primeras visualizaciones básicas de las categorías económicas.

3. **fase4.ipynb**:
   - Se profundiza en la **visualización de datos**. Se crean diagramas de caja y gráficos de líneas para observar la evolución temporal de los ingresos y detectar patrones de subejecución o sobre ejecución.

4. **fase5.ipynb**:
   - Finalmente, este notebook resume algunos **hallazgos** y destaca las **tendencias observadas** en la ejecución de ingresos junto a **propuestas de mejora** basadas en los resultados del análisis.

## Instalación y Configuración

Este proyecto se ejecuta utilizando **Python** y varias bibliotecas estándar para análisis de datos. A continuación, se detallan las versiones utilizadas (completar con la versión correspondiente).

- **Python**: (3.12.4)
- **Pandas**: (2.2.2)
- **Numpy**: (2.1.1)
- **Matplotlib**: (3.9.2)
- **Seaborn**: (0.13.2)

### Instalación de dependencias

Para instalar las dependencias necesarias para ejecutar los notebooks, has de instalar las bibliotecas manualmente utilizando `pip`. A continuación te dejo un ejemplo de cómo podrías hacerlo:

```bash
pip install pandas numpy matplotlib seaborn
```

## Cómo ejecutar los notebooks

1. Clonar este repositorio.
2. Navegar a la carpeta del proyecto:
   ```bash
   cd nombre_del_proyecto
   ```
3. Ejecutar los notebooks Jupyter:
   ```bash
   jupyter notebook
   ```

4. Abre cada uno de los notebooks (`fase1_fase2.ipynb`, `fase3.ipynb`, `fase4.ipynb`, `fase5.ipynb`) en el orden mencionado para seguir el flujo de trabajo.

## IMPORTANTE
- Puede que al ejecutar el primer notebook (fase1_fase2.ipynb) nos de un error al exportar el archivo de 'dfs_concatenados.csv' por la carpeta a la que se quiere exportar. En caso de ser asi, crear la carpeta 'tratados' dentro de 'datos' o cambiar la ruta donde se va a generar el archivo.

## Notas adicionales

- **Calidad de los datos**: A lo largo del proyecto, hay algunas categorías con falta de información (por ejemplo, categorías etiquetadas como "Sem informação").
  
- **Análisis Temporal**: Se observó que ciertas discrepancias en los ingresos previstos y realizados estaban muy influenciadas por factores externos, lo que resalta la importancia de ajustar las proyecciones presupuestarias anualmente para reflejar estos cambios.

- **Visualizaciones**: Las visualizaciones generadas en los notebooks (gráficos de barras, líneas y diagramas de caja) se guardan en la carpeta `imagenes/` para futuras referencias.

