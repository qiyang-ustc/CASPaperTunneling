import os
import re
import requests
from config import load_config_file

import browser_cookie3
cj = browser_cookie3.chrome() # load chrome cookies, maybe not a good idea.

def get_filename(url):
    return url.split('/')[-1]+".pdf"

def check_url(url):
    l = url.split('/')
    return l[0]=="https:" and l[1]=="" # poorman's check

def convert_url(input_url):
    l = input_url.split('/')
    l[2] = (l[2] + ".443").replace('.','-') + ".webvpn.las.ac.cn"
    return "/".join(l)

def download_pdf_from_url(url):
    r"""Download a PDF file from url and open it with the default PDF reader."""
    response = requests.get(url,cookies=cj)
    with open(load_config_file()['PaperDir']+"/"+ get_filename(url), 'wb') as f:
        print("Download File to "+load_config_file()['PaperDir']+"/"+ get_filename(url))
        f.write(response.content)
    os.system("echo '%s' >> $HOME/.cached-paper/downloaded" % url) # Maybe only availbale in macOS. But try this first