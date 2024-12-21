import numpy as np

np.random.seed(42)


# 30명의 몸무게
weight_data = np.random.randint(40, 80, size=(3, 10))  # 몸무게 범위는 40kg ~ 80kg


# 계급 - [40~50), [50, 60), [60, 70), [70, 80)


# 도수
group_40_50 = weight_data[(weight_data >= 40) & (weight_data < 50)]  
group_50_60 = weight_data[(weight_data >= 50) & (weight_data < 60)] 
group_60_70 = weight_data[(weight_data >= 60) & (weight_data < 70)]  
group_70_80 = weight_data[(weight_data >= 70) & (weight_data < 80)] 

freq = [len(group_40_50), len(group_50_60), len(group_60_70), len(group_70_80)] 


# 상대 도수
relative_freq = [count / weight_data.size for count in freq]


# 출력
print("도수:", freq)
print("상대 도수:", [f"{x:.2f}" for x in relative_freq])

'''
도수: [4, 7, 13, 6]
상대 도수: ['0.13', '0.23', '0.43', '0.20']
'''