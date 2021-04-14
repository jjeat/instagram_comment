import random

file = open("ids", 'r')
id_lists = []
end_list = []
while True:
    line = file.readline()
    id_lists.append(line)
    if not line:    
         break
    
print(id_lists)

cou = len(id_lists)

print("\n\n총 댓글 작성자 수는 :",cou," 명")

end_list = random.sample(id_lists, 3)

print("\n\n당첨자 -> ",end_list)

file.close()
