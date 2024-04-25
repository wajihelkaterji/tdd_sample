from accounts.models import ListUser, Token

class PasswordlessAuthenticationBackend(object):

    def authenticate(self, request, uid):
        print('uid', uid)
        if not Token.objects.filter(uid=uid).exists():
            print('no token found')
            return None
        token = Token.objects.get(uid=uid)
        print('got token')
        try:
            user = ListUser.objects.get(email=token.email)
            print('got user')
            return user
        except ListUser.DoesNotExist:
            print('new user')
            return ListUser.objects.create(email=token.email)


    def get_user(self, email):
        return ListUser.objects.get(email=email)
