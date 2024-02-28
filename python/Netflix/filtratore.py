import csv

def process_netflix_history(input_file, output_file):
    seen_titles = set()

    with open(input_file, 'r', encoding='utf-8') as input_f, open(output_file, 'w', encoding='utf-8') as output_f:
        # Scrivi l'intestazione nel file di output
        output_f.write("Title\n")

        # Leggi il file CSV
        csv_reader = csv.reader(input_f)

        # Ignora l'intestazione
        next(csv_reader)

        # Scansiona il file CSV riga per riga
        for row in csv_reader:
            # Estrai il titolo dalla riga e prendi solo le parole prima dei due punti
            title = row[0].strip().split(':')[0].strip()

            # Verifica se il titolo è già stato visto
            if title not in seen_titles:
                # Scrivi il titolo nel file di output
                output_f.write(f'"{title}"\n')

                # Aggiungi il titolo all'insieme dei titoli già visti
                seen_titles.add(title)

# Chiamata alla funzione con i nomi dei file di input e output
process_netflix_history("C:\\Users\\eindemini\\Pictures\\python\\project\\python\\Netflix\\NetflixViewingHistory.csv", "C:\\Users\\eindemini\\Pictures\\python\\project\\python\\Netflix\\output.txt")
