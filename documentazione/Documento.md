Data: 03/05/2018		09.00 - 12.30
Data: 07/05/2018		15.30 - 18.30
Data: 08/05/2018 	09.00 - 12.30 | 14.15 - 18.15
Data: 15/05/2018		09.00 - 12.30 | 14.15 - 18.15
Data: 21/05/2018 	15.00 - 18.30

## Descrizione del problema

È stato richiesto di installare in un forno per dentisti un dispositivo che permetta la sua geolocalizzazione ogni qual volta questo venga acceso.

Un forno per dentisti è un macchinario che permette di riscaldare a temperature elevate, intorno ai 1300/1600 °C, dei materiali ceramici, permettendo la realizzazione di qualunque tipo di oggetto utile per lo svolgimento del lavoro di un dentista, come protesi, corone, ponti e molto altro. I prezzi variano in base alle dimensioni; per forni ben realizzati e di grosse dimensioni il costo è intorno ai 2000€.

Dato che per dover comunicare la propria posizione il dispositivo deve essere in qualche modo collegato ad una rete internet (questo argomento verrà trattato meglio più avanti) si potrebbe sfruttare l'occasione per renderlo più smart, inviando anche dati di utilità come temperatura di utilizzo, tempo impiegato per la cottura insieme ad altri dati in modo tale da poter tenere sotto controllo il macchinario e utilizzare questi dati sotto numerosi campi:

- da parte del costruttore per sapere cosa migliorare nelle successive versioni grazie a problematiche che si verificano frequentemente in una certa zona o sotto certe condizioni di utilizzo
- da parte del consumatore per notare in anticipo possibili rotture e anticipare così la manutenzione, in modo tale da non rovinare il macchinario e poterlo usare più a lungo

##  Primo approccio al problema

### Analisi del forno

#### 1. Connessione alla rete

Il primo aspetto da affrontare riguarda l'ottenimento della connessione ad internet del dispositivo, aspetto fondamentale per poter poi comunicare qualunque tipo di dato necessario.
La connessione può essere ottenuta fisicamente, attraverso quindi l'installazione di una scheda di rete con relativa porta a cui connettere il cavo, e in aggiunta in modalità wireless, per rendere meno invasivo il dispositivo senza dover per forza utilizzare un cavo per la connessione. 
Non è detto che la connessione sia direttamente disponibile al forno stesso, infatti può presentare un modulo Bluetooth che gli permette di collegarsi alla rete tramite un gateway di un qualsiasi tipo (per esempio un dispositivo mobile).

#### 2. Ottenimento della posizione

Per poter ottenere la posizione del dispositivo si possono utilizzare tre metodi, a seconda della disponibilità della rete oppure dell'interfacciamento diretto con l'utente:

1. tramite installazione di un dispositivo GPS che permette la localizzazione del dispositivo attraverso longitudine e latitudine.
2. tramite le informazioni di geolocalizzazione ottenute tramite le rete wireless stessa; questo è possibile solamente se è disponibile una rete WiFi, inoltre è anche da considerarare come l'informazione ottenuta non è sempre precisa quanto quella ottenuta dal metodo 1.
3. tramite la richiesta e la consecutiva risposta da parte dell'utente stesso.

#### 3. Entità software presenti

Il software all'interno dei forni deve essere sviluppato in due moduli: un modulo che si occupa della raccolta delle informazioni, in questo caso la posizione, e un modulo che invece deve inviare i dati alla unità di memorizzazione tramite la rete. Non è detto che entrambi questi moduli debbano essere presenti all'interno del forno, si possono presentare le seguenti combinazioni:

- entrambi i moduli presenti sul forno

- modulo software per la raccolta dei dati tramite il gps presente sul forno + modulo software per l'invio dei dati su un gateway esterno collegato al forno tramite Bluetooth
- modulo software per la raccolta dei dati presente su un terminale collegato al forno tramite Bluetooth + modulo software per l'invio dei dati presente sul forno
- entrambi i moduli presenti all'esterno del forno stesso, in questo caso la connessione con il forno serve principalmente per ottenere un identificativo utile a riconoscere il forno.

![immagine forno1](./immagini/forno1.png)

---

![immagine forno 2](./immagini/forno2.png)

---

![immagine forno 3](./immagini/forno3.png)

---

![immagine forno 4](./immagini/forno4.png)

---

![immagine forno 5](./immagini/forno5.png)



