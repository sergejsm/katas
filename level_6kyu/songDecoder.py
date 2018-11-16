# My solution, also Best solution
def song_decoder(song):
    return ' '.join(song.replace('WUB'," ").split())


print(song_decoder("AWUBBWUBC"))
print(song_decoder("AWUBWUBWUBBWUBWUBWUBC"))