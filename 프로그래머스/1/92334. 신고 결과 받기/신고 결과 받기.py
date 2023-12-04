def solution(id_list, reports, k):
    answer = []
    
    report_dic = {id:set() for id in id_list}
    id_dic = {id:0 for id in id_list}
    
    for report in reports:
        a, b = report.split(" ")
        report_dic[b].add(a)
    
    for key, value in report_dic.items():
        if len(value) >= k:
            for target in value:
                id_dic[target] +=1
    
    for id in id_list:
        answer.append(id_dic[id])
    
    return answer