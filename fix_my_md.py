import os

# 修正路径（注意双反斜杠或原始字符串）
path = r'C:\04_Users\Desktop\Study\01_Crash Course\My-notes-about-CCCS'
# 或者使用：path = 'C:\\04_Users\\Desktop\\Study\\01_Crash Course\\My-notes-about-CCCS'

files = os.listdir(path)

# 修正旧路径（注意末尾的空格和路径格式）
old = 'https://github.com/WilliamWuLH/My-notes-about-CCCS/blob/master/image'
new = './image'  # 修正为相对路径格式

for file in files:
    if '.md' in file:
        print(f"处理文件: {file}")
        
        # 修正文件路径拼接
        mdpath = os.path.join(path, file)
        
        filedata = ''
        with open(mdpath, 'r', encoding="utf-8") as mdfile:
            for line in mdfile:
                if old in line:
                    line = line.replace(old, new)
                    print(f"替换: {line.strip()}")
                filedata += line
        
        with open(mdpath, 'w', encoding='utf-8') as mdfile:
            mdfile.write(filedata)
        
        print(f"完成处理: {file}\n")