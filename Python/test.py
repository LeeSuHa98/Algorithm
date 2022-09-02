def solution(id_list, report, k):
    answer = []
    answer = [0 for i in range(len(id_list))]
    for i in range(len(report)):
        name, r = report[i].split(" ")

        location = id_list.index(r)
        print(location)
        num = answer[location]
        num += 1
        answer[location] = num
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))