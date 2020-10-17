from isilon.api.base import BaseAPI


class Containers(BaseAPI):
    async def objects(self, container_name: str, headers: dict = {}, **kwargs):
        """Show container details and list objects."""
        await self.include_auth_header(headers)
        async with self.http.get(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}?format=json",
            headers=headers,
            **kwargs,
        ) as resp:
            response = await resp.json()
        return response

    async def create(self, container_name: str, headers: dict = {}, **kwargs) -> int:
        """Create container."""
        await self.include_auth_header(headers)
        async with self.http.put(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return int(resp.status)

    async def update_metadata(self, container_name: str, headers: dict = {}, **kwargs):
        """Create, update, or delete container metadata."""
        await self.include_auth_header(headers)
        async with self.http.put(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp.status

    async def show_metadata(self, container_name: str, headers: dict = {}, **kwargs):
        """Show container metadata."""
        await self.include_auth_header(headers)
        async with self.http.head(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return dict(resp.headers)

    async def delete(self, container_name: str, headers: dict = {}, **kwargs):
        """Delete container."""
        await self.include_auth_header(headers)
        async with self.http.delete(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp.status
