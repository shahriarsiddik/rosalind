f = open("rosalind_subs_1.txt", "r")
split_line = f.read().split()
joined_elements = "".join(split_line[:-1])
print(joined_elements)
prob_elem = split_line[-1]
print(prob_elem)
res = ""
for i in range(len(joined_elements)-len(prob_elem)):
    if joined_elements[i:i+len(prob_elem)] == prob_elem:
        res += " " +str(i+1)
        # print(joined_elements[i:i+4])
print(res)
