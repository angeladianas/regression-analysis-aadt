#import all libraries
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import statsmodels.api as sm
import statsmodels.formula.api as smf
%matplotlib inline
from sklearn.linear_model import LinearRegression
from pandas.plotting import scatter_matrix
from sklearn.metrics import mean_squared_error

df = pd.read_fwf('aadt.txt', header = None)
df.columns = ["aadt", "population", "num_lanes", \
        "width_road", "access_control", "others_1", \
        "others_2", "others_3"]
del df['others_1']
del df['others_2']
del df['others_2']
df.head()

scatter_matrix(df, alpha=1, figsize=(12, 12), \
            diagonal='kde') 

from sklearn.preprocessing import StandardScaler 
stdsc = StandardScaler() 
X_std = stdsc.fit_transform(df[cols].iloc[:,range(0,5)] \
        .values)
cov_mat = np.cov(X_std.T)
plt.figure(figsize=(10,10))
sns.set(font_scale=1.5)
hm = sns.heatmap(cov_mat,
                 cbar=True,
                 annot=True,
                 square=True,
                 fmt='.2f',
                 annot_kws={'size': 12},
                 cmap='coolwarm',                 
                 yticklabels=cols,
                 xticklabels=cols)
plt.title('Covariance matrix showing correlation \ 
            coefficients', size = 18)
plt.tight_layout()
plt.show()

model = smf.ols("aadt ~ population + num_lanes \ 
        + width_road + access_control", data = df).fit()
model.summary()

x = df[['population', 'num_lanes', 'width_road', \ 
    'access_control']]
y = df['aadt']
lm = LinearRegression()
lm.fit(x,y)
lm.intercept_
lm.coef_
yhat = lm.predict(x)

res = model.resid
fig = sm.qqplot(res, fit = True, line = '45')
plt.show()

raw <- read.table('Desktop/anaconda_files/aadt.txt',
        header=FALSE)
df <- data.frame(y=raw$V1,x1=raw$V2,x2=raw$V3,x3=raw$V4, 
        x4=raw$V5)
mlr2 <- lm(y ~ x1+x2+x3+x4, data=df)
plot(residuals(mlr2),ylab='Residuals',xlab='Time')
plot(residuals(mlr2),fitted(mlr2),ylab='Residuals'
    ,xlab='Fitted values')

# residual plot
fig, axs = plt.subplots(2,2, figsize =(20,20))

sns.residplot(df['population'], df['aadt'], \ 
                ax = axs[0,0])
sns.residplot(df['num_lanes'], df['aadt'], \ 
                ax = axs[0,1])
sns.residplot(df['width_road'], df['aadt'], \ 
                ax = axs[1,0])
sns.residplot(df['access_control'], df['aadt'], \ 
                ax = axs[1,1])

axs[0,0].set(ylabel = 'Residuals')
axs[0,1].set(ylabel = 'Residuals')
axs[1,0].set(ylabel = 'Residuals')
axs[1,1].set(ylabel = 'Residuals')

plt.show()

tr_model = smf.ols("np.sqrt(aadt) ~ population + \ 
            num_lanes + width_road + access_control", \ 
            data = df).fit()
tr_model.summary()

res = tr_model.resid
fig = sm.qqplot(res, fit = True, line = '45')
plt.show()

b_tr_model = smf.ols("np.true_divide((np.power(aadt, \ 
            0.2626263)-1), 0.262626263) ~ population \ 
            + num_lanes + width_road + access_control", \ 
            data = df).fit()
b_tr_model.summary()

res = b_tr_model.resid
fig = sm.qqplot(res, fit = True, line = '45')
plt.show()

from patsy import dmatrices
from statsmodels.stats.outliers_influence \ 
        import variance_inflation_factor
vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor \
                    (x.values, i) for i in \ 
                    range(x.shape[1])]
vif["features"] = x.columns
vif.round(1)

reduced_model = smf.ols("np.sqrt(aadt) ~ population \ 
                + num_lanes + access_control", \ 
                data = df).fit()
reduced_model.summary()

res = reduced_model.resid
fig = sm.qqplot(res, fit = True, line = '45')
plt.show()

