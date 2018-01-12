class XXX:
 def login(self):

  r = self.s.get('https://nosec.org/users/sign_in')
  html = r.text
  p1 = re.compile(r'city_token" value="(.*?)"')
  res = re.search(p1,html)
  authenticity_token = str(res.group(1))
  print 'authenticity_token:',authenticity_token
  # print 'cookies',self.s.cookies
  # print s.cookies
  data = {
   'authenticity_token':authenticity_token,
   'user[login]':'xxxxx',
   'user[password]':'xxxxx'
  }
  r = self.s.post('https://nosec.org/users/sign_in',data=data)
  # print r.headers
  # print r.request.headers
  # print self.s.cookies
  print '[*] OK!'
  return True