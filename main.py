import bs4
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
import asyncio
ua = UserAgent()
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("user-agent="+ua.random)
driver = webdriver.Chrome(options=options)
driver.get(f"https://discord.gg/")
