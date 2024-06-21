#!/bin/sh
echo "---------------------------------------------"
echo "|       Iniciando nuestra super app         |"
echo "---------------------------------------------"
docker compose run --rm backend sh -c "python manage.py && flake8"
echo "---------------------------------------------"
echo "|          Finalizando super app            |"
echo "---------------------------------------------"