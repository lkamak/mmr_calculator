import requests
import json
from riotwatcher import LolWatcher, ApiError
from riot_api_config import *

summoner_name = "LongandGirthy"

lol_watcher = LolWatcher(API_KEY)
region = "na1"

me = lol_watcher.summoner.by_name(region, summoner_name)
print(me)