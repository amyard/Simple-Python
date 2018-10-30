import time
from datetime import datetime as dt

# time.sleep(5) каждый 5 секунл будет делать что-то
hosts_temp = r'C:\Users\Admin\10 apps\app 3 websiteblocker\hosts'
hosts_path = r"C:\Windows\System32\drivers\etc\hosts"   # r - row string
redirect = '127.0.0.1'
website_list = ['www.facebook.com', 'facebook.com', 'www.instagram.com', 'instagram.com', 'www.linkedin.com','linkedin.com']


while True:
	if dt(dt.now().year,dt.now().month, dt.now().day, 9) < dt.now() < dt(dt.now().year,dt.now().month, dt.now().day, 18):
		print(' Working hours...')
		with open(hosts_path,'r+') as file:  # r+ read and write
			content = file.read()
			for website in website_list:
				if website in content:
					pass
				else:
					file.write(redirect + ' ' +website+'\n')
	else:
		with open(hosts_path, 'r+') as file:
			content = file.readlines()
			file.seek(0)   # repcale first pointer before needed line
			for line in content:
				if not any(website in line for website in website_list):
					file.write(line)
			file.truncate()   # delete rows which we dont need
		print('Fun hours ...')
	time.sleep(600)



