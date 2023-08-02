import requests


def r_get(baseurl, baseparam, check):
    res = requests.get(url=baseurl, params=baseparam)
    if res.status_code == check:
        return True
    else:
        return False
# def r_post(baseurl, baseparam, check):
#     res = requests.post
#
# def result_check(res,check):
#     if res.status_code == check:
#         return True
#     else:
#         return False
testurl = ""
testparam = ""
check = 200
result = r_get(testurl,testparam,check)
assert result == False,"Test Failed"
