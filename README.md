
# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>

# <h1 align=center>**`Machine Learning Operations (MLOps)`**</h1>

<p align="center">
<img src="https://user-images.githubusercontent.com/67664604/217914153-1eb00e25-ac08-4dfa-aaf8-53c09038f082.png"  height=300>
</p>
<hr>  

## **Descripción del problema (Contexto y rol a desarrollar)**

## Contexto

Tienes tu modelo de recomendación entrenado dando unas buenas métricas :smirk:, y ahora, cómo lo llevas al mundo real? :eyes:

El ciclo de vida de un proyecto de Machine Learning debe contemplar desde el tratamiento y recolección de los datos (Data Engineer stuff) hasta el entrenamiento y mantenimiento del modelo de ML según llegan nuevos datos.


## Rol a desarrollar

Empezaste a trabajar como **`Data Scientist`** en una start-up que provee servicios de agregación de plataformas de streaming. El mundo es bello y vas a crear tu primer modelo de ML que soluciona un problema de negocio: un sistema de recomendación que aún no ha sido puesto en marcha! 

Vas a sus datos y te das cuenta que la madurez de los mismos es poca (ok, es nula :sob:): Datos sin transformar, no hay procesos automatizados para la actualización de nuevas películas o series, entre otras cosas….  haciendo tu trabajo imposible :weary:. 

Debes empezar desde 0, haciendo un trabajo rápido de **`Data Engineer`** y tener un **`MVP`** (_Minimum Viable Product_) para la próxima semana! Tu cabeza va a explotar 🤯, pero al menos sabes cual es, conceptualmente, el camino que debes de seguir :exclamation:. Así que te espantas los miedos y te pones manos a la obra :muscle:

## **Propuesta de trabajo (requerimientos de aprobación)**

**`Transformaciones`**:  Para este MVP no necesitas perfección, ¡necesitas rapidez! ⏩ Vas a hacer estas, ***y solo estas***, transformaciones a los datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

<br/>

**LAS TRANSFORMACIONES ANTES MENCIONADOS SE REFLEJAN EN EL ARCHIVO LLAMADO ETL.ipynb. SE USO LA LIBRERIA PANDAS PARA SUBIR LOS DATOS UTILIZADOS**

<br/>

<br/>
<br/>

**LUEGO  GENERAMOS LAS DIFERENTES CONSULTAS A CONTINUACION Y QUE SE MUESTRAN EN EL ARCHIVO main.py.
PARA REALIZA DICHAS CONSULTAS SE UTILIZO LA LIBRERIA FASTAPI, PANDAS Y TYPING**

<br/>
<br/>


**`Desarrollo API`**:   Propones disponibilizar los datos de la empresa usando el framework ***FastAPI***. Las consultas que propones son las siguientes:

+ Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse get_max_duration(year, platform, duration_type))

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse get_score_count(platform, scored, year))

+ Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse get_count_platform(platform))

+ Actor que más se repite según plataforma y año. (La función debe llamarse get_actor(platform, year))


<br/>


**`Deployment`**: 

**EL DEPLOYMENT DE LAS CONSULTAS LO REALICE CON DETA SPACE. EL LINK PARA INSTALAR LA APLICACION ES https://deta.space/discovery/r/ycgthmwudmapctfc, LA APLICACION SE LLAMA DETA Y MI USUARIO ES "fjlu1989".

RECORDEMOS QUE EL TEXTO DEBE SER ESCRITO EN MINUSCULAS, SIN CARACTERES ESPECIALES, EL PUNTAJE DE LAS PELICULAS PUEDE LLEVAR DECIMAL SEPARADOS CON "." Y EL AÑO DEBE SER UN NUMERO DE 4 DIGITOS

A CONTINUACIÓN Y A MODO DE EJEMPLO SE PRUEBAN LAS CONSULTAS:

+ Película con mayor duración para el año 2000, de la plataforma "amazon", es dil hai tumhara... https://deta-1-q3009082.deta.app/get_max_duration?year=2000&platform=amazon&duration_type=min

+ La cantidad de peñiculas con un puntaje promedio mayor a 3.4 de la plataforma netflix para el año 2018 es de 1141..https://deta-1-q3009082.deta.app/get_movie_count/?platform=netflix&score=3.4&year=2018

+ La cantidad de peliculas de la plataforma hulu es de 3073...https://deta-1-q3009082.deta.app/get_count_platform/?platform=hulu

+ El actor que mas se repite de la plataforma disney para el año 2015 es carlos alazraqui... https://deta-1-q3009082.deta.app/get_actor/?platform=disney&release_year=2015


**
<br/>

**`Análisis exploratorio de los datos`**: _(Exploratory Data Analysis-EDA)_

**LUEGO REALIZAMOS UN ANALISIS EXPLORATORIO DE DATOS QUE SE MUESTRA EN EL ARCHIVO EDA.ipynb, PARA PODER PREPARAR LOS DATOS PARA EL SISTEMA DE RECOMENDACION DE PELICULAS. PARA ESTO SE UTILIZO PANDAS, MATPLOTLIB, SEABORN, 

**`Sistema de recomendación`**: 

Una vez que toda la data es consumible por la API ya lista para consumir para los departamentos de Analytics y de Machine Learning, y nuestro EDA bien realizado entendiendo bien los datos a los que tenemos acceso, es hora de entrenar nuestro modelo de machine learning para armar un sistema de recomendación de películas para usuarios, donde dado un id de usuario y una película, nos diga si la recomienda o no para dicho usuario. De ser posible, este sistema de recomendación debe ser deployado para tener una interfaz gráfica amigable para ser utilizada, utilizando Gradio o Deta Space para su deployment o bien con alguna solución como Streamlit o algo similar en local (tener el deployment del sistema de recomendación o una interfaz gráfica es un plus al proyecto).

PARA ESTE MODELO SE UTILIZO PANDAS, SURPRISE, Y GRADIO.

UNA VEZ CARGADOS LOS DATOS QUE SE MODIFICARON CON EL ANALISIS EDA, SE UTILIZA EL ALGORITMO SVD, USAMOS LA FUNCION CROSS_VALIDATION PARA EVALUAR EL PROYECTO Y LUEGO LO PUSIMOS A PRUEBA CON UNA FUNCION. AL FINAL CREAMOS LA INTERFAZ CON GRADIO. EL LINK PARA PODER UTILIZARLO ES https://huggingface.co/spaces/FJLU1989/RECOMENDADOR_DE_PELICULAS

**EL LINK DEL VIDEO ES https://youtu.be/clI-GJ2S3mU**