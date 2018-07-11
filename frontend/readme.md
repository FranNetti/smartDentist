# Folder del programma con cui si potrà interagire dai dispositivi con il backend

### Personalizzazione del sistema

Il sistema può avere un numero variabile di forni che invieranno con una certa frequenza i dati con un proprio codice identificativo.
Per modificare il numero di forni aprire il file docker-compose.yml e aggiungere tanti servizi uguali a forn1, modificando opportunatamente il numero del servizio per non avere servizi con nomi uguali; è possibile inoltre personalizzare la frequenza di invio dei dati andando a modificare il parametro passato nella riga

> command: python3 app/smartDentistForno/smartDentistForno.py <<inserire il numero di minuti voluti>>

In base all'indirizzo Ip del server di backend modificare anche la riga:

> command: python3 app/smartDentistBroker/smartDentistBroker.py <<inserire l'indirizzo IP>>

oltre che a modificarlo all'interno del file app/smartDentistFornoHttp/index.html nell'action della form

### Esecuzione del sistema

Per fare partire il sistema, digitare

```
docker-compose up (aggiungere -d se non si vogliono vedere i risultati intermedi)
```

se si vuole far partire la pagina html bisogna collegarsi al seguente indirizzo:

http://aaa:8080  dove aaa sta ad indicare l'indirizzo del container in cui ci troviamo ora