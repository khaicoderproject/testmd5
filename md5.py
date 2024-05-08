import requests, threading


banner = """
\033[1m\033[91m
   ___  ____   ____  ____       _       _____   ______    ________  
|_  ||_  _| |_   ||   _|     / \     |_   _| |_   _ `. |  __   _| 
  | |_/ /     | |__| |      / _ \      | |     | | `. \|_/  / /   
  |  __'.     |  __  |     / ___ \     | |     | |  | |   .'.' _  
 _| |  \ \_  _| |  | |_  _/ /   \ \_  _| |_   _| |_.' / _/ /__/ | 
|____||____||____||____||____| |____||_____| |______.' |________| 
                                                                  \033[0m
"""
print(banner)


input_file = input("Enter File Md5: ")
threads = int(input("Enter Threads: "))
filemd5 = open(input_file, encoding= "UTF-8").read().strip().split("\n")

list_md5 = []
for i in range(len(filemd5)):
    md5 = filemd5[i]
    list_md5.append(md5)
    
def main(md5):
    header={
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'
    }
    
    data={
        'md5': md5
    }
    response = requests.post("https://md5.my-addr.com/md5_decrypt-md5_cracker_online/md5_decoder_tool.php", headers= header, data= data)
    kq = response.text.split('Hashed string</span>: ')[1].split('</div>')[0]
    if "class='middle_title'>Hashed string</span>:" in (response.text):
        print(kq)
    else :
        print("MD5 chua duoc giai")
    
while True:
    th = []
    for i in range(threads):
        md5 = list_md5.pop(0)
        th += [threading.Thread(target= main, args= (md5,))]
    for i in range(len(th)):
        th[i].start()
    for i in range(len(th)):
        th[i].join()  
              
    