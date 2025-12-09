watchlist = []

def add_to_watchlist(movie):
    watchlist.append(movie)

def get_watchlist():
    return watchlist

def get_average_rating():
    if not watchlist:
        return 0
    return sum(m["vote_average"] for m in watchlist) / len(watchlist)

def most_common_genre():
    genre_count = {}
    for m in watchlist:
        for g in m["genre_ids"]:
            genre_count[g] = genre_count.get(g, 0) + 1
    if not genre_count:
        return None
    return max(genre_count, key=genre_count.get)
