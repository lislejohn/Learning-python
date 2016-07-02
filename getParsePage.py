# Get a page and read in to beautiful soup

#Get a page using request

import requests
import bs4

def getPage(page, fileOut):
    res = requests.get(page)
    res.raise_for_status()
    print("Request status = ", res.status_code == requests.codes.ok)
    #print("type =", type(res))
    #print("Length", len(res.text))
    #print(res.text[:250])

    with open(fileOut, 'wb') as f:
        for chunk in res.iter_content(100000):
            f.write(chunk)


#targetPage = "http://www.rmweb.co.uk/community/index.php?/topic/18451-peterborough-north/page-1"
targetPage = "http://www.rmweb.co.uk/community/index.php?/topic/85326-dave-fs-photos-ongoing-more-added-29th-june/page-3" \
#targetPage = "http://www.aps.anl.gov"

#getPage(targetPage, "testFile.txt" )

with open('testFile.txt', 'r') as f:
    targetPageSoup = bs4.BeautifulSoup(f, "lxml")

pic = targetPageSoup.find_all(class_='resized_img')
#pic = targetPageSoup.select('.resized_img')

print(len(pic))
print(type(pic[0]))
print(type(pic[0].attrs))

if pic == []:
    print('Could not find picture.')
else:
    print("pic =", pic[0])

for link in pic:
    print(link.get('href'), link.get('title'))
#print (targetPageSoup.prettify())

#images = targetPageSoup.find_all(class_='resized_img')
#images = targetPageSoup.find_all("a")
#print (type(images))
#print(images)
#print(images[0])

#for image in images:
#    print (image)
#for link in targetPageSoup.find_all('a'):
#    print(link.get('href'))


