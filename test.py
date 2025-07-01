#判断奇偶数
def is_odd(n):
    if n % 2 == 0:
        return "偶数"
    else:
        return "奇数"


#交换变量的值
def swap(a, b):
    a,b=b,a
    return a,b


#列表最大值
def find_list_max(list):
    max_num=list[0]
    for num in list:
        if num>=max_num:
            max_num=num
    return max_num


#fizzbuzz问题
def fizzbuzz_problem():
    for num in range(1,101):
        if num %3==0 and num%5==0:
            print("fizzbuzz")
        elif num%3==0:
            print("fizz")
        elif num%5==0:
            print("buzz")
        else:
            print(num)

#统计字符的次数
from collections import Counter
def char_count(str):
    count=Counter(str)
    print(dict(count.most_common()))


#返回反转字符串
def reverse_string(s:str) -> str:
    s=s.strip()
    return s[::-1]


#找出字符串中第一个不重复的字符
from collections import Counter
def first_unique_char(s: str) -> str:
    count=Counter(s)
    for char in s:
        if count[char]==1:
            return char
    else:
        return None


#判断一个列表是否是回文
def is_palindrome(lst: list) -> bool:
    #原地修改列表返回值为None lst_reverse=lst.reverse()
    if lst==lst[::-1]:
        return True
    else:
        return False



#统计单词出现次数
from collections import Counter
def word_count(s: str) -> dict:
    count=Counter(s)
    return dict(count)


#提取列表中所有奇数
def extract_odds(lst: list) -> list:
    lst_qishu=[x for x in lst if x%2==1]
    return lst_qishu

#判断左右括号是否匹配
#实现思路:通过栈的思想,将左括号与右括号配对,最后判断左括号是否不配右括号以及栈是否为空,两者符合其一返回false,否则返回true
def is_brackets_valid(s: str) -> bool:
    #创建空栈
    stack=[]
    #创建匹配关系的字典
    brack_dict={'(':')','[':']','{':'}'}
    #遍历字符串,符合则将左括号入栈
    for bracket in s:
        if bracket in brack_dict.keys():
            stack.append(bracket)
        elif bracket in brack_dict.values():
            if not stack or brack_dict[stack.pop()]!=bracket:
                return False
    #最后需要判断栈是否为空才能返回True
    return not stack

#判断两个字符串是否是字母异位词
from collections import Counter
def is_different_word(s1:str,s2:str)->bool:
    count1=Counter(s1)
    count2=Counter(s2)
    if count1==count2:
        return True
    else:
        return False


#找出列表最多的元素
from collections import Counter
def find_max_element(lst):
    count=Counter(lst)
    max_element=count.most_common(1)[0][0]
    return max_element


#输出一个字符串中所有只出现一次的字符（按原顺序）
def new_string_with_one(s:str)->str:
    lst=[]
    for char in s:
        if s.count(char)==1:
            lst.append(char)
    new_str="".join(lst)
    return new_str

#判断列表是否严格升序
def list_is_aesc(lst:list)->bool:
    for i in range(0,len(lst)-1):
        if lst[i]>=lst[i+1]:
            return False
    return True
#将多个键值对字符串合并成一个字典
def merge_keyvalues_to_dict(s:str)->dict:
    lst=[]
    for item in s:
        speparte_item=item.split("=")
        lst.append(speparte_item)
    return dict(lst)
#判断是否是回文数（数字类型）
def num_is_huiwen(num:int)->bool:
    if num!=0:
        if num<0:
            return False
        elif num>0:
            num_str=str(num)
            return num_str==num_str[::-1]
    else:
        return "输入不能为0"
#统计每个单词出现的次数（不区分大小写）
from collections import Counter
def count_every_word(s:str)->int:
    count=Counter(s)
    return dict(count)

#给定字符串,移除相同的字符直到没有重复且相邻的字符
def str_remove_duplicate(str1):
    str1=str1.lower()
    for char in str1:
        if str1.count(char)>=2:
            str1=str1.replace(char,' ')
    return str1


#给定整数n,求小于该整数n的素数
def sushu_below_n(n):
    list=[]
    if n==1:
        print("1就是素数")
    if n>1:
        for num in range(1,n+1):
            if num%2!=0 and num%3!=0 and num%5!=0:
                list.append(num)
    for num in list:
        print(num)  


