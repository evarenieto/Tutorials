low_primes = {1,3,5,7}
low_primes
low_primes.add(17)
low_primes
low_primes.update({19,23}, {2,29})
low_primes
low_primes.add(15)
low_primes
low_primes.remove(15)
low_primes

set1 = set(range(10))
set2 = {1,2,5,7,11,13,17,19,23}
set1.union(set2)

#| or .union(*others) - all of the items from all of the sets
#& or .intersection(*others) - all of the common items between all of the sets
#- or .difference(*others) - all of the items in the first set that are not in the other sets
#^ or .symmetric_difference(other) - all of the items that are not shared by the two sets

COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(arg):
    hold = []
    for key, value in COURSES.items():
        if value & arg:
            hold.append(key)
    return hold


def covers_all(topics):
    all_courses = []
    for keys, values in COURSES.items():
        if values.issuperset(topics):
            all_courses.append(keys)
    return all_courses
