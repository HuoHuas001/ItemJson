import json

items = {}
ico = {}
item = {}

with open('Resource path.json','r',encoding='UTF-8') as f:
    ico = json.loads(f.read())

with open('zh_CN.json','r',encoding='UTF-8') as f:
    item = json.loads(f.read())

for i in item:
    try:
        icn = ico[i]
    except Exception as e:
        icn = ''
        with open('no.txt','a',encoding='UTF-8') as f:
            f.write(str(e).replace("'",'')+' '+item[i]+'\n')
    items[i] = {
        'NameCh':item[i],
        "icon": icn,
        "NameEn":i
    }
with open('Item.json','w',encoding='UTF-8',) as f:
    f.write(json.dumps(items,ensure_ascii=False))

print('整理完成')