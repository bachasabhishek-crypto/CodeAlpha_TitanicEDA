# ============================================
# GLOBAL SALES ANALYTICS DASHBOARD
# Converted from HTML/Chart.js to Python
# ============================================

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import FancyBboxPatch
import warnings
warnings.filterwarnings('ignore')

# ── STYLE SETTINGS ──
plt.rcParams.update({
    'figure.facecolor':  '#09090f',
    'axes.facecolor':    '#16161f',
    'axes.edgecolor':    '#1e1e2e',
    'axes.labelcolor':   '#6b6b80',
    'xtick.color':       '#6b6b80',
    'ytick.color':       '#6b6b80',
    'text.color':        '#e8e8f0',
    'grid.color':        '#1a1a26',
    'grid.linestyle':    '--',
    'grid.alpha':        0.6,
    'font.family':       'DejaVu Sans',
    'font.size':         10,
    'axes.titlecolor':   '#ffffff',
    'axes.titlesize':    13,
    'axes.titleweight':  'bold',
    'legend.facecolor':  '#16161f',
    'legend.edgecolor':  '#1e1e2e',
    'legend.labelcolor': '#6b6b80',
})

# ── COLORS ──
ACCENT  = '#f97316'
CYAN    = '#06b6d4'
PURPLE  = '#a855f7'
GREEN   = '#22c55e'
GOLD    = '#fbbf24'
RED     = '#ef4444'
PINK    = '#ec4899'
TEAL    = '#14b8a6'

# ============================================
# CHART 1: Monthly Revenue Trend (Line Chart)
# ============================================
months = ['Jan','Feb','Mar','Apr','May','Jun',
          'Jul','Aug','Sep','Oct','Nov','Dec']

revenue_2022 = [210,190,240,260,280,310,295,330,350,380,460,520]
revenue_2023 = [240,225,275,295,320,355,340,380,410,445,530,605]
revenue_2024 = [285,265,320,360,395,430,415,465,510,555,640,740]

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#09090f')

ax.plot(months, revenue_2022, color='#334155', linewidth=2,
        marker='o', markersize=4, label='2022')
ax.plot(months, revenue_2023, color=CYAN, linewidth=2,
        marker='o', markersize=4, label='2023')
ax.fill_between(months, revenue_2023, alpha=0.08, color=CYAN)
ax.plot(months, revenue_2024, color=ACCENT, linewidth=2.5,
        marker='o', markersize=5, label='2024')
ax.fill_between(months, revenue_2024, alpha=0.10, color=ACCENT)

