# coding=utf-8
import json
import urllib2

code = "000905.SS"
url = "https://api-ddc-wscn.xuangubao.cn/market/trend?fields=tick_at,close_px,px_change,px_change_rate&prod_code={}".format(
    code)
data = urllib2.urlopen(url)
obj = json.load(data)

stock = obj["data"]["candle"][code]
lines = stock["lines"]
pre_close_px = stock["pre_close_px"]
if len(lines):
    latest = lines[-1]
    close_px = latest[1]
    px_change = latest[2]
    px_change_rate = "%.2f%%" % (latest[3])
    if px_change > 0:
        trend = "▲"
        font_color = "255,96,94,255"
    else:
        trend = "▼"
        font_color = "122,174,61,255"
    res = {'text': "中证500 " + str(close_px) + "(" + px_change_rate + ")" + trend, 'font_color': font_color}
else:
    close_px = pre_close_px
    font_color = "255,255,255,255"
    res = {'text': "中证500 " + str(close_px), 'font_color': font_color}

print(json.dumps(res))
