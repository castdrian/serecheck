from ntpath import join
from halo import Halo
from html_to_json import convert
from urllib.request import urlopen

spinner = Halo(text='Fetching Serebii.net')
spinner.start()

page = urlopen('https://serebii.net/index2.shtml')
html_bytes = page.read()
html = html_bytes.decode('utf8', 'ignore')

json = convert(html)
news = json['html'][0]['body'][0]['div'][0]['div'][1]['main'][0]['div'][0]['div'][1]['p'][1]['_values']
spinner.stop()

print(f'Latest Serebii news entry:\n\n{join(news[0])}')