#!/usr/bin/python3
from dvtmstatus import StatusBar
import time

def ticker(writer):
    text = 'This is an example. '
    n = 0
    l = len(text)
    while True:
        writer.write(text[n:] + text[:n])
        n = (n + 1) % l
        time.sleep(0.5)

def clock(writer):
    while True:
        writer.write(time.ctime())
        time.sleep(1)

StatusBar('][ ', ticker, ' ][ ', clock, ' ').start()
