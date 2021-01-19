import requests
import hashlib
import sys

def passchecker(query_pwd):
    url='https://api.pwnedpasswords.com/range/'+ query_pwd # website used to validate the password with SHA1 password
    res=requests.get(url,verify=False)
    if res.status_code!=200:
        raise RuntimeError(f'Error fetching:{res.status_code} check the api and try again..')
    return res

def  validate_password(password):
    sha1password=hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char,tail=sha1password[:5],sha1password[5:]
    response=passchecker(first5_char)
    return get_password_leak_count(response,tail)

def get_password_leak_count(res,has_check):
    hashes=(line.split(':') for line in res.text.splitlines())
    for item,count in hashes:
        if(item==has_check):
            return count
    return 0

def password_checker_main(args):
    for password in args:
        count=validate_password(password)
        if count :
            print(f'{password} was found {count} times... you need to change the password')
        else :
            print(f'{password} not found. carry on..')
    return 'done!'

       