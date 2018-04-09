import json

text = '{"status":"0","info":"\u5bf9\u4e0d\u8d77\u60a8\u7684\u5361\u53f7\u4e0d\u5b58\u5728\uff01"}';
jsonObj = json.loads(text)
print(jsonObj)
