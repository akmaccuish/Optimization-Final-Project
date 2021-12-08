# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:43:12 2021

@author: aidan
"""

import gurobipy as gp
from gurobipy import GRB

year = 10
warehouse = 4
# Indexed sets
stores = range(len(demandfy)) # k
plants = range(len(concostfy)) # i 
warehouses = range(warehouse) # j
years = range(year) # t

r = gp.Model("Model")

# Variables
zvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "z") # units of Flugels produced by plant i in year t
xvars = r.addVars(plants, warehouses, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "x") # units of Flugels shipped from plant i to warehouse j in year t
ivars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "ivar")
yvars = r.addVars(warehouses, stores, years, vtype=GRB.CONTINUOUS, obj=whtocust, name = "y") # units of Flugels shipped from warehouse j to retail center k in year t
lamda1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "lamda1") # calculating the weighted units of purchased raw materials of plant i in year t
lamda2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "lamda2") # calculating the weighted units of purchased raw materials of plant i in year t
lamda3vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "lamda3") # calculating the weighted units of purchased raw materials of plant i in year t
pvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "pvar") # whether the plant i’s production line is open at the beginning of year t. 1: open, 0: close (binary) 
e1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "e1")
e2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "e2")
fvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = sdcost, lb = 0, ub = 1,  name = "fvar") # whether the production line in the plant i is going to be shut down at the end of year t or not. 1: shut down, 0: close (binary) 
gvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = rocost, lb = 0, ub = 1,  name = "gvar") # whether the production line in the plant i in year t is the initial construction year. 1: initial, 0: not initial (binary)
hvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = conscost, lb = 0, ub = 1,  name = "hvar") # whether the production line in the plant i was never opened before year t or not. 1: not opened before, 0: opened before (binary) 

# Constraints
# Plant Cost
r.addConstrs((gvars[i][t] == 1 - pvars[i][t-1] for i in plants for t in years), "Reopening cost binary variable")
r.addConstrs((fvars[i][t] == 1 - pvars[i][t+1] for i in plants for t in years), "Shut down cost binary variable")
r.addConstrs((zvars[i][t] <= pvars[i][t] * capacity[i] for i in plants for t in years), "Plant capacity binary variable")
r.addConstrs((pvars[j][0] = 0 for j in warehouses), 'Year 0 P variable')
r.addConstrs((pvars[j][11] = 0 for j in warehouses), 'Year 11 P variable')
r.addConstrs((gvars[j][0] = 0 for j in warehouses), 'Year 0 G variable')
# Shipping Cost
r.addConstrs((xvars.sum(i,'*',t) == zvars[i][t] for i in plants for t in years), "Sum of Products Shipped") # sum of products shipped from each plant in year t equals to the amount of flugels produced by it in year t 
r.addConstrs((xvars.sum('*',j,t) + ivars[j][t-1] == yvars.sum(j,'*',t) + ivars[j][t] for j in warehouses for t in years), "Sum of Products Recieved at Warehouses") # sum of products received by warehouse j in year t equals to sum of products shipped from warehouse j in year t
r.addConstrs((ivars.sum(j,'*') <= 40000 for j in warehouses), "Average Inventory") # average inventory in any year to be no more than 4000 items (among all Warehouses)
r.addConstrs((xvars.sum('*',j,t) <= 12000 for j in warehouses for t in years), "Warehouse Inflow") # both the flow into a warehouse and the flow out of a warehouse should not exceed an average of 1000 units per month
r.addConstrs((yvars.sum(j,'*',t) <= 12000 for j in warehouses for t in years), "Warehouse Outflow") # both the flow into a warehouse and the flow out of a warehouse should not exceed an average of 1000 units per month
r.addConstrs((ivars[j][0] = 0 for j in warehouses), 'Year 0 Inventory')
r.addConstrs((ivars[j][10] = 0 for j in warehouses), 'Year 10 Inventory')
r.addConstrs((ivars[j][11] = 0 for j in warehouses), 'Year 11 Inventory')
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