#输入一些整数 将从大到小输出
def sort_by_number(num_list):
    num_list.sort()
    print(num_list)

#统计字符串中每个单词的出现次数（区分大小写）
from collections import Counter
def every_word_count(s:str)->dict:
    count=Counter(s)
    return dict(count.most_common())

#找出列表中第二大的数（不排序）
def find_second_max_number(lst:list)->int:
    max_num=max(lst)
    min_num=min(lst)
    second_num=lst[0]
    for num in lst:
        if num <max_num and num>second_num:
            second_num=num
        elif max_num==min_num:
            return lst[0]
    return second_num
#判断一个数是否是质数（素数）
import math
def num_is_prime(num:int)->bool:
    if num<=1:
        return "输入一个大于1的整数"
    elif num>1:
        for i in range(2,num):
            if num%i==0:
                return False
        return True

#从列表中删除所有的偶数
def remove_oushu_from_list(lst:list)->list:
    return [x for x in lst if x%2==1]
#找出所有和为目标值的两数组合
def find_num_sum_equals_target(lst:list,target:int)->list:
    result=[]
    for i in range(0,len(lst)-1):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]==target:
                combination=tuple((lst[i],lst[j]))
                result.append(combination)
    return result
#找出字符串中出现次数最多的字符
from collections import Counter
def find_max_char(s:str)->str:
    count=Counter(s)
    return count.most_common(1)[0][0]

#提取列表中出现次数大于1的元素
def extract_element_greater_one(lst:list)->list:
    result=[]
    for num in lst:
        if lst.count(num)>1:
            result.append(num)
    return list(set(result))

#找出最长的单词
def find_max_word(s:str)->str:
    max_len=len(s[0])
    max_word=" "
    for word in s:
        if len(word)>=max_len:
            max_len=len(word)
            max_word=word
    return max_word
#判断两个列表是否含有相同的元素（不考虑顺序）
def two_lists_have_same_element(lst1,lst2:list)->bool:
    lst1=set(lst1)
    lst2=set(lst2)
    return lst1==lst2

#将列表中连续出现的重复元素合并为一个
def two_duplicate_element_merge_to_one(lst:list)->list:
    result=[]
    result.append(lst[0])
    for i in range(0,len(lst)-1):
        if lst[i+1]!=lst[i]:
            result.append(lst[i+1])
    return result
#统计每个字符的出现次数（忽略大小写）
from collections import Counter
def count_every_time(s:str)->str:
    count=Counter(s)
    return dict(count.most_common())
#判断列表中是否有重复元素
def whether_list_is_duplicate(lst:list)->bool:
    for num in lst:
        if lst.count(num)>=2:
            return True
    return False
#找出列表中所有长度大于3的字符串
def find_length_greater_three(s:list)->str:
    result=[]
    for word in s:
        if len(word)>=3:
            result.append(word)
    return result
#判断一个字符串是否是回文数字（忽略非数字字符）
'''输入一个字符串，提取其中的所有数字字符，并判断这些数字组成的字符串是否为回文。 '''      
def whether_str_is_huiwen_number(s:str)->bool:
    new_s=""
    for char in s:
        if char.isdigit():
            new_s+=char
    return new_s==new_s[::-1]
#找出列表中只出现一次的元素（整数列表）
def find_one_element(lst:list)->list:
    result=[]
    for num in lst:
        if lst.count(num)==1:
            result.append(num)
    return result
#统计字符串中每个单词的长度
def count_word_length(s:str)->dict:
    result={}
    for word in s:
        result[word]=len(word)
    return result
#找出一个列表中第二大的数字
'''
@param lst: 整数数字构成的列表
@return: 返回第二大的数字
'''
def find_second_max_number_copy(lst:list)->int:
    max_num=max(lst)
    min_num=min(lst)
    second_num=lst[0]
    for num in lst:
        if num <max_num and num>second_num:
            second_num=num
        elif max_num==min_num:
            return lst[0]
    return second_num

