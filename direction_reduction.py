'''
Write a function dirReduc which will take an array of strings and returns an array of strings with the needless directions removed (W<->E or S<->N side by side).
'''

def dirReduc(arr):
    #рабочий код, но codewars говорит, что долгий
    # arr_lenght=len(arr)
    # a=True
    # while a:
    #     j=0
    #     for j in range(arr_lenght):
    #         try:
    #             if arr[j]=="NORTH" and arr[j+1]=="SOUTH" or (
    #             arr[j]=="SOUTH" and arr[j+1]=="NORTH") or (
    #             arr[j]=="EAST" and arr[j+1]=="WEST") or (
    #             arr[j]=="WEST" and arr[j+1]=="EAST"):
    #                 del arr[j:j+2]
    #                 break
    #             else:continue
    #         except IndexError: a=False
    # print(arr)

    opposites = { "NORTH": "SOUTH", "SOUTH": "NORTH", "EAST": "WEST", "WEST": "EAST" }

    new_list = [ ] 
    for i in range(0,len(arr)): 
        if len(new_list) == 0: 
            new_list.append(arr[i]) 
        elif new_list[-1] != opposites[arr[i]]: 
            new_list.append(arr[i]) 
        else: 
            new_list.pop() 
    print(new_list)

dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"])