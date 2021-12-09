<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 00:07:29 2021

@author: acmcn
"""
#printSolution()
# Objective Function Value
print('\nTotal Costs: %g' % r.objVal)

# Cost per year -- is there a way we can do this with our current objective value format?

# Plants to warehouses
print('SOLUTION:')
for i in plants:
    if pvars[i,t].x > 0.99:
        print('Plant %d open in year %d' % ((i+1), (t+1)))
        # do we also want to track other binary variables, or just use those for our costs?
        for j in warehouses:
            for t in years:
                if xvars[i,j,t].x > 0:
                    print('Transport %d units to warehouse %d in year %d' % ((xvars[i,j,t].x, (j+1),(t+1))))
    else:
        print('Plant %s closed in year %d' % ((i+1),(t+1)))
        

## Warehouses to retail centers
for j in warehouses:
        for k in customers:
            for t in years:
                if yvars[j,k,t].x > 0:
                    print('Transport %d Flugels to retail center %d in year %d' % ((yvars[j,k,t].x), (k+1), (t+1)))
                else:
                    print('Warehouse %d will ship 0 units to retail center %d in year %d' % (j+1))


# Flugels produced (zvars)
for i in plants:
    for j in warehouses:
        for t in years:
            if zvars[i,j,t].x > 0:
                print('Plant %d will produce %d units in year %d' % 
                      ((i+1), (zvars[i,j,t].x),(t+1)))
          
    
# Units of inventory stored in each warehouse each year (ivars)
for j in warehouses:
    for t in years:
        if ivars[j,t].x > 0:
            print('Warehouse %d will have %d units of inventory in year %d' % ((j+1),
            (ivars[j][t].x), (t+1)))


# are we tracking the number of materials to purchase in each year?
        
# plant shutdown (fvars)
for i in plants:
    for t in years:
        if fvars[i][t] > 0.99:
            print('Plant %d will shutdown in the end of year %d' % ((i+1),(t+1)))

# plant reopening (gvars)
for i in plants:
    for t in years:
        if gvars[i][t] > 0.99:
            print('Plant %d will reopen in the beginning of year %d' % ((i+1),(t+1)))

# plant construction (hvars)

=======
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 00:07:29 2021

@author: acmcn
"""
#printSolution()
# Objective Function Value
print('\nTotal Costs: %g' % r.objVal)

# Cost per year -- is there a way we can do this with our current objective value format?

# Plants to warehouses
print('SOLUTION:')
for i in plants:
    if pvars[i,t].x > 0.99:
        print('Plant %d open in year %d' % ((i+1), (t+1)))
        # do we also want to track other binary variables, or just use those for our costs?
        for j in warehouses:
            for t in years:
                if xvars[i,j,t].x > 0:
                    print('Transport %d units to warehouse %d in year %d' % ((xvars[i,j,t].x, (j+1),(t+1))))
    else:
        print('Plant %s closed in year %d' % ((i+1),(t+1)))
        

## Warehouses to retail centers
for j in warehouses:
        for k in customers:
            for t in years:
                if yvars[j,k,t].x > 0:
                    print('Transport %d Flugels to retail center %d in year %d' % ((yvars[j,k,t].x), (t+1)))
                else:
                    print('Warehouse %d will ship 0 units to retail center %d in year %d' % (j+1))


# Flugels produced (zvars)
for i in plants:
    for j in warehouses:
        for t in years:
            if zvars[i,j,t] >= 0:
                print('Plant %d will produce %d units in year %d' % 
                      ((i+1), (zvars[i,j,t].x),(t+1)))
          
    
# Units of inventory stored in each warehouse each year (ivars)
for j in warehouses:
    for t in years:
        if ivars[j,t] >= 0:
            print('Warehouse %d will have %d units of inventory in year %d' % ((j+1),
            (ivars[j][t].x), (t+1)))
            
        
>>>>>>> 74141b4071e75c392fdd860cf59e2a00082d3c11
