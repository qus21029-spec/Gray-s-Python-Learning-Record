import pandas as pd
import random
from datetime import datetime, timedelta

# === 配置生成规则 ===
products = {
    '无线耳机': 299,
    '机械键盘': 499,
    '电竞鼠标': 199,
    '4K显示器': 1299,
    '人体工学椅': 899,
    'Type-C数据线': 39,
    '智能手环': 159
}

data = []
start_date = datetime(2023, 10, 1)

# === 模拟生成 500 条订单数据 ===
print("正在生成模拟订单数据...")

for i in range(500):
    # 1. 随机日期 (最近30天内)
    date = start_date + timedelta(days=random.randint(0, 30))
    date_str = date.strftime('%Y-%m-%d')

    # 2. 随机选一个产品
    product_name = random.choice(list(products.keys()))
    price = products[product_name]

    # 3. 随机数量 (1-3个)
    quantity = random.randint(1, 3)

    # 4. 计算总价
    total = price * quantity

    # 添加到列表
    data.append([date_str, product_name, price, quantity, total])

# === 保存为 CSV ===
df = pd.DataFrame(data, columns=['日期', '产品名称', '单价', '数量', '订单总额'])

# 关键：保存到 data 文件夹里
file_path = "data/sales_data.csv"
df.to_csv(file_path, index=False, encoding='utf-8-sig')

print(f"✅ 成功！数据已生成: {file_path}")
print("前5行数据预览：")
print(df.head())