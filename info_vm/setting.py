CONF_PATH = 'test.conf'

STATE_MAPPER = {
    0: 'NONE',
    1: 'RUNNING',
    2: 'BLOCKED',
    3: 'PAUSED',
    4: 'SHUTDOWN',
    5: 'SHUTOFF',
    6: 'CRASHED',
    7: 'SUSPENDED'
}

UNITS = {
    'Ki': 1024,  # Binary kilo unit
    'Mi': 1024 ** 2,  # Binary mega unit
    'Gi': 1024 ** 3,  # Binary giga unit
    'Ti': 1024 ** 4,  # Binary tera unit
}
