import json

movie2 = {}
movie2["title"] = "Minority Report"
movie2["director"] = "Steven Spielberg"
movie2["actors"] = ["Tom Cruise", "Colin Farrel", "Samantha Morton", "Max von Sydow"]
movie2["is_awesome"] = True
movie2["budget"] = 102000000
movie2["cinematographer"] = "Janusz Kami\u0144ski"

file2 = open("N:/Git/codewars/movie_2.txt", "w", encoding="utf-8")
json.dump(movie2, file2, ensure_ascii=False) #by default ensure_ascii==True
file2.close()

