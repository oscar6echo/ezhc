
import numpy as np
import pandas as pd
import json


def df_one_idx_several_col():
    dic = {'John': [5, 3, 4, 7, 2],
          'Jane': [2, 2, 3, 2, 1],
          'Joe': [3, 4, 4, 2, 5]}
    
    df = pd.DataFrame.from_dict(dic)
    df.index = ['Apples', 'Oranges', 'Pears', 'Grapes', 'Bananas']
    df.index.name = 'Fruit'
    return df



def df_one_idx_one_col():
    arr = np.array([['Firefox', 'IE', 'Chrome', 'Safari', 'Opera', 'Others'],
                    ['45.0', '26.8', '12.8', '8.5', '6.2', '0.7']]).T

    df = pd.DataFrame(index=data[:, 0], data=data[:, 1], columns=['MktShare'], dtype=np.float)
    df.index.name = 'Brand'
    return df



def df_one_idx_two_col():
    data = [
        [-9.7, 9.4],
        [-8.7, 6.5],
        [-3.5, 9.4],
        [-1.4, 19.9],
        [0.0, 22.6],
        [2.9, 29.5],
        [9.2, 30.7],
        [7.3, 26.5],
        [4.4, 18.0],
        [-3.1, 11.4],
        [-5.2, 10.4],
        [-13.5, 9.8]
    ]
    idx = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']      
    df = pd.DataFrame(index=idx, data=data, columns=['Min', 'Max'])
    df.index.name = 'Month'
    return df



def df_two_idx_one_col():
    data =  [
            ['Internet Explorer',8.0,26.61],
            ['Internet Explorer',9.0,16.96],
            ['Chrome',18.0,8.01],
            ['Chrome',19.0,7.73],
            ['Firefox',12,6.72],
            ['Internet Explorer',6.0,6.40],
            ['Firefox',11,4.72],
            ['Internet Explorer',7.0,3.55],
            ['Safari',5.1,3.53],
            ['Firefox',13,2.16],
            ['Firefox',3.6,1.87],
            ['Opera','11.x',1.30],
            ['Chrome',17.0,1.13],
            ['Firefox',10,0.90],
            ['Safari',5.0,0.85],
            ['Firefox',9.0,0.65],
            ['Firefox',8.0,0.55],
            ['Firefox',4.0,0.50],
            ['Chrome',16.0,0.45],
            ['Firefox',3.0,0.36],
            ['Firefox',3.5,0.36],
            ['Firefox',6.0,0.32],
            ['Firefox',5.0,0.31],
            ['Firefox',7.0,0.29],
            ['Unknown','Unknown',0.29],
            ['Chrome',18.0,0.26],
            ['Chrome',14.0,0.25],
            ['Chrome',20.0,0.24],
            ['Chrome',15.0,0.18],
            ['Chrome',12.0,0.16],
            ['Opera','12.x',0.15],
            ['Safari',4.0,0.14],
            ['Chrome',13.0,0.13],
            ['Safari',4.1,0.12],
            ['Chrome',11.0,0.10],
            ['Firefox',14,0.10],
            ['Firefox',2.0,0.09],
            ['Chrome',10.0,0.09],
            ['Opera','10.x',0.09],
            ['Internet Explorer',8.0,0.09]
            ]

    df = pd.DataFrame(data=data, columns=['Brand', 'Version', 'Market Share'])
    df = df.groupby(['Brand', 'Version']).sum().reset_index()
    df['Agg'] = df[['Brand', 'Market Share']].groupby(['Brand']).transform(sum)
    df = df.sort(['Agg', 'Version'], ascending=[False, True])
    df = df.set_index(['Brand', 'Version'])
    df = df.drop('Agg', axis=1)

    return df



def df_scatter_old(N=10):
    np.random.seed(123456)
    mi = pd.MultiIndex.from_arrays([np.random.uniform(0, 10, size=N), np.random.uniform(0, 10, size=N)])
    df = pd.DataFrame(index=mi, data=np.random.choice(['A', 'B'], size=N))
    df.index.names = ['x', 'y']
    df.columns = ['value']

    return df



