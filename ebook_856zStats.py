df['Econnect'].value_counts()
newdf = pd.DataFrame(columns = ['values', 'counts'])
values = df['Econnect'].value_counts().keys().tolist()
counts = df['Econnect'].value_counts().tolist()
newdf['counts'] = counts
newdf['values'] = values
newdf.to_csv(csvOut, index = False)

df['clicks']=df['clicks'].fillna(0)

aggregate=df.groupby(['Econnect'], as_index=False)['clicks'].agg(['count', 'sum', 'mean', 'median']).to_csv(csvOut)
