# Folder del programma backend

## Prerequisito

Se nella cartella non sono presenti il file manage.py e la cartella smartDentist, digitare

```
sudo docker-compose run web django-admin.py startproject smartDentist .
```

## Esecuzione del programma

Per fare partire la prova, digitare

```
docker-compose up
```
Nel caso in cui su Windows desse problemi, modificare il file settings.py nel punto

> ```
> ALLOWED_HOSTS[]
> ```

in

> ```
> ALLOWED_HOSTS['*']
> ```

