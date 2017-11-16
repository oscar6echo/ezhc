
from IPython.display import HTML, display

from ._config import FULLNAME, DESCRIPTION, DEMO
from ._state import State, state_HC, state_HS


class Wrapper(object):

    def __init__(self, lib, path=''):
        self.path = path
        self.lib = lib
        if lib == 'highcharts':
            self.state = state_HC
        if lib == 'highstock':
            self.state = state_HS

    def __getattr__(self, item):
        _path = item if not self.path else self.path+'.'+item
        for attr in self.state._OPTION:
            if _path == attr.get(FULLNAME):
                var = Wrapper(self.lib, _path)
                if len(dir(var)):
                    setattr(self, item, var)
                # setattr(self, item, var if len(dir(var)) else '')
                return var

    def __dir__(self):
        _dir = []
        _path = self.path.split('.')
        if len(_path) == 1 and self.path is '':
            for attr in self.state._OPTION:
                if len(attr.get(FULLNAME).split('.')) == 1:
                    _dir.append(attr.get(FULLNAME))
        else:
            for attr in self.state._OPTION:
                _attr_path = attr.get(FULLNAME).split('.')
                if len(_path) < len(_attr_path):
                    if _path[len(_path)-1] == _attr_path[len(_path)-1] \
                            and len(_attr_path) == len(_path)+1:
                        _dir.append(_attr_path[len(_path)])
        return _dir

    def to_dict(self):
        _dic = dict(self.__dict__)
        _dic.pop('path')
        _dic.pop('lib')

        for k in list(_dic.keys()):
            if isinstance(_dic[k], list):
                for i, e in enumerate(_dic[k]):
                    if isinstance(e, Wrapper):
                        _dic[k][i] = _dic[k][i].to_dict()
                    elif isinstance(e, dict):
                        pass
                    elif _dic[k][i] == {} or _dic[k][i] is None or isinstance(_dic[k][i], State):
                        _dic[k].pop(i)
            else:
                if isinstance(_dic[k], Wrapper):
                    _dic[k] = _dic[k].to_dict()
                elif isinstance(_dic[k], dict):
                    pass
                elif _dic[k] == {} or _dic[k] is None or isinstance(_dic[k], State):
                    _dic.pop(k)

        return _dic

    @property
    def __doc__(self):
        for attr in self.state._OPTION:
            if self.path == attr.get(FULLNAME):
                _desc = attr.get(DESCRIPTION)
                _demo = attr.get(DEMO)
                break

        doc = "Documentation for '%s'\n\n" % self.path + \
            "Description\n%s\n\n" % _desc
        if _demo:
            doc += "Demo\n%s\n" % _demo

        return doc

    def info(self):
        def correct_url(s):
                url = 'href=\"#'
                url_highcharts = 'href=\"https://api.highcharts.com/highcharts#'
                url_highstock = 'href=\"https://api.highcharts.com/highstock#'
                li = s.split(url)
                if len(li) == 1:
                    return s
                else:
                    if self.lib == 'highcharts':
                        return url_highcharts.join(li)
                    if self.lib == 'highstock':
                        return url_highstock.join(li)

        if self.path != '':
            for attr in self.state._OPTION:
                if self.path == attr.get(FULLNAME):
                    _desc = attr.get(DESCRIPTION)
                    _demo = attr.get(DEMO)
                    break

            doc = "<h4> Documentation for '%s' </h4><br>" % self.path
            if _desc:
                _desc = correct_url(_desc)
                doc += "<li>Description </li>%s<br><br>" % _desc
            if _demo:
                _demo = correct_url(_demo)
                doc += "<li>Demo</li> %s<br>" % _demo

            display(HTML(doc))
