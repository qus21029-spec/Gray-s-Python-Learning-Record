import pandas as pd
import matplotlib.pyplot as plt

# ==========================================
# 知识点 1: 读取数据
# 逻辑: 把 CSV 文件加载到内存中，变成一个 DataFrame (大表格)
# ==========================================
df = pd.read_csv("data/air_quality.csv")
print("=== 🌍 城市空气质量报告 ===")

# ==========================================
# 知识点 2: 数据筛选 (Boolean Indexing)
# 逻辑: 我们想找出 PM2.5 大于 150 的行。
# 写法 df[ 条件 ] 就像拿着一个筛子，只留下符合条件的沙金。
# ==========================================
bad_days = df[df['PM2.5'] > 150]

# shape[0] 代表行数，也就是有多少天
count = bad_days.shape[0]
print(f"\n1. 严重污染天数统计: 本月共有 {count} 天空气不达标！")

if count > 0:
    print("   具体日期如下:")
    # iterrows() 是一个让我们可以一行一行读取数据的工具
    for index, row in bad_days.iterrows():
        print(f"   - {row['日期']}: PM2.5高达 {row['PM2.5']}")

# ==========================================
# 知识点 3: 数据打标 (Apply + Lambda) -> 这是进阶技能！
# 逻辑: 老板看不懂数字，我们要加一列中文说明。
# apply(...) 意思是：对这一列的每一个数字，都执行一遍后面的规则。
# lambda x: ... 意思是：对于每一个数字 x，如果它<=100，就叫'优良'，否则叫'污染'。
# ==========================================
df['空气等级'] = df['PM2.5'].apply(lambda x: '🟢优良' if x <= 100 else '🔴污染')

print("\n2. 数据打标预览 (前5行):")
print(df.head())

# ==========================================
# 知识点 4: 可视化与警戒线
# 逻辑: 画图不仅是画数据，还要画标准。
# ==========================================
print("\n3. 正在生成趋势图...")
plt.figure(figsize=(10, 6))

# 画折线图
plt.plot(df['日期'], df['PM2.5'], marker='o', label='PM2.5 Index')

# 关键点: 添加一条红色的警戒线 (y=150)
# axhline = Axis Horizontal Line (水平参考线)
plt.axhline(y=150, color='red', linestyle='--', label='Warning Level (150)')

plt.title("Air Quality Trend (PM2.5)")
plt.xlabel("Date")
plt.ylabel("PM2.5 Value")
plt.legend() # 显示图例
plt.xticks(rotation=45) # 让日期斜着放，防止重叠
plt.grid(True) # 画网格

plt.savefig("air_quality_trend.png")
print("📈 图表已生成: air_quality_trend.png")