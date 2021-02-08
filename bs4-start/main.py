import requests
from bs4 import BeautifulSoup

URL = "https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text
soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in all_movies]
#for n in range(len(movie_titles) -1, -1, -1):
   # print(movie_titles[n])
movies = movie_titles[::-1]

with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


#URL = "https://www.billboard.com/charts/hot-100/"

#question = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:")
#response = requests.get(URL + question)
#song_website = response.text

#soup = BeautifulSoup(song_website, "html.parser")
#all_songs = soup.find_all(name="span", class_="chart-element__information__song text--truncate color--primary")

#song_names = [song.getText() for song in all_songs]
#songs = song_names[::-1]

#with open("songs.txt", mode="w") as file:
 #   for song in songs:
  #      file.write(f"{song}\n")









#response = requests.get("https://news.ycombinator.com/news")
#yo_web_page = response.text

#soup = BeautifulSoup(yo_web_page, "html.parser")

#articles = soup.find_all(name="a", class_="storylink")
#for article_tag in articles:
 #   article_text = article_tag.getText()
  #  article_link = article_tag.get("href")
#article_upvote = soup.find_all(name="span", class_="score").getText()

#print(article_text)
#print(article_link)
#print(article_upvote)







#import lxml

#with open("website.html", encoding="utf8") as file:
    #contents = file.read()

#soup = BeautifulSoup(contents, "html.parser")
#print(soup.title)
#print(soup.title.name)
#print(soup.title.string)
#print(soup.prettify())
#print(soup.p)

#all_anchor_tags = soup.find_all(name="a")
#for tag in all_anchor_tags:
    #print(tag.getText())
    #print(tag.get("href"))


#heading = soup.find(name="h1", id="name")
#print(heading)

#section_heading = soup.find(name="h3", class_="heading")
#print(section_heading)

#company_url = soup.select_one(selector="p a")
#print(company_url)