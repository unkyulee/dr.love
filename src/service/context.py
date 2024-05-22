# Define global context
_config = {
    'A': {
        'value': 0,
        'active': False,
        'diff': 0
    },
    'B': {
        'value': 0,
        'active': False,
        'diff': 0
    },
    'DISPLAY': {
        'screen': 1,
        'brightness': 1
    },
    'LOVER': {
        "A": {
            "start": 0,
            "end": 0
        },
        "B": {
            "start": 0,
            "end": 0
        }
    }
}

# SCREENS
S_WELCOME = 1
S_CALIBRATION = 2
S_MEASURING = 3
S_LOVE = 4
S_SORRY = 5
S_ONE = 6

# Function to get configuration settings
def get():
    return _config
