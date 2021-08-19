
# For example, 
# given [0, 1, 3, 50, 75], lower = 0 and upper = 99, 
# return ["2", "4->49", "51->74", "76->99"].
def find_range(lower, upper):
    if lower == upper :
        return "{}".format(lower)
    else:
        return "{}->{}".format(lower, upper)


def find_missing_range(list_verify,lower_val,upper_val):
    pre = lower_val
    range_list = [] 
    for i in range(len(list_verify) + 1):
        if i == len(list_verify):
            upper_val_check = upper_val + 1
        else:
            upper_val_check = list_verify[i]
            lower_val_check = list_verify[i-1]
        if upper_val_check - lower_val_check >= 2:
            range_list.append(find_range(lower_val_check + 1, upper_val_check - 1))
    return range_list
     
lower_val =0
upper_val= 99
list_verify = [0, 1, 3, 50, 75]
output_list = []

p = find_missing_range(list_verify,lower_val,upper_val)   
print(p)
