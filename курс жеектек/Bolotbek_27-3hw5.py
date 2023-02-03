GeekTech = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}

del GeekTech['bag']
GeekTech['address'] = 'ibraimova 103'
GeekTech['courses'].insert(1, 'IOS')
GeekTech['courses'] = set(GeekTech['courses'])
GeekTech['instagram'] = '@geektech_edu'
GeekTech['number'] = '+996507052018'
GeekTech['date'] = '07.05.2018'
print(f"curses count - {len(GeekTech['courses'])}")
for k, v in GeekTech.items():
    print(f'{k} ==>  {v}')








