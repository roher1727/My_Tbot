from time import sleep
from selenium import webdriver
import requests
import shutil
import random
from webdriver_manager.firefox import GeckoDriverManager
from selenium.common.exceptions import NoSuchElementException

def getDriver():
	profile = webdriver.FirefoxProfile('/Users/roher/AppData/Roaming/Mozilla/Firefox/Profiles/b8vn6197.default-release')
	geoEnable = webdriver.FirefoxOptions()
	geoEnable.set_preference('geo.enabled', True)
	geoEnable.set_preference('geo.provider.use_corelocation', True)
	geoEnable.set_preference('geo.prompt.testing', True)
	geoEnable.set_preference('geo.prompt.testing.allow', True)
	return webdriver.Firefox(executable_path=GeckoDriverManager().install(), options=geoEnable, firefox_profile=profile)

def __closePopups():
	try:
		driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div/div/div[1]/button').click()
	except:
		pass
	try:
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
	except:
		pass
	sleep(2)
	try:
		driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div[3]/button[1]').click()
	except:
		pass

	sleep(2)
	try:
		element = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/a')
		element.click()
		driver.get('https://tinder.com/app/recs')
		sleep(2)
	except NoSuchElementException:
		pass


driver = getDriver()


print('=== Tinder login ===')
#driver.execute_script('document.cookie = ""; localStorage.clear(); sessionStorage.clear();')
driver.get('https://tinder.com/')
sleep(6)
# Boton de iniciar sesion
driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a').click()
sleep(3)
# Boton de iniciar con google
button = driver.find_element_by_css_selector('button[aria-label~="Google"]')
button.click()
window_before = driver.window_handles[0]
sleep(8)
#driver.switch_to.window(driver.window_handles[1])
#sleep(2)
#driver.find_element_by_id('identifierId').send_keys("roher1727")
#sleep(2)
#driver.find_element_by_id('identifierNext').click()
driver.switch_to.window(window_before)

__isLogged = 'tinder.com/app/recs' in driver.current_url
if __isLogged:
	__closePopups()
works = True

if not works:
	driver.close()
	print('Error: Login is no available now. Try later.')

# Obtener imagen 

imagen = driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div/div/div/div[3]/div/div/span/div[1]')
imagen_url = imagen.get_attribute('style').split("\"")[1]

r = requests.get(imagen_url, stream = True)

if r.status_code == 200:
	# Set decode_content value to True, otherwise the downloaded image file's size will be zero.
	r.raw.decode_content = True
	
	# Open a local file with wb ( write binary ) permission.
	with open("prueba.jpg",'wb+') as f:
		shutil.copyfileobj(r.raw, f)


# Loop de swipe

while True:
	prob_like = random.uniform(0,1)

	if prob_like > 0.5:
		# Boton de Like
		print("Like con probabilidad: ", prob_like)
		likesButtons = ['/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[4]/button']
		
		for path in likesButtons:
			try:
				driver.find_element_by_xpath(path).click()
			except:
				pass
	else:
		print("Dislike con probabilidad: ", 1-prob_like)
		dislikesButtons = ['/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[4]/div/div[2]/button', '/html/body/div[1]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div/div[5]/div/div[2]/button']
		# Boton de dislike
		for path in dislikesButtons:
			try:
				driver.find_element_by_xpath(path).click()
			except:
				pass

	sleep(4)

