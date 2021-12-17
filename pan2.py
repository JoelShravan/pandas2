import pandas as pd
class B:
    def statewise(self,file):
      df=pd.read_csv('governors_county_candidate.csv')
      states=list(set(df['state']))
      winner=[]
      for i in states:
       won=df[(df['won']==True) & (df['state']==i)]
       party=won['party']
       winner.append(party.mode())
      for i in range(0,len(states)):
       print(states[i],end=' won by ')
       print(winner[i])      
      



    
    def total_votes_statewise(self,file):
        df=pd.read_csv('governors_county_candidate.csv')
        return df.groupby(["state"])["votes"].sum()
    


    def total_votes_by_each_parties_statewise(self,file):
        df=pd.read_csv('governors_county_candidate.csv')
        return df.groupby(["state",'party'])["votes"].sum()
        
file='governors_county_candidate.csv'
b=B()
b.statewise(file)
print(b.total_votes_statewise(file))
print(b.total_votes_by_each_parties_statewise(file))