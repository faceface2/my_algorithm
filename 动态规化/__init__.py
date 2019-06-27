import flask
# def mul_str():
#     str1 = '345'
#     str2 = '455'
#     if not str1 or not str2:
#         return ""
#     res = [0] * (len(str1) + len(str2))
#     for i in range(len(str1) - 1, -1, -1):
#         add = 0
#         for j in range(len(str2) - 1, -1, -1):
#             mul = int(str1[i]) * int(str2[j])
#             sums = res[i + j + 1] + add + mul % 10
#             res[i + j + 1] = sums % 10
#             add = int(mul / 10) + int(sums / 10)
#         res[i] += add
#     print(res)
#     j = 0
#     for i in res:
#         if i == 0:
#             j += 1
#         else:
#             break
#     print(''.join(map(str, res[j:])))


# mul_str()
import os

from werkzeug.datastructures import TypeConversionDict


# class A:
#     def __init__(self):
#         self.static_folder = None
#
#     def _get_static_url_path(self):
#         if self._static_url_path is not None:
#             return self._static_url_path
#
#         if self.static_folder is not None:
#             return '/' + os.path.basename(self.static_folder)
#
#     def _set_static_url_path(self, value):
#         self._static_url_path = value
#
#     static_url_path = property(
#         _get_static_url_path, _set_static_url_path,
#         doc='The URL prefix that the static route will be registered for.'
#     )
#     del _get_static_url_path, _set_static_url_path

    # a = A()
    # print(dir(a))
    # a.static_url_path = 'C://a.txt'
    # print(a.static_url_path)


import pickle

iterlists = lambda d, *args, **kwargs: iter(d.lists(*args, **kwargs))

iteritems = lambda d, *args, **kwargs: iter(d.items(*args, **kwargs))


class MultiDict(TypeConversionDict):

    def __init__(self, mapping=None):
        if isinstance(mapping, MultiDict):
            dict.__init__(self, ((k, l[:]) for k, l in iterlists(mapping)))
        elif isinstance(mapping, dict):
            tmp = {}
            for key, value in iteritems(mapping):
                if isinstance(value, (tuple, list)):
                    if len(value) == 0:
                        continue
                    value = list(value)
                else:
                    value = [value]
                tmp[key] = value
            dict.__init__(self, tmp)
        else:
            tmp = {}
            for key, value in mapping or ():
                tmp.setdefault(key, []).append(value)
            dict.__init__(self, tmp)

    # def __getstate__(self):
    #     return dict(self.lists())

    def lists(self):
        """Return a iterator of ``(key, values)`` pairs, where values is the list
        of all values associated with the key."""

        for key, values in iteritems(dict, self):
            yield key, list(values)

    # def __setstate__(self, value):
    #     dict.clear(self)
    #     dict.update(self, value)


am = MultiDict({'1': 1, '2': 2})

p = pickle.dumps(am)
print(p)
a = pickle.loads(p)
print(a['1'])
