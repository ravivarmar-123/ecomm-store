# Ecommerce Store with Django
This is an Ecommerce store based on `Django 2.2` and `python 3.6`


## Features
* Categorizing products by adding categories and subcategories
* Adding Products with details and pictures
* User Review for products
* Searching for Products
* User favorite list
* Saving user addresses

## Installation
1. Clone the repository and navigate to the directory:

    ```
    git clone https://github.com/ravivarma-r/ecomm-store.git
    cd ecommerce_store
    ```
1. Setup virtual env and install dependancies:

    ```
    virtualenv smoothquarentine
    ```
1. Install Dependencies:

    ```
    sudo pip install -r requirements.txt .
    ```
1. migrate django project:

    ```
    python manage.py makemigrations
    python manage.py migrate
    ```
1. run docker image:

    ```
    python manage.py runserver
    ```
1. Navigate to [localhost](http://localhost:8000) to see the homepage
1. Admin dashboard is available at [localhost/admin](http://localhost:8000/admin). to access the dashboard, first create a superuser:

    ```
    python manage.py createsuperuser
    ```
