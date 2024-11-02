

# -*- coding: utf-8 -*-
"""http_requests_solution.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1vGdv4Nm_yD8kymZ1MI3RwydfALVsKe_n?usp=sharing
"""

import requests

"""**1. Perform a simple GET request**"""

# def perform_get_request():
#     resp = requests.get('https://httpbin.org/get')
#     print(resp.json())
#     return resp
def perform_get_request():
    url = 'https://httpbin.org/get'
    response = requests.get(url)
    return response

perform_get_request()

"""**2. Perform a GET request with parameters**"""

def perform_get_request_with_params():
    url = 'https://httpbin.org/get'
    params={'q': 'python'}
    response = requests.get(url, params=params)
    return response.json()

perform_get_request_with_params()

"""**3. Perform a POST request**"""

def perform_post_request():
    url = 'https://httpbin.org/post'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.post(url, data=data) #add in form
    return response.json()

perform_post_request()

"""**4. Perform a PUT request**"""

def perform_put_request():
    url = 'https://httpbin.org/put'
    data = {
        'first_name': 'Guido',
        'last_name': 'van Rossum'
    }
    response = requests.put(url, data=data) #add in form
    return response.json()

perform_put_request()

"""**5. Perform a PATCH request**"""

def perform_patch_request():
    url = 'https://httpbin.org/patch'
    data = {
        'first_name': 'Guido'
    }
    response = requests.patch(url, json=data) #add in json
    return response.json()

perform_patch_request()

"""**6. Perform a DELETE request**"""

def perform_delete_request():
    url = 'https://httpbin.org/delete'
    response = requests.delete(url)
    return response.json()

perform_delete_request()

"""**7. Inspect headers during a redirect request**"""

def perform_redirect_request():
    # HINT: you should use the allow_redirects parameter while doing the request
    url = 'https://httpbin.org/redirect/1'
    response = requests.get(url, allow_redirects=False) #allow_redirects set to False to prevent automatic redirection
    return response.headers['Location']

perform_redirect_request()