#将一个嵌套列表拉平成一维列表
'''
@param:一个二维整数的列表
@return:返回一个一维度列表
'''
def flatten_second_div_to_list(lst:list)->list:
    result=[]
    for num_list in lst:
        for num in num_list:
            result.append(num)
    return result
#检查一段 HTML 是否是成对闭合的标签（只考虑 <tag></tag> 格式）
'''
@param:输入带有html标签的字符串
@return:是否闭合的Boolean值
'''
def html_tag_is_match(s:str) -> bool:
    html_dict={'[':']','{':'}'}
    stack=[]
    for tag in s:
        if tag in html_dict.keys():
            stack.append(tag)
        elif tag in html_dict.values():
            if not stack or html_dict[stack.pop()]!=tag:
                return False
    return True
#读取文件中的每一行
def read_lines_from_file(filename: str) -> list:
    with open(filename,'r') as f:
        #readlines读取所有行,以列表的形式返回但是会保留换行符号,如果想去除需要strip()处理
        file_content=f.readlines()
    result=[]
    for line in file_content:
        #使用strip()去除换行符号
        result.append(line.strip())
    return result
#file_name=input("输入文件路径或当前目录下的文件名: ")
#异常处理模拟
def divide(num1: int, num2: int) -> float:
    try:
        result=num1/num2
        return result
    except ZeroDivisionError:
        return "除0错误"
#写入文件
def write_list_to_file(file_name:str,lst:list) -> None:
    with open(file_name,'w') as f:
        for word in lst:
            f.write(word+'\n')
#读取文本文件的所有行，并逆序输出到屏幕上。
def read_files_reverse_print(file_name:str)->None:
    with open(file_name,'r') as f:
        file_content=f.readlines()
        for word in reversed(file_content):
            print(word.strip())
#读取一个文件，统计文件中总共的字符数、单词数和行数。
def count_char_word_line(file_name:str)->str:
    with open(file_name,'r') as f:
        #readlines返回的是行的列表,读取完一整行后添加换行符号
        file_content=f.readlines()
        line_count=len(file_content)
        char_count=0
        word_count=0
        for line in file_content:
            char_count+=len(line)
            word_count+=len(line.split())
    print("字符数: ",char_count,"单词数: ",word_count,"行数: ",line_count)
#将用户输入的多行文本写入文件（直到输入空行）
def write_mutiple_line_to_file(file_name:str)->None:
    with open(file_name,'a',encoding='utf-8') as f:
        while True:
            line_content=input("输入一行数据: ")
            if line_content=="":
                break
            f.write(line_content+"\n")
#将一个文件的内容拷贝到另一个新文件中
def copy_file_to_new_file(file1,file2):
    with open(file1,'r',encoding='utf-8') as f1:
        file_countent=f1.readlines()
    with open(file2,'w',encoding='utf-8') as f2:
        f2.writelines(file_countent)
#过滤空行并将文件内容复制到新文件
def filter_blank_file1_to_file2(file1,file2):
    with open(file1,'r') as f1:
        f1_filter_content=[line for line in f1 if not line.isspace()]
    with open(file2,'w') as f2:
        f2.writelines(f1_filter_content)
#读取csv文件,并提取列
import csv
def read_csv_file_extract_column(file1,file2,column_name):
    with open(file1,'r') as f1,open(file2,'w') as f2:
        reader=csv.DictReader(f1)
        for row in reader:
            if column_name in row:
                f2.write(row[column_name]+"\n")
#读取一个文件，找出出现次数最多的单词
from collections import Counter
def read_file_find_most_count_word(file1):
    result=[]
    with open(file1,'r') as f1:
        file_content=f1.readlines()
    for line in file_content:
        #字符串不可修改,需要赋值返回
        words_in_line = line.strip().split()
        #split()分开后以列表的形式返回
        result.extend(words_in_line)
    count=Counter(result)
    return count.most_common(1)
#将日志文件中包含某个关键词的行提取出来，写入新文件
def contains_error_to_new_file(file1,file2,keyword):
    keyword=input("输入关键词: ")
    with open(file1,'r') as f1:
        file1_lines=f1.readlines()
    file2_content=[]
    for line in file1_lines:
        if keyword in line:
            new_line=line.strip()
            file2_content.append(new_line)
    with open(file2,'w') as f2:
        f2.writelines(file2_content)
