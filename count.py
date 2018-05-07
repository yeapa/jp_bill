import re

pay=[[],[],[]]
youzhanghao_index = 0
liangxiangxin_index = 1
yexiang_index = 2
file_name="fee.txt"


def parse_payfile(file_name):
    index=-1
    pattern_pay = re.compile(r'(\d|\*|\-|\+|\/)+')
    pattern_name = re.compile(r'youzhanghao.*|liangxiangxin.*|yexiang.*')

    fee = open(file_name, 'r')
    for line in fee.readlines():
        match_pay = pattern_pay.match(line)
        match_name = pattern_name.match(line)

        if(match_name):
            print(match_name.group())
            index += 1
            
        if(match_pay):
            item=eval(match_pay.group())
            print(index," : ",item)
            pay[index].append(item)

def count_pay():
    youzhanghao_total = sum(pay[youzhanghao_index])
    liangxiangxin_total = sum(pay[liangxiangxin_index])
    yexiang_total = sum(pay[yexiang_index])
    print(youzhanghao_total, liangxiangxin_total, yexiang_total)
    ave = (youzhanghao_total + liangxiangxin_total + yexiang_total) / 3.0
    print(ave)
    youzhanghao_bias = youzhanghao_total - ave
    liangxiangxin_bias = liangxiangxin_total - ave
    yexiang_bias = yexiang_total - ave


    print("--------------result--------------------")
    print("youzhangyhao_bias:",youzhanghao_bias,"liangxiangxin_bias:", liangxiangxin_bias,"yexiang_bias:", yexiang_bias)

    pass

def main():
    parse_payfile(file_name)
    print(pay[youzhanghao_index], pay[liangxiangxin_index], pay[yexiang_index],sep='\n')
    count_pay()


if __name__ == '__main__':
    main()