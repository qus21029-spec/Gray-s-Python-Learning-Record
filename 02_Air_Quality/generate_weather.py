import pandas as pd
import random
from datetime import datetime, timedelta

# === 模拟生成 30 天的空气数据 ===
data = []
start_date = datetime(2023, 11, 1)

print("正在生成空气质量数据...")

for i in range(30):
    # 1. 日期递增
    current_date = start_date + timedelta(days=i)
    date_str = current_date.strftime('%Y-%m-%d')
    
    # 2. 模拟 PM2.5 数值 (范围 20 到 300)
    # 逻辑：随机生成一个整数，模拟空气好坏
    pm25 = random.randint(20, 300)
    
    # 3. 模拟温度
    temp = random.randint(5, 25)
    
    data.append([date_str, pm25, temp])

# 保存 CSV
df = pd.DataFrame(data, columns=['日期', 'PM2.5', '温度'])
df.to_csv("data/air_quality.csv", index=False, encoding='utf-8-sig')

print("✅ 数据生成完毕: data/air_quality.csv")