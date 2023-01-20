import json


with open('json_file', 'r') as json_files:
    data = json.load(json_files)
    for names in data:
        print(names['name'])

    unique_positions = set()
    for position in data:
        if position['position'] not in unique_positions:
            print(position['position'])
            unique_positions.add(position['position'])

    salary_sum =0
    salary_rank =dict()
    for salary in data:
        salary_rank.update(sorted(data, key = salary['salary'], reverse=True)[:10])
        salary_sum += salary['salary']

    print(salary_sum)
    tax_procent = int(input('Introdul procentul de impozit'))
    tax = (tax_procent / 100) * salary_sum
    print(tax)

    print(salary_rank)

