from pymongo import MongoClient
import requests
from personal.functions import pdb_function
from lxml import html, etree
import re
"""
conn = MongoClient(host="mangomiracle.link", port=27017)
db = conn.fantasy_academia
these = db.fa_players.find()
"""

# Search pattern string for google scholar
url_pattern_search = "https://scholar.google.com/citations?mauthors={}&"\
                     "hl=en&view_op=search_authors"

def parse_search(search_string, pages=5):
    """
    Function parses a search, getting data on
    all of the people returned by the search
    """
    init_url = url_pattern_search.format(search_string)
    req = requests.get(init_url)
    init_tree = html.fromstring(req.content)
    ext = init_tree.xpath('//button[@aria-label="Next"]')[0]
    #.get('onclick').split('=')[1]
    authors = init_tree.xpath('//h3[@class="gsc_1usr_name"]')
    names = [a.text_content() for a in authors]
    author_ids = [a.getchildren()[0].get('href') for a in authors]
    m = re.compile('user=(.+)&hl=')
    author_ids = [m.search(a).groups()[0] for a in author_ids]
    next_page = "https://scholar.google.com/{}".format(ext)
    return stuff

if __name__=='__main__':
    pdb_function(parse_search, 'a')
