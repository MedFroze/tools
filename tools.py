#!python
import os,sys,time,random
from random import choice
from time import sleep

m = '\033[1;31m'
h = '\033[1;32m'
k = '\033[1;33m'
u = '\033[1;34m'
b = '\033[1;35m'
c = '\033[1;36m'
p = '\033[1;37m'

def loop():
    print("")
    print(f" {p}[•] {k}Lagi? {p}({h}y{p}/{m}t{p}]")
    l = input(f" {p}<•> {u}")
    if(l=="y"):
      time.sleep(3)
      kasir()
    elif(l=="t"):
      time.sleep(3)
      awal()
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def awal():
    print(f" {c}")
    os.system("clear")
    os.system("figlet TOOLS")
    os.system("bash waktu.sh")
    print("")
    print(f"   {p}[ {c}Menu{p} ]")
    print(f" {p}[1] {k}Kasir")
    print(f" {p}[2] {k}Games")
    print(f" {p}[0] {b}Exit")
    print("")
    print(f" {p}[•] {k}Masukan pilihan anda")
    x = int(input(f" {p}<•> {u}"))
    if(x==1):
      time.sleep(3)
      kasir()
    elif(x==2):
      time.sleep(3)
      games()
    elif(x==0):
      time.sleep(3)
      os.system("clear")
      os.system("exit")
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def kasir():
    print(f"{c}")
    os.system("clear")
    os.system("figlet KASIR")
    os.system("bash waktu.sh")
    print("")
    print(f"                     {p}[ {c}Menu {p}]")
    print(f" {p}[1] {k}Pempek                    {p}[{h}Rp 100.000{p}]")
    print(f" {p}[2] {k}Martabak                  {p}[{h}Rp 115.000{p}]")
    print(f" {p}[3] {k}Pizza kecil               {p}[{h}Rp  45.000{p}]")
    print(f" {p}[4] {k}Pizza besar + Minuman     {p}[{h}Rp  95.000{p}]")
    print(f" {p}[5] {k}Nasi Goreng               {p}[{h}Rp  25.000{p}]")
    print(f" {p}[0] {b}Back")
    print("")
    print(f" {p}[•] {k}Masukan angka yang ingin anda order")
    order = int(input(f" {p}<•> {u}"))
    if(order==1):
      time.sleep(3)
      pempek()
    elif(order==2):
      time.sleep(3)
      martabak()
    elif(order==3):
      time.sleep(3)
      pizza_kecil()
    elif(order==4):
      time.sleep(3)
      pizza_besar()
    elif(order==5):
      time.sleep(3)
      nasgor()
    elif(order==0):
      time.sleep(3)
      awal()
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def pempek():
    print("")
    print(f" {p}[•] {k}Masukan uang pembayaran anda")
    g = int(input(f" {p}<•> {u}"))
    if(g>100000):
      time.sleep(3)
      j = g-100000
      print("")
      print(f" {p}[•] {k}Berhasil membeli pempek dengan harga {h}Rp 100.000")
      print(f" {p}[•] {k}Uang anda: {h}{g}")
      print(f" {p}[•] {k}Kembalian: {h}{j}")
      time.sleep(3)
      loop()
    elif(g==100000):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Berhasil membeli pempek dengan harga {h}Rp 100.000")
      print(f" {p}[•] {k}Uang anda: {h}{g}")
      print(f" {p}[•] {k}Kembalian: {p}-")
      time.sleep(3)
      loop()
    elif(g<100000):
      time.sleep(3)
      print("")
      print(f" {p}[!] {m}Uang anda tidak cukup")
      time.sleep(3)
      loop()

def martabak():
    print("")
    print(f" {p}[•] {k}Masukan uang pembayaran anda")
    ga = int(input(f" {p}<•> {u}"))
    if(ga>115000):
      time.sleep(3)
      print("")
      ja = ga-115000
      print(f" {p}[•] {k}Berhasil membeli martabak dengan harga {h}Rp 115.000")
      print(f" {p}[•] {k}Uang anda: {h}{ga}")
      print(f" {p}[•] {k}Kembalian: {h}{ja}")
      time.sleep(3)
      loop()
    elif(ga==115000):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Berhasil membeli martabak dengan harga {h}Rp 115.000")
      print(f" {p}[•] {k}Uang anda: {h}{ga}")
      print(f" {p}[•] {k}Kembalian: {p}-")
      time.sleep(3)
      loop()
    elif(ga<115000):
      time.sleep(3)
      print("")
      print(f" {p}[!] {m}Uang anda tidak cukup")
      time.sleep(3)
      loop()

