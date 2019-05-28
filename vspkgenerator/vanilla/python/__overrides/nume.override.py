def save(self, as_async=False, callback=None, **kwargs):
    """ """
    if 'async' in kwargs.keys() and not as_async:
        as_async = kwargs['async']
    super(NUMe, self).save(as_async=as_async, callback=callback, encrypted=False)
