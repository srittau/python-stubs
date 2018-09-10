from httplib2 import Http


class Credentials(object):
    def authorize(self, http: Http) -> Http: ...


class OAuth2Credentials(Credentials):
    ...


class GoogleCredentials(OAuth2Credentials):
    ...


class AssertionCredentials(GoogleCredentials):
    ...