def df_scatter():
    data = """
    [{
        "name": "Female",
        "color": "rgba(223, 83, 83, .5)",
        "data": [[161.2, 51.6], [167.5, 59.0], [159.5, 49.2], [157.0, 63.0], [155.8, 53.6],
            [170.0, 59.0], [159.1, 47.6], [166.0, 69.8], [176.2, 66.8], [160.2, 75.2],
            [172.5, 55.2], [170.9, 54.2], [172.9, 62.5], [153.4, 42.0], [160.0, 50.0],
            [147.2, 49.8], [168.2, 49.2], [175.0, 73.2], [157.0, 47.8], [167.6, 68.8],
            [159.5, 50.6], [175.0, 82.5], [166.8, 57.2], [176.5, 87.8], [170.2, 72.8],
            [174.0, 54.5], [173.0, 59.8], [179.9, 67.3], [170.5, 67.8], [160.0, 47.0],
            [154.4, 46.2], [162.0, 55.0], [176.5, 83.0], [160.0, 54.4], [152.0, 45.8],
            [162.1, 53.6], [170.0, 73.2], [160.2, 52.1], [161.3, 67.9], [166.4, 56.6],
            [168.9, 62.3], [163.8, 58.5], [167.6, 54.5], [160.0, 50.2], [161.3, 60.3],
            [167.6, 58.3], [165.1, 56.2], [160.0, 50.2], [170.0, 72.9], [157.5, 59.8],
            [167.6, 61.0], [160.7, 69.1], [163.2, 55.9], [152.4, 46.5], [157.5, 54.3],
            [168.3, 54.8], [180.3, 60.7], [165.5, 60.0], [165.0, 62.0], [164.5, 60.3],
            [156.0, 52.7], [160.0, 74.3], [163.0, 62.0], [165.7, 73.1], [161.0, 80.0],
            [162.0, 54.7], [166.0, 53.2], [174.0, 75.7], [172.7, 61.1], [167.6, 55.7],
            [151.1, 48.7], [164.5, 52.3], [163.5, 50.0], [152.0, 59.3], [169.0, 62.5],
            [164.0, 55.7], [161.2, 54.8], [155.0, 45.9], [170.0, 70.6], [176.2, 67.2],
            [170.0, 69.4], [162.5, 58.2], [170.3, 64.8], [164.1, 71.6], [169.5, 52.8],
            [163.2, 59.8], [154.5, 49.0], [159.8, 50.0], [173.2, 69.2], [170.0, 55.9],
            [161.4, 63.4], [169.0, 58.2], [166.2, 58.6], [159.4, 45.7], [162.5, 52.2],
            [159.0, 48.6], [162.8, 57.8], [159.0, 55.6], [179.8, 66.8], [162.9, 59.4],
            [161.0, 53.6], [151.1, 73.2], [168.2, 53.4], [168.9, 69.0], [173.2, 58.4],
            [171.8, 56.2], [178.0, 70.6], [164.3, 59.8], [163.0, 72.0], [168.5, 65.2],
            [166.8, 56.6], [172.7, 105.2], [163.5, 51.8], [169.4, 63.4], [167.8, 59.0],
            [159.5, 47.6], [167.6, 63.0], [161.2, 55.2], [160.0, 45.0], [163.2, 54.0],
            [162.2, 50.2], [161.3, 60.2], [149.5, 44.8], [157.5, 58.8], [163.2, 56.4],
            [172.7, 62.0], [155.0, 49.2], [156.5, 67.2], [164.0, 53.8], [160.9, 54.4],
            [162.8, 58.0], [167.0, 59.8], [160.0, 54.8], [160.0, 43.2], [168.9, 60.5],
            [158.2, 46.4], [156.0, 64.4], [160.0, 48.8], [167.1, 62.2], [158.0, 55.5],
            [167.6, 57.8], [156.0, 54.6], [162.1, 59.2], [173.4, 52.7], [159.8, 53.2],
            [170.5, 64.5], [159.2, 51.8], [157.5, 56.0], [161.3, 63.6], [162.6, 63.2],
            [160.0, 59.5], [168.9, 56.8], [165.1, 64.1], [162.6, 50.0], [165.1, 72.3],
            [166.4, 55.0], [160.0, 55.9], [152.4, 60.4], [170.2, 69.1], [162.6, 84.5],
            [170.2, 55.9], [158.8, 55.5], [172.7, 69.5], [167.6, 76.4], [162.6, 61.4],
            [167.6, 65.9], [156.2, 58.6], [175.2, 66.8], [172.1, 56.6], [162.6, 58.6],
            [160.0, 55.9], [165.1, 59.1], [182.9, 81.8], [166.4, 70.7], [165.1, 56.8],
            [177.8, 60.0], [165.1, 58.2], [175.3, 72.7], [154.9, 54.1], [158.8, 49.1],
            [172.7, 75.9], [168.9, 55.0], [161.3, 57.3], [167.6, 55.0], [165.1, 65.5],
            [175.3, 65.5], [157.5, 48.6], [163.8, 58.6], [167.6, 63.6], [165.1, 55.2],
            [165.1, 62.7], [168.9, 56.6], [162.6, 53.9], [164.5, 63.2], [176.5, 73.6],
            [168.9, 62.0], [175.3, 63.6], [159.4, 53.2], [160.0, 53.4], [170.2, 55.0],
            [162.6, 70.5], [167.6, 54.5], [162.6, 54.5], [160.7, 55.9], [160.0, 59.0],
            [157.5, 63.6], [162.6, 54.5], [152.4, 47.3], [170.2, 67.7], [165.1, 80.9],
            [172.7, 70.5], [165.1, 60.9], [170.2, 63.6], [170.2, 54.5], [170.2, 59.1],
            [161.3, 70.5], [167.6, 52.7], [167.6, 62.7], [165.1, 86.3], [162.6, 66.4],
            [152.4, 67.3], [168.9, 63.0], [170.2, 73.6], [175.2, 62.3], [175.2, 57.7],
            [160.0, 55.4], [165.1, 104.1], [174.0, 55.5], [170.2, 77.3], [160.0, 80.5],
            [167.6, 64.5], [167.6, 72.3], [167.6, 61.4], [154.9, 58.2], [162.6, 81.8],
            [175.3, 63.6], [171.4, 53.4], [157.5, 54.5], [165.1, 53.6], [160.0, 60.0],
            [174.0, 73.6], [162.6, 61.4], [174.0, 55.5], [162.6, 63.6], [161.3, 60.9],
            [156.2, 60.0], [149.9, 46.8], [169.5, 57.3], [160.0, 64.1], [175.3, 63.6],
            [169.5, 67.3], [160.0, 75.5], [172.7, 68.2], [162.6, 61.4], [157.5, 76.8],
            [176.5, 71.8], [164.4, 55.5], [160.7, 48.6], [174.0, 66.4], [163.8, 67.3]]

    }, {
        "name": "Male",
        "color": "rgba(119, 152, 191, .5)",
        "data": [[174.0, 65.6], [175.3, 71.8], [193.5, 80.7], [186.5, 72.6], [187.2, 78.8],
            [181.5, 74.8], [184.0, 86.4], [184.5, 78.4], [175.0, 62.0], [184.0, 81.6],
            [180.0, 76.6], [177.8, 83.6], [192.0, 90.0], [176.0, 74.6], [174.0, 71.0],
            [184.0, 79.6], [192.7, 93.8], [171.5, 70.0], [173.0, 72.4], [176.0, 85.9],
            [176.0, 78.8], [180.5, 77.8], [172.7, 66.2], [176.0, 86.4], [173.5, 81.8],
            [178.0, 89.6], [180.3, 82.8], [180.3, 76.4], [164.5, 63.2], [173.0, 60.9],
            [183.5, 74.8], [175.5, 70.0], [188.0, 72.4], [189.2, 84.1], [172.8, 69.1],
            [170.0, 59.5], [182.0, 67.2], [170.0, 61.3], [177.8, 68.6], [184.2, 80.1],
            [186.7, 87.8], [171.4, 84.7], [172.7, 73.4], [175.3, 72.1], [180.3, 82.6],
            [182.9, 88.7], [188.0, 84.1], [177.2, 94.1], [172.1, 74.9], [167.0, 59.1],
            [169.5, 75.6], [174.0, 86.2], [172.7, 75.3], [182.2, 87.1], [164.1, 55.2],
            [163.0, 57.0], [171.5, 61.4], [184.2, 76.8], [174.0, 86.8], [174.0, 72.2],
            [177.0, 71.6], [186.0, 84.8], [167.0, 68.2], [171.8, 66.1], [182.0, 72.0],
            [167.0, 64.6], [177.8, 74.8], [164.5, 70.0], [192.0, 101.6], [175.5, 63.2],
            [171.2, 79.1], [181.6, 78.9], [167.4, 67.7], [181.1, 66.0], [177.0, 68.2],
            [174.5, 63.9], [177.5, 72.0], [170.5, 56.8], [182.4, 74.5], [197.1, 90.9],
            [180.1, 93.0], [175.5, 80.9], [180.6, 72.7], [184.4, 68.0], [175.5, 70.9],
            [180.6, 72.5], [177.0, 72.5], [177.1, 83.4], [181.6, 75.5], [176.5, 73.0],
            [175.0, 70.2], [174.0, 73.4], [165.1, 70.5], [177.0, 68.9], [192.0, 102.3],
            [176.5, 68.4], [169.4, 65.9], [182.1, 75.7], [179.8, 84.5], [175.3, 87.7],
            [184.9, 86.4], [177.3, 73.2], [167.4, 53.9], [178.1, 72.0], [168.9, 55.5],
            [157.2, 58.4], [180.3, 83.2], [170.2, 72.7], [177.8, 64.1], [172.7, 72.3],
            [165.1, 65.0], [186.7, 86.4], [165.1, 65.0], [174.0, 88.6], [175.3, 84.1],
            [185.4, 66.8], [177.8, 75.5], [180.3, 93.2], [180.3, 82.7], [177.8, 58.0],
            [177.8, 79.5], [177.8, 78.6], [177.8, 71.8], [177.8, 116.4], [163.8, 72.2],
            [188.0, 83.6], [198.1, 85.5], [175.3, 90.9], [166.4, 85.9], [190.5, 89.1],
            [166.4, 75.0], [177.8, 77.7], [179.7, 86.4], [172.7, 90.9], [190.5, 73.6],
            [185.4, 76.4], [168.9, 69.1], [167.6, 84.5], [175.3, 64.5], [170.2, 69.1],
            [190.5, 108.6], [177.8, 86.4], [190.5, 80.9], [177.8, 87.7], [184.2, 94.5],
            [176.5, 80.2], [177.8, 72.0], [180.3, 71.4], [171.4, 72.7], [172.7, 84.1],
            [172.7, 76.8], [177.8, 63.6], [177.8, 80.9], [182.9, 80.9], [170.2, 85.5],
            [167.6, 68.6], [175.3, 67.7], [165.1, 66.4], [185.4, 102.3], [181.6, 70.5],
            [172.7, 95.9], [190.5, 84.1], [179.1, 87.3], [175.3, 71.8], [170.2, 65.9],
            [193.0, 95.9], [171.4, 91.4], [177.8, 81.8], [177.8, 96.8], [167.6, 69.1],
            [167.6, 82.7], [180.3, 75.5], [182.9, 79.5], [176.5, 73.6], [186.7, 91.8],
            [188.0, 84.1], [188.0, 85.9], [177.8, 81.8], [174.0, 82.5], [177.8, 80.5],
            [171.4, 70.0], [185.4, 81.8], [185.4, 84.1], [188.0, 90.5], [188.0, 91.4],
            [182.9, 89.1], [176.5, 85.0], [175.3, 69.1], [175.3, 73.6], [188.0, 80.5],
            [188.0, 82.7], [175.3, 86.4], [170.5, 67.7], [179.1, 92.7], [177.8, 93.6],
            [175.3, 70.9], [182.9, 75.0], [170.8, 93.2], [188.0, 93.2], [180.3, 77.7],
            [177.8, 61.4], [185.4, 94.1], [168.9, 75.0], [185.4, 83.6], [180.3, 85.5],
            [174.0, 73.9], [167.6, 66.8], [182.9, 87.3], [160.0, 72.3], [180.3, 88.6],
            [167.6, 75.5], [186.7, 101.4], [175.3, 91.1], [175.3, 67.3], [175.9, 77.7],
            [175.3, 81.8], [179.1, 75.5], [181.6, 84.5], [177.8, 76.6], [182.9, 85.0],
            [177.8, 102.5], [184.2, 77.3], [179.1, 71.8], [176.5, 87.9], [188.0, 94.3],
            [174.0, 70.9], [167.6, 64.5], [170.2, 77.3], [167.6, 72.3], [188.0, 87.3],
            [174.0, 80.0], [176.5, 82.3], [180.3, 73.6], [167.6, 74.1], [188.0, 85.9],
            [180.3, 73.2], [167.6, 76.3], [183.0, 65.9], [183.0, 90.9], [179.1, 89.1],
            [170.2, 62.3], [177.8, 82.7], [179.1, 79.1], [190.5, 98.2], [177.8, 84.1],
            [180.3, 83.2], [180.3, 83.2]]
    }]
    """

    import json
    data = json.loads(data)
    li_df = []
    for k, d in enumerate(data):
        df = pd.DataFrame(d['data'], columns=['Height', 'Weight'])
        df['Sex'] = 'Female' if k==0 else 'Male'
        li_df.append(df)

    df = pd.concat(li_df)
    df = df.set_index(['Height', 'Weight'])

    return df



