# (간단 예시)
import pandas as pd
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor


d = pd.read_csv('transcribed_population_2010_2024.csv', index_col='year')
reg_df = d[['births','marriages','median_age','total_population']].dropna()
X = reg_df[['marriages','median_age','total_population']]
X = sm.add_constant(X)
y = reg_df['births']
model = sm.OLS(y, X).fit()
print(model.summary())


# VIF
vif = pd.DataFrame()
vif['variable'] = X.columns
vif['VIF'] = [variance_inflation_factor(X.values, i) for i in range(X.shape[1])]
print(vif)