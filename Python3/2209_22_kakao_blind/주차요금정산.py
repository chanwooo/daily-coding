import math


def solution(fees, records):
    # "05:34" 300+34

    record_dict = {key.split(" ")[1]: [0, True] for key in records}
    # print(record_dict)

    for record in records:
        record = record.split(" ")
        time = time_to_min(record[0])
        car_number = record[1]
        in_out = record[2]
        # print(car_number, time, in_out)

        if in_out == "IN":
            record_dict[car_number][0] -= time
            record_dict[car_number][1] = False

        if in_out == "OUT":
            record_dict[car_number][0] += time
            record_dict[car_number][1] = True

    for record in record_dict:
        if not record_dict[record][1]:
            record_dict[record][0] += time_to_min("23:59")
            record_dict[record][1] = True

    for record in record_dict:
        if record_dict[record][0] <= fees[0]:
            record_dict[record][0] = fees[1]
        else:
            record_dict[record][0] = fees[1] \
                                     + math.ceil((record_dict[record][0] - fees[0]) / fees[2]) \
                                     * fees[3]

    record_dict = sorted(record_dict.items())
    print(record_dict)

    answer = []
    for r in record_dict:
        answer.append(r[1][0])
    return answer

def time_to_min(time):
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])


print(solution([180, 5000, 10, 600],
               ["05:34 5961 IN", "06:00 0000 IN",
                "06:34 0000 OUT", "07:59 5961 OUT",
                "07:59 0148 IN", "18:59 0000 IN",
                "19:09 0148 OUT", "22:59 5961 IN",
                "23:00 5961 OUT"]))  # [14600, 34400, 5000]
