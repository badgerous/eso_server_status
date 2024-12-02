import requests
from bs4 import BeautifulSoup
import threading

URL = "https://esoserverstatus.net/"

def get_status():
  r = requests.get(URL)
  parsed_r = BeautifulSoup(r.text)

  pc_eu_status = parsed_r.body.find("span", attrs={"id": "PC-EU"}).text
  pc_na_status = parsed_r.body.find("span", attrs={"id": "PC-NA"}).text
  pc_pts_status = parsed_r.body.find("span", attrs={"id": "PC-PTS"}).text

  print("PC EU Server: " + pc_eu_status)

def start():
  thread = threading.Timer(3.0, start)
  thread.start()
  get_status()
  
start()
