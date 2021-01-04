mt=pd.read_csv('data/meteorshowers.csv')
cities=pd.read_csv('data/cities.csv')
constellations=pd.read_csv('data/constellations.csv')
moon_phases=pd.read_csv('data/moonphases.csv')



###################   Date   ###################

months={'january':1, 'february':2, 'march':3, 'april':4, 'may':5, 'june':6, 'july':7, 'august':8, 'september':9, 'october':10, 'november':11, 'december':12}

mt.bestmonth=mt.bestmonth.map(months)
mt.startmonth=mt.startmonth.map(months)
mt.endmonth=mt.endmonth.map(months)
moon_phases.month=moon_phases.month.map(months)
constellations.bestmonth=constellations.bestmonth.map(months


mt['startdate']=pd.to_datetime(2020*10000+mt.startmonth*100+mt.startday, format='%Y%m%d')
mt['enddate']=pd.to_datetime(2020*10000+mt.endmonth*100+mt.endday, format='%Y%m%d')
moon_phases['date']=pd.to_datetime(2020*10000+moon_phases.month*100+moon_phases.day, format='%Y%m%d')



###################   Hemispheres   ###################

hemispheres={'northern':0, 'southern':1, 'northern, southern':3}

mt.hemisphere=mt.hemisphere.map(hemispheres)
constellations.hemisphere=constellations.hemisphere.map(hemispheres)


###################   Moon Phases  ###################


phases={'new moon':0, 'first quarter':0.5, 'third quarter':0.5, 'full moon':1.0}

moon_phases['percentage']=moon_phases.moonphase.map(phases)
moon_phases = moon_phases.drop(['day','month','moonphase','specialevent'],axis=1)

#Keep only the last phase
lastPhase = 0

for index, row in moon_phases.iterrows():
    if pd.isnull(row['percentage']):
        moon_phases.at[index, 'percentage'] = lastPhase
    else:
        lastPhase = row['percentage']



mt = mt.drop(['startmonth','startday','endmonth','endday','hemisphere'],axis=1)
moon_phases.loc[moon_phases['percentage'].idxmin()]['date']

                                                      
                                                      ##TO-DO: dvelopping an app linked 
