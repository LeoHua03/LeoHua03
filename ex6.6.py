languages={'Mike':'chinese','Jack':'Korean','Mura':'Japanese'}
names=['Mike','Leo','Linda']
lists=[]
for language in languages.keys():
    lists.append(language)

for name in names:
    if name in lists:
        print(f'welcome {name}')
    else:
        print(f'{name} you are invited')