
# Task 1: Artist Lineup Compilation
# You are provided with a list of artist names scheduled to perform at different stages of the music 
# festival. Using a loop, compile these artist names into a set to create a unique lineup without 
# duplicates.

# Example Code:

artist_names = ["The Lumineers", "Tame Impala", "Billie Eilish", "The Lumineers", "Arctic Monkeys", "Tame Impala"]
unique_artists = set()

# Expected Outcome:
# A set containing unique artist names, such as {'The Lumineers', 'Tame Impala', 'Billie Eilish', 'Arctic Monkeys'}.

for artist in artist_names:
    unique_artists.add(artist)

print(unique_artists)