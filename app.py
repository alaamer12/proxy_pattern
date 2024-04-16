# Subject interface
class Subject:
    def request(self):
        pass

# RealSubject
class RealSubject(Subject):
    def request(self):
        print("RealSubject: Handling request")

# Proxy
class Proxy(Subject):
    def __init__(self):
        self._real_subject = RealSubject()

    def request(self):
        # Additional functionality before/after forwarding the request
        print("Proxy: Logging the request")
        self._real_subject.request()
        print("Proxy: Request completed")

# Client
if __name__ == "__main__":
    proxy = Proxy()
    proxy.request()
