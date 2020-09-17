import requests
import json
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ast
import os
import os.path
from os import path
import requests
import sys
search = input("Name: ")
# url
Search_url = f"https://vidstreaming.io/ajax-search.html?keyword={search}"
# replace userinput 'space' with %20
Search_url = Search_url.replace(" ", "%20")

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive',
           'X-Requested-With': 'XMLHttpRequest'}


Search_url_x = Request(url=Search_url,  headers=headers)
html = urlopen(Search_url_x)

search_t = BeautifulSoup(html.read(), "html5lib")

Count_t = -1
search_loop_main = True
search_loop_snd = True
while search_loop_main:

    while search_loop_snd:

        if str(search_t.findAll('a')) == "[]":
            print("Anime not found")
            break

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
                list_i_loop = -1
                continue
            elif int(list_i) > Count_t:
                print("Not Available")
                
                continue
            elif list_i.isdigit():
                # print(type(synlist))
                str_list = str(synlist[int(f"{list_i}")].text)
                str_list = (str_list.replace("<\/a><\/li>", ""))
                str_list = str_list.replace('<\/ul>"}', '')
                print(str_list)
                list_i_next_status = True
                break

            else:
                list_i = 0
            break

        while list_i_next_status:

          Anime_Name = f"{str_list}"
          Anime_Name = Anime_Name.lower()
          Anime_Name = Anime_Name.replace('-', '')
          print(Anime_Name)
          Anime_Name = Anime_Name.replace('  ', '-')
          Anime_Name = Anime_Name.replace(' ', '-')
          print(Anime_Name)
          characters_to_remove = "():`"

          new_string = Anime_Name
          for character in characters_to_remove:
              new_string = new_string.replace(character, "")

          print("last")
          break
    break

    Anime_Url = f"https://vidstreaming.io/videos/{Anime_Name}-epispde-"

    Anime_Episode = 0
    Anime_Start = 0
    Main_Loop = True

    Folder_check = path.exists(f"./Anime_downloader/{Anime_Name}")
    while Folder_check == False:
        os.makedirs(f"./Anime_downloader/{Anime_Name}")
        break

    while Main_Loop:
        # Anime_Episode = 1
        Anime_Episode = Anime_Episode + 1
        Anime_Name_Full = f"{Anime_Name}{Anime_Episode}"
        # print(Anime_Name_Full)
        print(f"\nDownloading Episode {Anime_Episode}")

        reg_url = f"{Anime_Url}{Anime_Episode}"
        my_request = Request(url=reg_url, headers=headers)

        html = urlopen(my_request)
        my_iframe = BeautifulSoup(html.read(), "html5lib")
        error = my_iframe.body.get_text()
        # print(error)
        if error == "404\n":
            print("No Anime Available")
            break
        vidstreaming = "http:" + str(my_iframe.iframe["src"])

        # print(vidstreaming)
        vidstreaming = vidstreaming.replace('streaming.php', 'ajax.php')
        # print(vidstreaming)

        my_request = Request(url=vidstreaming, headers=headers)
        html = urlopen(my_request)
        my_iframe = BeautifulSoup(html.read(), "html5lib")
        # print(my_iframe)
        stream_json = my_iframe.body.get_text()

        # print(stream_json)
        # print(type(stream_json))

        stream_json = json.loads(stream_json)

        # print(stream_json)

        # print(type(stream_json))

        stream_json = stream_json['source']
        stream_json = str(stream_json)
        stream_json = stream_json.replace('[', '')
        stream_json = stream_json.replace(']', '')
        # print(type(stream_json))
        stream_json = ast.literal_eval(stream_json)
        # print(stream_jsonn)

        stream_json = stream_json.get("file")

        # print(stream_json)
        Anime_download_path = f"./Anime_downloader/{Anime_Name}/{Anime_Name_Full}.mp4"

        with open(Anime_download_path, "wb") as f:
            print(f"Downloading...\n{Anime_Name}\nEpisode No: {Anime_Episode}")
            response = requests.get(
                stream_json, stream=True, allow_redirects=True)
            total_length = response.headers.get('content-length')
            print("File size: %s MB" % int(int(total_length) / (1024 * 1024)))

            if total_length is None:  # no content length header
                f.write(response.content)
            else:
                dl = 0
                total_length = int(total_length)
                # 1000 equals to 1 MB bandwidth
                for data in response.iter_content(chunk_size=100000):
                    dl += len(data)
                    f.write(data)
                    done = int(40 * dl / total_length)
                    sys.stdout.write("\r[%s%s]" %
                                     ('█' * done, ' ' * (40-done)))
                    sys.stdout.flush()


    break






















    Bye_Bye = input("Type 1 to exit\nType 2 to Retry : ")
    if Bye_Bye == "1":
        break
    elif Bye_Bye == "2":
        continue
    else:
        print("Sayonara")
        break

    # Anime_Name = "One Piece Movie 14: Stampede"
    # Anime_Name = Anime_Name.lower()
    # Anime_Name = Anime_Name.replace(' ','-')
    # characters_to_remove = "():"

    # new_string = Anime_Name
    # for character in characters_to_remove:
    #   new_string = new_string.replace(character, "")

    # print(new_string)



# /html/body/ul/li[1]/a
