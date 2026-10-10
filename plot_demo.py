import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_csv('demo_trend.csv')
df['release_year'] = df['release_year'].astype(int)  # 转整数
df = df[df['release_year'] >= 2010]                   # 只看2010年后
df = df.sort_values('release_year')

plt.figure(figsize=(10, 6))
sns.lineplot(data=df, x='release_year', y='demo_pct', marker='o', color='#1f77b4')

plt.title('Steam 游戏 Demo 占比变化趋势 (2010-2024)', fontsize=16, fontweight='bold')
plt.xlabel('发行年份', fontsize=12)
plt.ylabel('Demo 占比 (%)', fontsize=12)
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(df['release_year'], rotation=45)

if not os.path.exists('images'):
    os.makedirs('images')
plt.savefig('images/demo_trend.png', dpi=300, bbox_inches='tight')
plt.show()