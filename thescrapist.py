import requests
import threading
import os

n = "http://www.randomwebsite.com/cgi-bin/random.pl"
LIMIT = 10

def websites():
    r = requests.get(n)
    print 'Searching: ' + r.url
    emails = findBetween(r.text, 'mailto:', '"')
    if (len(emails) < 50) & (emails != ''):
      print('\nEMAIL FOUND: ' + emails + '\n')
      f = open("list.txt","a")
      f.write(emails + "\n")
      f.close()
    

def findBetween(s, first, last):
    try:
        start = s.index( first ) + len( first )
        end = s.index( last, start )
        return checkExtra(s[start:end], '?')
    except ValueError:
        return ''

def checkExtra(s, look):
    try:
        end = s.index( look )
        return s[0:end]
    except ValueError:
        return s

def scrape():
  i = 0
  while i < LIMIT:
    try:
      websites()
    except:
      pass
    i += 1

print '\n\nTheScrapist v1.0\nA blazin fast email scraper\n\n'
scrape()
