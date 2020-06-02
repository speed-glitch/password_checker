import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError('Error Fetching:{}'.format(res.status_code))
    return res

def get_passwords_leaks_count(hashes,hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h,count in hashes:
        #print(h, count)
        if h == hash_to_check:
            return count
    return 0

# def read_res(response):
#     print(response.text)

def pwned_api_check(password):
    #print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first5_char)
    #print(first5_char,tail)
    print(response)
    return get_passwords_leaks_count(response,tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print('{} was found {}times.. you should probably change your password'.format(password,count))
        else:
            print('{} was not found. Carry on!'.format(password))

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
    
#pwned_api_check('123')

# import requests
# import hashlib

# def request_api_data(query_char):
#     url = 'https://api.pwnedpasswords.com/range/' + query_char
#     res = requests.get(url)
#     if res.status_code != 200:
#         raise RuntimeError('Error Fetching:{}'.format(res.status_code))
#     return res
# def pwned_api_check(password):
#     print(hashlib.sha1(password.encode('utf-8')).hexdigest().upper())
    
# pwned_api_check('tejaswini')