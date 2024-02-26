import sys, hashlib, getpass

def get_hashed_text(text:str):
    return hashlib.sha256(text.encode()).hexdigest()

while 1:
   key = getpass.getpass('[+] Enter key: ')
   if get_hashed_text(key) != '967b3f776748eb3690b605a1f06d243a5963951772cf6ecae557bced29fe54e2':
      sys.stderr,write(f'your given key "{key}" is incorrect.\n')
   
   else:
       break
