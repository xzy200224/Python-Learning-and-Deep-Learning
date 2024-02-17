import json
# 从python对象转换为json字符串
person = {'name': 'zhangsan', 'age': 18, 'telephone': ['123456789', '987654321'], 'isonly': True}
print(person)

# indent=4：这个参数指定了生成的 JSON 字符串中的缩进空格数，使得生成的 JSON 字符串更易读。
# sort_keys=True：这个参数指定了是否按照键的字母顺序对生成的 JSON 字符串中的键进行排序。
person_json = json.dumps(person, indent=4, sort_keys=True)
print(person_json, type(person_json))   # 字符串

json.dump(person, open('person.json', 'w'), indent=4, sort_keys=True)  # 写入文件