import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import norm
import statistics
import random

def american_to_prob(american):
    prob_list = []
    for x in american:
        if x < 0:
            prob = (-x / (-x +100)) *0.8
        else:
            prob = (100 / (x +100))*0.8
        prob_list.append(prob)

    return prob_list

times= 100000

Porz_Points_Over = [17,19,21,23,25,27,29,31,33]
Porz_Points_American = [-225,-115,105,155,240,370,550,750,900]
Porz_Points_Prob = american_to_prob(Porz_Points_American)


Porz_Rbd_Over = [7,8,9,10,11,12,13,14]
Porz_Rbd_American = [-212,-105,115,200,360,650,1500,2500]
Porz_Rbd_Prob = american_to_prob(Porz_Rbd_American)


Porz_Ast_Over = [1,2,3,4,5]
Porz_Ast_American = [-188,120,280,650,1400]
Porz_Ast_Prob = american_to_prob(Porz_Ast_American)


Porz_PRA_Results = []
for i in range(times):
    Porz_Points_Result = random.choices(Porz_Points_Over, weights=Porz_Points_Prob, k=1)
    Porz_Rbd_Result = random.choices(Porz_Rbd_Over, weights=Porz_Rbd_Prob, k=1)
    Porz_Ast_Result = random.choices(Porz_Ast_Over, weights=Porz_Ast_Prob, k=1)
    Porz_PRA = Porz_Points_Result[0]+Porz_Rbd_Result[0]+Porz_Ast_Result[0]
    Porz_PRA_Results.append(Porz_PRA)

Doncic_Points_Over = [19,24,26]
Doncic_Points_American = [-650,-174,-112]
Doncic_Points_Prob = american_to_prob(Doncic_Points_American)


Doncic_Rbd_Over = [7,8,9,10,11,12,13,14,15]
Doncic_Rbd_American = [-250,-130,-118,150,250,450,800,2000,3000]
Doncic_Rbd_Prob = american_to_prob(Doncic_Rbd_American)


Doncic_Ast_Over = [6,7,8,9,10,11,12]
Doncic_Ast_American = [-400,-250,-138,-118,130,205,333]
Doncic_Ast_Prob = american_to_prob(Doncic_Ast_American)


Doncic_PRA_Results = []
for i in range(times):
    Doncic_Points_Result = random.choices(Doncic_Points_Over, weights=Doncic_Points_Prob, k=1)
    Doncic_Rbd_Result = random.choices(Doncic_Rbd_Over, weights=Doncic_Rbd_Prob, k=1)
    Doncic_Ast_Result = random.choices(Doncic_Ast_Over, weights=Doncic_Ast_Prob, k=1)
    Doncic_PRA = Doncic_Points_Result[0]+Doncic_Rbd_Result[0]+Doncic_Ast_Result[0]
    Doncic_PRA_Results.append(Doncic_PRA)

Total_Results = np.add(Doncic_PRA_Results,Porz_PRA_Results)

pd.DataFrame(Doncic_PRA_Results).hist()

plt.hist(Doncic_PRA_Results, density=True, bins=30)  # density=False would make counts
plt.ylabel('Count')
plt.xlabel('PRA of Porz+Doncic');
plt.title('Histogram of PRA')
plt.show()
# plt.plot(Curry_Over,Curry_Prob)
# plt.plot(Giannis_Over,Giannis_Prob)
# plt.plot(Demar_Over,Demar_Prob)
# print(np.interp(20,Giannis_Over,Giannis_Prob))
#
# plt.show()
