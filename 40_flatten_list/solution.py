import copy


def flatten(a_list):
    res = []
    newList = copy.deepcopy(a_list)

    def helper(a_list):

        # count += 1

        # res = []
        # if type(a_list) == type(1):
        #     print(a_list)
        #     return a_list

        for i in range(len(a_list)):
            val = a_list[i]
            # print(val)
            if type(val) == type(["sample list"]):
                temp = helper(val)
                a_list[i] = temp
                # print(a_list, temp)

            else:
                res.append(val)
                # print(val, res)

        # print(res, count)

        return res

    helper(newList)
    return res
