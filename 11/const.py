"""A combo is when two directons combine to form a single direction."""
COMBOS = {
    'nwne': 'n',
    'nenw': 'n',
    'nse': 'ne',
    'sen': 'ne',
    'nes': 'se',
    'sne': 'se',
    'sesw': 's',
    'swse': 's',
    'snw': 'sw',
    'nws': 'sw',
    'swn': 'nw',
    'nsw': 'nw'}

"""A cancel is when two directons are opposite each other."""
CANCEL = [
    'ns',
    'sn',
    'nesw',
    'swne',
    'senw',
    'nwse']