def df_bubble_old(N=10, P=3):
    np.random.seed(123456)
    mi = pd.MultiIndex.from_arrays([np.random.choice(['Cat'+str(1+k) for k in range(P)], size=N),
                                    np.random.uniform(0, 10, size=N),
                                    np.random.uniform(0, 10, size=N),
                                    ])
    df = pd.DataFrame(index=mi, data=np.random.choice(range(1, 5), size=(N)), columns=['value'])
    df.index.names = ['series', 'x', 'y']
    df = df.sortlevel('series')
    return df



def df_bubble():
    data = """
    [{
    "data": [[97, 36, 79], [94, 74, 60], [68, 76, 58], [64, 87, 56], [68, 27, 73], [74, 99, 42], [7, 93, 87], [51, 69, 40], [38, 23, 33], [57, 86, 31]]
    }, {
    "data": [[25, 10, 87], [2, 75, 59], [11, 54, 8], [86, 55, 93], [5, 3, 58], [90, 63, 44], [91, 33, 17], [97, 3, 56], [15, 67, 48], [54, 25, 81]]
    }, {
    "data": [[47, 47, 21], [20, 12, 4], [6, 76, 91], [38, 30, 60], [57, 98, 64], [61, 17, 80], [83, 60, 13], [67, 78, 75], [64, 12, 10], [30, 77, 82]]
    }]
    """
    data = json.loads(data)
    li_df = []
    for k, d in enumerate(data):
        df = pd.DataFrame(d['data'], columns=['x', 'y', 'Size'])
        df['Cat'] = 'Cat'+str(1+k)
        li_df.append(df)
    # pd.read_json(tt[0])

    df = pd.concat(li_df)
    df = df.set_index(['Cat', 'x', 'y'])
    return df



