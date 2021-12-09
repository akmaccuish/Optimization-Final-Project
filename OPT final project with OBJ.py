# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 16:47:02 2021

@author: congh
"""
import gurobipy as gp
from gurobipy import GRB

import pandas as pd



plant_l = [1,2,3,4,5]
retail_l = [1,2,3,4,5,6,7,8]
year_l = [0,1,2,3,4,5,6,7,8,9,10,11]
warehouse_l = [1,2,3,4]

# dataframe for retail centers demands
demandfy = [1000,1200,1800,1200,1000,1400,1600,1000]
demand = {}
for j in retail_l:
    demand[j]={}
    for t in year_l:
        if j == 3 or j == 6 or j == 7:
            demand[j][t] = demandfy[j-1]+0.25*(demandfy[j-1])*(t-1)
        else:
            demand[j][t] = demandfy[j-1]+0.20*(demandfy[j-1])*(t-1)

for x in demand:
    for key in demand[x]:
        if key == 0 or key == 11:
            demand[x][key]=0
demand


#construction costs
conscostfy = [2000,1600,1800,900,1500]
conscost = {}
for i in plant_l:
    conscost[i]={}
    for t in year_l:
        conscost[i][t] = conscostfy[i-1]*(1+0.03)**(t-1)

for x in conscost:
    for key in conscost[x]:
        if key == 0 or key == 11:
            conscost[x][key]=0
conscost

# operating cost
aocostfy = [420,380,460,280,340]
aocost = {}
for i in plant_l:
    aocost[i]={}
    for t in year_l:
        aocost[i][t] = aocostfy[i-1]*(1+0.03)**(t-1)

for x in aocost:
    for key in aocost[x]:
        if key == 0 or key == 11:
            aocost[x][key]=0
aocost


# reopening cost
rocostfy = [190,150,160,100,130]
rocost = {}
for i in plant_l:
    rocost[i]={}
    for t in year_l:
        rocost[i][t] = rocostfy[i-1]*(1+0.03)**(t-1)

for x in rocost:
    for key in rocost[x]:
        if key == 0 or key == 11:
            rocost[x][key]=0
rocost


# shutdown cost
sdcost = {}
sdcostfy = [170,120,130,80,110]
for i in plant_l:
    sdcost[i]={}
    for t in year_l:
        sdcost[i][t] = sdcostfy[i-1]*(1+0.03)**(t-1)

for x in sdcost:
    for key in sdcost[x]:
        if key == 0 or key == 11:
            sdcost[x][key]=0
sdcost


# alloy cost
acost = {}
acostfy = [0.02,0.02,0.02,0.02,0.02]
for i in plant_l:
    acost[i]={}
    for t in year_l:
        acost[i][t] = acostfy[i-1]*(1+0.03)**(t-1)

for x in acost:
    for key in acost[x]:
        if key == 0 or key == 11:
            acost[x][key]=0
acost

# Widget subassemblies original cost
wocost = {}
wocostfy = [0.15,0.15,0.15,0.15,0.15]
for i in plant_l:
    wocost[i]={}
    for t in year_l:
        wocost[i][t] = wocostfy[i-1]*(1+0.03)**(t-1)

for x in wocost:
    for key in wocost[x]:
        if key == 0 or key == 11:
            wocost[x][key]=0
wocost

# Widget subassemblies discounted cost
wdcost = {}
wdcostfy = [0.12,0.12,0.12,0.12,0.12]
for i in plant_l:
    wdcost[i]={}
    for t in year_l:
        wdcost[i][t] = wdcostfy[i-1]*(1+0.03)**(t-1)

for x in wdcost:
    for key in wdcost[x]:
        if key == 0 or key == 11:
            wdcost[x][key]=0
wdcost

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

Aijt = {}
for i in plant_l:
    Aijt[i]={}
    for j in warehouse_l:
        Aijt[i][j]={}
        for t in year_l:
            Aijt[i][j][t]=dfwscostfy[i][j]*(1+0.03)**(t-1)

for x in Aijt:
    for y in Aijt[x]:
        for key in Aijt[x][y]:
            if key == 0 or key == 11:
                Aijt[x][y][key]=0
    
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

Bjkt = {}
for j in warehouse_l:
    Bjkt[j]={}
    for k in retail_l:
        Bjkt[j][k]={}
        for t in year_l:
            Bjkt[j][k][t]=dfrscostfy[j][k]*(1+0.03)**(t-1)    
            
for x in Bjkt:
    for y in Bjkt[x]:
        for key in Bjkt[x][y]:
            if key == 0 or key == 11:
                Bjkt[x][y][key]=0

Bjkt

# year = 11
warehouse = 4
# Indexed sets
#stores = range(len(demandfy)) # k
stores = [1,2,3,4,5,6,7,8]
#plants = range(len(conscostfy)) # i 
plants = [1,2,3,4,5]
#warehouses = range(warehouse) # j
warehouses = [1,2,3,4]
#years = range(year) # t
years = [0,1,2,3,4,5,6,7,8,9,10,11]
year = [1,2,3,4,5,6,7,8,9,10]

capacity = [16000,12000,14000,10000,13000]
r = gp.Model("Model")
r.params.NonConvex = 2

# Variables
zvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, name = "z") # units of Flugels produced by plant i in year t
xvars = r.addVars(plants, warehouses, years, vtype=GRB.CONTINUOUS, name = "x") # units of Flugels shipped from plant i to warehouse j in year t
ivars = r.addVars(warehouses, years, vtype=GRB.CONTINUOUS, name = "ivar")
yvars = r.addVars(warehouses, stores, years, vtype=GRB.CONTINUOUS, name = "y") # units of Flugels shipped from warehouse j to retail center k in year t
lamda1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, name = "lamda1") # calculating the weighted units of purchased raw materials of plant i in year t
lamda2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, name = "lamda2") # calculating the weighted units of purchased raw materials of plant i in year t
lamda3vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, name = "lamda3") # calculating the weighted units of purchased raw materials of plant i in year t
pvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "pvar") # whether the plant i’s production line is open at the beginning of year t. 1: open, 0: close (binary) 
e1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "e1")
e2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "e2")
fvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "fvar") # whether the production line in the plant i is going to be shut down at the end of year t or not. 1: shut down, 0: close (binary) 
gvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "gvar") # whether the production line in the plant i in year t is the initial construction year. 1: initial, 0: not initial (binary)
hvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, lb = 0, ub = 1,  name = "hvar") # whether the production line in the plant i was never opened before year t or not. 1: not opened before, 0: opened before (binary) 

#r.modelSense = GRB.MINIMIZE

# Constraints
# Plant Cost
r.addConstrs((gvars[i,t] == 1 - pvars[i,t-1] for i in plants for t in year), "Reopening_cost_binary_variable")
r.addConstrs((fvars[i,t] == 1 - pvars[i,t+1] for i in plants for t in year), "Shut_down_cost_binary_variable")
r.addConstrs((zvars[i,t] <= pvars[i,t] * capacity[i-1] for i in plants for t in year), "Plant_capacity_binary_variable")
r.addConstrs((pvars[i,0] == 0 for i in plants), 'Year_0_P_variable')
r.addConstrs((pvars[i,11] == 0 for i in plants), 'Year_11_P_variable')
r.addConstrs((gvars[i,0] == 0 for i in plants), 'Year_0_G_variable')
r.addConstrs((hvars[i,0] == 0 for i in plants), 'Year_1_H_variable')
# Shipping Cost
r.addConstrs((xvars.sum(i,'*',t) == zvars[i,t] for i in plants for t in year), "Sum_of_Products_Shipped") # sum of products shipped from each plant in year t equals to the amount of flugels produced by it in year t 
r.addConstrs((xvars.sum('*',j,t) + ivars[j,t-1] == yvars.sum(j,'*',t) + ivars[j,t] for j in warehouses for t in year), "Sum_of_Products_Recieved_at_Warehouses") # sum of products received by warehouse j in year t equals to sum of products shipped from warehouse j in year t
r.addConstrs((ivars.sum(j,'*') <= 40000 for j in warehouses), "Average_Inventory") # average inventory in any year to be no more than 4000 items (among all Warehouses)
r.addConstrs((xvars.sum('*',j,t) <= 12000 for j in warehouses for t in year), "Warehouse_Inflow") # both the flow into a warehouse and the flow out of a warehouse should not exceed an average of 1000 units per month
r.addConstrs((yvars.sum(j,'*',t) <= 12000 for j in warehouses for t in year), "Warehouse_Outflow") # both the flow into a warehouse and the flow out of a warehouse should not exceed an average of 1000 units per month
r.addConstrs((ivars[j,0] == 0 for j in warehouses), 'Year_0_Inventory')
r.addConstrs((ivars[j,10] == 0 for j in warehouses), 'Year_10_Inventory')
r.addConstrs((ivars[j,11] == 0 for j in warehouses), 'Year_11_Inventory')
# Demand
r.addConstrs((yvars.sum('*',k,t) == demand[k][t] for k in stores for t in year), "Meet_Demand")
# Alloy
r.addConstrs((4.7 * zvars[i,t] <= 60000 for i in plants for t in year), "Pounds_of_Alloy")
# Material
r.addConstrs((lamda1vars[i,t] <= e1vars[i,t] for i in plants for t in year), "Lamda1")
r.addConstrs((lamda2vars[i,t] <= e1vars[i,t] + e2vars[i,t] for i in plants for t in year), "Lamda2")
r.addConstrs((lamda3vars[i,t] <= e2vars[i,t] for i in plants for t in year), "Lamda3")
r.addConstrs((lamda1vars[i,t] + lamda2vars[i,t] + lamda3vars[i,t] == 1 for i in plants for t in year), "Lamda_Sum")
r.addConstrs((e1vars[i,t] + e2vars[i,t] == 1 for i in plants for t in year), "e1_and_e2_value")
r.addConstrs((((9000*(lamda2vars[i,t]) + 1000000*(lamda3vars[i,t])) / 3) == zvars[i,t] for i in plants for t in year), "Z_value")

# Optimize Model
#r.optimize()

#r.setObjective(gp.quicksum(pvars[i][t]*aocost[i][t]+fvars[i][t]*sdcost[i][t]+pvars[i][t]*gvars[i][t]*rocost[i][t]+hvars[i][t]*pvars[i][t]*conscost[i][t]+(9000*wocost[i][t])*lamda2vars[i][t]+(9000*wocost[i][t]+wdcost[i][t]*(1000000-9000))*lamda3vars[i][t]+4.7*acost[i][t]*zvars[i][t] for i in plants for t in years)+gp.quicksum(xvars[i][j][t]*Aijt[i][j][t] for i in plants for j in warehouses for t in years)+gp.quicksum(yvars[j][k][t]+Bjkt[j][k][t] for j in plants for k in stores for t in years), gp.MINIMIZE)

#r.setObjective(gp.quicksum(pvars.sum('*','*')*aocost.sum('*','*')), GRB.MINIMIZE)

# first function
# pvars[i][t]*aocost[i][t]
pa = 0
for i in aocost:
    for t in years:
        pa += aocost[i][t] * pvars[(i,t)]
pa
# fvars[i][t]*sdcost[i][t]
fs = 0
for i in sdcost:
    for t in years:
        fs += aocost[i][t] * pvars[(i,t)]
fs

# pvars[i][t]*gvars[i][t]*rocost[i][t]
pgr = 0
for i in rocost:
    for t in years:
        pgr += rocost[i][t] * pvars[(i,t)] * gvars[(i,t)]
pgr

# hvars[i][t]*pvars[i][t]*conscost[i][t]
chp = 0
for i in conscost:
    for t in years:
        chp += conscost[i][t] * hvars[(i,t)] * pvars[(i,t)]
chp

# second function
#(9000*wocost[i][t])*lamda2vars[i][t]
wl2 = 0
for i in wocost:
    for t in years:
        wl2 += (9000*wocost[i][t]) * lamda2vars[(i,t)]
wl2

#(9000*wocost[i][t]+wdcost[i][t]*(1000000-9000))*lamda3vars[i][t]
wl3 = 0
for i in wocost:
    for t in years:
        wl3 += (9000*wocost[i][t] * wdcost[i][t]*(1000000-9000))*lamda3vars[(i,t)]
wl3

# third function (alloy)
az = 0
for i in acost:
    for t in years:
        az += 4.7*acost[i][t] * zvars[(i,t)]
az

# fourth function (shipping cost)
# xvars[i][j][t]*Aijt[i][j][t]
xa = 0
xa
for i in Aijt:
    for j in warehouses:
        for t in years:
            xa += xvars[(i,j,t)] * Aijt[i][j][t]
xa


# yvars[j][k][t]+Bjkt[j][k][t]
yb = 0
yb
for j in Bjkt:
    for k in stores:
        for t in years:
            yb += yvars[(j,k,t)] * Bjkt[j][k][t]
yb


r.setObjective(pa+fs+pgr+chp+wl2+wl3+az+xa+yb,GRB.MINIMIZE)

r.optimize()


#printSolution()
# Objective Function Value
print('\nTotal Costs: %g' % r.objVal)

# Cost per year -- is there a way we can do this with our current objective value format?

# Plants to warehouses
print('SOLUTION:')
for i in plants:
    for j in warehouses:
        for t in year:
            if pvars[i,t].x > 0.99:
                if xvars[i,j,t].x > 0:
                    print('Plant %d will transport %d units to warehouse %d in year %d' % ((i, xvars[i,j,t].x, j,t)))
# pvars
for i in plants:
    for t in year:
        if pvars[i,t].x > 0.99:
            print('Plant %d will be open in year %d' % (i,t))
        else:
            print('Plant %s closed in year %d' % ((i,t)))


## Warehouses to retail centers
for j in warehouses:
        for k in stores:
            for t in year:
                if yvars[j,k,t].x > 0:
                    print('Warehouse %d will transport %d Flugels to retail center %d in year %d' % (j,(yvars[j,k,t].x), k, t))
                else:
                    print('Warehouse %d will transport 0 Flugels to retail center %d in year %d' % (j,k,t))


# Flugels produced (zvars)
for i in plants:
    for t in year:
        if zvars[(i,t)].x > 0:
            print('Plant %d will produce %d units in year %d' % (i, (zvars[i,t].x),(t)))
          
    
# Units of inventory stored in each warehouse each year (ivars)
for j in warehouses:
    for t in year:
        if ivars[(j,t)].x > 0:
            print('Warehouse %d will have %d units of inventory in year %d' % (j, (ivars[j,t].x), t))

        
# plant shutdown (fvars)
for i in plants:
    for t in year:
        if fvars[(i,t)].x > 0.99:
            print('Plant %d will shutdown in the end of year %d' % (i,t))

# plant reopening (gvars)
for i in plants:
    for t in year:
        if gvars[(i,t)].x > 0.99:
            print('Plant %d will reopen in the beginning of year %d' % (i,t))

# plant construction (hvars)
for i in plants:
    for t in year:
        if hvars[(i,t)].x > 0.99:
            print('Plant %d will be constructed in the beginning of year %d' % (i,t))

r.write('xyz.lp')

# print our objective function
# print(r.getObjective())





