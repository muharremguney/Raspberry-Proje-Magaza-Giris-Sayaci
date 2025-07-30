import RPi.GPIO as GPIO
import time
import smtplib
import datetime
import pygame

def blink(pin):
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(pin, GPIO.LOW)
    time.sleep(1)
    return

counter = 1
while True:
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(16, GPIO.IN)
    m = "Musteri"

    if GPIO.input(16):
        print counter, m
        counter = counter + 1
        GPIO.cleanup()
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(18, GPIO.OUT)
        for i in range(0, 1):
            blink(18)
        GPIO.cleanup()
        pygame.mixer.init()
        pygame.mixer.music.load("/home/pi/Desktop/hosgeldiniz.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
    if (datetime.datetime.now().strftime("%H:%M:%S") == "03:07:01"):
        counter= counter - 1
        content = str(counter)
        mail = smtplib.SMTP("smtp.gmail.com",587)
        mail.ehlo()
        mail.starttls()
        mail.login("mhrmgny74@gmail.com","sifre gir")
        mail.sendmail("mhrmgny74@gmail.com","mhrm74123@gmail.com",content)
        print("Gun Sonunda Giris Yapan Musteri Sayisi Mail Olarak Gonderildi.")
        break

    time.sleep(1)


