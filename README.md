# Product Recommendation System
## Getting Started
### Python Installation
* The project runs on [Python 3.10](https://www.python.org/downloads/).

### Running the project
Clone the repository.

```sh
https://github.com/imranasq/product-recommendation-system.git
```
Create and activate a virtual environment for the project.

For creating virtual environment we can use packages like [Virtualenv](https://pypi.org/project/virtualenv/) or [Pyenv](https://github.com/pyenv/pyenv). I've used Virtualenv.
### For Linux System
```sh
cd product-recommendation-system
virtualenv venv
source venv/bin/activate
```

### For Windows System
```sh
cd product-recommendation-system
python -m virtualenv venv
source venv/Scripts/activate
```
Install all required packages.

```sh
pip install -r requirements.txt
```
### Database
This project will set up on default Sqlite3. No need to worry about set up database by own.

Rename `.env.example` file as `.env` and update these values.
```env
# Comma separated hosts or IPs, set * to allow all
ALLOWED_HOSTS=127.0.0.1
DEBUG=True
# Secret key should be atleast 32 characters long and consists of alphanumeric and special characters. You can use the given Secret key
SECRET_KEY=****
# You can use the given API key. 
WEATHER_API_KEY=
```

Run migrations
```sh
python manage.py migrate
```

### Load Initial Data
Here you can load some initial data to your database. This step is not mandatory. It's only for reduce set up times and giving you initial 3 types of user.
```sh
python manage.py loaddata user/fixtures/users.json
```
Create a super-user
```sh
python manage.py createsuperuser
```
Run the project. It's better if the Port is 8000
```sh
python manage.py runserver 8000
```
## Now You are good to go!
You can log in with(If you already load the user fixture)
```sh
Admin 
email: admin@mail.com
password: admin@123
```
or
```sh
Vendor
email: vendor@mail.com
password: admin@123
```
or
```sh
Customer
email: customer@mail.com
password: admin@123
```
or
```sh
Your Newly created super-user credentials. You have to set the `user_type` as `Admin` from admin panel for further operation with super admin.
```
### Additional instruction
1. Since this project has no user interface you should use [Postman](https://www.postman.com/downloads/?utm_source=postman-home) or any third party API tools to use it.
2. Swagger documentation is provided, so you can see the API documentation by simply going [swagger_doc](http://127.0.0.1:8000/swagger/) by your browser. 
3. You can also download the API documentation by hitting [api_document_yaml](http://127.0.0.1:8000/schema/) endpoint.

### Some Constraints 
1. Since this project's Authentication is based on JSON Web Token, the lifetime of access token is set at 5 minutes. You need to generate access token using your refresh token(You can find it while log in).
2. If you log out with your credentials(access token) your refresh token will be black listed. You can not use that refresh token again. So generate another by simply logging in.
3. The `user_type` field is pre-defined. You need to choose between `Admin, Vendor and Customer` while register a user. Other value won't work!
4. The `weather` field is pre-defined. You need to choose between `Hot, Normal and Cold` while create a weather type as Admin. Other value won't work!

### Unit Test
Run unit tests
```sh
pytest
```

## API Documentation
You can test APIs in swagger. Just go to the [URL](http://127.0.0.1:8000/swagger/) specified before. 
