import json
from . import routes
from flask import request
from models.management_system import ManagementSystem


@routes.route("/healthcheck")
def healthcheck():
    return "Success"


@routes.route('/get_user', methods=['GET'])
def get_user():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().get_user(request.args.get('name'))
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_all_users', methods=['GET'])
def get_all_users():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().show_all_users()
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_vehicle', methods=['GET'])
def get_vehicle():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().get_vehicle(request.args.get('registration_num'))
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_all_vehicles', methods=['GET'])
def get_all_vehicles():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().show_all_vehicles()
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/add_user', methods=['POST'])
def add_user():
    final_result = dict()
    final_result.setdefault('success', True)
    result = None
    request_obj = json.loads(request.data)
    try:
        ManagementSystem().add_user(request_obj.get('name', None), request_obj.get('gender', None),
                                    request_obj.get('age', None))
        result = 'User added'
    except Exception as e:
        final_result['success'] = False
        result = None
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/add_vehicle', methods=['POST'])
def add_vehicle():
    final_result = dict()
    final_result.setdefault('success', True)
    result = None
    request_obj = json.loads(request.data)
    try:
        ManagementSystem().add_vehicle(request_obj.get('name', None), request_obj.get('company', None),
                                       request_obj.get('registration_num', None),  request_obj.get('capacity', 5))
        result = 'Vehicle added'
    except Exception as e:
        final_result['success'] = False
        result = None
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/offer_ride', methods=['POST'])
def offer_ride():
    final_result = dict()
    final_result.setdefault('success', True)
    result = None
    request_obj = json.loads(request.data)
    try:
        ManagementSystem().offer_ride(request_obj.get('origin', None), request_obj.get('destination', None),
                                      request_obj.get('registration_num', None))
        result = 'Ride offer up for acceptance'
    except Exception as e:
        final_result['success'] = False
        result = None
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/show_rides', methods=['GET'])
def show_rides():
    final_result = dict()
    final_result.setdefault('success', True)
    result = []
    try:
        result = ManagementSystem().show_rides(request.args.get('origin', ''), request.args.get('destination', ''),
                                               request.args.get('seats_required', 1),
                                               request.args.get('preference', 'vacancy'))
    except Exception as e:
        final_result['success'] = False
        result = []
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/select_ride', methods=['POST'])
def select_ride():
    final_result = dict()
    final_result.setdefault('success', True)
    result = None
    request_obj = json.loads(request.data)
    try:
        ManagementSystem().select_ride(request_obj.get('name', None), request_obj.get('registration_num', None), request_obj.get('seats_required', 1))
        result = 'User added to ride'
    except Exception as e:
        final_result['success'] = False
        result = None
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/end_ride', methods=['POST'])
def end_ride():
    final_result = dict()
    final_result.setdefault('success', True)
    result = None
    request_obj = json.loads(request.data)
    try:
        ManagementSystem().end_ride(request_obj.get('name', None))
        result = 'Ride ended'
    except Exception as e:
        final_result['success'] = False
        result = None
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_user_stats', methods=['GET'])
def get_ride_stats():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().get_user_stats(request.args.get('name', None))
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_ride_details', methods=['GET'])
def get_ride_details():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().get_ride_details(request.args.get('registration_num', None))
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_ride_details_for_user', methods=['GET'])
def get_ride_details_for_user():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().get_ride_details_for_user(request.args.get('name', None))
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)


@routes.route('/get_current_snapshot', methods=['GET'])
def show_current_snapshot():
    final_result = dict()
    final_result.setdefault('success', True)
    result = {}
    try:
        result = ManagementSystem().show_current_snapshot(request.args.get('origin', None),
                                                          request.args.get('destination', None),
                                                          request.args.get('registration_num', None))
    except Exception as e:
        final_result['success'] = False
        result = {}
        final_result.setdefault('error', str(e))
    finally:
        final_result.setdefault('result', result)

    return json.dumps(final_result)





