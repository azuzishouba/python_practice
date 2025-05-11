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
    with open(file_name,'r') as f:
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
if __name__=="__main__":
    num1=int(input("输入整数数字1: "))
    num2=int(input("输入整数数字2: "))
    print(divide(num1,num2))