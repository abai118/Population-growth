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
    
    countriesData=rawdata("population-estimates.csv") # getting data from csv file
    
    indianPopulation={}
    #getting of indian population from the totla population
    for countries in countriesData :
        
        if countries["Region"] == "India" :
            
            indianPopulation[countries['Year']]= countries['Population']
        
    #print(indianPopulation)
    
    
    plt.bar(indianPopulation.keys(),indianPopulation.values())
    
    plt.gcf().autofmt_xdate()
    plt.show()
            
            
def ForTheYear2014BarChartOfPopulationOfASEANcountries() :
    
    populationData=rawdata("population-estimates.csv") # getting data from csv file
    
    AseanCountriesPopulation ={}
    #getting population of asean countries in the year 2014
    for country in populationData :
        
        if country['Region'] in aseanCountries and country['Year'] == "2014" :
            
            AseanCountriesPopulation[country["Region"]] = country["Population"]
            
            
    #print(AseanCountriesPopulation)

    plt.bar(AseanCountriesPopulation.keys(),AseanCountriesPopulation.values(),align='center',alpha=1)
    plt.gcf().autofmt_xdate()
        
    plt.xlabel("ASEAN Countries")
    plt.ylabel("Population")
    plt.title(" 2014 Bar Chart of population of ASEAN countries")
    plt.show()

def TotalPopulationOfSAARCcountries() :
    populationData=rawdata("population-estimates.csv") # getting data from csv file
    
    saarcCountriesPopulation ={}
    #getting population of SAARC countries over all years and storing it in a dictionary
    for country in populationData :
        
        if country['Region'] in saarcCountries  :
            
            if country["Year"] in saarcCountriesPopulation :
                
                saarcCountriesPopulation[country["Year"]] = saarcCountriesPopulation[country["Year"]] + int(float(country["Population"])) 
                
            else :
                saarcCountriesPopulation[country["Year"]] = int(float(country["Population"])) 
                
                
    #print(saarcCountriesPopulation)
    
    plt.bar(saarcCountriesPopulation.keys(),saarcCountriesPopulation.values())
    plt.xlabel("Population of SAARC countries")
    plt.ylabel("Years")
    plt.gcf().autofmt_xdate()
    plt.show()
        
        
def ASEANpopulationOverYears() :
    
    populationData=rawdata("population-estimates.csv") 
    
    values=[0]*len(Years)
    # converting years from 2004 to 2014 to dectionary and assigning 0 to them 
    yearsDict=dict(zip(Years,values))
    
    #print(yearsDict)
 
    
    # getting asean countries list and assigning yearsDict to it 
    aseanCountriesPopulation=dict(zip(aseanCountries,[yearsDict]*len(aseanCountries)))
    #print(aseanCountriesPopulation["Malaysia"]["2006"])
    
    
    #getting asean countries population from 2004 to 2014 
    for country in populationData :
        
        if country["Region"] in aseanCountries and country["Year"] in Years :
            year=country["Year"]
            countryName=country["Region"]
            aseanCountriesPopulation[countryName][year]= float(country["Population"])
           
            
    #print(aseanCountriesPopulation) 
            
    
    
    populationOverYears=list(aseanCountriesPopulation.values()) # population of asean countries over 2004 to 2014 
    #print(populationOverYears)
    countriesListDictonary={}
    count=0
    for country in aseanCountries :  # getting population of asean countries into a dictionary to convert them to list of values 
        countriesListDictonary[country]=list(populationOverYears[count].values())
        count=count+1
    #print(countriesListDictonary)
    populationOfaseanCountries=list(countriesListDictonary.values()) #converting the values into list 
    #print(populationOfaseanCountries)
    
    
    for i in range(len(aseanCountries)) : #adding the name of the country to list to show it in bar chart
        
        populationOfaseanCountries[i]=[aseanCountries[i]] + populationOfaseanCountries[i]  
        
    #print(populationOfaseanCountries)
        
    #converting data into bar chart
    df=pd.DataFrame(populationOfaseanCountries,columns=["Country",*Years])

    df.plot(x="Country", y=Years, kind="bar",figsize=(10,10))
    
    plt.show()
    
                
                
                
                

def main() :
    IndiaPopulationOverYears()
    ForTheYear2014BarChartOfPopulationOfASEANcountries()
    TotalPopulationOfSAARCcountries()
    ASEANpopulationOverYears()
    
main()