ax.set_title('Monthly Revenue Trend', pad=15)
ax.set_ylabel('Revenue ($000s)')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${int(v)}k'))
ax.legend()
ax.grid(True, axis='y')
plt.tight_layout()
plt.savefig('chart1_revenue_trend.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 1 saved: chart1_revenue_trend.png")


# ============================================
# CHART 2: Sales by Category (Grouped Bar)
# ============================================
quarters    = ['Q1 2024','Q2 2024','Q3 2024','Q4 2024']
categories  = ['Electronics','Clothing','Home & Garden','Sports','Books']
cat_data    = [
    [380, 420, 395, 510],
    [180, 210, 260, 310],
    [140, 155, 175, 190],
    [95,  115, 135, 160],
    [60,  70,  65,  88 ],
]
cat_colors  = [ACCENT, CYAN, GREEN, PURPLE, GOLD]

x      = np.arange(len(quarters))
width  = 0.15
offsets= np.linspace(-2, 2, len(categories)) * width

fig, ax = plt.subplots(figsize=(12, 5))
fig.patch.set_facecolor('#09090f')

for i, (cat, data, color, offset) in enumerate(
        zip(categories, cat_data, cat_colors, offsets)):
    bars = ax.bar(x + offset, data, width, label=cat,
                  color=color, zorder=3)

ax.set_title('Sales by Category (2024)')
ax.set_xticks(x)
ax.set_xticklabels(quarters)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${int(v)}k'))
ax.legend()
ax.grid(True, axis='y', zorder=0)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('chart2_sales_by_category.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 2 saved: chart2_sales_by_category.png")


# ============================================
# CHART 3: Revenue by Region (Pie / Donut)
# ============================================
regions = ['North America','Asia-Pacific','Europe','Latin America','Middle East & Africa']
shares  = [35, 27, 22, 10, 6]
colors  = [ACCENT, CYAN, PURPLE, GREEN, GOLD]

fig, ax = plt.subplots(figsize=(8, 6))
fig.patch.set_facecolor('#09090f')

wedges, texts, autotexts = ax.pie(
    shares,
    labels=regions,
    colors=colors,
    autopct='%1.0f%%',
    pctdistance=0.78,
    startangle=140,
    wedgeprops=dict(width=0.5, edgecolor='#16161f', linewidth=3)
)

for t in texts:
    t.set_color('#6b6b80')
    t.set_fontsize(9)
for at in autotexts:
    at.set_color('#ffffff')
    at.set_fontsize(9)
    at.set_fontweight('bold')

ax.set_title('Revenue by Region', pad=15)
plt.tight_layout()
plt.savefig('chart3_revenue_by_region.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 3 saved: chart3_revenue_by_region.png")


# ============================================
# CHART 4: Radar — Performance by Category
# ============================================
metrics = ['Revenue', 'Growth Rate', 'Profit Margin', 'Satisfaction', 'Return Rate']
N       = len(metrics)
angles  = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
angles += angles[:1]   # close the loop

radar_data = {
    'Electronics':   [95, 72, 48, 74, 60],
    'Clothing':      [60, 88, 65, 78, 55],
    'Home & Garden': [45, 55, 72, 94, 82],
}
radar_colors = [ACCENT, CYAN, GREEN]

fig, ax = plt.subplots(figsize=(7, 6), subplot_kw=dict(polar=True))
fig.patch.set_facecolor('#09090f')
ax.set_facecolor('#16161f')

for (label, values), color in zip(radar_data.items(), radar_colors):
    vals = values + values[:1]
    ax.plot(angles, vals, color=color, linewidth=2, label=label)
    ax.fill(angles, vals, color=color, alpha=0.15)

ax.set_thetagrids(np.degrees(angles[:-1]), metrics, color='#9999aa', size=10)
ax.set_ylim(0, 100)
ax.set_yticks([20, 40, 60, 80, 100])
ax.set_yticklabels(['20','40','60','80','100'], color='#6b6b80', size=8)
ax.grid(color='#1e1e2e', linewidth=0.8)
ax.spines['polar'].set_color('#1e1e2e')
ax.set_title('Performance by Category', pad=20)
ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1))
plt.tight_layout()
plt.savefig('chart4_radar_performance.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 4 saved: chart4_radar_performance.png")


# ============================================
# CHART 5: Scatter — Marketing Spend vs Revenue
# ============================================
np.random.seed(42)

def generate_scatter(n, slope, intercept, noise):
    x = np.random.uniform(5, 35, n)
    y = slope * x + intercept + (np.random.rand(n) - 0.5) * noise
    return x, np.maximum(y, 5)

fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor('#09090f')

campaigns = [
    ('Digital Campaigns', 30, 4.2, 20, 40,  ACCENT),
    ('Print / Outdoor',   25, 3.1, 15, 35,  CYAN),
    ('Influencer',        25, 5.0, 10, 55,  PURPLE),
]

for label, n, slope, intercept, noise, color in campaigns:
    x, y = generate_scatter(n, slope, intercept, noise)
    ax.scatter(x, y, label=label, color=color, alpha=0.75, s=60, zorder=3)

ax.set_title('Marketing Spend vs Revenue Generated')
ax.set_xlabel('Marketing Spend ($000s)')
ax.set_ylabel('Revenue Generated ($000s)')
ax.legend()
ax.grid(True, zorder=0)
plt.tight_layout()
plt.savefig('chart5_scatter_marketing.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 5 saved: chart5_scatter_marketing.png")


# ============================================
# CHART 6: Customer Sentiment (Stacked Bar)
# ============================================
channels   = ['In-Store','Website','Mobile App','Social Media','Phone']
positive   = [72, 65, 68, 48, 58]
neutral    = [18, 22, 20, 28, 25]
negative   = [10, 13, 12, 24, 17]

x = np.arange(len(channels))

fig, ax = plt.subplots(figsize=(10, 5))
fig.patch.set_facecolor('#09090f')

ax.bar(x, positive, label='Positive', color=GREEN,  zorder=3)
ax.bar(x, neutral,  bottom=positive, label='Neutral',  color=GOLD, zorder=3)
ax.bar(x, negative, bottom=[p+n for p,n in zip(positive, neutral)],
       label='Negative', color=RED, zorder=3)

ax.set_title('Customer Sentiment by Channel')
ax.set_xticks(x)
ax.set_xticklabels(channels)
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'{int(v)}%'))
ax.set_ylim(0, 110)
ax.legend()
ax.grid(True, axis='y', zorder=0)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('chart6_sentiment.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 6 saved: chart6_sentiment.png")


# ============================================
# CHART 7: Top 8 Products by Revenue (H-Bar)
# ============================================
products = [
    'KitchenAid Mixer','Dyson V15','Nike Air Max','iPad Pro',
    'Sony WH-1000XM5','Samsung 4K TV','MacBook Air M3','iPhone Pro Max'
]
revenues  = [105, 118, 132, 154, 167, 198, 242, 285]
bar_colors= [RED, TEAL, PINK, GOLD, GREEN, PURPLE, CYAN, ACCENT]

fig, ax = plt.subplots(figsize=(10, 6))
fig.patch.set_facecolor('#09090f')

bars = ax.barh(products, revenues, color=bar_colors, zorder=3, height=0.6)

for bar, val in zip(bars, revenues):
    ax.text(val + 3, bar.get_y() + bar.get_height() / 2,
            f'${val}k', va='center', ha='left',
            color='#e8e8f0', fontsize=9)

ax.set_title('Top 8 Products by Revenue')
ax.set_xlabel('Revenue ($000s)')
ax.xaxis.set_major_formatter(plt.FuncFormatter(lambda v, _: f'${int(v)}k'))
ax.set_xlim(0, 330)
ax.grid(True, axis='x', zorder=0)
ax.set_axisbelow(True)
plt.tight_layout()
plt.savefig('chart7_top_products.png', dpi=150, facecolor='#09090f')
plt.show()
print("✔ Chart 7 saved: chart7_top_products.png")


# ============================================
# KPI SUMMARY PRINTOUT
# ============================================
print("\n" + "="*50)
print("   GLOBAL SALES ANALYTICS — KPI SUMMARY")
print("="*50)
print(f"  Total Revenue   : $4.8M   ↑ 18.4% vs last year")
print(f"  Total Orders    : 12,480  ↑ 11.2% vs last year")
print(f"  Avg Order Value : $384    ↑  6.8% vs last year")
print(f"  Customer Sat.   :  4.6/5  ↑  0.3  vs last year")
print("="*50)
print("\n✅ All 7 charts generated successfully!")
