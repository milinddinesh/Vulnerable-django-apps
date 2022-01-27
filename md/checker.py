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
