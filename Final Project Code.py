# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 15:41:44 2021

@author: aidan
"""

import gurobipy as gp
from gurobipy import GRB

import pandas as pd

# Capacity for each plant
capacity = [16000,12000,14000,10000,13000]

# dataframe for retail centers demands
demand = []
demandfy = [1000,1200,1800,1200,1000,1400,1600,1000]
for x in demandfy:
    retailcenter = []
    for t in range(1,11):
        if x == demandfy[1-1] or x == demandfy[2-1] or x == demandfy[4-1] or x == demandfy[5-1] or x == demandfy[8-1]:
            d = x+0.20*(x)*(t-1)
            retailcenter.append(d)
        else:
            d = x+0.25*(x)*(t-1)
            retailcenter.append(d)
    demand.append(retailcenter)
dfdemand = pd.DataFrame(demand,columns=[1,2,3,4,5,6,7,8,9,10])
dfdemand.index = [1,2,3,4,5,6,7,8]
dfdemand
print(dfdemand)

# columns are years, rows are retaliers
# select values through indexing column and row: dfdemand[1][2]

# dataframe for construction costs
conscost = []
conscostfy = [2000,1600,1800,900,1500]
for x in conscostfy:
    plant = []
    for t in range(1,11):
        cc = x*(1+0.03)**(t-1)
        plant.append(cc)
    conscost.append(plant)

dfconscost = pd.DataFrame(conscost,columns=[1,2,3,4,5,6,7,8,9,10])
dfconscost.index = [1,2,3,4,5]
dfconscost

# dataframe for annual operating costs
aocost = []
aocostfy = [420,380,460,280,340]
for x in aocostfy:
    plant = []
    for t in range(1,11):
        aoc = x*(1+0.03)**(t-1)
        plant.append(aoc)
    aocost.append(plant)

dfaocost = pd.DataFrame(aocost,columns=[1,2,3,4,5,6,7,8,9,10])
dfaocost.index = [1,2,3,4,5]
dfaocost

# dataframe for reopening costs
rocost = []
rocostfy = [190,150,160,100,130]
for x in rocostfy:
    plant = []
    for t in range(1,11):
        roc = x*(1+0.03)**(t-1)
        plant.append(roc)
    rocost.append(plant)

dfrocost = pd.DataFrame(rocost,columns=[1,2,3,4,5,6,7,8,9,10])
dfrocost.index = [1,2,3,4,5]
dfrocost

# dataframe for shutdown costs
sdcost = []
sdcostfy = [170,120,130,80,110]
for x in sdcostfy:
    plant = []
    for t in range(1,11):
        sdc = x*(1+0.03)**(t-1)
        plant.append(sdc)
    sdcost.append(plant)

dfsdcost = pd.DataFrame(sdcost,columns=[1,2,3,4,5,6,7,8,9,10])
dfsdcost.index = [1,2,3,4,5]
dfsdcost

# raw material costs
# alloy cost
acost = []
acostfy = [0.02,0.02,0.02,0.02,0.02]
for x in acostfy:
    a = []
    for t in range(1,11):
        ac = x*(1+0.03)**(t-1)
        a.append(ac)
    acost.append(a)

dfacost = pd.DataFrame(acost,columns=[1,2,3,4,5,6,7,8,9,10])
dfacost.index = [1,2,3,4,5]
dfacost

# Widget subassemblies original cost
wocost = []
wocostfy = [0.15,0.15,0.15,0.15,0.15]
for x in wocostfy:
    wo = []
    for t in range(1,11):
        woc = x*(1+0.03)**(t-1)
        wo.append(woc)
    wocost.append(wo)

dfwocost = pd.DataFrame(wocost,columns=[1,2,3,4,5,6,7,8,9,10])
dfwocost.index = [1,2,3,4,5]
dfwocost

# Widget subassemblies discounted cost
wdcost = []
wdcostfy = [0.12,0.12,0.12,0.12,0.12]
for x in wdcostfy:
    wd = []
    for t in range(1,11):
        wdc = x*(1+0.03)**(t-1)
        wd.append(wdc)
    wdcost.append(wd)

dfwdcost = pd.DataFrame(wdcost,columns=[1,2,3,4,5,6,7,8,9,10])
dfwdcost.index = [1,2,3,4,5]
dfwdcost

# 3D dictionary for the shipping cost from plants to warehouses
w1scostfy = [0.12,0.1,0.05,0.06,0.06]
w2scostfy = [0.13,0.03,0.07,0.03,0.02]
w3scostfy = [0.08,0.1,0.06,0.07,0.04]
w4scostfy = [0.05,0.09,0.03,0.07,0.08]
wscostfy = [w1scostfy,w2scostfy,w3scostfy,w4scostfy]
wscostfy
dfwscostfy = pd.DataFrame(wscostfy,columns=[1,2,3,4,5])
dfwscostfy.index = [1,2,3,4]
dfwscostfy
plant = [1,2,3,4,5]
warehouse = [1,2,3,4]
year = [1,2,3,4,5,6,7,8,9,10]

Aijt = {}
for i in plant:
    Aijt[i]={}
    for j in warehouse:
        Aijt[i][j]={}
        for t in year:
            Aijt[i][j][t]=dfwscostfy[i][j]*(1+0.03)**(t-1)
            
Aijt
# basically Aijt[2][2][5] means the shipping cost of shipping products from plant 2 to warehouse 2 in year 5   


# 3D dictionary for the shipping cost from warehouses to retail centers
r1scostfy = [0.09,0.05,0.06,0.07]
r2scostfy = [0.1,0.07,0.09,0.08]
r3scostfy = [0.06,0.12,0.07,0.09]
r4scostfy = [0.05,0.04,0.09,0.06]
r5scostfy = [0.08,0.03,0.09,0.1]
r6scostfy = [0.09,0.09,0.04,0.07]
r7scostfy = [0.02,0.03,0.11,0.06]
r8scostfy = [0.12,0.08,0.07,0.09]
rscostfy = [r1scostfy,r2scostfy,r3scostfy,r4scostfy,r5scostfy,r6scostfy,r7scostfy,r8scostfy]
dfrscostfy = pd.DataFrame(rscostfy,columns=[1,2,3,4])
dfrscostfy.index = [1,2,3,4,5,6,7,8]
dfrscostfy
warehouse = [1,2,3,4]
retail = [1,2,3,4,5,6,7,8]
year = [1,2,3,4,5,6,7,8,9,10]

Bjkt = {}
for j in warehouse:
    Bjkt[j]={}
    for k in retail:
        Bjkt[j][k]={}
        for t in year:
            Bjkt[j][k][t]=dfrscostfy[j][k]*(1+0.03)**(t-1)    

Bjkt
# basically Bjkt[1][2][2] means the shipping cost of shipping products from warehouse 1 to retail center 2 in year 2   

year = 11
warehouse = 4
# Indexed sets
stores = range(len(demandfy)) # k
plants = range(len(conscostfy)) # i 
warehouses = range(warehouse) # j
years = range(year) # t

r = gp.Model("Model")

# Variables
zvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = acost, name = "z") # units of Flugels produced by plant i in year t
xvars = r.addVars(plants, warehouses, years, vtype=GRB.CONTINUOUS, obj = Aijt, name = "x") # units of Flugels shipped from plant i to warehouse j in year t
ivars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, name = "ivar")
yvars = r.addVars(warehouses, stores, years, vtype=GRB.CONTINUOUS, obj = Bjkt, name = "y") # units of Flugels shipped from warehouse j to retail center k in year t
lamda1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, name = "lamda1") # calculating the weighted units of purchased raw materials of plant i in year t
lamda2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = wocost, name = "lamda2") # calculating the weighted units of purchased raw materials of plant i in year t
lamda3vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = wocost + wdcost, name = "lamda3") # calculating the weighted units of purchased raw materials of plant i in year t
pvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = aocost + rocost + conscost, lb = 0, ub = 1,  name = "pvar") # whether the plant i’s production line is open at the beginning of year t. 1: open, 0: close (binary) 
e1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "e1")
e2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "e2")
fvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = sdcost, lb = 0, ub = 1,  name = "fvar") # whether the production line in the plant i is going to be shut down at the end of year t or not. 1: shut down, 0: close (binary) 
gvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = rocost, lb = 0, ub = 1,  name = "gvar") # whether the production line in the plant i in year t is the initial construction year. 1: initial, 0: not initial (binary)
hvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = conscost, lb = 0, ub = 1,  name = "hvar") # whether the production line in the plant i was never opened before year t or not. 1: not opened before, 0: opened before (binary) 

r.modelSense = GRB.MINIMIZE

# Constraints
# Plant Cost
r.addConstrs((gvars[i][t] == 1 - pvars[i][t-1] for i in plants for t in years), "Reopening cost binary variable")
r.addConstrs((fvars[i][t] == 1 - pvars[i][t+1] for i in plants for t in years), "Shut down cost binary variable")
r.addConstrs((zvars[i][t] <= pvars[i][t] * capacity[i] for i in plants for t in years), "Plant capacity binary variable")
r.addConstrs((pvars[j][0] == 0 for j in warehouses), 'Year 0 P variable')
r.addConstrs((pvars[j][11] == 0 for j in warehouses), 'Year 11 P variable')
r.addConstrs((gvars[j][0] == 0 for j in warehouses), 'Year 0 G variable')
# Shipping Cost
r.addConstrs((xvars.sum(i,'*',t) == zvars[i][t] for i in plants for t in years), "Sum of Products Shipped") # sum of products shipped from each plant in year t equals to the amount of flugels produced by it in year t 
r.addConstrs((xvars.sum('*',j,t) + ivars[j][t-1] == yvars.sum(j,'*',t) + ivars[j][t] for j in warehouses for t in years), "Sum of Products Recieved at Warehouses") # sum of products received by warehouse j in year t equals to sum of products shipped from warehouse j in year t
r.addConstrs((ivars.sum(j,'*') <= 40000 for j in warehouses), "Average Inventory") # average inventory in any year to be no more than 4000 items (among all Warehouses)
r.addConstrs((xvars.sum('*',j,t) <= 12000 for j in warehouses for t in years), "Warehouse Inflow") # both the flow into a warehouse and the flow out of a warehouse should not exceed an average of 1000 units per month
r.addConstrs((yvars.sum(j,'*',t) <= 12000 for j in warehouses for t in years), "Warehouse Outflow") # both the flow into a warehouse and the flow out of a warehouse should not exceed an average of 1000 units per month
r.addConstrs((ivars[j][0] == 0 for j in warehouses), 'Year 0 Inventory')
r.addConstrs((ivars[j][10] == 0 for j in warehouses), 'Year 10 Inventory')
r.addConstrs((ivars[j][11] == 0 for j in warehouses), 'Year 11 Inventory')
# Demand
r.addConstrs((yvars.sum('*',k,t) == demand[k][t] for k in stores for t in years), "Meet Demand")
# Alloy
r.addConstrs((4.7 * zvars[i][t] <= 60000 for i in plants for t in years), "Pounds of Alloy")
# Material
r.addConstrs((lamda1vars[i][t] <= e1vars[i][t] for i in plants for t in years), "Lamda1")
r.addConstrs((lamda2vars[i][t] <= e1vars[i][t] + e2vars[i][t] for i in plants for t in years), "Lamda2")
r.addConstrs((lamda3vars[i][t] <= e2vars[i][t] for i in plants for t in years), "Lamda3")
r.addConstrs((lamda1vars[i][t] + lamda2vars[i][t] + lamda3vars[i][t] == 1 for i in plants for t in years), "Lamda Sum")
r.addConstrs((e1vars[i][t] + e2vars[i][t] == 1 for i in plants for t in years), "e1 and e2 value")
r.addConstrs((((9000*(lamda2vars[i][t]) + 1000000*(lamda3vars[i][t])) / 3) == zvars[i][t] for i in plants for t in years), "Z value")

# Optimize Model
r.optimize()

#printSolution()
# Objective Function Value
print('\nTotal Costs: %g' % r.objVal)




