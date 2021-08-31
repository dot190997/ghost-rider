# ghost-rider
A flask-based web-app for ride-pooling management system

## Installation
Find requirements.txt file in ghost-rider directory and run the following command:
```bash
pip install -r requirements.txt
```
## Setup steps:

- cd to ghost-rider/app
- Set PYTHONPATH to $pwd
- Update port number as per your requirement in settings/dev_data_config.yml file
- Run the following command: `python app.py -config settings/dev_data_config.yml`
- Note: url_prefix=`/ghost-rider`

## List of exposed APIs along with the arguments:
> All arguments are mandatory unless specified otherwise.

> Assume default data_type to be string unless otherwise specified.
- `/healthcheck`
    - **Request Type**: - GET
    - **Description**: Just for checking if server is up. Endpoint along with prefix will be `/ghost-rider/healthcheck`
    - **Arguments**: -


- `/get_user`
    - **Request Type**: GET
    - **Description**: Returns user details
    - **Arguments**: 
        - name


- `/get_all_users`
    - **Request Type**: - GET
    - **Description**: Returns a list with all user names
    - **Arguments**: -


- `/get_vehicle`
    - **Request Type**: GET
    - **Description**: Returns vehicle details
    - **Arguments**: 
        - registration_num


- `/get_all_vehicles`
    - **Request Type**: GET
    - **Description**: Returns a list with all vehicle registration numbers
    - **Arguments**: 


- `/add_user`
    - **Request Type**: POST
    - **Description**: Adds a user
    - **Arguments**:
        - name
        - age `int`
        - gender


- `/add_vehicle`
    - **Request Type**: POST
    - **Description**: Adds a vehicle
    - **Arguments**: 
        - name (owner of vehicle)
        - company
        - registration_num
        - capacity `int` `optional` `default: 5`


- `/offer_ride`
    - **Request Type**: POST
    - **Description**: Makes a vehicle available for a journey
    - **Arguments**: 
        - origin
        - destination
        - registration_num


- `/show_rides`
    - **Request Type**: GET
    - **Description**: Returns list of all available vehicles for given trip
    - **Arguments**: 
        - origin
        - destination
        - seats_required `int` `optional` `default: 1`
        - preference `optional` `default: vacancy`


- `/select_ride`
    - **Request Type**: POST
    - **Description**: Selects/books seats in some vehicle
    - **Arguments**:
        - name (customer, who wants to book)
        - registration_num
        - seats_required `int` `optional` `default: 1`


- `/end_ride`
    - **Request Type**: POST
    - **Description**: Ends the ride
    - **Arguments**:
        - name (any customer, who is riding)


- `/get_user_stats`
    - **Request Type**: GET
    - **Description**: Returns stats for a given user
    - **Arguments**: 
        - name 


- `/get_ride_details`
    - **Request Type**: GET
    - **Description**: Returns details for a given ride
    - **Arguments**: 
        - registration_num


- `/get_ride_details_for_user`
    - **Request Type**: GET
    - **Description**: Returns ride details for a given user
    - **Arguments**: 
        - name


- `/get_current_snapshot`
    - **Request Type**: GET
    - **Description**: Returns a list of all active rides with trip and vehicle details. Allows filter on trip and vehicles.
    - **Arguments**:
        - origin `optional`
        - destination `optional`
        - registration_num `optional`

## Assumptions and notes:
- As discussed, every user name is unique.
- Every registration number is unique.
- Things not handled, although easily resolvable, because of time constraint:
    - Case-sensitivity
    - Variable data-types (assuming things like age will be integers)
- Bulk APIs not provided. Easy to implement.
- Using registration_number for ride details, since 1 user can have multiple vehicles.
