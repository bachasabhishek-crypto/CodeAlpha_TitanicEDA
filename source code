# ============================================
# TITANIC DATASET - EXPLORATORY DATA ANALYSIS
# CodeAlpha Internship Project
# ============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ============================================
# 1. LOAD DATASET
# ============================================
df = pd.read_csv('train.csv')
print(df.shape)
print(df.head())
print(df.info())
print(df.describe())

# ============================================
# 2. MISSING VALUES
# ============================================
print("\nMissing Values:")
print(df.isnull().sum())
print(df.isnull().sum() / len(df) * 100)

# ============================================
# 3. DATA DISTRIBUTIONS
# ============================================

# Gender Distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
df['Sex'].value_counts().plot(kind='bar', color=['steelblue', 'coral'])
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')

# Passenger Class Distribution
plt.subplot(1, 2, 2)
df['Pclass'].value_counts().sort_index().plot(kind='bar', color=['green', 'blue', 'gray'])
plt.title('Passenger Class Distribution')
plt.xlabel('Class')
plt.ylabel('Count')
plt.tight_layout()
plt.savefig('distributions.png')
plt.show()

# Age Distribution
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
df['Age'].hist(bins=30, color='steelblue', edgecolor='black')
plt.axvline(df['Age'].mean(), color='red', linestyle='--', label=f"Mean: {df['Age'].mean():.1f}")
plt.axvline(df['Age'].median(), color='green', linestyle='--', label=f"Median: {df['Age'].median():.1f}")
plt.title('Age Distribution')
plt.xlabel('Age')
plt.legend()

# Fare Distribution
plt.subplot(1, 2, 2)
df[df['Fare'] < 300]['Fare'].hist(bins=30, color='orange', edgecolor='black')
plt.axvline(df['Fare'].mean(), color='red', linestyle='--', label=f"Mean: {df['Fare'].mean():.1f}")
plt.axvline(df['Fare'].median(), color='green', linestyle='--', label=f"Median: {df['Fare'].median():.1f}")
plt.title('Fare Distribution (clipped at £300)')
plt.xlabel('Fare')
plt.legend()
plt.tight_layout()
plt.savefig('age_fare.png')
plt.show()

# ============================================
# 4. SURVIVAL ANALYSIS
# ============================================

# Survival by Gender
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
df.groupby('Sex')['Survived'].mean().mul(100).plot(kind='bar', color=['coral', 'steelblue'])
plt.title('Survival Rate by Gender')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)

# Survival by Class
plt.subplot(1, 2, 2)
df.groupby('Pclass')['Survived'].mean().mul(100).plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('Survival Rate by Passenger Class')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig('survival_gender_class.png')
plt.show()

# Survival by Gender x Class Interaction
pivot = df.groupby(['Pclass', 'Sex'])['Survived'].mean().unstack()
pivot.mul(100).plot(kind='bar', figsize=(8, 5), color=['coral', 'steelblue'])
plt.title('Survival: Sex x Class Interaction')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)
plt.savefig('sex_class_interaction.png')
plt.show()

# Survival by Age Group
df['AgeGroup'] = pd.cut(df['Age'], bins=[0, 12, 18, 35, 60, 100],
                         labels=['Child', 'Teen', 'Adult', 'Middle-aged', 'Senior'])
df.groupby('AgeGroup')['Survived'].mean().mul(100).plot(kind='bar', color='teal', figsize=(8, 5))
plt.title('Survival Rate by Age Group')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)
plt.savefig('survival_agegroup.png')
plt.show()

# Survival by Family Size
df['FamilySize'] = df['SibSp'] + df['Parch'] + 1
df.groupby('FamilySize')['Survived'].mean().mul(100).plot(kind='bar', color='purple', figsize=(8, 5))
plt.title('Survival Rate by Family Size')
plt.ylabel('Survival Rate (%)')
plt.xticks(rotation=0)
plt.savefig('survival_familysize.png')
plt.show()

# ============================================
# 5. HYPOTHESIS TESTING
# ============================================

# H1: Sex affects survival
ct = pd.crosstab(df['Sex'], df['Survived'])
chi2, p, dof, expected = stats.chi2_contingency(ct)
print(f"\nH1 - Sex vs Survival: chi2={chi2:.2f}, p={p:.4f}")

# H2: Pclass affects survival
ct2 = pd.crosstab(df['Pclass'], df['Survived'])
chi2, p, dof, expected = stats.chi2_contingency(ct2)
print(f"H2 - Pclass vs Survival: chi2={chi2:.2f}, p={p:.4f}")

# H3: Age differs between survivors
survived_age = df[df['Survived'] == 1]['Age'].dropna()
not_survived_age = df[df['Survived'] == 0]['Age'].dropna()
t, p = stats.ttest_ind(survived_age, not_survived_age)
print(f"H3 - Age vs Survival: t={t:.3f}, p={p:.4f}")

# H4: Fare differs between survivors
survived_fare = df[df['Survived'] == 1]['Fare']
not_survived_fare = df[df['Survived'] == 0]['Fare']
t, p = stats.ttest_ind(survived_fare, not_survived_fare)
print(f"H4 - Fare vs Survival: t={t:.3f}, p={p:.4f}")

# H5: Embarkation affects survival
ct3 = pd.crosstab(df['Embarked'], df['Survived'])
chi2, p, dof, expected = stats.chi2_contingency(ct3)
print(f"H5 - Embarked vs Survival: chi2={chi2:.2f}, p={p:.4f}")

# ============================================
# 6. CORRELATION
# ============================================
plt.figure(figsize=(8, 5))
corr = df[['Pclass', 'Age', 'Fare', 'SibSp', 'Parch', 'Survived']].corr()
corr['Survived'].drop('Survived').sort_values().plot(kind='barh', color='steelblue')
plt.title('Correlation of Features with Survival')
plt.xlabel('Pearson Correlation Coefficient')
plt.savefig('correlation.png')
plt.show()

# ============================================
# 7. MISSING VALUE TREATMENT
# ============================================
df['Age'] = df.groupby(['Pclass', 'Sex'])['Age'].transform(lambda x: x.fillna(x.median()))
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])
df.drop(columns=['Cabin'], inplace=True)

print("\nMissing values after imputation:")
print(df.isnull().sum())

print("\nEDA Complete!")
