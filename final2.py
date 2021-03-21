from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from stoixeia import user, pw
import time

list_of_following = []
list_of_followers = []
final_list = []
PATH = "C:\Program Files (x86)\chromedriver.exe"
driver = webdriver.Chrome(PATH)
driver.get("https://www.instagram.com/")
cookies = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]")
cookies.click()
time.sleep(2)
username = driver.find_element_by_name("username")
username.click()
username.send_keys(user)
password = driver.find_element_by_name("password")
password.click()
password.send_keys(pw)
password.send_keys(Keys.RETURN)
time.sleep(4)
not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
not_now.click()
time.sleep(2)
second_not_now = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
second_not_now.click()
url = 'https://www.instagram.com/' # after slash (/) put username of ig acc you want.
driver.get(url)
time.sleep(4)
following = driver.find_element_by_partial_link_text('Ακολουθείτε ')
final_number = following.text
following.click()
time.sleep(5)
if len(final_number) == 21:
    print(final_number[12])
    real_final_number = final_number[12]
elif len(final_number) == 22:
    print(final_number[12:14])
    real_final_number = final_number[12:14]
elif len(final_number) == 23:
    print(final_number[12:15])
    real_final_number = final_number[12:15]
elif len(final_number) == 25:
    print(final_number[12:17])
    real_final_number = float(final_number[12:17]) * 1000
for i in range(1, int(real_final_number)+1):
    try:
        element = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']')
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    except:
        break


time.sleep(1)
element = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[1]')
driver.execute_script("return arguments[0].scrollIntoView(true);", element)
time.sleep(1)
for i in range(1, int(real_final_number)+1):
    try:
        person = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[' + str(i) + ']')
        list_of_following.append(person.text)
    except:
        break
new_list_of_following = []
for e in list_of_following:
    s = 0
    for c in e:
        if c == "\n":
            s = e.index(c)
            break
    e1 = slice(0, s)
    new_string = e[e1]
    new_list_of_following.append(new_string)
print(new_list_of_following)
exit1 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/button')
exit1.click()
time.sleep(1)
followers = driver.find_element_by_partial_link_text(' ακόλουθοι')
followers.click()
time.sleep(2)
final_followers = followers.text
if len(final_followers) == 11:
    real_follow_number = final_followers[0]
    print(real_follow_number)
elif len(final_followers) == 12:
    real_follow_number = final_followers[0:2]
    print(real_follow_number)
elif len(final_followers) == 13:
    real_follow_number = final_followers[0:3]
    print(real_follow_number)
elif len(final_followers) == 15:
    print(final_followers[0:5])
    real_follow_number = float(final_followers[0:5]) * 1000
for i in range(1, int(real_follow_number)+1):
    try:
        element = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']')
        driver.execute_script("return arguments[0].scrollIntoView(true);", element)
        time.sleep(0.5)
    except:
        break

time.sleep(1)
element = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li[1]')
driver.execute_script("return arguments[0].scrollIntoView(true);", element)
time.sleep(1)
for i in range(1, int(real_follow_number)+1):
    try:
        person2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/ul/div/li['+str(i)+']')
        list_of_followers.append(person2.text)
    except:
        break
new_list_of_followers = []
for e in list_of_followers:
    s = 0
    for c in e:
        if c == "\n":
            s = e.index(c)
            break
    e1 = slice(0, s)
    new_string = e[e1]
    new_list_of_followers.append(new_string)
print(new_list_of_followers)
for i in new_list_of_following:
    if i not in new_list_of_followers:
        final_list.append(i)

print(final_list)
try:
    f = open("notfollowingback.txt", "w")
    f.write(str(final_list))
    f.close()
except:
    f = open("notfollowingback.txt", "x")
    f.write(str(final_list))
    f.close()


