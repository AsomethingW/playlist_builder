playlists = ["Through the Wire", "Lay your head on my pillow", "RYD/Dark Red", "Spaceship", "Sweetest Taboo"]

print(playlists[0])
print(playlists[4])
print(playlists[-3])

for i in playlists:
    print(i)

playlists.append("Doomsday")
playlists.remove("Doomsday")
playlists.insert(1, "All caps")

(playlists[-1] == "Good Days")
