from bs4 import BeautifulSoup
import requests

# # to prevent frequent requests, save the response to web.txt
# response = requests.get(
#     "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
# with open("web.txt", "w") as file:
#     file.write(response.text)

with open("web.txt") as file:
    movie_webpage = file.read()

soup = BeautifulSoup(movie_webpage, "html.parser")
# find all the movies
movie_titles = soup.find_all(name="h3", class_="title")
# format the movies
movie_titles = [movie.getText() for movie in movie_titles]


# swap the orders of the list
def reverse_list(movie_list):
    n = len(movie_list)
    i = 0
    for i in range(n // 2):
        movie_list[i], movie_list[n - i - 1] = movie_list[n - i - 1], movie_list[i]
    return movie_list


movie_titles = reverse_list(movie_titles)
# format the list to str
movie_str = "\n".join(movie_titles)
# save the list to txt
with open("movie_100.txt", "w") as file:
    file.write(movie_str)