import requests

def auth_api(url, data):
    """Authorization in the api rest

    Args:
        url (str): path of login in api
        data (dict): body of request

    Returns:
        json: json with response with user and his atribute
    """
    response = requests.post(url, json=data)
    return response.json()

def refresh(url, token_refresh):
    """refresh token access api

    Args:
        url (str): path of refresh token 
        token_refresh (str): token refresh

    Returns:
        json: json with new token access 
    """
    head = {'Authorization': 'Bearer {}'.format(token_refresh)}
    response = requests.get(url, headers=head)
    return response.json()

def get_clients(url, token_access):
    """get clients by page

    Args:
        url (str): path of get clients by page  
        token_access (str): token access

    Returns:
        json: json with all clients of page
    """
    head = {'Authorization': 'Bearer {}'.format(token_access)}
    response = requests.get(url, headers=head)
    return response.json()

def get_sales(url,token_access):
    """get sales by page

    Args:
        url (str): path of get clients by page  
        token_access (str): token access

    Returns:
        json: json with all sales of page
    """
    head = {'Authorization': 'Bearer {}'.format(token_access)}
    response = requests.get(url, headers=head)
    return response.json()