import csv
import numpy as np
import matplotlib.pyplot as plt

try:
    with open('Dati1.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)

        if len(rows) == 0:
            print("Il file CSV è vuoto.")
        else:
            col_index = 0

            if col_index < 0 or col_index >= len(rows[0]):
                print("Indice di colonna non valido.")
            else:
                # Estrai la colonna specificata
                column = [float(row[col_index]) for row in rows[1:]]  # Ignora la prima riga (intestazione)

                # Calcola la trasformata di Fourier
                fft_result = np.fft.fft(column)
                freq = np.fft.fftfreq(len(column))
                #for freq1,amp1 in zip(freq,np.abs(fft_result)):
                #    print(freq1,amp1)

                plt.plot(freq, np.abs(fft_result))
                plt.title("Spettro di Ampiezza - Teorema di Fourier")
                plt.xlabel("Frequenza")
                plt.ylabel("Ampiezza")
                plt.show()

except FileNotFoundError:
    print("Il file CSV non è stato trovato.")
except csv.Error as e:
    print(f"Errore durante la lettura del file CSV: {e}")
