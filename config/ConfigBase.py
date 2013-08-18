__author__ = 'matt'

class Config(dict):
    """
    Base class for configurations.
    """
    def dumpData(self):
        for key, value in self.iteritems():
            print key, ":", str(value)

    def __getattr__(self, attr):
        if attr in self:
            return self[attr]
        else:
            raise AttributeError('Config object has no attribute "%s"' % attr)
