"""
    range ---> datatype ---> create iterable object --->
    ---> range can be used like a counter

"""

r = range(10)  ##  ---> (0, 10, 1) ---> 0 9
### (20,2,-1)  ---> 20 , 3 =====> 2-(-1)
print(r)  # range object ---> iterate over it
"""
    range: 
        start:0
        step:1
        end:10
        
    from:  start ---> last value < end 
"""
l = list(r)
print(l)

"""
    range ---> suppot integer values only ----> 
"""

# myrange=range(3,20,2)
# print(list(myrange))


# myrange=range(3,20,-2)
# print(list(myrange))

# myrange=range(2000000,3,-2)
# print(list(myrange))

###################################
# import  sys
# print(sys.getsizeof(myrange))  # fixed size in the memory


############################# loop #############################
"""
    while condition:
        do something 
"""
### control flow statement
# for i in range(5):  # 0---> 4
#     if i ==4:
#         break  # break loop
#     print(i)

##### continue
# for i in range(5):  # 0---> 4
#     if i ==3:
#         continue  # skip to the next iteration  ---> complete the loop --->
#     print(i)






# nums = []
#
# # for i  in range(5):
# #     while True:
# #         num = input(f"please enter number {i}: ")
# #         if num.isdigit():
# #             nums.append(int(num))
# #             break
# #         print(f"---- please provide suitable input for {i} ,,,, ")
# #
#
# # i=0
# # while i < 5:
# #     print(i)
# #     i +=1
# #
#
#
#
#
#
#
# r = range(0,20,2)
# print(list(r))


#################################################
# for i in range(10):
#     if i == 5:
#         break
#     print(i)
#
# print(f"===== > loop reached the end ============= {i}")


# for i in range(10):  # 0 ----> 9
#     if i == 5:
#         continue
#     print(i)
#
# print(f"===== > loop reached the end ============= {i}")

#
# for i in range(10):  # 0 ----> 9
#     if i == 5:
#         continue
#     print(i)
# else:
#     # this block will be exectuted only if the loop reached the end
#     print(f"===== > loop reached the end ============= {i}")





###############################
print("---- Hello world ----")
##### development phase
for i in range(5):
    pass  # null operation

print("0----- huiii-----")

