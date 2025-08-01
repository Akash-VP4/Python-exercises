def select_student(students, threshold):
    result = {}
    accepted = []
    refused = []

    for i in students:
        if i[1] < threshold:
            refused.append(i)
        else:
            accepted.append(i)

    result["Accepted"] = sorted(accepted, reverse=True, key=lambda student: student[1])
    result["Refused"] = sorted(refused, key=lambda student: student[1])

    # print(result)
    return result
