from requests import Request, Session


class ApiConsumer:
    __instance = None

    def __init__(self, api_url, api_key, token):
        self.session = Session()
        self.api_url = api_url
        self.api_key = api_key
        self.token = token
        self.session.headers.update({"Accept": "application/json"})

    @classmethod
    def get_instance(cls, context):
        if cls.__instance == None:
            cls.__instance = cls(
                api_url=context.API_URL,
                api_key=context.API_KEY,
                token=context.API_TOKEN,
            )
        return cls.__instance

    def api_request(self, endpoint, method, params=None, data=None):
        if params is None:
            params = {}
        params["key"] = self.api_key
        params["token"] = self.token
        print(method, params, data)
        req = Request(
            url=f"{self.api_url.rstrip('/')}/{endpoint.lstrip('/')}",
            method=method,
            params=params,
            data=data,
        )
        response = self.session.send(req.prepare())
        return response

    def get(self, endpoint):
        response = self.api_request(
            endpoint,
            "GET",
        )
        return response.text

    def post(self, endpoint, params, body):
        response = self.api_request(endpoint, "POST", params, body)
        return response.text

    def put(self, endpoint, params):
        response = self.api_request(endpoint, params)
        return response.text

    def delete(self, endpoint):
        response = self.api_request(
            endpoint,
            "DELETE",
        )
        return response.text
