from typing import List, Union, Optional

#-------------------------------------------------------------------------------------------------

def mean(nums:list[float]) -> float | None:
    if len(nums) == 0: 
        return None
    result = 0
    for i in nums:
        result += i
    return result / len(nums)

def median(nums: list[float]) -> float | None:
    if len(nums) == 0:
        return None
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_nums[mid - 1] + sorted_nums[mid]) / 2
    else:
        return sorted_nums[mid]

def mode(nums: List[float]) -> Union[float, int, List[Union[float, int]], None]:
    if len(nums) == 0:
        return None
    
    frequency = {}
    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1
    
    max_freq = max(frequency.values())

    modes = [num for num, freq in frequency.items() if freq == max_freq]
    
    if len(modes) == 1:
        return modes[0]
    else:
        if len(modes) == len(nums):
            return None
        return modes
    
def g_mean(nums: list)->float | None:
    if len(nums) == 0: return None
    r = 1
    for i in nums:
        r *= i
    return r ** (1/len(nums))

def h_mean(nums: list) -> float | None:
    l = len(nums)
    if l == 0 :
        return None
    numl = []
    r = 0

    for i in nums:
        numl.append(1/i)

    for i in numl:
        r += i
    r = l / r

    return r

def t_mean(nums: List[float], trim_percent: float = 0.2) -> float | None:
    if trim_percent < 0 or trim_percent > 0.5:
        return None
    
    if not nums:
        return 0.0
    
    sorted_data = sorted(nums)
    n = len(sorted_data)
    
    k = int(n * trim_percent)
    
    if k == 0:
        return sum(sorted_data) / n

    trimmed_data = sorted_data[k:-k]
    
    if not trimmed_data:
        return 0.0
    
    return sum(trimmed_data) / len(trimmed_data)

def variance(nums:list[float]) -> float | None:
    l = len(nums)
    if l == 0: return None
    if l == 1: return 0
    Mean = mean(nums)
    ltm = []
    stm = []
    result = 0
    for i in nums:
        ltm.append(i - Mean)
    for i in ltm:
        stm.append(i ** 2)
    for i in stm:
        result += i
    result /= l - 1

    return result
def pvariance(nums:list[float]) -> float | None:
    l = len(nums)
    if l == 0: return None
    if l == 1: return 0
    Mean = mean(nums)
    ltm = []
    stm = []
    result = 0
    for i in nums:
        ltm.append(i - Mean)
    for i in ltm:
        stm.append(i ** 2)
    for i in stm:
        result += i
    result /= l

    return result

def std_deviation(nums:list[float]) -> float:
    return variance(nums)**0.5
def std_pdeviation(nums:list[float]) -> float:
    return pvariance(nums)**0.5

def data_r(nums:list[float]) -> float:
    if len(nums) == 0 : return 0
    return max(nums)-min(nums)


def percentile(nums: List[float], p: float) -> float:
    if not nums:
        return 0.0
    
    sorted_nums = sorted(nums)
    n = len(sorted_nums)
    
    position = (p / 100) * (n - 1) + 1
    
    if position <= 1:
        return sorted_nums[0]
    elif position >= n:
        return sorted_nums[-1]
    
    lower_index = int(position) - 1
    fractional = position - int(position)
    
    return sorted_nums[lower_index] + fractional * (sorted_nums[lower_index + 1] - sorted_nums[lower_index])