#统计文件中每个单词出现的次数
from collections import Counter
def count_word_times(file1):
    word_lst=[]
    with open(file1,'r') as f1:
        file_content=f1.readlines()
    for line in file_content:
        new_line_lst=line.strip().split()
        word_lst.extend(new_line_lst)
    count=Counter(word_lst)
    for word_times in count.most_common():
        print("单词为:",word_times[0],"次数为:",word_times[1])
#统计文件中每个单词出现次数（忽略大小写）
from collections import Counter
def count_word_count(file_path):
    new_word_list=[]
    with open(file_path,"r") as f:
        file_content=f.readlines()
    for line in file_content:
        word_list=line.strip().split()
        new_word_list.extend(word_list)
    count=Counter(new_word_list)
    return count.most_common()
#将文本文件中所有数字提取出来，写入新文件
def extract_num_to_new_file(file1,file2):
    write_content=[]
    with open(file1,'r',encoding='utf-8') as f1:
        file_content=f1.readlines()
    for line in file_content:
        new_line=line.strip().split()
        for element in new_line:
            if element.isdigit():
                write_content.append(element)
                write_content.append(';')
    with open(file2,'w',encoding='utf-8') as f2:
        f2.writelines(write_content)
#读取csv文件
import csv
def read_csv_file(file_path):
    with open(file_path,'r',encoding='utf-8') as f:
        csv_reader=csv.reader(f)
        for row in csv_reader:
            print(row)
#写入csv文件
import csv
def write_csv_file(file_path):
    data=[[12,'peter'],[14,'david']]
    with open(file_path,'a',encoding='utf-8',newline='') as f:
        csv_writer=csv.writer(f)
        for row in data:
            csv_writer.writerow(row)
#使用dict_reader读取文件
import csv
def read_file_from_dict(file_path):
    with open(file1,'r',encoding='utf-8') as f:
        csv_reader=csv.DictReader(f)
        for row in csv_reader:
            print(row)
#使用dict_writer写入文件
import csv
def write_file_from_dict(file_path):
    data=[{'age':12,'name':'cc'},{'age':11,'name':'aa'}]
    with open(file_path,'a',encoding='utf-8',newline='') as f:
        colname=['age','name']
        csv_dict_writer=csv.DictWriter(f,fieldnames=colname)
        #判断表头是否为空,空的话写表头
        for row in data:
            csv_dict_writer.writerow(row)
#读取csv文件过滤出年龄大于25的数据并写入新文件
import csv
def filter_age_to_new_file(file1,file2):
    with open(file1,'r',encoding='utf-8') as f1,open(file2,'w',encoding='utf-8',newline='') as f2:
        csv_reader=csv.reader(f1)
        csv_writer=csv.writer(f2)
        for row in csv_reader:
            for item in row:
                if item.isdigit() and int(item)>25:
                    csv_writer.writerow(row)
#读取csv文件过滤出年龄大于25的数据并写入新文件（使用csv_dict）
import csv
def filter_age_to_new_file_dict(file1,file2):
    with open(file1,'r',encoding='utf-8') as f1,open(file2,'a',encoding='utf-8',newline='') as f2:
        colname=csv.DictReader(f1).fieldnames
        csv_dict_reader=csv.DictReader(f1,fieldnames=colname)
        csv_dict_writer=csv.DictWriter(f2,fieldnames=colname)
        for row in csv_dict_reader:
            if row['age'].isdigit() and int(row['age'])>25:
                csv_dict_writer.writerow(row)
#读取csv文件
import csv
def read_csv_file_use_dict(file1):
    with open(file1,'r',encoding='utf-8') as f1:
        csv_reader=csv.DictReader(f1)
        for row in csv_reader:
            print(row)
#写入并读取文件内容
#描述：将一个字符串写入 example.txt 文件中，然后读取出来并打印。
def write_str_to_file(file1):
    with open(file=file1,mode='w',encoding='utf-8') as f1:
        f1.write("hello world!")
    with open(file1,'r') as f1:
        print(f1.read())
#文件 lines.txt 中包含多行文本，请统计该文件共有多少行。
def count_line(file1):
    with open(file1,'r',encoding='utf-8') as f1:
        line_count=len(f1.readlines())
    return line_count
