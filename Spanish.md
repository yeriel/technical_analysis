# Analisis Tecnico

## Contexto
Trabajo realizado en este repositorio corresponde a una prueba técnica para la empresa Comunidad Feliz (link). La prueba está diseñada para realizar un análisis de un conjunto de productos disponibles, recuperando información desde un endpoint diseñado para esta prueba.

## Para empezar
Para ejecutar el código presente en este repositorio debes clonar el repositorio e instalar las dependencias necesarias de la siguiente manera

``` 
git clone https://github.com/yeriel/technical_analysis.git
cd technical_analysis
pip install -r requirements.txt
```

## Estructura del repositorio
Este repositorio esta estructurado en dos partes en los scripts que permiten la extracción de la información desde el endpoit preparado para esta prueba y en el análisis de datos.

### Extracción de información
Para realizar la extracción de información se debe ejecutar los archivos extract_clients.py y extract_sales.py utilizando Python mediante el comando

 ```
python extract_clients.py 
python extract_sales.py
```
### Análisis
El análisis de datos se realizó utilizando jupyter notebook para ellos debes ejecutar tu ambiente de conda o tu entorno virtual de preferencia y ejecutar el siguiente comando

```
jupyter notebook analysis.ipynb
```

