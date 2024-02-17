import json
# json字符串转换为python对象
Str = '{"name": "zhangsan", "age": 18, "telephone": ["123456789", "987654321"], "isonly": true}'
pythonObj = json.loads(Str)
print(pythonObj, type(pythonObj))  # 字典
# 从文件中读取json字符串
person = json.load(open('person.json', 'r'))
print(person, type(person))  # 字典