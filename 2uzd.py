""" 
Iegūt ziņas, izmantojot RSS plūsmu no google.lv.

Kas ir RSS?

"""

import feedparser

# URL uz RSS plūsmu

rss_url='https://news.google.com/home?hl=lv&gl=LV&ceid=LV:lv'

# iegūsim RSS plūsmas datus
kkk=feedparser.parse(rss_url)

# parāda un jānoformē

for entry in kkk.entries:
    print("Virsraksts: ", entry.title)
    print("Saites: ", entry.link)
    print("Publicēšanas datums:", entry.published)
    print("\n")