class Movie:
    id_counter: int = 0

    def __init__(self, title: str, rating: float):
        Movie.id_counter += 1
        self.title = title
        self.rating = rating
        self.id = Movie.id_counter


mov1 = Movie("Merlin", 4.6)
mov2 = Movie("Legend of the seeker", 4.2)

print("[ID] Movie 1:", mov1.id)
print("[ID] Movie 2:", mov2.id)
