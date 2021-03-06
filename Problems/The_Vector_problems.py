# version code b7f7ff63f9f3+
# Please fill out this stencil and submit using the provided submission script.

# Some of the GF2 problems require use of the value GF2.one so the stencil imports it.

from GF2 import one



## 1: (Problem 2.14.1) Vector Addition Practice 1
#Please express each answer as a list of numbers
p1_v = [-1, 3]
p1_u = [0, 4]
p1_v_plus_u = [-1,7]
p1_v_minus_u = [-1,-1]
p1_three_v_minus_two_u = [-3,1]



## 2: (Problem 2.14.2) Vector Addition Practice 2
p2_u = [-1,  1, 1]
p2_v = [ 2, -1, 5]
p2_v_plus_u = [1,0,6]
p2_v_minus_u = [3,-2,4]
p2_two_v_minus_u = [5,-3,9]
p2_v_plus_two_u = [0,1,7]



## 3: (Problem 2.14.3) Vector Addition Practice 3
# Write your answer using GF2's one instead of the number 1
p3_vector_sum_1 = [one,0,0]
p3_vector_sum_2 = [0,one,one]


### TODO
## 4: (Problem 2.14.4) GF2 Vector Addition A
# Please express your solution as a subset of the letters {'a','b','c','d','e','f'}.
# For example, {'a','b','c'} is the subset consisting of:
#   a (1100000), b (0110000), and c (0011000).
# The answer should be an empty set, written set(), if the given vector u cannot
# be written as the sum of any subset of the vectors a, b, c, d, e, and f.

def get_gf_sum(u,v):
    return [u+v for u,v in zip(u,v)]


gf_dict = {'a':[one,one,0,0,0,0,0],'b':[0,one,one,0,0,0,0],'c': [0,0,one,one,0,0,0],'d' :[0,0,0,one,one,0,0],'e': [0,0,0,0,one,one,0],'f': [0,0,0,0,0,one,one]}

t1 = [0,0,one,0,0,one,0]
t2 = [0,one,0,0,0,one,0]

# sum_result = sum_all(gf_dict)
# print(check(sum_result,t1))

u_0010010 = ...
u_0100010 = ...



## 5: (Problem 2.14.5) GF2 Vector Addition B
# Use the same format as the previous problem

v_0010010 = ...
v_0100010 = ...



## 6: (Problem 2.14.6) Solving Linear Equations over GF(2)
#You should be able to solve this without using a computer.


# two answers
# x_gf2 = [1,0,0,0] or
x_gf2 = [0,1,1,1]
# x+1111 --> if 1000 then 0111 else if 0111 then 1000

## 7: (Problem 2.14.7) Formulating Equations using Dot-Product
#Please provide each answer as a list of numbers
v1 = [2,3,-4,1]
v2 = [1,-5,2,0]
v3 = [4,1,-1,-1]



## 8: (Problem 2.14.9) Practice with Dot-Product
uv_a = 5
uv_b = 6
uv_c = -5+21
uv_d = -1

