# Folder del programma con cui si potrà interagire dai dispositivi con il backend

### Personalizzazione del sistema

Il sistema può avere un numero variabile di forni che invieranno con una certa frequenza i dati con un proprio codice identificativo.
Per modificare il numero di forni aprire il file docker-compose.yml e aggiungere tanti servizi uguali a forn1, modificando opportunatamente il numero del servizio per non avere servizi con nomi uguali; è possibile inoltre personalizzare la frequenza di invio dei dati andando a modificare il parametro passato nella riga

> command: python3 app/smartDentistForno/smartDentistForno.py <<inserire il numero di minuti voluti>>

### Esecuzione del sistema

Per fare partire il sistema, digitare

```
docker-compose up
```

se si vuole far partire la pagina html bisogna collegarsi al seguente indirizzo:

http://192.168.99.100:8080