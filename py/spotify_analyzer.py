# spotify data analyzer
# asher
# 2024-01-16

import csv

# Create a function that searches through data
# Finds all songs from a given artist


def find_all_songs(artist: str) -> list:
    """Searches through a set of data and
    returns all songs found from a given artist

    Returns:
        list of found songs, an empty list if
        none are found
    """

    # Open the file
    with open("./spotify.csv") as f:
        # ----- Search for all artist's songs
        # ----- Use linear search
        # Create a csv reader object
        csv_reader = csv.DictReader(f)

        # Make a list to store all songs
        songs = []

        # Create a counter to store the current line number
        line_num = 0

        # For every line in the file
        for line in csv_reader:
            # If it's the first line, print out all the headings
            if line_num == 0:
                # print("The columns are: ")

                # Print on one line
                # print(", ".join(line))

                # Print one on every line
                # for item in line:
                #     print(item)

                line_num += 1
            else:
                # If the artist for this song is given artist
                # Store the song info in the list
                # ---- artist, song title, danceability
                if artist.lower() in line["artist"].lower():
                    songs.append(
                        (
                            line["artist"],
                            line["song_title"],
                            line["valence"],
                            line["danceability"],
                        )
                    )
                line_num += 1

        return songs


drake_songs = find_all_songs("drake")
ed_sheeran_songs = find_all_songs("ed sheeran")
kendrick_songs = find_all_songs("kendrick")

# Print only the drake songs
# that have a danceability of .5 or higher

# for song in kendrick_songs:
#     if float(song[-1]) >= 0.5:
#         print(song)

# Right now our songs have three pieces of info:
#    - artist
#    - song title
#    - danceability
# Can you add one more piece of info for every song:
#    - valence
# Right now: ('artist', 'song_title', 'danceability')
# Change: ('artist', 'song_title', 'valence', 'danceability')

# --- Sort using SELECTION sort from smallest to biggest
#     - Danceability

# Starting at the beginning of the list until the end
for i, song in enumerate(drake_songs):
    # Set the current item to the smallest danceability
    smallest_danceability = song[-1]
    smallest_idx = i

    # For the rest of the list
    for j in range(i + 1, len(drake_songs)):
        # If the current item is smaller than smallest
        if drake_songs[j][-1] < smallest_danceability:
            # Set the smallest danceability to the current
            smallest_danceability = drake_songs[j][-1]
            smallest_idx = j

    # Swap the smallest danceability with the current item
    drake_songs[i], drake_songs[smallest_idx] = (
        drake_songs[smallest_idx],
        drake_songs[i],
    )

for song in drake_songs:
    print(song)

# Can you modify the code so that it sorts from biggest to smallest
