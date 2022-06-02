import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

aseanCountries=['Brunei','Cambodia','Indonesia','Laos','Malaysia','Myanmar','Philippines','Singapore','Thailand','Vietnam' ]
saarcCountries=['Bangladesh', 'Bhutan', 'India', 'Maldives', 'Nepal', 'Pakistan' ,'Sri Lanka']

Years=["2004",'2005','2006','2007','2008','2009','2010','2011','2012','2013','2014']
colors=["red","cyan","orange","green","black","blue","purple","yellow","violet"]


def rawdata(filename): #collecting the .csv files and converting into data
    with open(filename,"r") as f :
        csvReader=csv.DictReader(f)
        data=list(csvReader)
        
    return data

def IndiaPopulationOverYears() :
    
    countriesData=rawdata("population-estimates.csv")
    
    indianPopulation={}
    
    for countries in countriesData :
        
        if countries["Region"] == "India" :
            
            indianPopulation[countries['Year']]= countries['Population']
        
    print(indianPopulation)
    
    
    plt.bar(indianPopulation.keys(),indianPopulation.values())
    
    plt.gcf().autofmt_xdate()
    plt.show()
            
            
def ForTheYear2014BarChartOfPopulationOfASEANcountries() :
    
    populationData=rawdata("population-estimates.csv")
    
    AseanCountriesPopulation ={}
    for country in populationData :
        
        if country['Region'] in aseanCountries and country['Year'] == "2014" :
            
            AseanCountriesPopulation[country["Region"]] = country["Population"]
            
            
    print(AseanCountriesPopulation)

    plt.bar(AseanCountriesPopulation.keys(),AseanCountriesPopulation.values(),align='center',alpha=1)
    plt.gcf().autofmt_xdate()
        
    plt.xlabel("ASEAN Countries")
    plt.ylabel("Population")
    plt.title(" 2014 Bar Chart of population of ASEAN countries")
    plt.show()

def TotalPopulationOfSAARCcountries() :
    populationData=rawdata("population-estimates.csv")
    
    saarcCountriesPopulation ={}
    for country in populationData :
        
        if country['Region'] in saarcCountries  :
            
            if country["Year"] in saarcCountriesPopulation :
                
                saarcCountriesPopulation[country["Year"]] = saarcCountriesPopulation[country["Year"]] + int(float(country["Population"])) 
                
            else :
                saarcCountriesPopulation[country["Year"]] = int(float(country["Population"])) 
                
                
    print(saarcCountriesPopulation)
    
    plt.bar(saarcCountriesPopulation.keys(),saarcCountriesPopulation.values())
    plt.xlabel("Population of SAARC countries")
    plt.ylabel("Years")
    plt.gcf().autofmt_xdate()
    plt.show()
        
def test():
    
        
    # create data
    x = np.arange(5)
    y1 = [34, 56, 12, 89, 67]
    y2 = [12, 56, 78, 45, 90]
    y3 = [14, 23, 45, 25, 89]
    y4=[10,15,30,45,100]
    y5=[10,15,30,45,100]
    y6=[10,15,30,45,100]
    width = 0.02
    
    # plot data in grouped manner of bar type
    plt.bar(x, y1, width, color='cyan')
    plt.bar(x+0.1, y2, width, color='orange')
    plt.bar(x+0.2, y3, width, color='green')
    plt.bar(x+0.3, y4, width, color='black')
    plt.bar(x+0.4, y5, width, color='black')
    plt.bar(x+0.5, y6, width, color='black')
    plt.xticks(x, ['Team A', 'Team B', 'Team C', 'Team D', 'Team E'])
    plt.xlabel("Teams")
    plt.ylabel("Scores")
    plt.legend(["Round 1", "Round 2", "Round 3"])
    plt.show()
        
def ASEANpopulationOverYears() :
    
    populationData=rawdata("population-estimates.csv") 
    
    values=[0]*len(Years)
    
    yearsDict=dict(zip(Years,values))
    
    #print(yearsDict)
 
    

    aseanCountriesPopulation=dict(zip(aseanCountries,[yearsDict]*len(aseanCountries)))
    #print(aseanCountriesPopulation["Malaysia"]["2006"])
    for country in populationData :
        
        if country["Region"] in aseanCountries and country["Year"] in Years :
            year=country["Year"]
            countryName=country["Region"]
            aseanCountriesPopulation[countryName][year]= float(country["Population"])
            count=count+1
            
    #print(aseanCountriesPopulation) 
                
   
    
    count=1
    
    countries=list(aseanCountriesPopulation.keys())
    
    populationOverYears=list(aseanCountriesPopulation.values())
    #print(populationOverYears)
    countriesListDictonary={}
    for country in countries :
        countriesListDictonary[country]=list(populationOverYears[count].values())
        
    #print(countriesListDictonary)
    populationOfaseanCountries=list(countriesListDictonary.values())
    #print(populationOfaseanCountries)
    
    
    for i in range(len(countries)) :
        
        populationOfaseanCountries[i]=[countries[i]] + populationOfaseanCountries[i]  
        
    #print(populationOfaseanCountries)
        
    
    df=pd.DataFrame(populationOfaseanCountries,columns=["Country",*Years])

    df.plot(x="Country", y=Years, kind="bar",figsize=(10,10))
    
    plt.show()
    
                
                
                
                

def main() :
    #IndiaPopulationOverYears()
    #ForTheYear2014BarChartOfPopulationOfASEANcountries()
    #TotalPopulationOfSAARCcountries()
    ASEANpopulationOverYears()
    #test()
    
main()
