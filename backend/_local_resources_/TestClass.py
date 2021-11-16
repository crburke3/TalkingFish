from io import BytesIO


class RequestForm:
    arguments: dict = {}

    def __init__(self, arguments:dict):
        self.arguments = arguments

    def to_dict(self):
        return self.arguments


class TestClass:
    _args = {}
    method = "GET"
    path = "/"
    files = None

    @property
    def args(self):
        if self.method == "GET":
            ret_dict = {}
            for key, val in self._args.items():
                ret_dict[key] = str(val)
            return ret_dict
        else:
            return self._args

    def __init__(self, args: dict, headers:dict = {"content-type": "application/json"}, method="GET"):
        self._args = args
        self.headers = headers
        self.json = args
        self.method = method
        self.form = RequestForm(args)

    def get_json(self):
        return self.args


class RequestFiles:
    def __init__(self, file_path:str):
        self.files = {
            file_path: RequestFile(file_path)
        }

    def to_dict(self):
        return self.files


class RequestFile:
    def __init__(self, file_path:str):
        file_data = open(file_path, "rb")
        self.stream = DummyClass(file_data)


class DummyClass:

    def __init__(self, data):
        self.data = data

    def read(self):
        return self.data


def pretty_print_POST(response):
    print(response.request.url)
    print(response.request.body)
    print(response.request.headers)

