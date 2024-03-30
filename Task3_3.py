
# Task 3: Playlist Duplication Check
# Create a Python script that takes multiple playlist sets and checks if any playlist is a duplicate 
# of another (i.e., contains the same set of songs).

# Example Code:

playlist1 = {"Song A", "Song B", "Song C"}
playlist2 = {"Song D", "Song E", "Song F"}
playlist3 = {"Song A", "Song B", "Song C"}

playlists = [playlist1, playlist2, playlist3]

# Expected Outcome:
# A confirmation of whether there are duplicate playlists, such as Duplicate playlists found: True.

def check_duplicate_playlists(playlists):
    unique_playlists = set()
    for playlist in playlists:
        if frozenset(playlist) in unique_playlists:
            return True
        unique_playlists.add(frozenset(playlist))
    return False

duplicate_playlists_found = check_duplicate_playlists(playlists)
print("Duplicate playlists found:", duplicate_playlists_found)