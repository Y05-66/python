info_dict = {
    "王力宏":{
        "部门":"科技部",
        "工资":3000,
        "级别":1
    },
    "周杰伦":{
        "部门":"市场部",
        "工资":5000,
        "级别":2
    },
    "林俊杰":{
        "部门":"市场部",
        "工资":7000,
        "级别":3
    },
    "张学友":{
        "部门":"科技部",
        "工资":4000,
        "级别":1
    },
    "刘德华": {
        "部门": "市场部",
        "工资": 6000,
        "级别": 2
    }
}

for name in info_dict:
    if info_dict[name]["级别"] == 1:
        employee_info_dict = info_dict[name]
        employee_info_dict["级别"] = 2
        employee_info_dict["工资"] += 1000
        info_dict[name] = employee_info_dict
print(info_dict)