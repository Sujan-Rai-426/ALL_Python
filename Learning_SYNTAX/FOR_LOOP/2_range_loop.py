# NOTE: range( end+1 ) 
# NOTE: range( start, end+1 ) 
# NOTE: range( start, end+1, jump ) 

# NOTE: range(end)
for i in range(10):
    print(i)


# NOTE: range(start, end+1)
print("NEW LOOP:")
for j in range(5, 10):
    print(j)



# NOTE: range(start, end+1, jump)
print("NEW LOOP:")
for k in range(5, 20, 2):
    print(k)



# --------------- for REVERSE Loop [start from high, toward Low, & jump by Negative]------------
# NOTE: range(start, end+1, jump)
print("NEW LOOP:")
for k in range(20, 5, -2):
    print(k)