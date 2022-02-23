# test_sp-api

## description
Test connecting to amazon sp-api via python saleveawer

## deploy

### Windows
```sh
#Establishment package virtual environment
py pip install --user virtualenv
#Creating a virtual environment
py -m venv env
#Activation of the virtual environment
.\env\Scripts\activate
#Install basic project dependencies
py pip install -r requirements.txt
```

### UNIX
```sh
#Establishment package virtual environment
python3 -m pip install --user virtualenv
#Creating a virtual environment
python3 -m venv env
#Activation of the virtual environment
source env/bin/activate
#Install basic project dependencies
python3 -m pip install -r requirements.txt
```
After installation, you need to go to the main.py file and fill in the credentials variable 

Checking the receipt of a list of orders is implemented in the main.py file


The list of orders without restricted data works correctly. but getting RD token is not working showing error
'Application does not have access to one or more requested data elements: [shippingAddress]'

The probable cause of the error is incorrect formation of the signature in the file

venv/lib/site-packages/sp_api/base/aws_sig_v4.py 

or in a file
venv/lib/site-packages/sp_api/base/client.py

in the _sign_request, __init__ and _request methods
