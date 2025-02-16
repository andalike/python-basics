scores =[89,98,97,87,50,60,100,109,-9]

def calcualte_average(numbers):
    return sum(numbers)/len(numbers)

def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num>max_num:
            max_num=num
    return max_num        


print(f"Average Score :{calcualte_average(scores)}")
print(f"Max Score :{find_max(scores)}")


def analyze_number(num):
    is_even  = num%2 ==0
    is_positive = num>0
    return is_even , is_positive


num = 19
val1, val2 = analyze_number(num)
print(f"{num} is even : {val1}")
print(f"{num} is positive : {val2}")