import pandas as pd
import matplotlib.pyplot as plt

# 1. 读取数据
# 注意：因为我们和 data 文件夹在同一层，所以路径还是 data/sales_data.csv
df = pd.read_csv("data/sales_data.csv")

print("=== 📊 电商销售数据分析报告 ===")

# --- 任务 1: 计算总销售额 ---
total_sales = df['订单总额'].sum()
print(f"1. 本月总销售额: {total_sales} 元")

# --- 任务 2: 谁是销量冠军？(按产品分组统计) ---
# 逻辑：把所有订单按“产品名称”归类，然后把它们的“订单总额”加起来，最后倒序排列
product_rank = df.groupby('产品名称')['订单总额'].sum().sort_values(ascending=False)

print("\n2. 最畅销产品 Top 3:")
print(product_rank.head(3))

# --- 任务 3: 每天卖得怎么样？(趋势分析) ---
# 逻辑：按“日期”归类，看每天卖了多少钱
daily_trend = df.groupby('日期')['订单总额'].sum()

print("\n3. 销售趋势分析:")
# 找出销售额最高的那一天
best_day = daily_trend.idxmax()
best_day_sales = daily_trend.max()
print(f"   生意最好的一天是: {best_day}, 卖了 {best_day_sales} 元")

# --- 进阶: 画个图看看 (保存为图片) ---
# 为了防乱码，我们这里暂时用英文做图表标签
plt.figure(figsize=(10, 6))
daily_trend.plot(kind='line', marker='o', color='orange')
plt.title("Daily Sales Trend (Oct 2023)")
plt.xlabel("Date")
plt.ylabel("Sales (CNY)")
plt.grid(True)
plt.savefig("sales_trend.png")
print("\n📈 趋势图已生成: sales_trend.png")