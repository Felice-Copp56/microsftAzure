# Paddock Passione F1 function App 
## Introduzione

L'obiettivo di questa funzione è quello di ottenere informazioni da un sito web (motorsport.it) in relazione alle ultime notizie pubblicate, ottenerle ed inviare i link tramite messaggi su un canale Telegram **Paddock Passione F1**

## Funzionalità

La Function App svolge le seguenti attività:

1. **Ottenimento di Informazioni:**
   - Utilizza librerie Python come `requests` o `BeautifulSoup` per effettuare una richiesta HTTP al sito web di destinazione.
   - Esegue lo scraping o analizza il contenuto HTML per ottenere le informazioni desiderate.

2. **Invio di Messaggi su Telegram:**
   - Utilizza il modulo `python-telegram-bot` per inviare messaggi a un canale o a un utente su Telegram.
   - Configura e utilizza il token del bot Telegram per l'autenticazione.

3. **Trigger di Timer:**
   - La Function App è configurata con un trigger di tipo timer, che consente l'esecuzione periodica delle operazioni.Il timer è stato settato in maniera tale da chiamare la funzione ad intervalli di un'ora dalle 8 del mattino alle 22 di sera.
4. **CosmosDB:**
   - La Function App sarà collegata ad un database CosmosDB per il salvataggio delle informazioni ottenute dal sito web di destinazione, in questo modo prima della pubblicazione verranno scartate le notizie già pubblicate. Definito meccanismo di pulizia del file/tabella che si occuperà di contenere i dati.

## Configurazione
Prima di deployare e eseguire la Function App, segui questi passaggi:

1. **Creazione della Function App su Azure:**
   - Crea una nuova Function App su [Azure Portal](https://portal.azure.com/).

2. **Configurazione delle Variabili d'Ambiente:**
   - Configura le variabili d'ambiente necessarie, come il token del bot Telegram e altre informazioni sensibili.

3. **Deploy della Function App:**
   - Utilizza gli strumenti di deployment di Azure, ad esempio Azure CLI o GitHub Actions, per deployare la Function App.

4. **Configurazione del Trigger di Timer:**
   - Configura il trigger di tipo timer per specificare l'intervallo di esecuzione.

## Esecuzione Localemente (Opzionale)

Se desideri eseguire la Function App localmente per sviluppo o test, segui questi passaggi:

1. **Installazione delle Dipendenze:**
   - Installa le dipendenze Python specificate nel file `requirements.txt`.

2. **Configurazione delle Variabili d'Ambiente Locali:**
   - Crea un file `.env` con le variabili d'ambiente locali necessarie.

3. **Esecuzione Locale:**
   - Esegui la Function App localmente utilizzando strumenti come Azure Functions Core Tools.

## Documentazione Aggiuntiva


Per ulteriori dettagli sulla configurazione, l'utilizzo e la personalizzazione, consulta la documentazione aggiuntiva nella cartella `docs`.

## Contatti

Per domande, segnalazioni di bug o contributi, contatta l'autore della Function App tramite l'indirizzo email o il profilo GitHub indicato nel file `CONTRIBUTING.md`.

## Next Steps....
