import logging

def setup():
  logging.basicConfig(format='[%(asctime)-15s] %(message)s')

def info(message):
  logging.log(50, message)
