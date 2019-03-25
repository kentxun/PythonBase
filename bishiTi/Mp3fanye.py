
import  sys

music_num= sys.stdin.readline()
operation = sys.stdin.readline()
op_list = list(operation.strip())

cur_head = 1
cur_pos = 0
if music_num<=4:
    for i in range(len(op_list)):
        if op_list[i]=='U':
            cur_pos = (cur_pos+music_num-1)% music_num
        else:
            cur_pos = (cur_pos+1)% music_num

else:
    for t in range(len(op_list)):
        if op_list[t]=='U':
            if cur_head == 1 and cur_pos==0:
                cur_head = music_num -3
                cur_pos = 3
            else:
                if cur_pos>0:
                    cur_pos=cur_pos-1
                else:
                    cur_head=cur_head-1
        else:
            if cur_head==music_num-3 and cur_pos==3
                cur_head = 1
                cur_pos =0
            else:
                if cur_pos<3:
                    cur_pos=cur_pos+1
                else:
                    cur_head=cur_head