#题目 3：复制文件内容
#描述：将 source.txt 中的内容复制到 destination.txt。
def copy_file1_to_file2(file1,file2):
    with open(file1,'r',encoding='utf-8') as f1,open(file2,'w+',encoding='utf-8') as f2:
        f2.writelines(f1.readlines())
    with open(file2,'r',encoding='utf-8') as f2:
        print(f2.read())
#写一个函数，返回前 n 项斐波那契数列
def return_fibnacci_list(n):
    result=[1,1]
    if n<=2:
        return result[:n] 
    if n>2:
        for i in range(2,n):
            next_num=result[i-1]+result[i-2]
            result.append(next_num)
        return result
#给定一个字典 {‘a’: 3, ‘b’: 1, ‘c’: 2}，按 value 从小到大排序。
def sort_dict_by_values(dict1):
    item=list(dict1.items())
    item.sort(key=lambda x: x[1])
    new_dict={}
    for key,values in item:
        new_dict[key]=values
    return new_dict
#找出字典中 value 最大的 key
def find_value_max_key(dict1):
    items=list(dict1.items())
    items.sort(key=lambda x:x[1],reverse=True)
    return items[0][0]
#统计字符串中每个字符出现的次数（构建字典）
from collections import Counter
def count_char_time(str1):
    count=Counter(str1)
    return dict(count)
#交换字典中的 key 和 value
def exchange_key_value(dict1):
    new_dict={}
    for key,values in dict1.items():
        new_dict[values]=key
    return new_dict
#匹配所有 3 位数字
#字符串： "abc123 xyz456 78 9000"
import re
def match_three_number(str):
    pattern = re.compile(r'(?<!\d)\d{3}(?!\d)')
    return pattern.findall(str)
#提取所有以 a 开头、以 c 结尾的三字母单词
#字符串： "abc a7c acc adc a-c aac"
import re
def match_a_and_c(str):
    pattern=re.compile(r'\ba[a-zA-Z]{1}c\b')
    return pattern.findall(str)
#匹配合法的邮箱地址
#字符串： "tom@example.com, not_an_email, jane-doe@company.org"
import re
def match_email(str):
    pattern=re.compile(r'[a-zA-Z-.]+@[a-zA-Z]+\.+(com|org)')
    print(pattern.match(str))
    #for result in pattern.finditer(str):
        #print(result.group(0))
#给定数组长度为n的数组找到峰值并返回索引
import random
def find_top_index(lst)->int:
    result=[]
    try:
        for i in range(1,len(lst)-1):
            #判断是否为山峰
            if lst[i]>lst[i-1] and lst[i]>lst[i+1]:
                result.append(i)
        #使用random.choice返回任一索引
        return random.choice(result)
    #choice无法在空列表的情况下使用
    except IndexError:
        return "输入列表无山峰"
# 绝对值转int类型
import math
def fabs_convert_to_int(num:int)->int:
    return int(math.fabs(num))
#统计字符串中各字符出现的次数
from collections import Counter
def count_times_in_string(str):
    count=Counter(str)
    return dict(count)
#找出列表中的最大差值
#题目描述：
#给定一个整数列表，找出其中两个数的最大差值（较大的数必须出现在较小的数之后）。
def find_max_difference(lst):
    result=[]
    for i in range(0,len(lst)-1):
        for j in range(i,len(lst)):
            if lst[j]>lst[i]:
                cha=lst[j]-lst[i]
                result.append(cha)
    return max(result)
#输入一个字符串，判断是否为回文（正着读和反着读都一样）。
def panduan_is_huiwen(str):
    return str==str[::-1]
#给定一段英文文本字符串，统计各单词出现的频率，返回一个字典，按频率从高到低排序
from collections import Counter
def count_word_in_str(s):
    new_s=s.replace('.','')
    count=Counter(new_s.split())
    return dict(count)
#给定一个整数列表，所有元素都出现了两次，只有一个元素只出现一次，找出它
def find_one_element(lst):
    new_lst=[x for x in lst if lst.count(x)==1]
    return new_lst[0]

