#!/usr/bin/env python
"""
This script downloads the Excel data supplementing the original papers
and shape file for geographic visualization
"""
import requests
import os
import yaml

# Read in config file
conf = {k: v for d in yaml.safe_load(open("conf.yaml")) for k, v in d.items()}

# URLs of source data
url1 = "https://journals.plos.org/plosone/article/file?type=supplementary&id=info:doi/10.1371/journal.pone.0156340.s002"
url2 = "https://static-content.springer.com/esm/art%3A10.1038%2Fnature02801/MediaObjects/41586_2004_BFnature02801_MOESM2_ESM.xls"

url3 = "https://github.com/nvkelso/natural-earth-vector/raw/master/50m_physical/ne_50m_land.shp"
url4 = "https://github.com/nvkelso/natural-earth-vector/raw/master/50m_physical/ne_50m_land.shx"
url5 = "https://github.com/nvkelso/natural-earth-vector/raw/master/50m_physical/ne_50m_land.prj"

urls = [url1, url2, url3, url4, url5]
names = ["Atkinson2016.xlsx", "Rollet2004.xls",
         "ne_50m_land.shp", "ne_50m_land.shx", "ne_50m_land.prj"]


for url, name in zip(urls, names):
    print("Downloading", name)
    excel_file = requests.get(url)
    with open(os.path.join(conf["data"]["raw"], name), 'wb') as f:
        f.write(excel_file.content)
