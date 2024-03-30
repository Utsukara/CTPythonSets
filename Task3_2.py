
# Task 2: Genre Sorting
# You have a list of genres associated with each artist. 
# Using a loop with sets, categorize artists by their genres, creating a set for each genre.

# Example Code:

artists_genres = {
    "The Lumineers": "Folk",
    "Tame Impala": "Psychedelic Rock",
    "Billie Eilish": "Pop",
    "Arctic Monkeys": "Indie Rock",
    "Dua Lipa": "Pop"
}

# Expected Outcome:
# A categorization of artists by genres, such as Genre: Folk, Artists: The Lumineers

genre_sets = {}
for artist, genre in artists_genres.items():
    if genre not in genre_sets:
        genre_sets[genre] = set()
    genre_sets[genre].add(artist)

for genre, artists in genre_sets.items():
    print("Genre:", genre, "Artists:", artists)