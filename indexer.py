# pip install -r requirements.txt
# Zbuduj system składający się z indeksera dokumentów oraz wyszukiwarki (2 programy).

# Indekser:
# - przydziela unikatowy identyfikator każdemu z dokumentów,
# - przetwarza dokument na reprezentację dokumentu -  słownik częstości tokenów występujących w dokumencie (tf-idf),
#   * wybrane słowa/tokeny są pomijane.
# - zapisuje identyfikator, ścieżkę do pliku oraz reprezentację do bazy danych.

# Wyszukiwarka:
# - przetwarza zapytanie na odpowiadające tokeny
#   * wybrane słowa/tokeny są pomijane.
# - dla wybranego zapytania zwraca posortowaną listę identyfikatorów dokumentów wraz z odpowiednimi ścieżkami
#   * f. podobieństwa pomiędzy zapytaniem a reprezentacją dokumentu - podobieństwo cosinusowe (wymienna na inną)

