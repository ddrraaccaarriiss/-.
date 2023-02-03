GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
del GeekTech['bag']
GeekTech['address'] = 'Ibraimova 103'
GeekTech['contacts'] = 'tel:+996507052018', 'inst:geektech_edu'
GeekTech['courses'].append('UX/UI-дизайн')
GeekTech['courses'] = set(GeekTech['courses'])
GeekTech['founding date'] = '2018'
amount_of_courses = len(GeekTech['courses'])
GeekTech['amount_of_courses'] = amount_of_courses
for k, v in GeekTech.items():
    print(f'{k} ===> {v}')




