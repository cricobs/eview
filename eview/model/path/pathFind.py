import inspect
import os

from eview.model.path.path import Path


class PathFind(Path):
    def __init__(self, *args, **kwargs):
        super(PathFind, self).__init__(*args, **kwargs)

    @classmethod
    def relative(cls, thing=None, extension=None):
        """
        thing type assumed order for defining input path: class, module, string
        :param thing:
        :param extension:
        :return:
        """
        thing = thing if thing is not None else cls
        try:
            path = inspect.getfile(thing.__class__)
        except TypeError:
            try:
                path = inspect.getfile(thing)
            except TypeError:
                path = thing

        if extension:
            path = "{0}.{1}".format(os.path.splitext(path)[0], extension.lstrip("."))

        return path
