import requests
from re import split, search
import mechanize

'''
HOW TO MAKE KEYS:
use the script thats in the same repository as this script. github.com/Spoowy

'''

def getData(pw):
    try:
        browser = mechanize.Browser()
        browser.set_handle_robots(False)
        cookies = mechanize.CookieJar()
        browser.set_cookiejar(cookies)
        browser.set_handle_refresh(False)
    # PUT YOUR PASTEBIN LINK HERE 
        url = 'https://pastebin.com/'
        browser.open(url)
        browser.select_form(nr = 0)
        browser.form['PostPasswordVerificationForm[password]'] = pw
        response = browser.submit()
        return(response.read())
    except:
        raise SystemExit(0)
        
    
def checks():
    if (int(len(result) > 3)):
        print("INVALID KEY ASK FOR A NEW KEY")
        raise SystemExit(0)
        
    elif (int(len(result) == 3)):
        dataReturned = getData(pw)
        strData = str(dataReturned)
        if search(r'\b' + combined_List_Items + r'\b', strData):
            print("SUCCESS")
            getData(pw)
            #your function call here
        else:
            print("NOT REGISTERED/WRONG KEY")
            
    elif (int(len(result) == 2)):
        if search(r'\b' + combined_List_Items + r'\b', strData):
            print("SUCCESS")
            getData(pw)
            #your function call here             
        else:
            print("NOT REGISTERED/WRONG KEY")
            
            
print("AUTH MADE BY github.com/Spoowy63")            
key =  str(input("Enter Your Key: "))
result = split(r'(-?\d*\.?\d+)', key)
pw = result[2]
combined_List_Items = result[0] + result[1]
checks()