def pizza_kecil():
    print("")
    print(f" {p}[•] {k}Masukan uang pembayaran anda")
    gb = int(input(f" {p}<•> {u}"))
    if(gb>45000):
      time.sleep(3)
      jb = gb-45000
      print("")
      print(f" {p}[•] {k}Berhasil membeli pizza kecil dengan harga {h}Rp 45.000")
      print(f" {p}[•] {k}Uang anda: {h}{gb}")
      print(f" {p}[•] {k}Kembalian: {h}{jb}")
      time.sleep(3)
      loop()
    elif(gb==45000):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Berhasil membeli pizza kecil dengan harga {h}Rp 45.000")
      print(f" {p}[•] {k}Uang anda: {h}{gb}")
      print(f" {p}[•] {k}Kembalian: {p}-")
      time.sleep(3)
      loop()
    elif(gb<45000):
      time.sleep(3)
      print("")
      print(f" {p}[!] {m}Uang anda tidak cukup")
      time.sleep(3)
      loop()

def pizza_besar():
    print("")
    print(f" {p}[•] {k}Masukan uang pembayaran anda")
    gc = int(input(f" {p}<•> {u}"))
    if(gc>95000):
      time.sleep(3)
      jc = gc-95000
      print("")
      print(f" {p}[•] {k}Berhasil membeli pizza besar + minuman dengan harga {h}Rp 95.000")
      print(f" {p}[•] {k}Uang anda: {h}{gc}")
      print(f" {p}[•] {k}Kembalian: {h}{jc}")
      time.sleep(3)
      loop()
    elif(gc==95000):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Berhasil membeli pizza besar + minuman dengan harga {h}Rp 95000")
      print(f" {p}[•] {k}Uang anda: {h}{gc}")
      print(f"{p} [•] {k}Kembalian: {p}-")
      time.sleep(3)
      loop()
    elif(gc<95000):
      time.sleep(3)
      print("")
      print(f" {p}[!] {m}Uang anda tidak cukup")
      time.sleep(3)
      loop()

def nasgor():
    print("")
    print(f" {p}[•] {k}Masukan uang pembayaran anda")
    gd = int(input(f" {p}<•> {u}"))
    if(gd>25000):
      time.sleep(3)
      jd = gd-25000
      print("")
      print(f" {p}[•] {k}Berhasil membeli nasi goreng dengan harga {h}Rp 25.000")
      print(f" {p}[•] {k}Uang anda: {h}{gd}")
      print(f" {p}[•] {k}Kembalian: {h}{jd}")
      time.sleep(3)
      loop()
    elif(gd==25000):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Berhasil membeli nasi goreng dengan harga {h}Rp 25.000")
      print(f" {p}[•] {k}Uang anda: {h}{gd}")
      print(f" {p}[•] {k}Kembalian: {p}-")
      time.sleep(3)
      loop()
    elif(gd<25000):
      time.sleep(3)
      print("")
      print(f" {p}[!] {m}Uang anda tidak cukup")
      time.sleep(3)
      loop()

