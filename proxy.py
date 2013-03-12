def test_proxy(prxoy):
  try:
    proxy = urllib2.ProxyHandler({'http': str(proxy)})
    opener = urllib2.build_opener(proxy)
    urllib2.install_opener(opener)
  except Exception:
    return False
  return True

def load_proxy(file_name):
  with open(file_name) as p:
    proxies = []
    for line in proxies:
      if line.startswith('http://'):
        line = line[7::]
      if len(line) > 1:
        port = line.split(':')[-1]
      else:
        port = 80
    
