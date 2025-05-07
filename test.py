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
def is_brackets_valid(s: str) -> bool:
    stack=[]
    dict={'(':')','[':']','{':'}'}
    for char in s:
        if char in dict.keys():
            stack.append(char)
        elif char in dict.values():
            if len(stack)==0 or dict[stack.pop()] != char:
                return False
    return True


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
    
if __name__=="__main__":
    lst=list(map(int,input("输入整数:").split()))
    print(two_duplicate_element_merge_to_one(lst))