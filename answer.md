# 期中考
>
>學號：112111234
><br />
>姓名：阮陳家興
><br />
>作業撰寫時間：180 (mins，包含程式撰寫時間)
><br />
>最後撰寫文件日期：2023/09/22
>

本份文件包含以下主題：(至少需下面兩項，若是有多者可以自行新增)
- [x] 說明內容

## 說明程式與內容

開始寫說明，該說明需說明想法，
並於之後再對上述想法的每一部分將程式進一步進行展現，
若需引用程式區則使用下面方法，
若為.cs檔內程式除了於敘述中需註明檔案名稱外，
還需使用語法` ```語言種類 程式碼 ``` `，其中語言種類若是要用python則使用py，java則使用java，C/C++則使用cpp，
下段程式碼為語言種類選擇csharp使用後結果：

```csharp
public void mt_getResult(){
    ...
}
```

若要於內文中標示部分網頁檔，則使用以下標籤` ```html 程式碼 ``` `，
下段程式碼則為使用後結果：

```html
<%@ Page Language="C#" AutoEventWireup="true" ...>

<!DOCTYPE html>

<html xmlns="http://www.w3.org/1999/xhtml">
<head runat="server">
<meta http-equiv="Content-Type" ...>
    <title></title>
</head>
<body>
    <form id="form1" runat="server">
        <div>
        </div>
    </form>
</body>
</html>
```
更多markdown方法可參閱[https://ithelp.ithome.com.tw/articles/10203758](https://ithelp.ithome.com.tw/articles/10203758)
請在撰寫"說明程式與內容"該塊內容，請把原該塊內上述敘述刪除，該塊上述內容只是用來指引該怎麼撰寫內容。


a. 小題

Ans
```py
#a
map = [[0 for _ in range(10)] for _ in range(10)]
```

b. 小題

Ans
```py
rowMap = [0]*10
```

c. 小題

Ans
```py
rowMap = [0, 7, 13, 28, 44, 62, 74, 75, 87, 90]
```

d. 小題

Ans
```py
for index in rowMap:
    row = index // 10
    col = index % 10
    map[row][col] = "*"
```

e. 小題

Ans
```py
def is_valid(x,y):
    return 0 <= x < 10 and 0 <= y < 10
   

for i in range(10):
        for j in range (10):
            if map[i][j] == '*':
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        ni, nj = i + dx, j + dy 
                        if is_valid(ni,nj) and map[ni][nj] != '*':
                            map[ni][nj] += 1
for i in range(10):
    for j in range(10):
        if map[row][col] == '0':
            map[row][col] = ' '                      

for row in map:                        
    print(" | ".join(str(cell) for cell in row))
    print("-" * (4 * 10 - 1))
```