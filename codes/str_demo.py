import re


def _process_content(vs):
    """去除 4 字节的 utf-8 字符，否则插入 mysql 时会出错"""
    try:
        # python UCS-4 build的处理方式
        highpoints = re.compile(u'[\U00010000-\U0010ffff]')
    except re.error:
        # python UCS-2 build的处理方式
        highpoints = re.compile(u'[\uD800-\uDBFF][\uDC00-\uDFFF]')

    params = list()
    for v in vs:
        # 对插入数据进行一些处理
        nv = highpoints.sub(u'', v)
        nv = filter_char(nv)
        if nv.strip():     # 不需要在字符串之间保留空格
            params.append(nv)
    # print(params)
    return "".join(params)


def filter_char(_str):
    """处理特殊的空白字符"""
    for cha in ['\n', '\r', '\t',
                '\u200a', '\u200b', '\u200c', '\u200d', '\u200e',
                '\u202a', '\u202b', '\u202c', '\u202d', '\u202e',
                ]:
        _str = _str.replace(cha, '')
    # _str = _str.replace(u'\xa0', u' ')  # 把 \xa0 替换成普通的空格
    _str = _str.replace(u'\xa0', u'')     # 把 \xa0 去除
    return _str

