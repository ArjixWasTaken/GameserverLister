import os
import socket

ROOT_DIR = rootDir = os.path.join(os.path.dirname(os.path.realpath(__file__)), '..')
GSLIST_CONFIGS = {
    'bf1942': {
        'gameName': 'bfield1942',
        'gameKey': 'HpWx9z',
        'encType': '2',
        'superQueryType': '0',
        'servers': {
            'bf1942.sk': {
                'hostname': 'master.bf1942.sk',
                'port': 28900
            },
            'qtracker': {
                'hostname': 'master2.qtracker.com',
                'port': 28900
            }
        }
    },
    'bfvietnam': {
        'gameName': 'bfvietnam',
        'gameKey': 'h2P9dJ',
        'encType': '2',
        'superQueryType': '0',
        'servers': {
            'qtracker': {
                'hostname': 'master2.qtracker.com',
                'port': 28900
            }
        }
    },
    'bf2142': {
        'gameName': 'stella',
        'gameKey': 'M8o1Qw',
        'encType': '-1',
        'superQueryType': '8',
        'servers': {
            'openspy': {
                'hostname': 'stella.ms5.openspy.net',
                'port': 28910
            }
        }
    },
    'bf2': {
        'gameName': 'battlefield2',
        'gameKey': 'hW6m9a',
        'encType': '-1',
        'superQueryType': '8',
        'servers': {
            'bf2hub': {
                'hostname': 'servers.bf2hub.com',
                'port': 28911
            },
            'playbf2': {
                'hostname': 'battlefield2.ms.playbf2.ru',
                'port': 28910
            }
        }
    }
}
BATTLELOG_GAME_BASE_URIS = {
    'bf3': 'https://battlelog.battlefield.com/bf3/servers/getAutoBrowseServers/',
    'bf4': 'https://battlelog.battlefield.com/bf4/servers/getServers/pc/',
    'bfh': 'https://battlelog.battlefield.com/bfh/servers/getServers/pc/',
    'mohwf': 'https://battlelog.battlefield.com/mohw/servers/getAutoBrowseServers/'
}
QUAKE3_CONFIGS = {
    'cod4': {
        'protocol': 6,
        'servers': {
            'activision': {
                'hostname': 'cod4master.activision.com',
                'port': 20810
            }
        }
    },
    'cod4x': {
        'protocol': 6,
        'keywords': 'full empty \x00',
        'network_protocol': socket.SOCK_STREAM,
        'server_entry_prefix': b'\x00\x00\x00\x00\x04',
        'servers': {
            'cod4x.me': {
                'hostname': 'cod4master.cod4x.me',
                'port': 20810
            }
        }
    },
    'quake3arena': {
        'protocol': 68,
        'servers': {
            'quake3arena.com': {
                'hostname': 'master.quake3arena.com',
                'port': 27950
            },
            'urbanterror.info-1': {
                'hostname': 'master.urbanterror.info',
                'port': 27900
            },
            'urbanterror.info-2': {
                'hostname': 'master2.urbanterror.info',
                'port': 27900
            },
            'excessiveplus.net': {
                'hostname': 'master0.excessiveplus.net',
                'port': 27950
            },
            'ioquake3.org': {
                'hostname': 'master.ioquake3.org',
                'port': 27950
            },
            'huxxer.de': {
                'hostname': 'master.huxxer.de',
                'port': 27950
            },
            'maverickservers.com': {
                'hostname': 'master.maverickservers.com',
                'port': 27950
            },
            'deathmask.net': {
                'hostname': 'dpmaster.deathmask.net',
                'port': 27950
            }

        }
    }
}