def df_heatmap():
    def mapping(s):
        return [x_cat[s[0]], y_cat[s[1]], s[2]]

    data = [[0, 0, 10], [0, 1, 19], [0, 2, 8], [0, 3, 24], [0, 4, 67], [1, 0, 92], [1, 1, 58], [1, 2, 78], [1, 3, 117], [1, 4, 48], [2, 0, 35], [2, 1, 15], [2, 2, 123], [2, 3, 64], [2, 4, 52], [3, 0, 72], [3, 1, 132], [3, 2, 114], [3, 3, 19], [3, 4, 16], [4, 0, 38], [4, 1, 5], [4, 2, 8], [4, 3, 117], [4, 4, 115], [5, 0, 88], [5, 1, 32], [5, 2, 12], [5, 3, 6], [5, 4, 120], [6, 0, 13], [6, 1, 44], [6, 2, 88], [6, 3, 98], [6, 4, 96], [7, 0, 31], [7, 1, 1], [7, 2, 82], [7, 3, 32], [7, 4, 30], [8, 0, 85], [8, 1, 97], [8, 2, 123], [8, 3, 64], [8, 4, 84], [9, 0, 47], [9, 1, 114], [9, 2, 31], [9, 3, 48], [9, 4, 91]]
    x_cat = ['Alexander', 'Marie', 'Maximilian', 'Sophia', 'Lukas', 'Maria', 'Leon', 'Anna', 'Tim', 'Laura']
    y_cat = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

    df = pd.DataFrame(data=data)
    df = df.apply(mapping, axis=1)
    df.columns = ['Name', 'Day', 'Sales']
    df = df.set_index(['Name', 'Day'])
    return df



