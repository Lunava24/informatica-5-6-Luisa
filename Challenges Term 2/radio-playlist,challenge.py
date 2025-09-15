weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
print(weekly_playlist)

weekly_playlist.append("Drivers License")
weekly_playlist.insert(0,"Bohemian Rhapsody")
weekly_playlist.remove("Good 4 u")
print(weekly_playlist.index("Levitating"))
print(weekly_playlist.count("As it was"))
weekly_playlist.reverse()
print(weekly_playlist)
weekly_playlist.sort()
print(len(weekly_playlist))

weekly_playlist = ["Blinding Lights", "Levitating", "As It Was", "Heat Waves", "Good 4 u"]
original = weekly_playlist[:]
songs = 0

while True:
    songs += 1
    first = weekly_playlist.pop(0)
    weekly_playlist.append(first)
    if len(weekly_playlist) >= 2:
        weekly_playlist[0], weekly_playlist[1] = weekly_playlist[1], weekly_playlist[0]
        print(f"song {songs}: {weekly_playlist}")
    if weekly_playlist == original:
        print("\nPlaylist returned ro original!")
        print(f"Total songs: {songs}")
        break    