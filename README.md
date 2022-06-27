# Shipment Backend Application.

This is the shipment backend application.


### Requirements for setting up the project.
1. Python3. 
2. Django
3. Virtualenv.
4Postgres DB

### Installation on Mac

1 . First clone this repository 

```
$ git clone https://github.com/huxaiphaer/shipmentapp.git
```

2 . Add the following variables in your Environment Variables permanently:

```
DATABASE_URL=postgresql://captiq:namungoona@localhost:5432/shipment
DEBUG=True
ACCESS_TOKEN_LIFETIME=2
REFRESH_TOKEN_LIFETIME=2
SECRET_KEY=hey
```

After, setting up the environment variables add create a Postgres Database called `huxy_tours`, followed by running SQLAlchemy migrations with the commands 
below to create all the necessary tables :


**NOTE :**
- The commands below won't run unless  you have your Redis server running and as well
as setting all the environment variables above.

```
$ ./manage.py migrate

```


3 . Then, create a virtual environment and install in on Mac :

```
$ virtualenv env
$ source env/bin/activate
```

4.  After activating the `virtualenv`, then install the necessary dependencies :

```
$ pip3 install -r requirements.txt
```

#### Run tests.

```
$ ./manage.py test
```


 #### Endpoints.

| HTTP Method   | End Point                      | Action                  |
|---------------|--------------------------------|-------------------------|
| POST          | /api/v1/users/create/          | Create a user           |
| POST          | /api/v1/users/login/           | Login a user            |
| POST          | /api/v1/shipments/             | Submit a shipment       |
| GET           | /api/v1/shipments/             | Get all shipments.      |
| GET           | /api/v1/shipments/<uuid:uuid>/ | Get shipment by uuid    |
| EDIT OR PATCH | /api/v1/shipments/<uuid:uuid>/ | Edit shipment by uuid   |
| DELETE        | /api/v1/shipments/<uuid:uuid>/ | Delete shipment by uuid |


### Contributors 

* [Lutaaya Idris](https://github.com/huxaiphaer)