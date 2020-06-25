import sys
import config.loader as loader

def get():
  target = loader.load()
  if len(sys.argv) > 1:
    target['url'] = sys.argv[1]
  return target
