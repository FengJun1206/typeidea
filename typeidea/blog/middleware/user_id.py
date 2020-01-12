"""
生成用户用户唯一 ID，存入 cookie 中，用于标识用户，统计用户访问量，文章访问量
"""
import uuid

USER_KEY = 'uid'
TEN_YEARS = 60 * 60 * 24 * 365 * 10


class UserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        uid = self.generate_uid(request)
        request.uid = uid
        response = self.get_response(request)
        response.set_cookie(USER_KEY, uid, max_age=TEN_YEARS, httponly=True)    # 只能在服务器访问
        return response

    def generate_uid(self, request):
        try:
            uid = request.COOKIES[USER_KEY]
        except KeyError:
            uid = uuid.uuid4().hex
        return uid
