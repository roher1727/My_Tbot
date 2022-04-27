import requests 
import shutil
import urllib.request


with open('./datos1.txt','r') as texto_datos:
	rows = texto_datos.readlines()

classes = []
links = []
index = 0

for row in rows:
	try:
		classes.append(int(row[0]))
	except:
		links.append(row.replace(" ","").split("\"")[1])


for classe,link in zip(classes, links):
	image_url = link
	r = requests.get(image_url, stream = True)

	if r.status_code == 200:
		# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
		r.raw.decode_content = True
		
		# Open a local file with wb ( write binary ) permission.
		with open("imagenes/"+str(index)+".jpg",'wb+') as f:
			shutil.copyfileobj(r.raw, f)
		
		with open("clases/"+str(index)+".txt",'w+') as f:
			if classe == 1:
				f.write("Like")
			else:
				f.write("Dislike")
		print('Image sucessfully Downloaded')
	else:
		print('Image Couldn\'t be retreived')

	index += 1