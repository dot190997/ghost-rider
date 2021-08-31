import re
import uuid
from datetime import date
from multiprocessing import Process


def is_token_nan(token):
    return not token or token != token


def clean_string5(s, tokenize=True):
    s = re.sub(r'[-.(),/\\&`~!@#$%^*?"|=+:;]', ' ', s)
    s = re.sub(r'[\']', '', s)
    s = re.sub(r'<[^>]+>', '', s)
    s = s.strip().lower()
    if tokenize:
        s = re.sub(r'\s+', '_', s)
    else:
        s = re.sub(r'\s+', ' ', s)
    return s


def random_id_generator():
    _id = str(uuid.uuid4())
    return _id


def get_initial_set_field(value, _type):
    initializing_value = set()
    if isinstance(value, _type):
        initializing_value.add(value)
    elif isinstance(value, set) or isinstance(value, list):
        initializing_value = set(value)
    return initializing_value


def get_date(normalized=True):
    if normalized:
        return str(date.today()).replace('-', '')
    return str(date.today())


def run_in_parallel(*fns):
    process_list = []
    for fn in fns:
        p = Process(target=fn)
        p.start()
        process_list.append(p)
    for p in process_list:
        p.join()


def str2bool(v):
    if isinstance(v, bool):
       return v
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise ValueError("Invalid boolean input")
