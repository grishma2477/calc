import add_work
import divi_work
import multiply_work
import sub_work

a = 100
b = 50

total_sum = add_work.add(a,b)
total_sub = sub_work.sub(a,b)
total_multiply = multiply_work.mul(a,b)
total_div = divi_work.div(a,b)

print(f"Total sum is {total_sum}, Total Sub is {total_sub}. Total Multiply is {total_multiply}. Total Div is {total_div}")