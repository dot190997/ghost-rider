# ghost-rider
A flask-based web-app for ride-pooling management system

## Installation
Find requirements.txt file in ghost-rider directory and run the following command:
```bash
pip install -r requirements.txt
```
## Setup steps:

- cd to ghost-rider/app
- Set PYTHONPATH to pwd
- Updated port number as per your requirement in settings/dev_data_config.yml file
- Run the following command: python app.py -config settings/dev_data_config.yml
- Note: url_prefix=`/ghost-rider`

## List of exposed APIs along with the arguments:

- /healthcheck
- /get_user
- /get_all_users
- /get_vehicle
- /get_all_vehicles
- /add_user
- /add_vehicle
- /offer_ride
- /show_rides
- /select_ride
- /end_ride
- /get_user_stats
- /get_ride_details
- /get_ride_details_for_user
- /get_current_snapshot
