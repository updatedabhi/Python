# it stores data in key value pair
d = {
  "name": "Abhishek",
  "age": 34,
  "has_gf": False,
  "qualification": ["BTech", "Diploma", "Matric"],
  "marks": [29, 20, 00, 99],
  "address": {
    "city": "Araria",
    "zipcode": 3092,
    "state": "Bihar"
  }
}

# dictonary is mutable

d["qualification"].append("Hello")
d["marks"] = [99, 95]

print(d)
