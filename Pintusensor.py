from playsound import playsound
import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) #acuan pin Broadcom
GPIO.setup(23, GPIO.OUT) #Lampu1
GPIO.setup(24, GPIO.OUT) #Lampu2
GPIO.setup(25, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sen1
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sen4
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sen3
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #Sen2

def LamOFF():
    GPIO.output(23, 0)
    GPIO.output(24, 0)

def LamON():
    GPIO.output(23, 1)
    sleep(0.05)
    GPIO.output(23, 0)
    sleep(0.05)
    GPIO.output(23, 1)
    sleep(0.05)
    GPIO.output(23, 0)
    sleep(0.05)
    GPIO.output(23, 1)
    sleep(0.05)
    GPIO.output(23, 0)
    sleep(0.1)
    GPIO.output(24, 1)
    sleep(0.05)
    GPIO.output(24, 0)
    sleep(0.05)
    GPIO.output(24, 1)
    sleep(0.05)
    GPIO.output(24, 0)
    sleep(0.05)
    GPIO.output(24, 1)
    sleep(0.05)
    GPIO.output(24, 0)
    sleep(0.1)

try:
    while True:
        sen1 = GPIO.input(25)
        sen2 = GPIO.input(17)
        sen3 = GPIO.input(27)
        sen4 = GPIO.input(22)
        if (sen1==sen2==sen3==sen4==0): #NILAI ASLI ADALAH 0, SENGAJA DIGANTI UNTUK TES SAJA
            print('Semua Pintu Terbuka')
            LamON()
            playsound("/home/belajarku/semua.mp3")
            LamON()
        else:

            if(sen1==0 or sen2==0 or sen3==0 or sen4==0):
                print('Salahsatu Pintu Terbuka')
                LamON()
                playsound("/home/belajarku/salahsatu.mp3")
                LamON()
            else:

                if(sen1==sen2==sen3==sen4==1): #NILAII ASLI ADALAH 1, SENGAJA DIGANTI UNTUK TES SAJA
                    print('Sistem Aman Jaya')
                    LamOFF()
                    sleep(0.1) #PEMBERI JEDA DURASI
            


except KeyboardInterrupt:
    x = "Program Pemantauan Di Nonaktifkan"
    notif = x.center(500)
    print (x)
    GPIO.cleanup()
