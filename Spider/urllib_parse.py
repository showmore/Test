import urllib.parse

s = "javascript:submit('%E7%BB%BC%E5%90%88','A','1','%E5%9B%BD%E5%86%85%E6%A0%87%E5%87%86')"
s2 = "CB%252FT%2520282-1994/"
print(urllib.parse.unquote(s2,encoding = "utf-8"))

