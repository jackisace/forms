#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup
import sys
import argparse



parser = argparse.ArgumentParser(prog='forms', description='finds all forms, automates posting', epilog='Good luck!')          
                                                                                                                               
parser.add_argument('target', help="target page to parse eg: 'index.html' or 'http://10.10.10.10/index.html'")                 
parser.add_argument('-f', '--form', help="specify the form number if there are multiple forms on a page")                      
parser.add_argument('-a', '--auto', help="specify all variables via the command line, eg: 'username=admin,password=P@$$w0rd'") 
parser.add_argument('-m', '--manual', action='store_true', help="step through each of the variables manually")                 
parser.add_argument('-v', '--verbose', action='store_true', help="print each result")                                          
                                                                                                                               
                                                                                                                               
args = parser.parse_args()                                                                                                     







r = requests.get(args.target)

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







