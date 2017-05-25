class ServiceConsumerTest(object):
    pact_uri = None
    has_pact_with = None

    @property
    def states(self):
        for attr in dir(self):
            obj = getattr(self, attr)
            if callable(obj) and hasattr(obj, 'state'):
                yield obj


def pact_uri(pact_uri_value):
    def wrapper(calling_class):
        setattr(calling_class, 'set_pact_uri', eval('set_pact_uri(calling_class, "' + pact_uri_value + '")'))
        return calling_class
    return wrapper


def set_pact_uri(self, pact_uri_value):
    self.pact_uri = pact_uri_value


def has_pact_with(has_pact_with_value):
    def wrapper(calling_class):
        setattr(calling_class, 'set_has_pact_with', eval('set_has_pact_with(calling_class, "' + has_pact_with_value + '")'))
        return calling_class
    return wrapper


def set_has_pact_with(self, has_pact_with_value):
    self.has_pact_with = has_pact_with_value


def state(state_value):
    def decorate(function):
        function.state = state_value
        return function
    return decorate
