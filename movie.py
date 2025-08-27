a_watched_movies = {"Inception", "Titanic", "The Matrix", "Interstellar", "The Dark Knight"}
b_watched_movies = {"The Matrix", "Interstellar", "Avatar", "Gladiator", "The Godfather"}
common_movies = a_watched_movies & b_watched_movies
unique_to_user_a = a_watched_movies - b_watched_movies
suggested_for_user_a =a_watched_movies - b_watched_movies
print(" Movies both users have watched:", common_movies)
print(" Movies unique to User A:", unique_to_user_a)
print("Suggested movies for User A:", suggested_for_user_a)
