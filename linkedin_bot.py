from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.common.exceptions as exceptions
from selenium.webdriver.common.keys import Keys
from secret import Secret
import time





def login():
	global driver
	options = webdriver.ChromeOptions()
	options.add_argument("start-maximized")
	options.add_experimental_option("excludeSwitches", ["enable-automation"])
	options.add_experimental_option("detach",True)
	PATH = "/Users/trichau/Desktop/chromedriver"
	try:
		driver = webdriver.Chrome(chrome_options = options,executable_path =PATH)
	except exceptions.WebDriverException:
		print("you need to download a new version of the chromedriver")

	try:
		driver.get('https://www.linkedin.com/home')
		WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.ID,"session_key"))).send_keys(Secret.username)
		comment = driver.find_element_by_id('session_password')
		comment.send_keys(Secret.password)

		comment.send_keys(Keys.RETURN)
		time.sleep(1)
	except ImportError:
		print("Closing program")

	# click radio button
	#python_button = driver.find_elements_by_xpath("//input[@name='lang' and @value='Python']")[0]
	#python_button.click()
	#time.sleep(2)

	# type text
	#text_area = driver.find_element_by_id('session_key')
	#text_area.send_keys(Secret.username)

	#comment = driver.find_element_by_id('session_password')
	#comment.send_keys(Secret.password)

	#comment.send_keys(Keys.RETURN)
	#time.sleep(1)
#all_btn = driver.find_element_by_tag_name("button")
#searc_btn = driver.find_element_by_xpath("//*[@id='global-nav-typeahead']/input").send_keys("Software engineer")
#searc_btn.send_keys(Keys.RETURN)

def searchLink ():
	search_what = input("What do you want to search: ")
	search_what = search_what.split()
	link_search = search_what[0]+"%20"+search_what[1]
	print (link_search)
	login()
	link_search_url = "https://www.linkedin.com/search/results/people/?keywords="
	driver.get(link_search_url+link_search)
	#go_next_page(3)

def clickConnect():
	#click connect btn
	#for p in range(2,5):
	for i in range(3):
		all_btn = driver.find_elements_by_tag_name("button")
		connect_btn = [btn for btn in all_btn if btn.text == "Connect"]
		time.sleep(1) 
		for btn in connect_btn:
			driver.execute_script("arguments[0].click();",btn)
			time.sleep(2)
			#click on send
			send = driver.find_element_by_xpath("//button[@aria-label='Send now']")
			driver.execute_script("arguments[0].click();",send)
			#close = driver.find_element_by_xpath("//button[@aria-label='Dismiss']")
			#driver.execute_script("arguments[0].click();",close)
			time.sleep(2)
		go_next_page()
		time.sleep(2)

def go_next_page():
	#next_bttn = driver.find_element(By.XPATH, "//button[contains(@id, 'ember748') and contains(., 'Next')]").click()
	#next_bttn = driver.find_element_by_xpath("//button[@aria-label='Page "+str(n)+"']")
	next = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH,"//button[@aria-label='Next']")))
	#be able to work
	#next = driver.find_element_by_xpath("//button[@aria-label='Next']")
	driver.execute_script("arguments[0].click();",next)
	
	#next_bttn = driver.find_element_by_xpath("//button[@aria-label='Next']")
	#driver.find_element_by_css_selector( "[aria-label='Page "+str(n)+"']").click()
	#driver.execute_script("arguments[0].click();",next_bttn)
	#next_bttn.click()

def send_messages():
	#n_pages = 3
	#for n in range(1, n_pages):
	driver.get("https://www.linkedin.com/mynetwork/invite-connect/connections/")
	time.sleep(2)
	all_btn = driver.find_elements_by_tag_name("button")
	mess_btn = [btn for btn in all_btn if btn.text == "Message"]

	for i in range(8, len(mess_btn)):
		#click on Message button
		driver.execute_script("arguments[0].click();", mess_btn[i])
		time.sleep(2)

		#activate main dive
		main_div = driver.find_elements_by_tag_name("p")
		time.sleep(2)

		#send_messages
def post():
	driver.find_element(By.XPATH, "//button[contains(@id, 'ember34') and contains(., 'Start a post')]").click()
	#driver.find_element_by_xpath("//*[@id='ember314']/div/div/div[1]/div[2]/div/div/div[2]/div/div/div[1]").send_keys("THIS IS A AUTOMATED LINKEDINT_BOT THAT I CREATED TO POST MY POSTS ON LINKED IN. USING SELENIUM PYTHON ")
	driver.find_elements_by_tag_name("p").send_keys("THIS IS A AUTOMATED LINKEDINT_BOT THAT I CREATED TO POST MY POSTS ON LINKED IN. USING SELENIUM PYTHON ")

#driver.get('https://www.linkedin.com/search/results/all/?keywords=software%20engineer')

#post_button = [btn for btn in all_btn if btn.text == "Start a post"]

#for btn in post_button:
#	driver.execute_script("arguments[0].click();", btn)
#print(all_btn)
#post_btn = [btn for btn in all_btn if btn.text == "Start a post"]
# click submit button
#submit_button = driver.find_elements_by_xpath('//*[@id="u_0_d_g6"]')
#submit_button.click()
#time.sleep(2)
#driver.quit()

searchLink()
clickConnect()
driver.quit()



#login()
#post()
#send_messages()
#driver.quit()
