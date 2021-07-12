#jangan lupakan author kalo mau recode :)

import threading
import requests
from bs4 import BeautifulSoup

filename = "result.txt"
try:
    open(filename, "a")
except FileExistsError:
    pass

def parse_teks(teks):
    try:
        
        pnjng = len(teks)
        hitung = 50 - pnjng
        result = teks+" "*hitung
        return result
    except:
        pass
    
    
def simpan(konteks):
    #
    try:
        baca = open(filename, "r").read()
        if konteks in baca:
            return False
        else:
            save = open(filename, "a")
            save.write(konteks+"\n")
            return True
    except:
        pass

def final(source):
    try:
        soup = BeautifulSoup(source, "html.parser")
        parsing = soup.find_all("ul", class_="tr")[1:]
        for li in parsing:
            try:
                pisah = li.find_all("li")
                domain = pisah[0].find("a").text.strip()
                waktu = pisah[1].text
            except (ValueError, IndexError):
                pass
            cek_simpan = simpan(domain)
            parse_domain = parse_teks(domain)
            try:
                if cek_simpan:
                    print("\x1b[0;33m"+parse_domain+"\x1b[0;37m==> \x1b[0;32m"+waktu)
                else:
                    print("\x1b[0;33m"+parse_domain+"\x1b[0;37m==>\x1b[0;31m Duplicate")
            except:
                pass
    except:
        pass

def get_source(page):
	for i in range(1, int(page)+1):
		try:
			site = "https://www.thesiterank.com/index.php?p="+str(i)
			resp = requests.get(site, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"})
			body = resp.text
			final(body)
		except requests.exceptions:
			print("\x1b[0;31mPlease check your connection !!!")

print("""\x1b[0;32m
 _____ _          _____ _ _      ______            _    
|_   _| |        /  ___(_) |     | ___ \          | |   
  | | | |__   ___\ `--. _| |_ ___| |_/ /__ _ _ __ | | __
  | | | '_ \ / _ \`--. \ | __/ _ \    // _` | '_ \| |/ /
  | | | | | |  __/\__/ / | ||  __/ |\ \ (_| | | | |   < 
  \_/ |_| |_|\___\____/|_|\__\___\_| \_\SiteList Scrapper
  Created By Faiz
  Contact me : zalgans@hotmail.com
  
""")
p = input("\x1b[1;37mHow Much Page U Want ? ")
threading.Thread(target=get_source, args=(p,)).start()
