import json
import urllib.parse
from typing import Callable

import gevent.subprocess


def find_query_port(gamedig_path: str, game: str, server: dict, ports_to_try: list, validator: Callable) -> int:
    query_port = -1

    # Add current query port add index 0 if valid
    if server.get('queryPort', -1) != -1:
        ports_to_try.insert(0, server['queryPort'])
    # Try all unique ports
    for port_to_try in list(set(ports_to_try)):
        gamedig_result = gevent.subprocess.run(
            args=[gamedig_path, '--type', game, f'{server["ip"]}:{port_to_try}',
                  '--maxAttempts 2', '--socketTimeout 2000', '--givenPortOnly'],
            capture_output=True
        )
        # Stop searching if query was successful and response came from the correct server
        # (some servers run on the same IP, so make sure ip and game_port match)
        parsed_result = json.loads(gamedig_result.stdout)
        if not parsed_result.get('error', '').startswith('Failed all') and validator(server, parsed_result):
            query_port = port_to_try
            break

    return query_port


def battlelog_server_validator(server: dict, parsed_result: dict) -> bool:
    return parsed_result.get('connect') == f'{server["ip"]}:{server["gamePort"]}'


def bfbc2_server_validator(server: dict, parsed_result: dict) -> bool:
    return battlelog_server_validator(server, parsed_result) or parsed_result.get('name') == server['name']


def parse_raw_server_info(raw_server_info: str) -> dict:
    # Split on "\" and remove first element, since raw info starts with "\"
    elements = raw_server_info.split('\\')[1:]

    # Parse using elements at an even index as key, uneven index as value
    keys = [value for (index, value) in enumerate(elements) if index % 2 == 0]
    values = [value for (index, value) in enumerate(elements) if index % 2 == 1]

    # Build dict
    server = {key: urllib.parse.unquote(values[index].replace('"', '')) for (index, key) in enumerate(keys)}

    return server