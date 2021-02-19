import requests

def doPostRequest():
    url ="http://httpbin.org/post"

    url = 'http://httpbin.org/post'
    myobj = {'first_name': 'Humphrey','second_name': 'Mugambi','age': '34' }

    response = requests.post(url, data=myobj)
    print(f"The secret message is: {response.text}")

    
if __name__ == "__main__":
    doPostRequest()