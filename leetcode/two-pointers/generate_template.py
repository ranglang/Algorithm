# encoding=utf-8
# 根据 question title 生成模板
# 调用 python generate_template.py question_title
import sys

if __name__ == "__main__":
    file_name = sys.argv[1]
    file_name = file_name.replace('\n','')
    with open(file_name.strip()+'.md','wt',encoding='utf-8') as f:
        f.write(
            """
# 题目描述
[原题链接]()

题目描述

```
测试样例
```

<!--more-->

# 分析


# 代码
空间复杂度O(),时间复杂度O()
```C++
```
            """
        )
