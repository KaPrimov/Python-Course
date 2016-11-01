people = [
    {
        'name': "Мария",
        'interests': {'пътуване', 'танци', 'плуване', 'кино'},
        'gender': "female",
    },
    {
        'name': "Диана",
        'interests': {'мода', 'спортна стрелба', 'четене', 'скандинавска поезия'},
        'gender': "female",
    },
    {
        'name': "Дарина",
        'interests': {'танци', 'покер', 'история', 'софтуер'},
        'gender': "female",
    },
    {
        'name': "Лилия",
        'interests': {'покер', 'автомобили', 'танци', 'кино'},
        'gender': "female",
    },
    {
        'name': "Галя",
        'interests': {'пътуване', 'автомобили', 'плуване', 'баскетбол'},
        'gender': "female",
    },
    {
        'name': "Валерия",
        'interests': {'плуване', 'покер', 'наука', 'скандинавска поезия'},
        'gender': "female",
    },
    {
        'name': "Ина",
        'interests': {'кино', 'лов със соколи', 'пътуване', 'мода'},
        'gender': "female",
    },
    {
        'name': "Кирил",
        'interests': {'баскетбол', 'автомобили', 'кино', 'наука'},
        'gender': "male",
    },
    {
        'name': "Георги",
        'interests': {'автомобили', 'футбол', 'плуване', 'танци'},
        'gender': "male",
    },
    {
        'name': "Андрей",
        'interests': {'футбол', 'скандинавска поезия', 'история', 'танци'},
        'gender': "male",
    },
    {
        'name': "Емил",
        'interests': {'летене', 'баскетбол', 'софтуер', 'наука'},
        'gender': "male",
    },
    {
        'name': "Димитър",
        'interests': {'футбол', 'лов със соколи', 'автомобили', 'баскетбол'},
        'gender': "male",
    },
    {
        'name': "Петър",
        'interests': {'пътуване', 'покер', 'баскетбол', 'лов със соколи'},
        'gender': "male",
    },
    {
        'name': "Калоян",
        'interests': {'история', 'покер', 'пътуване', 'автомобили'},
        'gender': "male",
    },
]

for indx, records in enumerate(people):
    first_gender = records.get('gender')
    first_name = records.get('name')
    first_inter = records.get('interests')

    for indx in range(indx+1, len(people)):
        matching_gender = people[indx].get('gender')
        matching_name = people[indx].get('name')
        matching_interest = set(people[indx].get('interests'))

        if first_gender != matching_gender:
            if first_inter.intersection(matching_interest):
                common_interests = first_inter.intersection(matching_interest)
                print("{} и {} - общ интерес {}".format(first_name, matching_name, common_interests))
