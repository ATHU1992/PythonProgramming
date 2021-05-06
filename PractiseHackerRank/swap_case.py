def swap_case(s):
    result_str = ""
    for i in s:
        if not i.isalpha():
            result_str = result_str + i
        elif i.isupper():
            result_str = result_str + i.lower()
        elif i.islower():
            result_str = result_str + i.upper()
    return result_str


s_temp = swap_case("ATharva is Great !!!!! 1223")
print(s_temp)
