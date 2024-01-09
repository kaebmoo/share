import pandas as pd 

df_thai = pd.read_csv("/Users/seal/Documents/thai_dict.csv")
df_chinese = pd.read_csv("/Users/seal/Documents/chinese_dict.csv")

print(df_thai)
print(df_chinese)

result = pd.merge(
    df_thai, 
    df_chinese, 
    left_on = ["eng"], 
    right_on = ["eng"], 
    how = 'right')
print(result)
print(result[["eng", "thai"]])

result = pd.merge(
    df_thai, 
    df_chinese, 
    left_on = ["eng"], 
    right_on = ["eng"], 
    how = 'left')
print(result)

