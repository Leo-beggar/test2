import json

# 打开并读取JSON文件
with open('students.json', 'r') as file:
    data = json.load(file)

# 提取学生列表
students = data.get('students', [])

# 列出所有学生
for student in students:
    print(f"ID: {student['id']}, Name: {student['name']}, Age: {student['age']}")