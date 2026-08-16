# NOTE: continue tells loop to skip the part for which condition is satisfied.
# NOTE: print after continue

# EXAMPLE 1:

for i in range(10):
    if 3<=i<=5:
        continue
    print(i)
    
    # OUTPUT: 0, 1, 2, 6, 7, 8, 9