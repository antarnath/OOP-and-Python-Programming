data={
    'a':[{
        'aa':{'aax':5,'aay':6,'aaz':7},
        'ab':{'abx':8,'aby':9,'abz':10}
        },
        {
        'aaa':{'aaax':11,'aaay':12,'aaaz':13},
        'aab':{'aabx':14,'aaby':15,'aabz':16}
        }],
    'b':[{
        'ba':{'bax':17,'bay':18,'baz':19},
        'bb':{'bbx':20,'bby':21,'bbz':22}
        },
        {
        'bba':{'bbax':23,'bbay':24,'bbaz':25},
        'bbb':{'bbbx':26,'bbby':27,'bbbz':28}
        }],
    'c':[{
        'ca':{'cax':29,'cay':30,'caz':31},
        'cb':{'cbx':32,'cby':33,'cbz':34}
        },
        {
        'cca':{'ccax':35,'ccay':36,'ccaz':37},
        'ccb':{'ccbx':38,'ccby':39,'ccbz':40}
        }]
}

for key, val in data.items():
    for lis in val:
        for key1, val1 in lis.items():
            for key2, val2 in val1.items():
                print(f'Key:{key2} Value: {val2}')



