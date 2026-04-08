import json

class BaseAPI:
    def __init__(self, requests_context, base_url = None):
        self.requests_context = requests_context
        self.base_url = base_url or ""

    async def get(self, url, **kwargs):
        response = await self.requests_context.get(self.base_url + url, **kwargs)
        return response

    async def post(self, url, data = None, **kwargs):
        response = await self.requests_context.post(self.base_url + url, data=json.dumps(data), **kwargs)
        return response

    async def delete(self, url, **kwargs):
        response = await self.requests_context.delete(self.base_url + url, **kwargs)
        return response