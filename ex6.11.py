cities={
    'suzhou':{
        'country':'china',
        'population':'200',
        'fact':'garden',
    },
    
    'shanghai':{
        'country':'china',
        'population':'400',
        'fact':'bund',
    },
    'HK':{
        'country':'china',
        'population':'500',
        'fact':'the peak'
    },
} 
for k,v in cities.items():
    print(f"\n{k}")
    for k1,v1 in v.items():
        print(f"\t{k1}:{v1}")
