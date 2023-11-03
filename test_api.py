import requests
import pytest

class Test_api():

    # get user list
    def test_getuserlist(self):
        baseurl= "https://reqres.in/api/users?page=2"  #url which gets the user list

        response=requests.get(baseurl)  # calling GET request to get the user list

        data=response.json()  #storing the response in json format
        print(data)
        assert response.status_code==200 # validating whether the status code is 200
        assert response.json() # validating whether the response in json format

    # get single user from the list
    def test_singleuser(self):
        base_url = "https://reqres.in/api/users/2"
        expected_text = "To keep ReqRes free, contributions towards server costs are appreciated!"  # storing the response in a variable for assertion

        response = requests.get(base_url)
        data = response.json()
        support_text = data.get('support', {}).get('text', '')  # sorting the required text in a variable for the assertion

        assert support_text == expected_text  # validating whether the condition is true or not
        assert response.status_code==200

    # trying to fetch the user which not in list
    def test_usernotfound(self):
        baseurl="https://reqres.in/api/users/23"

        response=requests.get(baseurl)

        assert response.status_code==404
        assert response.status_code!=200  # validating whether the obtained status code is not equal to 200

    # creating new user
    def test_createuser(self):
        baseurl="https://reqres.in/api/users"
        body= {                             # storing the json content in a variable to pass to the request
            "name": "niyog",
            "job": "qa"
        }
        job='qa'  # storing the text in a variable for assertion
        name='niyog'

        response=requests.post(baseurl,body)
        print(response.json())
        data=response.json()
        expectedname=data.get('name','')
        expectedjob=data.get('job','')

        assert expectedname==name
        assert expectedjob==job
        assert response.status_code==201

    # update exsiting user
    def test_updateuser(self):
        baseurl="https://reqres.in/api/users/2"
        body={
            "name": "morpheus",
            "job": "zion resident"
        }

        name='morpheus'
        job='zion resident'

        response=requests.put(baseurl,body)  # calling PUT method
        print(response.json())

        data=response.json()
        expectedname=data.get('name','')
        expectedjob=data.get('job','')

        assert expectedname==name
        assert expectedjob==job

    # delete a user
    def test_deleteuser(self):
        baseurl='https://reqres.in/api/users/2'

        response=requests.delete(baseurl)  # calling delete method

        assert response.status_code==204
        assert response.status_code!=200

    # signup
    def test_userReg(self):
        baseurl="https://reqres.in/api/register"
        body={
            "email": "eve.holt@reqres.in",
            "password": "pistol"
        }

        id=4

        response=requests.post(baseurl,body)
        print(response.json())
        data=response.json()
        expectedid=data.get('id','')

        assert response.status_code==200
        assert expectedid==id
        if response.status_code not in [200,201]:  # if condition which check for the status code either 200 or 201 if not it will throw assertion error
            assert False

    # unsuccess signup
    def test_unsuccessfullreg(self):
        baseurl='https://reqres.in/api/register'
        body={
            "email": "niyog@google.com"
        }

        error='Missing password'

        response=requests.post(baseurl,body)
        print(response.json())
        data=response.json()

        expectederror=data.get('error','')

        assert expectederror==error
        assert response.status_code==400
        assert response.status_code!=200

    # login
    def test_userlogin(self):
        baseurl="https://reqres.in/api/login"
        body={
            "email": "eve.holt@reqres.in",
            "password": "cityslicka"
        }

        token='QpwL5tke4Pnpja7X4'

        response=requests.post(baseurl,body)
        print(response.json())
        data=response.json()
        expectedtoken=data.get('token','')

        assert expectedtoken==token
        assert response.status_code==200

    # login failed
    def test_userloginfailed(self):
        baseurl="https://reqres.in/api/login"
        body={
            "email": "eve.holt@reqres.in"
        }

        error='Missing password'

        response=requests.post(baseurl,body)
        print(response.json())
        data=response.json()
        expectederror=data.get('error','')

        assert response.status_code==400
        if response.status_code in [200,201]:
            assert False
        assert expectederror==error
