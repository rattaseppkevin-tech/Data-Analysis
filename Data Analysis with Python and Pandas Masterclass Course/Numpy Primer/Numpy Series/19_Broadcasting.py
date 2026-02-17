import numpy as np

# Creates a 3x3 matrix where each row is 1,2,3
test_array = np.array([[1, 2, 3], [1, 2, 3], [1, 2, 3]])
print(test_array)

# Adding + 1 to every element in the test array
print(test_array + 1)

# Adding a 1D array to each row of a 2D array
# Broadcasting: NumPy stretches the [3, 2, 1] row to match the (3, 3) shape of test_array
print(test_array + np.array([3, 2, 1]))

# Reshaping the 1D array to (3, 1) and broadcasting it across columns
# This adds 3 to the first row, 2 to the second, and 1 to the third
# Vertical broadcasting: Adding a column vector to a 2D matrix
# .reshape(3, 1) turns the row into a column to match the matrix height
print(test_array + np.array([3, 2, 1]).reshape(3, 1))
# If we don't have matching elements then we get an error.

#### Understanding the logic with AI (AI Generated example) ####
# 1. Meie poe müügitabel (3 poodi, 3 päeva)
# Read = Poed, Veerud = Päevad
sales = np.array([
    [100, 200, 300],  # Pood 1
    [50, 50, 50],     # Pood 2
    [1000, 1200, 1100] # Pood 3
])

# 2. Avamistasud iga poe kohta
# See on hetkel tavaline rida (1D array)
fees = np.array([10, 5, 100])

# 3. NÜÜD TULEB TRIKK: 
# Keerame tasud püsti (reshape), et need vastaksid ridadele (poodidele)
fees_reshaped = fees.reshape(3, 1)

# Vaatame, mis vahe on:
print("Tasud reana:", fees)           # [10, 5, 100]
print("Tasud veeruna:\n", fees_reshaped) 
# Tulemus on:
# [[10],
#  [ 5],
#  [100]]

# 4. Teeme arvutuse (Broadcasting)
# Nüüd NumPy teab: lahuta 10 esimesest reast, 5 teisest ja 100 kolmandast
final_profit = sales - fees_reshaped

print("\nLõplik kasum pärast tasude mahaarvamist:")
print(final_profit)
#################################################################

# Adding the first row (1D) and the second column (reshaped to 3,1)
# This creates a new 3x3 matrix where each element (i, j) is row[j] + col[i]
# 1. test_array[0, :] gets the first row as a horizontal vector
# 2. test_array[:, 1].reshape(3, 1) gets the second column and tips it vertically
# 3. Broadcasting sums them into a new 3x3 grid
print(test_array[0, :] + test_array[:, 1].reshape(3, 1))

#### Another AI Generated example how this works ####
# 1. Meie põhitooted (Vektor, mille me keerame püstiseks veeruks)
# Need on nagu sinu test_array[:, 1].reshape(3, 1)
products = np.array([2.00, 1.50, 3.00]).reshape(3, 1) 

# 2. Meie lisandid (Vektor, mis on horisontaalne rida)
# See on nagu sinu test_array[0, :]
add_ons = np.array([0.50, 0.20, 0.80])

# 3. NÜÜD TOIMUB MAAGIA (Broadcasting mõlemas suunas)
# NumPy venitab tooted laiaks ja lisandid pikkupidi alla
price_grid = products + add_ons

print("Kombineeritud hinnatabel:")
print(price_grid)
######################################################################################




