# Folder del programma backend

## Prerequisito
Se è la prima volta che si sta entrando nella cartella e si deve ancora effettuare il setup, digitare

```
docker-compose build
```

Per creare la tabella del database dal relativo modello presente in models.py digitare il seguente comando:

```
docker-compose run web python app/manage.py migrate
```

Ad ogni modifica dentro al file prima nominato,  prima digitare

```
docker-compose run web python app/manage.py makemigrations <<nome dell'app preso da apps.py>>
```

dopo di che digitare il primo comando di questo capitolo.

## Esecuzione del programma

Per fare partire il sistema, digitare

```
docker-compose up
```
Nel caso in cui su Windows desse problemi per il server web, modificare il file settings.py nel punto

```
ALLOWED_HOSTS[]
```

in

```
ALLOWED_HOSTS['*']
```



## Possibile errore con la java virtual machine

Se il programma richiede troppa memoria, fare le seguenti operazioni:

### Windows

Collegarsi alla docker machine con

```
docker-machine ssh
```

dopo di che inserire il seguente comando

```
sudo sysctl -w vm.max_map_count=262144
```

### Linux

Eseguire direttamente il secondo comando nella sezione windows
Se non si vuole eseguire il comando ad ogni accensione del computer, in questo caso si può andare ad inserire la costante all'interno del file /etc/sysctl.config per averlo permanentemente
