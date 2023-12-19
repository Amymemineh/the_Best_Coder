def solution(N, stages):
    answer = []
    fail_dict = {}
    num_people = len(stages)

    for stage in range(1, N+1):
        fail_num = stages.count(stage)
        if num_people > 0:
            fail_dict[stage] = fail_num / num_people
        else: 
            fail_dict[stage] = 0

        num_people -= fail_num

    fail_list = sorted(fail_dict.items(), key=lambda x: (-x[1], x[0]))
    answer = [info[0] for info in fail_list]

    return answer