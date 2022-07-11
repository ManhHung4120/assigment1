def get_data():
    return {"key": "value"}


def get_data_list():
    return [
        {"number": 1},
        {"number": 2},
        {"number": 3},
        {"number": 4},
    ]
DATA = [
    (1,{
        "check": {},
        "input":[
            ],
    },
        False,
        """"""
    ),
    (2,{
        "check": {"key": "value"},
        "input":[
        {"number": 1},
        {"number": 2},
        {"number": 3},
        {"number": 4},
            ],  
    },
        True,
    """1
Found
4
9
16
"""
    ),
    (3,{
        "check": {"key": "value"},
        "input":[
        {"number": 5},
        {"number": 2},
        {"number": 3},
        {"number": 4},
            ],  
    },
        True,
    """25
4
9
16
"""
    ),
]
