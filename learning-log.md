# 01 Python基础

## 学习目标

学习使用Python处理类似漏洞信息的结构化数据。

## 今天学习的内容

- list
- dict
- for循环
- if条件判断
- 多条件判断
- 字典取值

## 实践内容

创建了3条模拟漏洞数据：

- CVE-001
- CVE-002
- CVE-003

然后使用for循环遍历漏洞数据。

## 实践结果

成功筛选出：

CVE-001 LLM Prompt Injection
CVE-003 AI Model Vulnerability

## 遇到的问题

第一次运行if语句时忘记写冒号 `:`，
出现了SyntaxError。

## 问题解决

发现if条件后面需要添加 `:`。

## 我的理解

我现在理解了python语言中的for循环以及if条件判断字典以及列表每一件事情并不向想象中那样难，每一小步走好才能迈出一大步。cves 是保存多个漏洞信息的列表。

## 下一步

学习JSON以及API。



# 02 JSON + API

## 今天学习

JSON是什么？

## 我的理解

json就是一种字符串外面需要用引号进行包裹

## dumps
## loads
我理解为：
- **dumps**：dump to string → 输出字符串
- **loads**：load from string → **输入必须给字符串**


……

## 实验

Python对象
↓
JSON
↓
Python对象

## 遇到的问题
没有弄明白到底json是字符串还有python中封装的是字典

## 实验结果
成功将json字符串和python字典进行转换

## 下一步

学习HTTP和API。
API：我可以通过什么入口获取功能/数据

HTTP：我和这个服务器怎么进行网络通信