### Connessione fra l'entità composta forno e lato cliente

Una volta ottenuta la posizione in uno qualsiasi dei precedenti metodi, sarà compito del dispositivo comunicare i dati con una struttura apposita.

![struttura client-server](./immagini/client-server.png)

---

![struttura pub-sub](./immagini/pub-sub.png)

---

![struttura client-server con l'ausilio di una webApp](./immagini/webapp.png)





### Differenze fra database relazionali e database NoSql

|                        |                        Db relazionali                        |                           NoSql db                           |
| ---------------------- | :----------------------------------------------------------: | :----------------------------------------------------------: |
| Relazioni              | Le relazioni fra i vari elementi sono presenti e sono l'elemento caratterizzante del sistema; tutti i dati hanno la stessa struttura | Le relazioni possono essere presenti, ma non sono il punto centrale del database in quanto gli elementi possono anche non avere nulla in comune dal punto di vista della struttura interna |
| Struttura              |                          Verticale                           |                         Orizzontale                          |
| Scalabilità            |         Poca, dovuta al tipo di struttura impiegata          |                           Elevata                            |
| Disponibilità dei dati |                   I dati sono disponibili                    | Elevata, è un aspetto principale su cui si basano questi tipi di database |
| Consistenza dei dati   |                I dati sono sempre consistenti                | Presente ma meno rispetto a quelli relazionali, in questo caso si parla di "Eventuale consistenza": i dati che si leggono in un determinato istante non è detto che siano aggiornati all'ultima versione presente nel database |

## Sviluppo del sistema

Scegliamo come piattaforma di sviluppo OpenShift, un Platform as a Service per applicazioni cloud, in modo tale da poterci concentrare principalmente sullo sviluppo della applicazione, demandando alla piattaforma stessa tutto ciò che riguarda l'ambito di amministrazione del sistema. Come database per il sistema si usa un database noSql, MongoDb.

### Costruzione del database









































---

## Malacopia

all'interno della quale verranno memorizzati i dati: questa struttura potrebbe essere un database distribuito che memorizzerà l'identificativo della macchina, la sua posizione e data e ora della ricezione dei dati così da sapere quando e dove è stato attivato l'ultima volta.

Sarà poi l'utente ad interfacciarsi con questo database attraverso una applicazione web o addirittura un'applicazione mobile per poter filtrare il determinato macchinario e sapere tutti i vari spostamenti che questo ha effettuato ultimamente o in un dato periodo di tempo.

![Possibile diagramma casi d'uso del sistema](./immagini/UseCaseDiagram1.png)

### Architettura pub-sub[^1]

È comoda perchè permette di realizzare un'architettura scalabile e indipendente dal tipo di problema che si sta affrontando.

Pro per il sistema attuale:

- è scalabile, perciò è indipendente dal numero di forni che si possono collegare al sistema e di conseguenza usare per ricevere informazioni.
- interpone tra i forni e il database una struttura ulteriore, che permette al database di non ricevere informazioni contemporaneamente e creare quindi condizioni di corsa critica nella scrittura
- in caso di più informazioni inviate dai forni, grazie al concetto intrinseco dell'architettura si potrebbero filtrare le informazioni da memorizzare su diversi database in base al contenuto senza che i forni debbano conoscere la differenza fra un database che contenga solo dati di log e un altro dove vengono memorizzate le informazioni di utilità. Sempre grazie a questo principio di intermediario si dà la possibilità di ottenere informazioni dai forni anche nel caso in cui per una serie di operazioni di mantenimento i database si dovessero scollegare dal sistema per un periodo di tempo
- permetterebbe di poter considerare un messaggio di log contemporaneamente come due informazioni distinte: sia come nuovo dato da aggiungere al database per aggiornarne l'history, sia per notificare un certo utente, il quale ha deciso di essere notificato, che il forno è stato accesso e renderlo partecipe con poco ritardo e in maniera dinamica, senza che questo si debba per forza collegare ad un sito e verificare i log passati

Contro:

- si va ad aggiungere al sistema un'architettura non necessaria per la natura del problema allo stato attuale
- si potrebbe causare un certo ritardo nella memorizzazione delle informazioni

Per mantenere una certa astrazione del sistema, la modalità migliore adatta a questo caso è quella type-based.

[^1]: L'argomento è stato analizzato con il documento reperito [a questo indirizzo](https://infoscience.epfl.ch/record/165428/files/10.1.1.10.1076.pdf)