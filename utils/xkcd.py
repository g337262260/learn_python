#! python3
"""
    #: 网络抓取图片脚本
    #：待完善

"""


import requests, os, bs4

url = 'http://xkcd.com'
os.makedirs('xkcd', exist_ok=True)
while not url.endswith('#'):
    #: Download the page
    # print('Download... page %s...' % url)
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text)

    # Find the url of comic image
    comicElem = soup.select('#comic img')
    if not comicElem:
        print('Could not find comic image')
    else:
        if comicElem[0].get('src').startswith('//imgs.xkcd.com'):
            comicUrl = 'http:' + comicElem[0].get('src')
        else:
            comicUrl = 'http://xkcd.com'+comicElem[0].get('src')
        print('url'+comicUrl)
        try:
            res = requests.get(comicUrl)
            res.raise_for_status()
            # Save image
            imageFile = open(os.path.join('xkcd', os.path.basename(comicUrl)), 'wb')
            for chunk in res.iter_content(100000):
                imageFile.write(chunk)
            imageFile.close()
        except:
            raise ValueError('Image could not download')
    # get the prev button's url
    prevLink = soup.select('a[rel="prev"]')[0]
    url = 'http://xkcd.com' + prevLink.get('href')
print('Done..')
