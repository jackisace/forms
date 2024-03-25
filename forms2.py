#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys

r = requests.get(sys.argv[1])

soup = BeautifulSoup(r.content, "html.parser")

forms = soup.find_all("form")


for form in forms:
    action = form.get("action")
    print(f"action: {action}")
    inputs = form.find_all("input")
    for inp in inputs:
        name = inp.get("name")
        value = inp.get("value")
        print(f"{name}: {value}")








