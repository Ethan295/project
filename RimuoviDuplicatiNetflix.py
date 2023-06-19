import re

def extract_titles(filename):
    titles = set()
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            line = line.strip()
            if line:
                title = re.sub(r',"\d{2}\.\d{2}\.\d{2}"$', '', line)
                title = title.split(':')[0].strip()
                titles.add(title)
    
    return titles


def save_titles(titles, output_filename):
    with open(output_filename, 'w') as file:
        for title in titles:
            file.write(title + '\n')


def check_duplicates(existing_titles, new_titles):
    duplicates = []
    for title in new_titles:
        if title in existing_titles:
            duplicates.append(title)
    
    return duplicates


existing_titles_filename = 'AnimeList.txt'
input_filename = 'file.txt'
output_filename = 'file2.txt'

existing_titles = set()
with open(existing_titles_filename, 'r') as file:
    lines = file.readlines()
    for line in lines:
        title = line.strip()[2:]
        if title:
            existing_titles.add(title)

extracted_titles = extract_titles(input_filename)
new_titles = extracted_titles - existing_titles

duplicates = check_duplicates(existing_titles, new_titles)

save_titles(new_titles, output_filename)

print('Estrazione completata. I titoli unici sono stati salvati in', output_filename)

if duplicates:
    print('I seguenti titoli sono già presenti nella lista AnimeList.txt:')
    for duplicate in duplicates:
        print('- ' + duplicate)
