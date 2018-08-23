# -*- coding: utf-8 -*-

import csv
import urllib2
from bs4 import BeautifulSoup

quote_page = ['http://pipsc.ca/labour-relations/stewards/stewards-list?p_regioncode=ATL', 'http://pipsc.ca/labour-relations/stewards/stewards-list?p_regioncode=BC',
                'http://pipsc.ca/labour-relations/stewards/stewards-list?p_regioncode=NCR', 'http://pipsc.ca/labour-relations/stewards/stewards-list?p_regioncode=ONT',
                'http://pipsc.ca/labour-relations/stewards/stewards-list?p_regioncode=PRAI', 'http://pipsc.ca/labour-relations/stewards/stewards-list?p_regioncode=QUE']

data = []

for pg in quote_page:
    print "Running page: ", pg
    page = urllib2.urlopen(pg)
    soup = BeautifulSoup(page, 'html.parser')
    stewards = soup.find_all( attrs={'class': 'steward_item'})
    print "Stewards: ", len(stewards)
    print

    for s in stewards:

        name = s.a.get_text().encode('utf-8')
        group = s.p.get_text().split(' ',1)[-1].encode('utf-8')
        region = s.p.next_sibling.get_text().split(' ',1)[-1].encode('utf-8')
        department = s.p.next_sibling.next_sibling.get_text().split(' ',1)[-1].encode('utf-8')
        work_address = s.p.next_sibling.next_sibling.next_sibling.get_text().split(': ',1)[-1].encode('utf-8')

        data.append((name, group, region, department, work_address))


with open ("steward_data.csv", "wb") as csv_file:
    writer = csv.writer(csv_file)
    for name, group, region, department, work_address in data:
        writer.writerow([name, group, region, department, work_address])
