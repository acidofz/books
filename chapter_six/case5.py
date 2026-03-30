rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'yangtze': 'china',
    'volga': 'russia'
}

for river, country in rivers.items():
    print("The " + river.title() + " runs through " + country.title() + ".")
