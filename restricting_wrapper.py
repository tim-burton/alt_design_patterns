class RestrictingWrapper(object):

    def __init__(self, wrappee, block):
        self._wrappee = wrappee
        self._block = block

    def __getattr__(self, attr):
        if attr in self._block:
            raise RestrictionError(attr)

        return getattr(self._wrappee, attr)


class RestrictionError(Exception):
    pass


if __name__ == '__main__':
    obj = type("obj", (), {})
    obj.restricted_attr = object()
    obj.public_attr = object()
    wrapper = RestrictingWrapper(obj, ('restricted_attr', ))

    assert wrapper.public_attr == obj.public_attr
    try:
        wrapper.restricted_attr
    except RestrictionError:
        print("restricted_attr is restricted, you can't get it")
    else:
        raise RuntimeError("RestrictingWrapper is broken!")
