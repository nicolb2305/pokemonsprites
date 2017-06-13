import requests
import re
from PTL import Image

imagelinkregex = r"""<a href="\/\/(cdn.bulbagarden\.net\/upload\/.\/..\/Spr_5b_\d+_?m?\.png)"""
linkurl = ""
i = 1
while i < 650:
	i = str(i).zfill(3)
	url = "https://bulbapedia.bulbagarden.net/wiki/File:Spr_5b_%s.png" % i
	if linkurl == None:
		i = int(i)
		i -= 1
		i = str(i).zfill(3)
		url = "https://bulbapedia.bulbagarden.net/wiki/File:Spr_5b_%s_m.png" % i
	print(url)
	linkurl = None
	temp = requests.get(url)
	for line in temp.text.split("\n"):
		data = re.search(imagelinkregex, line)
		if data != None:
			linkurl = "https://" + data.group(1)
			print(i)
			f = open(i+".png", "wb")
			f.write(requests.get(linkurl).content)
			f.close()
			break
	i = int(i)
	i += 1

def iter_frames(im):
    try:
        i= 0
        while 1:
            im.seek(i)
            imframe = im.copy()
            if i == 0: 
                palette = imframe.getpalette()
            else:
                imframe.putpalette(palette)
            yield imframe
            i += 1
    except EOFError:
        pass

im = Image.open(001.png)
for i, frame in enumerate(iter_frames(im)):
    frame.save('test%d.png' % i,**frame.info)