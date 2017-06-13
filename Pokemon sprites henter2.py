import requests
import re

pokemon = r'<a href="(/sprites/[\w\-]+)"'
imagelinkregex = r'(https:\/\/img\.pokemondb\.net\/sprites\/[\w\-\/]+\/[\w\-]+\.\w+)"'
url = "https://pokemondb.net/sprites"
urls = []
results = requests.get(url).text.split("\n")
for line in results:
	temp = re.search(pokemon, line)
	if temp == None: continue
	urls.append("https://pokemondb.net"+temp.group(1))
for url in urls:
	print(url)
	image = requests.get(url).text.split("\n")
	for line in image:
		data = re.findall(imagelinkregex, line)
		if data == [] or "<span class=" not in line: continue
		i = 0
		for images in data:
			i += 1
			if i%2 == 1: continue 
			f = open("ALL/"+images[31:].replace("/", "_"), "wb")
			f.write(requests.get(images).content)
			f.close()