def df_two_idx_several_col():
    data = {
        "South-East Asia": {
            "Sri Lanka": {
                "Communicable & other Group I": "75.5",
                    "Injuries": "89.0",
                    "Noncommunicable diseases": "501.2"
            },
                "Bangladesh": {
                "Noncommunicable diseases": "548.9",
                    "Injuries": "64.0",
                    "Communicable & other Group I": "234.6"
            },
                "Myanmar": {
                "Communicable & other Group I": "316.4",
                    "Injuries": "102.0",
                    "Noncommunicable diseases": "708.7"
            },
                "Maldives": {
                "Injuries": "35.0",
                    "Noncommunicable diseases": "487.2",
                    "Communicable & other Group I": "59.2"
            },
                "Democratic People's Republic of Korea": {
                "Injuries": "91.9",
                    "Noncommunicable diseases": "751.4",
                    "Communicable & other Group I": "117.3"
            },
                "Bhutan": {
                "Injuries": "142.2",
                    "Noncommunicable diseases": "572.8",
                    "Communicable & other Group I": "186.9"
            },
                "Thailand": {
                "Injuries": "72.8",
                    "Communicable & other Group I": "123.3",
                    "Noncommunicable diseases": "449.1"
            },
                "Nepal": {
                "Noncommunicable diseases": "678.1",
                    "Injuries": "88.7",
                    "Communicable & other Group I": "251.8"
            },
                "Timor-Leste": {
                "Injuries": "69.2",
                    "Noncommunicable diseases": "670.5",
                    "Communicable & other Group I": "343.5"
            },
                "India": {
                "Communicable & other Group I": "253.0",
                    "Injuries": "115.9",
                    "Noncommunicable diseases": "682.3"
            },
                "Indonesia": {
                "Injuries": "49.3",
                    "Noncommunicable diseases": "680.1",
                    "Communicable & other Group I": "162.4"
            }
        },
            "Europe": {
            "Hungary": {
                "Communicable & other Group I": "16.8",
                    "Noncommunicable diseases": "602.8",
                    "Injuries": "44.3"
            },
                "Poland": {
                "Communicable & other Group I": "22.6",
                    "Noncommunicable diseases": "494.5",
                    "Injuries": "48.9"
            },
                "Israel": {
                "Communicable & other Group I": "31.2",
                    "Noncommunicable diseases": "311.2",
                    "Injuries": "20.8"
            },
                "France": {
                "Communicable & other Group I": "21.4",
                    "Noncommunicable diseases": "313.2",
                    "Injuries": "34.6"
            },
                "Turkey": {
                "Injuries": "39.1",
                    "Communicable & other Group I": "43.9",
                    "Noncommunicable diseases": "555.2"
            },
                "Kyrgyzstan": {
                "Communicable & other Group I": "65.8",
                    "Injuries": "65.1",
                    "Noncommunicable diseases": "835.4"
            },
                "Croatia": {
                "Communicable & other Group I": "12.2",
                    "Noncommunicable diseases": "495.8",
                    "Injuries": "40.1"
            },
                "Portugal": {
                "Injuries": "25.2",
                    "Communicable & other Group I": "39.9",
                    "Noncommunicable diseases": "343.3"
            },
                "Greece": {
                "Injuries": "26.5",
                    "Noncommunicable diseases": "365.0",
                    "Communicable & other Group I": "24.1"
            },
                "Italy": {
                "Injuries": "20.1",
                    "Communicable & other Group I": "15.5",
                    "Noncommunicable diseases": "303.6"
            },
                "Belgium": {
                "Communicable & other Group I": "27.8",
                    "Injuries": "38.9",
                    "Noncommunicable diseases": "356.8"
            },
                "Lithuania": {
                "Noncommunicable diseases": "580.6",
                    "Communicable & other Group I": "25.5",
                    "Injuries": "76.4"
            },
                "Uzbekistan": {
                "Communicable & other Group I": "85.8",
                    "Injuries": "47.4",
                    "Noncommunicable diseases": "810.9"
            },
                "Serbia": {
                "Communicable & other Group I": "19.4",
                    "Injuries": "32.0",
                    "Noncommunicable diseases": "657.7"
            },
                "Austria": {
                "Noncommunicable diseases": "359.5",
                    "Injuries": "30.6",
                    "Communicable & other Group I": "12.6"
            },
                "Bosnia and Herzegovina": {
                "Injuries": "42.4",
                    "Noncommunicable diseases": "512.5",
                    "Communicable & other Group I": "20.0"
            },
                "Slovakia": {
                "Injuries": "39.1",
                    "Communicable & other Group I": "35.3",
                    "Noncommunicable diseases": "532.5"
            },
                "The former Yugoslav republic of Macedonia": {
                "Injuries": "24.0",
                    "Communicable & other Group I": "16.9",
                    "Noncommunicable diseases": "636.5"
            },
                "Sweden": {
                "Communicable & other Group I": "19.3",
                    "Noncommunicable diseases": "333.5",
                    "Injuries": "26.1"
            },
                "Russian Federation": {
                "Noncommunicable diseases": "790.3",
                    "Communicable & other Group I": "73.8",
                    "Injuries": "102.8"
            },
                "Republic of Moldova": {
                "Noncommunicable diseases": "787.6",
                    "Injuries": "75.7",
                    "Communicable & other Group I": "44.5"
            },
                "Ireland": {
                "Injuries": "31.8",
                    "Communicable & other Group I": "21.5",
                    "Noncommunicable diseases": "343.9"
            },
                "Estonia": {
                "Injuries": "47.0",
                    "Communicable & other Group I": "18.5",
                    "Noncommunicable diseases": "510.7"
            },
                "Cyprus": {
                "Noncommunicable diseases": "333.0",
                    "Injuries": "26.6",
                    "Communicable & other Group I": "16.2"
            },
                "Kazakhstan": {
                "Noncommunicable diseases": "949.7",
                    "Injuries": "101.6",
                    "Communicable & other Group I": "55.3"
            },
                "Netherlands": {
                "Noncommunicable diseases": "355.2",
                    "Injuries": "22.3",
                    "Communicable & other Group I": "25.5"
            },
                "Finland": {
                "Noncommunicable diseases": "366.6",
                    "Injuries": "38.7",
                    "Communicable & other Group I": "9.0"
            },
                "Romania": {
                "Noncommunicable diseases": "612.2",
                    "Injuries": "40.7",
                    "Communicable & other Group I": "38.5"
            },
                "Albania": {
                "Noncommunicable diseases": "671.6",
                    "Injuries": "48.0",
                    "Communicable & other Group I": "46.5"
            },
                "Iceland": {
                "Injuries": "29.0",
                    "Noncommunicable diseases": "311.7",
                    "Communicable & other Group I": "14.0"
            },
                "Azerbaijan": {
                "Noncommunicable diseases": "664.3",
                    "Injuries": "33.6",
                    "Communicable & other Group I": "70.8"
            },
                "Tajikistan": {
                "Injuries": "51.6",
                    "Communicable & other Group I": "147.7",
                    "Noncommunicable diseases": "752.6"
            },
                "Bulgaria": {
                "Communicable & other Group I": "33.4",
                    "Injuries": "36.4",
                    "Noncommunicable diseases": "638.2"
            },
                "United Kingdom of Great Britain and Northern Ireland": {
                "Communicable & other Group I": "28.5",
                    "Injuries": "21.5",
                    "Noncommunicable diseases": "358.8"
            },
                "Spain": {
                "Communicable & other Group I": "19.1",
                    "Injuries": "17.8",
                    "Noncommunicable diseases": "323.1"
            },
                "Ukraine": {
                "Communicable & other Group I": "69.3",
                    "Injuries": "67.3",
                    "Noncommunicable diseases": "749.0"
            },
                "Norway": {
                "Noncommunicable diseases": "336.6",
                    "Communicable & other Group I": "25.2",
                    "Injuries": "25.6"
            },
                "Denmark": {
                "Injuries": "22.5",
                    "Communicable & other Group I": "29.5",
                    "Noncommunicable diseases": "406.1"
            },
                "Belarus": {
                "Noncommunicable diseases": "682.5",
                    "Communicable & other Group I": "28.3",
                    "Injuries": "91.3"
            },
                "Malta": {
                "Noncommunicable diseases": "364.5",
                    "Injuries": "19.0",
                    "Communicable & other Group I": "23.6"
            },
                "Latvia": {
                "Noncommunicable diseases": "623.7",
                    "Injuries": "54.5",
                    "Communicable & other Group I": "26.0"
            },
                "Turkmenistan": {
                "Injuries": "93.0",
                    "Communicable & other Group I": "115.8",
                    "Noncommunicable diseases": "1025.1"
            },
                "Switzerland": {
                "Communicable & other Group I": "14.5",
                    "Noncommunicable diseases": "291.6",
                    "Injuries": "25.4"
            },
                "Luxembourg": {
                "Injuries": "31.1",
                    "Noncommunicable diseases": "317.8",
                    "Communicable & other Group I": "20.5"
            },
                "Georgia": {
                "Injuries": "32.2",
                    "Communicable & other Group I": "39.3",
                    "Noncommunicable diseases": "615.2"
            },
                "Slovenia": {
                "Noncommunicable diseases": "369.2",
                    "Communicable & other Group I": "15.4",
                    "Injuries": "44.2"
            },
                "Montenegro": {
                "Communicable & other Group I": "18.7",
                    "Noncommunicable diseases": "571.5",
                    "Injuries": "41.2"
            },
                "Armenia": {
                "Noncommunicable diseases": "847.5",
                    "Communicable & other Group I": "45.0",
                    "Injuries": "49.2"
            },
                "Germany": {
                "Injuries": "23.0",
                    "Communicable & other Group I": "21.6",
                    "Noncommunicable diseases": "365.1"
            },
                "Czech Republic": {
                "Injuries": "39.1",
                    "Noncommunicable diseases": "460.7",
                    "Communicable & other Group I": "27.0"
            }
        },
            "Africa": {
            "Equatorial Guinea": {
                "Communicable & other Group I": "756.8",
                    "Injuries": "133.6",
                    "Noncommunicable diseases": "729.0"
            },
                "Madagascar": {
                "Noncommunicable diseases": "648.6",
                    "Communicable & other Group I": "429.9",
                    "Injuries": "89.0"
            },
                "Swaziland": {
                "Communicable & other Group I": "884.3",
                    "Injuries": "119.5",
                    "Noncommunicable diseases": "702.4"
            },
                "Congo": {
                "Noncommunicable diseases": "632.3",
                    "Communicable & other Group I": "666.9",
                    "Injuries": "89.0"
            },
                "Burkina Faso": {
                "Communicable & other Group I": "648.2",
                    "Noncommunicable diseases": "784.0",
                    "Injuries": "119.3"
            },
                "Guinea-Bissau": {
                "Communicable & other Group I": "869.8",
                    "Noncommunicable diseases": "764.7",
                    "Injuries": "111.6"
            },
                "Democratic Republic of the Congo": {
                "Noncommunicable diseases": "724.4",
                    "Injuries": "137.1",
                    "Communicable & other Group I": "920.7"
            },
                "Mozambique": {
                "Injuries": "175.3",
                    "Noncommunicable diseases": "593.7",
                    "Communicable & other Group I": "998.1"
            },
                "Central African Republic": {
                "Communicable & other Group I": "1212.1",
                    "Injuries": "107.9",
                    "Noncommunicable diseases": "550.8"
            },
                "United Republic of Tanzania": {
                "Noncommunicable diseases": "569.8",
                    "Communicable & other Group I": "584.2",
                    "Injuries": "129.2"
            },
                "Cameroon": {
                "Communicable & other Group I": "768.8",
                    "Injuries": "106.0",
                    "Noncommunicable diseases": "675.2"
            },
                "Togo": {
                "Noncommunicable diseases": "679.0",
                    "Communicable & other Group I": "681.8",
                    "Injuries": "93.0"
            },
                "Eritrea": {
                "Injuries": "118.7",
                    "Communicable & other Group I": "506.0",
                    "Noncommunicable diseases": "671.9"
            },
                "Namibia": {
                "Injuries": "76.4",
                    "Noncommunicable diseases": "580.2",
                    "Communicable & other Group I": "356.6"
            },
                "Senegal": {
                "Noncommunicable diseases": "558.1",
                    "Injuries": "89.3",
                    "Communicable & other Group I": "587.7"
            },
                "Chad": {
                "Communicable & other Group I": "1070.9",
                    "Injuries": "114.5",
                    "Noncommunicable diseases": "712.6"
            },
                "Benin": {
                "Injuries": "98.0",
                    "Noncommunicable diseases": "761.5",
                    "Communicable & other Group I": "577.3"
            },
                "Zimbabwe": {
                "Communicable & other Group I": "711.3",
                    "Injuries": "82.5",
                    "Noncommunicable diseases": "598.9"
            },
                "Rwanda": {
                "Noncommunicable diseases": "585.3",
                    "Injuries": "106.3",
                    "Communicable & other Group I": "401.7"
            },
                "Zambia": {
                "Noncommunicable diseases": "587.4",
                    "Injuries": "156.4",
                    "Communicable & other Group I": "764.3"
            },
                "Mali": {
                "Injuries": "119.5",
                    "Communicable & other Group I": "588.3",
                    "Noncommunicable diseases": "866.1"
            },
                "Ethiopia": {
                "Injuries": "94.5",
                    "Communicable & other Group I": "558.9",
                    "Noncommunicable diseases": "476.3"
            },
                "South Africa": {
                "Communicable & other Group I": "611.6",
                    "Injuries": "103.5",
                    "Noncommunicable diseases": "710.9"
            },
                "Burundi": {
                "Injuries": "146.6",
                    "Communicable & other Group I": "704.8",
                    "Noncommunicable diseases": "729.5"
            },
                "Cabo Verde": {
                "Injuries": "54.4",
                    "Noncommunicable diseases": "482.1",
                    "Communicable & other Group I": "141.9"
            },
                "Liberia": {
                "Noncommunicable diseases": "656.9",
                    "Injuries": "83.3",
                    "Communicable & other Group I": "609.1"
            },
                "Uganda": {
                "Noncommunicable diseases": "664.4",
                    "Communicable & other Group I": "696.7",
                    "Injuries": "166.8"
            },
                "Mauritius": {
                "Noncommunicable diseases": "576.5",
                    "Injuries": "44.1",
                    "Communicable & other Group I": "61.8"
            },
                "Algeria": {
                "Noncommunicable diseases": "710.4",
                    "Injuries": "53.8",
                    "Communicable & other Group I": "97.8"
            },
                "C\u00f4te d'Ivoire": {
                "Noncommunicable diseases": "794.0",
                    "Injuries": "124.0",
                    "Communicable & other Group I": "861.3"
            },
                "Malawi": {
                "Injuries": "97.7",
                    "Communicable & other Group I": "777.6",
                    "Noncommunicable diseases": "655.0"
            },
                "Botswana": {
                "Injuries": "87.9",
                    "Noncommunicable diseases": "612.2",
                    "Communicable & other Group I": "555.3"
            },
                "Guinea": {
                "Injuries": "96.0",
                    "Noncommunicable diseases": "681.1",
                    "Communicable & other Group I": "679.6"
            },
                "Ghana": {
                "Injuries": "76.1",
                    "Noncommunicable diseases": "669.9",
                    "Communicable & other Group I": "476.0"
            },
                "Kenya": {
                "Noncommunicable diseases": "514.7",
                    "Injuries": "101.1",
                    "Communicable & other Group I": "657.5"
            },
                "Gambia": {
                "Noncommunicable diseases": "629.6",
                    "Injuries": "96.0",
                    "Communicable & other Group I": "590.5"
            },
                "Angola": {
                "Injuries": "137.8",
                    "Noncommunicable diseases": "768.4",
                    "Communicable & other Group I": "873.3"
            },
                "Sierra Leone": {
                "Communicable & other Group I": "1327.4",
                    "Noncommunicable diseases": "963.5",
                    "Injuries": "149.5"
            },
                "Mauritania": {
                "Communicable & other Group I": "619.1",
                    "Injuries": "83.4",
                    "Noncommunicable diseases": "555.1"
            },
                "Comoros": {
                "Communicable & other Group I": "494.6",
                    "Injuries": "132.4",
                    "Noncommunicable diseases": "695.5"
            },
                "Gabon": {
                "Noncommunicable diseases": "504.6",
                    "Injuries": "77.4",
                    "Communicable & other Group I": "589.4"
            },
                "Niger": {
                "Injuries": "97.6",
                    "Communicable & other Group I": "740.0",
                    "Noncommunicable diseases": "649.1"
            },
                "Lesotho": {
                "Communicable & other Group I": "1110.5",
                    "Injuries": "142.5",
                    "Noncommunicable diseases": "671.8"
            },
                "Nigeria": {
                "Noncommunicable diseases": "673.7",
                    "Communicable & other Group I": "866.2",
                    "Injuries": "145.6"
            }
        },
            "Americas": {
            "Canada": {
                "Noncommunicable diseases": "318.0",
                    "Injuries": "31.3",
                    "Communicable & other Group I": "22.6"
            },
                "Bolivia (Plurinational State of)": {
                "Communicable & other Group I": "226.2",
                    "Noncommunicable diseases": "635.3",
                    "Injuries": "100.0"
            },
                "Haiti": {
                "Communicable & other Group I": "405.4",
                    "Noncommunicable diseases": "724.6",
                    "Injuries": "89.3"
            },
                "Belize": {
                "Noncommunicable diseases": "470.7",
                    "Injuries": "82.0",
                    "Communicable & other Group I": "104.6"
            },
                "Suriname": {
                "Injuries": "70.5",
                    "Communicable & other Group I": "83.7",
                    "Noncommunicable diseases": "374.8"
            },
                "Argentina": {
                "Communicable & other Group I": "68.7",
                    "Injuries": "50.7",
                    "Noncommunicable diseases": "467.3"
            },
                "Mexico": {
                "Injuries": "63.2",
                    "Communicable & other Group I": "57.0",
                    "Noncommunicable diseases": "468.3"
            },
                "Jamaica": {
                "Injuries": "51.5",
                    "Communicable & other Group I": "97.0",
                    "Noncommunicable diseases": "519.1"
            },
                "Peru": {
                "Noncommunicable diseases": "363.5",
                    "Injuries": "47.9",
                    "Communicable & other Group I": "121.3"
            },
                "Brazil": {
                "Injuries": "80.2",
                    "Communicable & other Group I": "92.8",
                    "Noncommunicable diseases": "513.8"
            },
                "Venezuela (Bolivarian Republic of)": {
                "Communicable & other Group I": "58.2",
                    "Injuries": "103.2",
                    "Noncommunicable diseases": "410.6"
            },
                "Paraguay": {
                "Noncommunicable diseases": "485.5",
                    "Communicable & other Group I": "77.3",
                    "Injuries": "67.6"
            },
                "Chile": {
                "Noncommunicable diseases": "366.5",
                    "Communicable & other Group I": "36.3",
                    "Injuries": "41.2"
            },
                "Trinidad and Tobago": {
                "Noncommunicable diseases": "705.3",
                    "Communicable & other Group I": "80.4",
                    "Injuries": "98.4"
            },
                "Colombia": {
                "Noncommunicable diseases": "377.3",
                    "Communicable & other Group I": "55.0",
                    "Injuries": "72.6"
            },
                "Cuba": {
                "Injuries": "45.3",
                    "Noncommunicable diseases": "421.8",
                    "Communicable & other Group I": "33.2"
            },
                "El Salvador": {
                "Noncommunicable diseases": "474.9",
                    "Injuries": "157.7",
                    "Communicable & other Group I": "96.2"
            },
                "Honduras": {
                "Injuries": "80.8",
                    "Communicable & other Group I": "117.5",
                    "Noncommunicable diseases": "441.5"
            },
                "Ecuador": {
                "Noncommunicable diseases": "409.7",
                    "Injuries": "83.7",
                    "Communicable & other Group I": "97.3"
            },
                "Costa Rica": {
                "Communicable & other Group I": "30.5",
                    "Noncommunicable diseases": "391.8",
                    "Injuries": "46.5"
            },
                "Dominican Republic": {
                "Noncommunicable diseases": "396.0",
                    "Injuries": "66.4",
                    "Communicable & other Group I": "76.8"
            },
                "Nicaragua": {
                "Communicable & other Group I": "75.2",
                    "Injuries": "64.4",
                    "Noncommunicable diseases": "546.6"
            },
                "Barbados": {
                "Noncommunicable diseases": "404.5",
                    "Injuries": "28.0",
                    "Communicable & other Group I": "60.8"
            },
                "Uruguay": {
                "Noncommunicable diseases": "446.0",
                    "Injuries": "53.8",
                    "Communicable & other Group I": "46.2"
            },
                "Panama": {
                "Communicable & other Group I": "86.1",
                    "Injuries": "67.4",
                    "Noncommunicable diseases": "372.9"
            },
                "Bahamas": {
                "Noncommunicable diseases": "465.2",
                    "Injuries": "45.7",
                    "Communicable & other Group I": "122.0"
            },
                "Guyana": {
                "Communicable & other Group I": "177.2",
                    "Noncommunicable diseases": "1024.2",
                    "Injuries": "150.0"
            },
                "United States of America": {
                "Noncommunicable diseases": "412.8",
                    "Injuries": "44.2",
                    "Communicable & other Group I": "31.3"
            },
                "Guatemala": {
                "Communicable & other Group I": "212.7",
                    "Noncommunicable diseases": "409.4",
                    "Injuries": "111.0"
            }
        },
            "Eastern Mediterranean": {
            "Egypt": {
                "Communicable & other Group I": "74.3",
                    "Noncommunicable diseases": "781.7",
                    "Injuries": "33.5"
            },
                "South Sudan": {
                "Injuries": "143.4",
                    "Communicable & other Group I": "831.3",
                    "Noncommunicable diseases": "623.4"
            },
                "Sudan": {
                "Injuries": "133.6",
                    "Noncommunicable diseases": "551.0",
                    "Communicable & other Group I": "495.0"
            },
                "Libya": {
                "Injuries": "62.8",
                    "Noncommunicable diseases": "550.0",
                    "Communicable & other Group I": "52.6"
            },
                "Jordan": {
                "Noncommunicable diseases": "640.3",
                    "Injuries": "53.5",
                    "Communicable & other Group I": "52.5"
            },
                "Pakistan": {
                "Communicable & other Group I": "296.0",
                    "Noncommunicable diseases": "669.3",
                    "Injuries": "98.7"
            },
                "Djibouti": {
                "Noncommunicable diseases": "631.1",
                    "Communicable & other Group I": "626.0",
                    "Injuries": "106.0"
            },
                "Syrian Arab Republic": {
                "Communicable & other Group I": "41.0",
                    "Injuries": "308.0",
                    "Noncommunicable diseases": "572.7"
            },
                "Morocco": {
                "Noncommunicable diseases": "707.7",
                    "Communicable & other Group I": "131.5",
                    "Injuries": "47.0"
            },
                "Yemen": {
                "Communicable & other Group I": "515.0",
                    "Noncommunicable diseases": "626.9",
                    "Injuries": "84.3"
            },
                "Bahrain": {
                "Injuries": "33.5",
                    "Noncommunicable diseases": "505.7",
                    "Communicable & other Group I": "48.5"
            },
                "United Arab Emirates": {
                "Noncommunicable diseases": "546.8",
                    "Injuries": "31.5",
                    "Communicable & other Group I": "35.6"
            },
                "Lebanon": {
                "Noncommunicable diseases": "384.6",
                    "Injuries": "40.6",
                    "Communicable & other Group I": "30.5"
            },
                "Saudi Arabia": {
                "Noncommunicable diseases": "549.4",
                    "Injuries": "41.1",
                    "Communicable & other Group I": "71.3"
            },
                "Iran (Islamic Republic of)": {
                "Injuries": "74.9",
                    "Communicable & other Group I": "56.2",
                    "Noncommunicable diseases": "569.3"
            },
                "Iraq": {
                "Communicable & other Group I": "87.0",
                    "Noncommunicable diseases": "715.5",
                    "Injuries": "128.5"
            },
                "Qatar": {
                "Communicable & other Group I": "28.3",
                    "Injuries": "41.0",
                    "Noncommunicable diseases": "407.0"
            },
                "Afghanistan": {
                "Communicable & other Group I": "362.7",
                    "Injuries": "169.2",
                    "Noncommunicable diseases": "846.3"
            },
                "Somalia": {
                "Noncommunicable diseases": "550.7",
                    "Communicable & other Group I": "927.2",
                    "Injuries": "188.5"
            },
                "Kuwait": {
                "Communicable & other Group I": "82.5",
                    "Injuries": "25.4",
                    "Noncommunicable diseases": "406.3"
            },
                "Oman": {
                "Injuries": "52.8",
                    "Noncommunicable diseases": "478.2",
                    "Communicable & other Group I": "84.2"
            },
                "Tunisia": {
                "Noncommunicable diseases": "509.3",
                    "Communicable & other Group I": "65.0",
                    "Injuries": "39.1"
            }
        },
            "Western Pacific": {
            "Mongolia": {
                "Injuries": "69.4",
                    "Noncommunicable diseases": "966.5",
                    "Communicable & other Group I": "82.8"
            },
                "Cambodia": {
                "Injuries": "62.2",
                    "Communicable & other Group I": "227.5",
                    "Noncommunicable diseases": "394.0"
            },
                "Japan": {
                "Injuries": "40.5",
                    "Noncommunicable diseases": "244.2",
                    "Communicable & other Group I": "33.9"
            },
                "Brunei Darussalam": {
                "Injuries": "44.6",
                    "Noncommunicable diseases": "475.3",
                    "Communicable & other Group I": "56.1"
            },
                "Solomon Islands": {
                "Communicable & other Group I": "230.6",
                    "Injuries": "75.1",
                    "Noncommunicable diseases": "709.7"
            },
                "Viet Nam": {
                "Communicable & other Group I": "96.0",
                    "Injuries": "59.0",
                    "Noncommunicable diseases": "435.4"
            },
                "Lao People's Democratic Republic": {
                "Communicable & other Group I": "328.7",
                    "Injuries": "75.2",
                    "Noncommunicable diseases": "680.0"
            },
                "China": {
                "Communicable & other Group I": "41.4",
                    "Noncommunicable diseases": "576.3",
                    "Injuries": "50.4"
            },
                "New Zealand": {
                "Injuries": "32.9",
                    "Noncommunicable diseases": "313.6",
                    "Communicable & other Group I": "18.0"
            },
                "Papua New Guinea": {
                "Injuries": "100.1",
                    "Communicable & other Group I": "554.3",
                    "Noncommunicable diseases": "693.2"
            },
                "Philippines": {
                "Communicable & other Group I": "226.4",
                    "Noncommunicable diseases": "720.0",
                    "Injuries": "53.8"
            },
                "Malaysia": {
                "Injuries": "62.8",
                    "Noncommunicable diseases": "563.2",
                    "Communicable & other Group I": "117.4"
            },
                "Australia": {
                "Communicable & other Group I": "13.7",
                    "Noncommunicable diseases": "302.9",
                    "Injuries": "28.2"
            },
                "Fiji": {
                "Noncommunicable diseases": "804.0",
                    "Injuries": "64.0",
                    "Communicable & other Group I": "105.2"
            },
                "Singapore": {
                "Communicable & other Group I": "66.2",
                    "Noncommunicable diseases": "264.8",
                    "Injuries": "17.5"
            },
                "Republic of Korea": {
                "Injuries": "53.1",
                    "Communicable & other Group I": "33.8",
                    "Noncommunicable diseases": "302.1"
            }
        }
    }

    key = data.keys()
    li_df = []

    for r in data.keys():
        df = pd.read_json(json.dumps(data[r])).T
        df.index.name = 'Country'
        df['Region'] = r
        df = df.set_index('Region', append=True)
        df = df.reorder_levels(['Region', 'Country'])
        li_df.append(df)

    df = pd.concat(li_df)

    return df

    