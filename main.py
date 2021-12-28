from bs4 import BeautifulSoup
import requests
import shutil
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json
from pprint import pprint

chrome_driver_path = "/Users/curlos/Desktop/Development/chromedriver"

def get_all_character_urls(url):
  page = requests.get(url)
  soup = BeautifulSoup(page.content, 'html.parser')
  character_url_elems = soup.select('table .wikitable a[title*="SSBU"]')

  all_character_urls = []

  for character_url_elem in character_url_elems:
    character_url = 'https://www.ssbwiki.com' + character_url_elem['href']
    
    if (character_url not in all_character_urls):
      all_character_urls.append(character_url)
  
  print(all_character_urls)


def save_to_json(dictionary, filename):
  print('Exporting dictionary to JSON file...')

  try:
    with open(filename, "w") as outputFile:
      json.dump(dictionary, outputFile, indent=4)
  except:
    print('Error occured!')

  print('JSON file created!')


get_all_character_urls('https://www.ssbwiki.com/Super_Smash_Bros._Ultimate')