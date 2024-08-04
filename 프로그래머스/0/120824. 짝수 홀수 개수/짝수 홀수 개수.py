def solution(num_list):
    answer = []
    evenNumber, oddNumber = 0, 0
    for i in num_list :
        if (i % 2) == 0 :
            evenNumber += 1
        else:
            oddNumber += 1        
    answer = [evenNumber, oddNumber]
    return answer