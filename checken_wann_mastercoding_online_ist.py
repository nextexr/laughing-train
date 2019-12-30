from bs4 import BeautifulSoup
import cfscrape
import re
from time import gmtime, strftime, sleep
from datetime import datetime

# SETUP:
# python3,
# sudo pip3 install cfscrape beautifulsoup4

looped = 0;

scores_before = []

game_modes = [
            "TTT", "TTT", "TTT", "TTT",
            "SG", "SG", "SG", "SG",
            "EG", "EG", "EG",
            "SW", "SW", "SW",
            "QSG", "QSG", "QSG", "QSG",
            "BW", "BW", "BW", "BW", "BW",
            "CORES", "CORES", "CORES",
            "GUNGAME",
            "UHC", "UHC", "UHC", "UHC",
            "COOKIES", "COOKIES",
            "MASTERBUILDERS", "MASTERBUILDERS", "MASTERBUILDERS",
            "HARDCORE", "HARDCORE",
            "SG_1.14", "SG_1.14", "SG_1.14", "SG_1.14"
        ]

print("Mastercoding online tracker v1")

while True:
    url = "https://www.gommehd.net/player/index?playerName=Mastercoding"

    scores_after = []

    scraper = cfscrape.create_scraper()

    content = scraper.get(url).content
    soup = BeautifulSoup(content, features="lxml")
    scores_raw = soup.findAll("span", {"class": "score"});
    for score_raw in scores_raw:
        scores_after.append(int(score_raw.text));

    try:
        if not looped == 0:
            for i in range(0, 41):
                if not scores_before[i] == scores_after[i]:
                    print("Mastercoding hat um " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " " + str(game_modes[i]) + " gespielt!  (" + str(scores_before[i]) + " vs " + str(scores_after[i]) + ")" + "\r\n")
                    file = open("index.html","a")
                    file.write("Mastercoding hat um " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + " " + str(game_modes[i]) + " gespielt!  (" + str(scores_before[i]) + " vs " + str(scores_after[i]) + ")" + "\r\n")
                    file.close()

    except IndexError:
        print("Request failed. -- " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\r\n")
        file = open("index.html","a")
        file.write("Request failed. -- " + strftime("%Y-%m-%d %H:%M:%S", gmtime()) + "\r\n")
        file.close()

    scores_before = scores_after

    looped += 1
    sleep(60);
