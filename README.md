# Contenedor Docker Python


## 1. Instalación

Para descargar la aplicación del repo, se debe escribir el siguiente comando:

```
$ git clone https://github.com/FragmentosTemporales/gestor-urls.git
```


### Instalación de Docker Compose

Para instalar la aplicación debes ejecutar el siguiente código:

```
$ docker compose build
```


### Variables de entorno

Al interior de la carpeta /backend debes crear un documento env.env el cual debe contener las siguiente variables, puedes guiarte con el documento example.env :

```

```


## 2. Ejecución

Para ejecutar la aplicación debes ingresar el siguiente comando:

```
$ docker compose run --rm backend sh -c "python manage.py"
```

Este repositorio incluye el corrector Flake8, por lo que también puedes ejecutarlo:

```
$ docker compose run --rm backend sh -c "python manage.py && flake8"
```

También puedes ejecutar la aplicación utilizando el script "init.sh":

```
$ sh scripts/init.sh
```


## 3.- ¿Qué estamos ejecutando?

Una función que copia un archivo "data.json" de una ubicación a otra.

## 4.- Bibliografía

A continuación te dejo el link de la imagen de Python en Docker:

```
https://hub.docker.com/_/python/
```
