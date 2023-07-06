**# AstroPi-frequencies_project

## Descrizione

Il progetto AstroPi è una collaborazione tra l'ESA (Agenzia Spaziale Europea) e la Raspberry Pi Foundation che permette agli studenti di condurre esperimenti scientifici e scrivere codice Python che viene eseguito sui computer Raspberry Pi a bordo della Stazione Spaziale Internazionale (ISS).

Questo progetto specifico mira a esplorare le variazioni di accelerazione tramite l'utilizzo di un Raspberry Pi e un Sensore di Ambienti elettronico (Sense HAT). Il codice Python sviluppato sfrutta i pixel del Sense HAT per creare tre grafici distinti basati sulle variazioni di accelerazione sugli assi x, y e z.

Successivamente, è stato sviluppato un secondo codice Python che analizza i dati ottenuti utilizzando la trasformata di Fourier. Questa analisi permette di identificare le frequenze dominanti nelle variazioni di accelerazione rilevate durante il funzionamento di un motore.

## Obiettivi

Gli obiettivi principali di questo progetto specifico includono:

1. **Studio delle variazioni di accelerazione**: Esplorare le variazioni di accelerazione negli assi x, y e z utilizzando il Raspberry Pi e il Sense HAT.

2. **Creazione di grafici**: Utilizzare i pixel del Sense HAT per creare grafici che rappresentano le variazioni di accelerazione rilevate.

3. **Analisi delle frequenze**: Utilizzare la trasformata di Fourier per analizzare i dati raccolti e identificare le frequenze dominanti nelle variazioni di accelerazione.

4. **Relazione con l'accensione del motore**: Determinare se esistono correlazioni tra le frequenze dominanti rilevate e l'accensione del motore.

## Hardware utilizzato

Per realizzare questo progetto, sono stati utilizzati i seguenti componenti hardware:

- **Raspberry Pi**: Un computer a basso costo e dalle dimensioni ridotte, dotato di potenza di calcolo e di interfaccia GPIO (General Purpose Input/Output) che permette di collegare sensori e altri dispositivi elettronici.

- **Sense HAT**: Una scheda di espansione progettata specificamente per il Raspberry Pi, che fornisce sensori di temperatura, umidità, pressione, nonché un accelerometro e un giroscopio. Il Sense HAT include anche un display a matrice di LED e un joystick per l'interazione utente.

## Esecuzione del Codice

Per eseguire il codice sviluppato, seguire i seguenti passaggi:

1. Assicurarsi che il Raspberry Pi sia correttamente collegato al Sense HAT.

2. Installare la libreria Python necessaria per l'utilizzo del Sense HAT eseguendo il seguente comando:

```bash
pip install sense-hat
```

3. Copiare il codice Python fornito nel proprio ambiente di sviluppo o editor di testo preferito.

4. Salvare il file con un nome appropriato, ad esempio "accelerazione.py".

5. Eseguire il file Python utilizzando il seguente comando:

```bash
python accelerazione.py
```

6. Osservare i grafici generati dai pixel del Sense HAT che rappresentano le variazioni di accelerazione sugli assi x, y e z.

7. Successivamente, eseguire il secondo codice Python fornito per analizzare i dati utilizzando la trasformata di Fourier. Salvare il file con un nome appropriato, ad esempio "analisi_frequenze.py", e utilizzare il comando precedente per eseguire il file.

8. Analizzare i risultati ottenuti e verificare se esistono correlazioni tra le frequenze dominanti rilevate e l'accensione del motore.

## Conclusioni

Il progetto AstroPi - Analisi delle Variazioni di Accelerazione offre agli studenti l'opportunità di esplorare l'ambiente spaziale e applicare conoscenze di programmazione Python per analizzare dati scientifici. Questa esperienza permette di sviluppare competenze nel campo della scienza, della tecnologia, dell'ingegneria e della matematica (STEM) e di approfondire la comprensione delle applicazioni pratiche della programmazione nel contesto dell'esplorazione spaziale.
