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
zvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "z")
xvars = r.addVars(plants, warehouses, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "x")
yvars = r.addVars(warehouses, stores, years, vtype=GRB.CONTINUOUS, obj=whtocust, name = "y")
lamda1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "lamda1")
lamda2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "lamda2")
lamda3vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = planttowh, name = "lamda3")
pvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "pvar")
e1vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "e1")
e2vars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = fixedcostplant, lb = 0, ub = 1,  name = "e2")
fvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = sdcost, lb = 0, ub = 1,  name = "fvar")
gvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = rocost, lb = 0, ub = 1,  name = "gvar")
hvars = r.addVars(plants, years, vtype=GRB.CONTINUOUS, obj = conscost, lb = 0, ub = 1,  name = "hvar")

# Constraints
r.addConstrs((gvars[i][t] == 1 - pvars[i][t-1] for i in plants for t in years), "Reopening cost binary variable")
r.addConstrs((fvars[i][t] == 1 - pvars[i][t+1] for i in plants for t in years), "Shut down cost binary variable")
r.addConstrs((zvars[i][t] <= pvars[i][t] * capacity[i] for i in plants for t in years), "Plant capacity binary variable")











