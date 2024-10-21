from mitmproxy import http
import sys

class ChangeHTTPCode:

    filt = "google.com"

    def response(self, flow: http.HTTPFlow) -> None:
        if not (self.filt in flow.request.pretty_url):
            flow.response.content=b'<h1>comlpete your exam</h1>'

addons = [ChangeHTTPCode()]