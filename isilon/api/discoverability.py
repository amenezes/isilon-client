from isilon.api.base import BaseAPI


class Discoverability(BaseAPI):
    async def info(self, headers: dict = {}, *args, **kwargs):
        """List activated capabilities."""
        await self.include_auth_header(headers)
        async with self.http.get(f"{self.address}/info", *args, **kwargs) as resp:
            json_response = await resp.json()
        return json_response
