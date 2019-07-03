# MyFlask python2.7

Simple framework for creating REST APIs http://flask-restful.readthedocs.io<br>

massage = u'\xce\xde\xd0\xa7\xb5\xc4\xd3\xc3\xbb\xa7 ID \xbb\xf2\xbf\xda\xc1\xee'<br>
print massage.encode('raw_unicode_escape').decode('gbk')

# ------------------------
a = '\\u8FD0\\u884C\\u7CFB\\u7EDF'
b = eval(u"'" + a + "'")
print(b)
