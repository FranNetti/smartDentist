# Folder del programma backend

## Prerequisito

Se nella cartella non sono presenti il file manage.py e la cartella smartDentist, digitare

```
docker-compose run web django-admin.py startproject smartDentist .
```

## Esecuzione del programma

Per fare partire il sistema, digitare

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



## Interazione con il db

Per creare la tabella del database dal relativo modello presente in models.py digitare il seguente comando:

```
docker-compose run web python app/manage.py migrate
```

Ad ogni modifica dentro al file prima nominato,  prima digitare

```
docker-compose run web python app/manage.py makemigrations <<nome dell'app preso da apps.py>>
```

dopo di che digitare il primo comando di questo capitolo.