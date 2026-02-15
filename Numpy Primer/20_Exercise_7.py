import numpy as np

family_array = np.array([
    'HOME CARE', 'LADIESWEAR', 'LAWN AND GARDEN', 'LINGERIE', 
    'LIQUOR,WINE,BEER', 'MAGAZINES', 'MEATS', 'PERSONAL CARE',
    'PET SUPPLIES', 'PLAYERS AND ELECTRONICS', 'POULTRY', 
    'PREPARED FOODS', 'PRODUCE', 'SCHOOL AND OFFICE SUPPLIES',
    'PRODUCE', 'PRODUCE', 'PRODUCE', 'PRODUCE'
])
sales_array = np.array([
    1662.394, 447.064, 962.866, 1077.44, 3404.531, 962.96,
    1089.319, 7860.031, 446.038, 1272.755, 2775.771, 2339.906,
    722.333, 1567.843, 2458.456, 673.885, 8834.15, 1200.50
])

rng = np.random.default_rng(2022)


produce_sales = sales_array[family_array == 'PRODUCE']
sales_samples = rng.choice(produce_sales, size=len(produce_sales) // 2, replace=False)

print(sales_samples.mean())
