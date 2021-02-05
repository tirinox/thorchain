import asyncio
import logging

import ujson
from aiohttp import ClientSession, ClientConnectorError

THORNODE_PORT = 1317


class ThorNodeClient:
    @staticmethod
    def connection_url(ip_address, path='', port=THORNODE_PORT):
        path = '/' + path.lstrip('/')
        return f'http://{ip_address}:{port}{path}'

    def __init__(self, node_ip: str, session: ClientSession, timeout=3.0, logger=None):
        self.session = session
        self.timeout = timeout
        self.node_ip = node_ip
        self.logger = logger or logging.getLogger('ThorNodeClient')

    async def request_raw(self, path):
        url = self.connection_url(self.node_ip, path)
        try:
            async with self.session.get(url, timeout=self.timeout) as resp:
                return await resp.text()
        except (ClientConnectorError, asyncio.TimeoutError) as e:
            self.logger.warning(f'Cannot connect to THORNode ({self.node_ip}) for "{path}" (err: {e}).')
            return ''

    async def request(self, path):
        data = await self.request_raw(path)
        return ujson.loads(data) if data else None
