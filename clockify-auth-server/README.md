# Server

## Create Virtual Environment
Follow the instruction in der [Docs](https://docs.python.org/3/tutorial/venv.html):

    $ python -m venv venv

    $ source venv/bin/activate

Freeze the requirements:
    $ pip freeze > requirements.txt

## Install Flask
Follow the instruction in der [Docs](http://flask.pocoo.org/):

    $ pip install Flask

## Run Server
Start flask server: 

    $ flask run

## Deploy

Zip the `functions` folder.

    $ cd functions
    $ zip -q -r ../functions.zip .
    $ cd ..
    $ cd venv/lib/python3.8/site-packages/
    $ zip -q -r ../../../../functions.zip .
    $ cd ../../../../

In [AWS Lambda](https://eu-west-1.console.aws.amazon.com/lambda) update the function:
1. Select the function code <br>
2. Actions -> upload zip <br>
3. Select `functions.zip` <br>
4. Publish new Version <br>

At the first time add a Trigger: 
1. Select **API-Gateway** <br>
2. Under API choose **Create an API** <br>
3. Select **REST API** <br>
4. Under Security choose **Open** <br>
5. In **Additional settings** name **Deployment stage**: *PROD* or *DEV*
6. Press on **Add** <br>

## Test 

With Postman. 

