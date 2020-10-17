from isilon.api.base import BaseAPI


class Objects(BaseAPI):
    async def get(
        self, container_name: str, object_name: str, headers: dict = {}, **kwargs
    ):
        """Get object content and metadata."""
        await self.include_auth_header(headers)
        async with self.http.get(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp

    async def get_large(
        self,
        container_name: str,
        object_name: str,
        filename: str,
        chunk_size: int = 50,
        headers: dict = {},
        **kwargs,
    ):
        """Get large object content and metadata."""
        await self.include_auth_header(headers)
        async with self.http.get(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
            chunk_size=chunk_size,
            headers=headers,
            **kwargs,
        ) as resp:
            with open(filename, "wb") as f:
                while True:
                    chunk = await resp.content.read(chunk_size)
                    if not chunk:
                        break
                    f.write(chunk)
            return resp

    async def create(
        self, container_name: str, object_name: str, data, headers: dict = {}, **kwargs
    ):
        """Create or replace object."""
        if "Content-Length" not in headers:
            headers.update({"Content-Length": f"{len(data)}"})
        await self.include_auth_header(headers)
        async with self.http.put(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
            headers=headers,
            data=data,
            **kwargs,
        ) as resp:
            return resp.status

    async def create_large(
        self,
        container_name: str,
        object_name: str,
        filename: str,
        headers: dict = {},
        *args,
        **kwargs,
    ):
        """Create or replace large object."""
        await self.include_auth_header(headers)
        with open(filename, "rb") as f:
            async with self.http.put(
                f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
                headers=headers,
                data=f,
                **kwargs,
            ) as resp:
                return resp.status

    async def copy(self, container_name, object_name, headers: dict = {}, **kwargs):
        """Copy object."""
        raise NotImplementedError("Operation not supported")

    async def delete(
        self, container_name: str, object_name, headers: dict = {}, **kwargs
    ):
        """Delete object."""
        await self.include_auth_header(headers)
        async with self.http.delete(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp.status

    async def show_metadata(
        self, container_name: str, object_name: str, headers: dict = {}, **kwargs
    ):
        """Show object metadata."""
        await self.include_auth_header(headers)
        async with self.http.head(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return dict(resp.headers)

    async def update_metadata(
        self, container_name: str, object_name: str, headers: dict = {}, **kwargs
    ):
        """Create or update object metadata."""
        await self.include_auth_header(headers)
        async with self.http.post(
            f"{self.address}/{self.API_VERSION}/AUTH_{self.account}/{container_name}/{object_name}",
            headers=headers,
            **kwargs,
        ) as resp:
            return resp.status
