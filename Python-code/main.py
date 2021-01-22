import requests
from bs4 import BeautifulSoup
#from the bs4 file, import Beatiful Soup

request= requests.get("https://www.quill.com/hon-mesh-mid-back-task-chair-center-tilt-tension-lock-fixed-arms-black-mesh-black-fabric-bsxvl511lh10/cbs/51128941.html?sfcp=1&gclid=CjwKCAiA2O39BRBjEiwApB2Iktby9qeRaQO4jlwFJGmrULLvXPxO8GntbIDcXL5Y7-TQIO3sXt3t4RoCQaYQAvD_BwE&gclsrc=aw.ds")
#gets page
content= request.content
#gets content of the page
soup = BeautifulSoup(content, "html.parser")
#parses through the content of the html page
element =  soup.find("span",{"class": "priceupdate","id":"SkuPriceUpdate","content":"139.99" })
#searches through data and finds price element
string_price = element.text.strip()
price = float(string_price)

if price < 200:
        print(" You should buy the chair! It is less than 200 dollars! ")
        print(" the current price is {}". format(price))
else:
        print("dont buy because it is over 200 dollars")
        print(" the current price is {}". format(price))



#prints the element, in this case it is the price
# the strip method removes white space
# the reason webscraping does not work in some sites is because they have a robots.txt file which blocks your program. Only some parts of sites are webscrapebable. if it is not webscrapeable, it is Disallowed


<span class="priceupdate" id="SkuPriceUpdate" content="139.99">139.99</span>
