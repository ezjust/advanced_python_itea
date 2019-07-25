"""lab items"""
# 1st task
new_list = []
for i in range(0, 101):
    if i % 2 == 0:
        new_list.append(i)

# 2nd task (Create dict with 5 elements where key is country and value is capital)
new_dict = {'Ukraine': 'Kyiv', 'Georgia': 'Tbilisi', 'Belarus': 'Minsk', 'Brasil': 'Brasilia', 'Poland': 'Warsaw'}
countries_list = ('Spain', 'Italy', 'France', 'Chech Republic', 'Great Britain', 'Ireland', 'Iceland', 'Denmark', 'Germany', 'Ukraine')
for country in countries_list:
    if country in new_dict.keys():
        print(f'{new_dict[country]} is THE BEST CITY IN THE WORLD!!!')