def games():
    print(f"{c}")
    os.system("clear")
    os.system("figlet GAMES")
    os.system("bash waktu.sh")
    print("")
    print(f" {p}[ {c}Games {p}]")
    print(f" {p}[1] {k}Batu Gunting Kertas (Versi Indonesia)")
    print(f" {p}[2] {k}Batu Gunting Kertas (Versi Jawa)")
    print(f" {p}[3] {k}Rock Paper Scissors (Versi Internasional)")
    print(f" {p}[0] {b}Back")
    print("")
    print(f" {p}[•] {k}Masukan pilihan anda")
    q = int(input(f" {p}<•> {u}"))
    if(q==1):
      time.sleep(3)
      bgk_indo()
    elif(q==2):
      time.sleep(3)
      bgk_jawa()
    elif(q==3):
      time.sleep(3)
      bgk_inter()
    elif(q==0):
      time.sleep(3)
      awal()
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def bgk_indo():
    bota = random.choice(["batu","gunting","kertas"])
    print(f"")
    print(f" {p}[•] {k}Pilihan: {h}Batu, Gunting, Kertas")
    print(f" {p}[•] {k}Tingkatan: {b}Batu -> Gunting -> Kertas -> Batu")
    print(f"")
    print(f" {p}[•] {k}Masukan pilihan anda")
    bgka = input(f" {p}<•> {u}")
    if(bgka=="batu"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Anda memilih: {b}{bgka}")
      if(bota=="batu"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print(f"")
        print(f" {p}[•] {k}Hasil: {p}SERI")
        loop_games()
      elif(bota=="gunting"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print("")
        print(f" {p}[•] {k}Hasil: {h}MENANG")
        loop_games()
      elif(bota=="kertas"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print("")
        print(f" {p}[•] {k}Hasil: {m}KALAH")
    elif(bgka=="gunting"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Anda memilih: {b}{bgka}")
      if(bota=="batu"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print(f"")
        print(f" {p}[•] {k}Hasil: {m}KALAH")
        loop_games()
      elif(bota=="gunting"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print("")
        print(f" {p}[•] {k}Hasil: {p}SERI")
        loop_games()
      elif(bota=="kertas"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print("")
        print(f" {p}[•] {k}Hasil: {h}MENANG")
    elif(bgka=="kertas"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Anda memilih: {b}{bgka}")
      if(bota=="batu"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print(f"")
        print(f" {p}[•] {k}Hasil: {h}MENANG")
        loop_games()
      elif(bota=="gunting"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print("")
        print(f" {p}[•] {k}Hasil: {m}KALAH")
        loop_games()
      elif(bota=="kertas"):
        print(f" {p}[•] {k}Bot memilih : {b}{bota}")
        print("")
        print(f" {p}[•] {k}Hasil: {p}SERI")
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def bgk_jawa():
    botb = random.choice(["gajah","manusia","semut"])
    print("")
    print(f" {p}[•] {k}Pilihan: {h}Gajah, Manusia, Semut")
    print(f" {p}[•] {k}Tingkatan: {b}Gajah -> Manusia -> Semut -> Gajah")
    print("")
    print(f" {p}[•] {k}Masukan pilihan anda")
    bgkb = input(f" {p}<•>  {u}")
    if(bgkb=="gajah"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Anda memilih: {b}{bgkb}")
      if(botb=="gajah"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print(f"")
        print(f" {p}[•] {k}Hasil: {p}SERI")
        loop_games()
      elif(botb=="manusia"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print("")
        print(f" {p}[•] {k}Hasil: {h}MENANG")
        loop_games()
      elif(botb=="semut"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print("")
        print(f" {p}[•] {k}Hasil: {m}KALAH")
        loop_games()
    elif(bgkb=="manusia"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Anda memilih: {b}{bgkb}")
      if(botb=="gajah"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print(f"")
        print(f" {p}[•] {k}Hasil: {m}KALAH")
        loop_games()
      elif(botb=="manusia"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print("")
        print(f" {p}[•] {k}Hasil: {p}SERI")
        loop_games()
      elif(botb=="semut"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print("")
        print(f" {p}[•] {k}Hasil: {h}MENANG")
        loop_games()
    elif(bgkb=="semut"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}Anda memilih: {b}{bgkb}")
      if(botb=="gajah"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print(f"")
        print(f" {p}[•] {k}Hasil: {h}MENANG")
        loop_games()
      elif(botb=="manusia"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print("")
        print(f" {p}[•] {k}Hasil: {m}KALAH")
        loop_games()
      elif(botb=="semut"):
        print(f" {p}[•] {k}Bot memilih : {b}{botb}")
        print("")
        print(f" {p}[•] {k}Hasil: {p}SERI")
        loop_games()
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def bgk_inter():
    botc = random.choice(["rock","paper","scissor"])
    print("")
    print(f" {p}[•] {k}Selection: {h}Rock, Scissor, Paper")
    print(f" {p}[•] {k}Level: {b}Rock -> Scissor -> Paper -> Rock")
    print(f"")
    print(f" {p}[•] {k}Please input your selection")
    bgkc = input(f" {p}<•> {u}")
    if(bgkc=="rock"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}You are choosing: {b}{bgkc}")
      if(botc=="rock"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {p}DRAW")
        loop_games()
      elif(botc=="paper"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {m}LOSE")
        loop_games()
      elif(botc=="scissor"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {h}WIN")
        loop_games()
    elif(bgkc=="paper"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}You are choosing: {b}{bgkc}")
      if(botc=="rock"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {h}WIN")
        loop_games()
      elif(botc=="paper"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {p}DRAW")
        loop_games()
      elif(botc=="scissor"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {m}LOSE")
        loop_games()
    elif(bgkc=="scissor"):
      time.sleep(3)
      print("")
      print(f" {p}[•] {k}You are choosing: {b}{bgkc}")
      if(botc=="rock"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {m}LOSE")
        loop_games()
      elif(botc=="paper"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {h}WIN")
        loop_games()
      elif(botc=="scissor"):
        print(f" {p}[•] {k}Bot is choosing : {b}{botc}")
        print("")
        print(f" {p}[•] {k}Result: {p}DRAW")
        loop_games()
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

def loop_games():
    time.sleep(3)
    print("")
    print(f" {p}[•] {k}Lagi? {p}({h}y{p}/{m}t{p}]")
    l = input(f" {p}<•> {u}")
    if(l=="y"):
      time.sleep(3)
      games()
    elif(l=="t"):
      time.sleep(3)
      awal()
    else:
      time.sleep(3)
      print(f" {p}[!]{m}InputError")
      time.sleep(3)
      os.system("clear")
      os.system("exit")

if __name__=="__main__":
    awal()
