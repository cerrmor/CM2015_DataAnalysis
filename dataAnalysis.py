# srinks the data frame to just the veriables where the home and away team score are the same in the first and final half
def fullVsHalfGoals(dataFrame):
    df = dataFrame
    # removes any game where the final results dont match the half time results
    df = df[df['FTR'] == df['HTR']]
    # removes any game where the home team score at half time doesent match full time
    df = df[df['FTHG'] == df['HTHG']]
    # removes any game where the away team score at half time doesent match full time
    df = df[df['FTAG'] == df['HTAG']]
    return df

# Builds a list of goals scored. the list includes: total goals by half time,
# total goals after half time and total goals in the dataframe
def goalsScored(dataFrame):
    data =[]
    df = dataFrame
    
#   Goals scored by half time
    homeGoals2 = df ['HTHG']
    awayGoals2 = df ['HTAG']
    halfTime = sum(homeGoals2 + awayGoals2)
    data.append(halfTime)
    
    homeGoals1 = df ['FTHG']
    awayGoals1 = df ['FTAG']
    fullTime = sum(homeGoals1 + awayGoals1)
#   Goals scored after half time
    data.append(fullTime-halfTime)
#   Total goals scored
    data.append(fullTime)

    return data

# calculates the percentage of games that were decided in the first half of the game
#inputs a data frame outputs a dict with total games, total games with no change, and the ratio
def percentageNoChange(dataFrame):
    data = {}
    df = dataFrame
    
    total1 = len(fullVsHalfGoals(df))
    total2 = len(dataFrame)
    percentage =((total1*100)/total2)
    data = {'total':total2, 'adjTotal':total1, 'percentage':percentage}
    
    return data

# Calculates the ratio of two numbers from a list of 3 elements
def percent(data):
    return ((data[1]*100)//data[2])
