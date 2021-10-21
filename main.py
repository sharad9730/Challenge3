def findkeys(my_dict, kv):
    if isinstance(my_dict, dict):
        if kv in my_dict:
            yield my_dict[kv]
        for j in my_dict.values():
            for x in findkeys(j, kv):
                yield x


object = {"x":{"y":{"z":"a", "g": {"3": {"j": 45}}}}}
assert 45 == list(findkeys(object, 'j'))[0], "Failed, Not found"


object = {"z":"y"}
assert "y" == list(findkeys(object, 'z'))[0], "Failed, Not found"


object = {"x":{"y":{"z":"a", "g": {"3": {"j": [1,2,3]}}}}}
assert [1,2,3] == list(findkeys(object, 'j'))[0], "Failed, Not found"

object = {"x":{"y":{"z":"a123", "g": {"3": {"j": [1,2,3]}}}}}
assert "a123" == list(findkeys(object, 'z'))[0], "Failed, Not found"
