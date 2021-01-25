from selenium import webdriver
import pickle
#pip install pickle-mixin
import time
#import mysql.connector
import sqlite3
#import util
import os
import asyncio
import sys

try:
  import discord
except ImportError:
  print ("Trying to Install required module: discord\n")
  os.system('py -3 -m pip install -U discord.py')
import discord
from datetime import datetime



driver = webdriver.Chrome()
driver.get('https://grafana.com/login?to=%2Foauth2%2Fauthorize%3Faccess_type%3Donline%26client_id%3Dca2e8a4986cf1145fec8%26redirect_uri%3Dhttps%253A%252F%252Fserverino.grafana.net%252Flogin%252Fgrafana_com%26response_type%3Dcode%26scope%3Duser%253Aemail%26state%3D_n_IPbyzauAwjZDsbV9VjCpi1DwiTnb-D-4yJ6UKcoU%253D')
driver.find_element_by_name("login").send_keys("serverinoguest")
driver.find_element_by_name("password").send_keys("Guest01")

button = driver.find_element_by_class_name("btn--large").click()
time.sleep(3)
driver.get("https://serverino.grafana.net/")
driver.find_element_by_class_name("btn-service--grafanacom").click()
time.sleep(3)
driver.get("https://serverino.grafana.net/render/d-solo/d6qG8JBMk/serverino-geral?orgId=1&from=1595688992768&to=1611586592768&panelId=6&width=1000&height=500&tz=America%2FSao_Paulo")
time.sleep(3)
driver.save_screenshot("img.png")






client = discord.Client()

async def on_ready():
  await client.wait_until_ready()
  barraco = client.get_channel(681516891113521235)
  await barraco.send("Vips Restantes")
  await barraco.send(file=discord.File('img.png'))
  #await client.get_channel(681516891113521235).send("Vips Restantes")
  #await client.get_channel(681516891113521235).send(file=discord.File('img.png'))
  conselho = client.get_channel(287685479057588225)
  await conselho.send("Vips Restantes")
  await conselho.send(file=discord.File('img.png'))
  #await client.get_channel(287685479057588225).send("Vips Restantes")
  #await client.get_channel(287685479057588225).send(file=discord.File('img.png'))
  driver.close()
  sys.exit()
  quit()


client.loop.create_task(on_ready())
client.run('')


