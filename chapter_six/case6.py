favorite_languages = {
'jen': 'python',
'sarah': 'c',
'edward': 'ruby',
'phil': 'python',
}

peoples_dont = ['amir', 'daler' , 'jen', 'sarah']

for name in favorite_languages.keys():
    if name in peoples_dont:
        print(name + " ok")
    else:
        print("no " + name)