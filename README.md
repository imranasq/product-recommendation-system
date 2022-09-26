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

Rename `.env.example` file as `.env` and update these values.
```env
# Comma separated hosts or IPs, set * to allow all
ALLOWED_HOSTS=127.0.0.1
DEBUG=True
# Secret key should be atleast 32 characters long and consists of alphanumeric and special characters
SECRET_KEY=****
WEATHER_API_KEY=
```
If you do any update on models run this command
```sh
python manage.py makemigrations
```
Run migrations to apply changes on database
```sh
python manage.py migrate
```

### Load Initial Data
Here you can load some initial data to your database. This step is not mandatory. It's only for reduce set up times.
```sh
python manage.py loaddata user/fixtures/user.json
```
Create a super user
```sh
python manage.py createsuperuser
```
Run the project.
```sh
python manage.py runserver
```
## Now You are good to go!

### Additional instruction
1. Since this project has no user interface you should use `Postman` or any third party API tools to use it.
1. Swagger documentation is provided, so you can see the API documentation by simply going `running_url/swagger/` by your browser. `running_url` will be the url where the project is currently running.
1. You can also download the API documentation by hitting `running_url/schema/` endpoint. `running_url` will be the url where the project is currently running.

### Some Constrains 
1. Since this project's Authentication is based on JSON Web Token, the lifetime of access token is set at 5 minutes. You need to generate access token using your refresh token(You can find it while log in).
2. If you log out with your credentials(access token) your refresh token will be black listed. You can not use that refresh token again. So generate another by simply logging in.
3. The `user_type` field is pre-defined. You need to choose between `Admin, Vendor and Customer`. Other value won't work!
4. The `weather` field is pre-defined. You need to choose between `Hot, Normal and Cold`. Other value won't work!

### Unit Test
Run unit tests
```sh
pytest
```