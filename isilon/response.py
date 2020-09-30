class Response:
    def __init__(self, response):
        self._response = response

    def __repr__(self):
        return f"Response(url='{self.url}', status={self.status}, http_version='{self.http_version}', method='{self.method}', headers={self.headers})"

    @property
    def status(self) -> int:
        return int(self._response.status)

    @property
    def http_version(self) -> str:
        return f"{self._response.version.major}.{self._response.version.minor}"

    @property
    def url(self) -> str:
        return str(self._response.url)

    @property
    def headers(self) -> dict:
        return dict(self._response.headers)

    @property
    def method(self) -> str:
        return str(self._response.request_info.method)

    async def text(self):
        resp = await self._response.text()
        return resp

    async def json(self):
        resp = await self._response.json()
        return resp

    async def content(self):
        resp = await self._response.content
        return resp