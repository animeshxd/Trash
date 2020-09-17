import requests
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
search = input("Name: ")
url = f"https://vidstreaming.io/ajax-search.html?keyword={search}"  # url
url = url.replace(" ", "%20")  # replace userinput 'space' with %20

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive',
           'X-Requested-With': 'XMLHttpRequest'}


x = Request(url=url,  headers=headers)
html = urlopen(x)
search_t = BeautifulSoup(html.read(), "html5lib")

Count_t = -1
search_loop_main = True
search_loop_snd = True
while search_loop_main:

    while search_loop_snd:

        if str(search_t.findAll('a')) == "[]":
            print("Anime not found")

        for node in search_t.findAll('a'):

            Count_t = Count_t + 1
            rslt2 = ''.join(node.findAll(text=True))
            rslt2 = (rslt2.replace("<\/a><\/li>", ""))
            rslt2 = rslt2.replace('<\/ul>"}', '')

            print(Count_t, ": ", rslt2)
        

        synlist = search_t.find_all("a", text=True)

        list_i_loop = True

        while list_i_loop:
            list_i = input("")

            if list_i == "q" or list_i == "quit":
                break
            elif list_i.isdigit() == False:
                print("not integer value")
                continue
            elif int(list_i) > Count_t:
                print("Not Available")
                continue
            elif list_i.isdigit():
                break
            else:
                list_i = 0
            break

        # print(type(synlist))
        str_list = str(synlist[int(f"{list_i}")].text)
        str_list = (str_list.replace("<\/a><\/li>", ""))
        str_list = str_list.replace('<\/ul>"}', '')
        print(str_list)

        print("last")
        break
    Bye_Bye = input("Type 1 to exit\nType 2 to Retry : ")
    if Bye_Bye == "1":
        break
    elif Bye_Bye == "2":
        continue
    else:
        print("Sayonara")
        break


# for a in search_t.find_all(href=False):
#     print ("Found the URL:", a)

# /html/body/ul/li[1]/a
