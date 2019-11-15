def _get_ratio(fasta):
    if fasta.count('C') > 0:
        return ((fasta.count('G')+fasta.count('C'))/len(fasta))*100


f = open("rosalind_gc.txt", "r")
split_line = f.read().split()

print(split_line)
make_dict = {}
for elm in split_line:

    if elm[0] == '>':
        make_dict[elm] = ""
        # put it into a new key
        key = elm
    else:
        make_dict[key] += elm
        # concat it with prev and put as value

res_dict = {}
res = 0
for i in make_dict.keys():
    res_io = _get_ratio(make_dict[i])
    if res_io>res:
        res = res_io
        fin_key = i
print(fin_key[1:])
print(res)
