import hashlib

email ="killer@gamil.com"
psd ="kiler123"
psd1 ="kiler123"
psd_encode=psd.encode()
psd_hash=hashlib.md5(psd_encode).hexdigest()



user_email ="killer@gamil.com"
user_pass = hashlib.md5(psd1.encode()).hexdigest()

if user_email == email and psd_hash ==user_pass:
      print("right user")
else: 
      print("wrong user")