#反转字符串
def reverse_a_string(str):
    res = []  # 用于存放所有单词
    word = ''  # 当前单词的字符

    i = len(str) - 1
    while i >= 0:
        if str[i] != ' ':
            word = str[i] + word  # 从后往前添加字符
        else:
            if word:
                res.append(word)
                word = ''
        i -= 1

    if word:  # 加入最后一个单词（如果有）
        res.append(word)

    # 手动拼接单词
    result = ''
    for i in range(len(res)):
        result += res[i]
        if i != len(res) - 1:
            result += ' '

    return result
#提取ms并计算最大最小平均
'''
logs = [
    "2025-06-19 12:00:01 - GET /api/user - 200 OK - 132ms",
    "2025-06-19 12:00:02 - GET /api/order - 200 OK - 215ms",
    "2025-06-19 12:00:03 - GET /api/user - 500 ERROR - 503ms",
    "2025-06-19 12:00:04 - GET /api/user - 200 OK - 87ms"
]
# TODO:提取所有ms值,统计 max/min/avg
'''
import re
def extract_ms_from_log(log_lst):
    pattern=re.compile(r'\d+ms')
    ms_lst,count_lst=[],[]
    for log in log_lst:
        ms=pattern.findall(log)
        ms_lst.extend(ms)
    for ms_log in ms_lst:
        ms_count=ms_log.strip('ms')
        count_lst.append(int(ms_count))
    print("ms值为:",ms_lst)
    print(f'ms的最大值为{max(count_lst)},最小值为{min(count_lst)},平均值为{sum(count_lst)//len(count_lst)}')


#写一个函数，接收一个字符串列表，返回其中 长度大于 5 且包含字母“a” 的所有字符串列表。
def return_contains_a(lst):
    new_lst=[x for x in lst if len(x)>5 and x.count('a')>=1]
    return new_lst
#写一个函数，统计一段文本中，每个单词出现的次数，结果用字典返回，忽略大小写
from collections import Counter
import re
def return_count_char(s):
    pattern=re.compile(r'\w+')
    new_lst=pattern.findall(text.lower())
    count=Counter(new_lst)
    return dict(count)
'''
编写一个函数：

    接收一个文件路径

    读取文件内容

    将所有行写入另一个新文件，但要剔除掉所有空行

    如果文件不存在，捕获异常并打印 文件不存在
'''
def write_file1_content_to_file2(file1,file2):
    try:
        with open(file1,'r',encoding='utf-8') as f1,open(file2,'w',encoding='utf-8') as f2:
            for line in f1:
                if not line.isspace():
                    f2.write(line)
    except FileNotFoundError:
        print("文件未找到")
'''
从下面的字符串里，提取所有以 http 或 https 开头的链接：

请访问：
https://www.baidu.com
也可以看看 http://example.org
还有一个：https://test.com/path
'''
import re 
def extract_http_from_str(s):
    pattern=re.compile(r'https?://\S+')
    return pattern.findall(s)
'''
有两个文本文件 file1.txt 和 file2.txt。

请编写一个函数：

    把 file1.txt 和 file2.txt 的所有内容合并到一个新文件 merged.txt

    合并时，每个文件的内容之间加一行分隔线："====分隔线====\n"
'''
def merge_file1_file2_to_file3(file1,file2,file3):
    with open(file1,'r',encoding='utf-8') as f1,open(file2,'r',encoding='utf-8') as f2,open(file3,'w',encoding='utf-8') as f3:
        f3.writelines(f1.readlines())
        f3.write('\n====分隔线====\n')
        f3.writelines(f2.readlines())

'''
给定如下列表：

people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 25},
    {"name": "David", "age": 35}
]

请按照：

    age 升序

    若 age 相同，按 name 字母顺序
'''
def sorted_dict_by_age_and_name(dict1):
    sorted_dict=sorted(people,key=lambda p:(p['age'],p['name']))
    return sorted_dict

#输入一个整数列表，找出所有差值最小的数对
def return_min_difference(lst):
    lst.sort()
    result=[]
    for i in range(0,len(lst)-1):
        result.append([lst[i],lst[i+1]])
    return result
if __name__=="__main__":
    arr = [4, 2, 1, 3]
    print(return_min_difference(lst=arr))
