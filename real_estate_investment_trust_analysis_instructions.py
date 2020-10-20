#!/usr/bin/env python
# coding: utf-8

# # REIT STOCK ANALYSIS

# In this project, you will analyze Real Estate Investment Trusts, commonly known as REITs. REITs are companies that own or operate real estate that produces income. REITs, like the stocks of regular public companies, are traded on different stock exchanges. Investing in a REIT allows you to invest in portfolios of real estate assets the same way you can invest in a company by buying its stock.
# 
# Using financial statistics and NumPy you will analyze two REITs: [Sabra Health Care REIT Inc. (NASDAQ: SBRA)](https://finance.yahoo.com/quote/SBRA/), which invests in health care real estate, and [Equity Residential (NASDAQ:EQR)](https://finance.yahoo.com/quote/EQR/), which invests in rental apartment properties.

# The time period for analysis we will be using is `Jan 1 2018` to `Dec 31 2018`. The REIT data for SBRA (`SBRA.csv`) and EQR (`EQR.csv`) can be found in the same folder as this file.

# 1. Import the numpy module as np

# In[83]:


import numpy as np

def display_as_percentage(val):
    return'{0:,f}%'.format(val*100)


# 2. Load the adjusted closings for SBRA

# In[54]:


sbra_data = np.genfromtxt('SBRA.csv',delimiter = ',')
print(adj_closings_sbra)


# 3. Load the adjusted closings for EQR

# In[58]:


eqr_data = np.genfromtxt('EQR.csv', delimiter =',')
adj_closings_eqr = eqr_data[1:,5]
print(adj_closings_eqr)


# ## Simple Rate of Return Function

# 4. To calculate the daily rate of return for the SBRA stock, we need the daily adjusted closing price. The formula we are using for the daily rate of return is out[n] = a[n+1] - a[n] 

# 5. Create a function that returns the daily rate of return
# 
#     step 1. define a function named `rate_of_return`
#     
#     step 2. create parameter for  `adj_closings`
#     
#     step 3. Within the function use np.diff() and set it to the variable `daily_simple_ror`
#     
#     step 4. return `daily_simple_ror`

# In[59]:


def simple_rate_of_return(adj_closings):
  daily_simple_ror = np.diff(adj_closings)/adj_closings[:-1]
  return daily_simple_ror


# ## Calculate Daily Rate of Return for SBRA

# 6. Call the function `simple_rate_of_return` with the arguments `adj_closings_sbra`. Then print the results. 

# In[81]:


daily_simple_returns_sbra = simple_rate_of_return(adj_closings_sbra)
print(daily_simple_returns_sbra)


# ## Calculate Daily Rate of Return for EQR

# 7. Call the function `simple_rate_of_return` with the arguments `adj_closings_eqr`. Then print the results. 

# In[64]:


simples_rate_of_return_eqr = simple_rate_of_return(adj_closings_eqr)
print(simples_rate_of_return_eqr)


# ## Calculate Average Daily Return for SBRA

# 8. Use `np.mean()` with the argument `daily_simple_returns_sbra` to calculate the average daily return for SBRA. Then set it to the variable name `average_daily_simple_return_sbra`

# In[107]:


average_daily_simple_return_sbra = np.mean(daily_simple_returns_sbra)
print(average_daily_simple_return_sbra)


# ## Calculate Average Daily Return for EQR

# 9. Use `np.mean()` with the argument `daily_simple_returns_eqr` to calculate the average daily return for EQR. Then set it to the variable name `average_daily_simple_return_eqr`

# In[108]:


average_daily_simple_return_eqr= np.mean(simples_rate_of_return_eqr)
print(average_daily_simple_return_eqr)


# ## Compare the Average Daily Return between EQR and SBRA

# 10. Based on the average daily simple returns of EQR and SBRA, which stock is more likely to be profitable in the future?

# 

# ## Daily Log Returns Function

# 11. Create a function that returns the daily rate of return
# 
#     step 1. define a function named log_returns
#     
#     step 2. create parameter for  `adj_closings`
#     
#     step 3. use np.log() to get the log of each adjusted closing price and set it to the variable `log_adj_closings`
#     
#     step 4. use np.diff() to get the diff of each daily log adjusted closing price and set it to the variable `daily_log_returns`
#     
#     step 5. return `daily_log_returns`

# In[77]:


def log_returns(adj_closings):
    log_adj_closings = np.log(adj_closings)
    daily_log_returns = np.diff(log_adj_closings)
    return daily_log_returns


# ## Calculate Daily Log Returns for SBRA

# 12. Call the function `log_returns` with the arguments `adj_closings_sbra`. Set it to the variable `daily_log_returns_sbra`. Then print the results. 

# In[85]:


daily_log_returns_sbra = log_returns(adj_closings_sbra)
print(daily_log_returns_sbra)


# ## Calculate Daily Log Returns for EQR

# 13. Call the function `log_returns` with the arguments `adj_closings_eqr`. Set it to the variable `daily_log_returns_eqr`. Then print the results. 

# In[88]:


daily_log_returns_eqr = log_returns(adj_closings_eqr)
print(daily_log_returns_eqr)


# ## Annualize Daily Log Return Function

# 14. Create a function that returns the daily rate of return
# 
#     step 1. define a function named `annualize_log_return`
#     
#     step 2. create parameter for  `daily_log_returns`
#     
#     step 3. use `np.mean()` with the argument `daily_log_returns` to calculate the average daily return. Then set it to the variable name `average_daily_log_returns`
#     
#     step 4. then multiply `average_daily_log_returns` by 250 and set it to the variable `annualized_log_return`
#     
#     step 5. return `annualized_log_return`

# In[103]:


def annualise_log_returns(daily_log_returns):
    average_daily_log = np.mean(daily_log_returns)
    annualised_log_return = average_daily_log * 250
    return annualised_log_return 


# ## Calculate Annualize Daily Log Return for SBRA

# 10. Call the function `annualize_log_return` with the arguments `daily_log_returns_sbra`. Set it to the variable `annualized_log_return_sbra`. Then print the results. 

# In[109]:


annualised_log_return_sbra = annualise_log_returns(daily_log_returns_sbra)
print(annualised_log_return_sbra)


# ## Calculate Annualize Daily Log Return for EQR

# 11. Call the function `annualize_log_return` with the arguments `daily_log_returns_eqr`. Set it to the variable `annualized_log_return_eqr`. Then print the results. 

# In[120]:


annualised_log_return_eqr = annualise_log_returns(daily_log_returns_eqr)
print(annualised_log_return_eqr)

# comparing each annualised return
print('SBRA: ' , annualised_log_return_sbra, ' EQR: ', annualised_log_return_eqr)


# ## Compare the Annualize Daily Log Return between EQR and SBRA

# 12. Based on the differences between the Annualize Daily Log Return for EQR and SBRA, Which could be more profitable in the future and why?

# 

# ## Calculate Variance of Daily Log Return for SBRA

# 13. Calculate the variance of the daily logarithmetic return for SBRA. Use the function `.var()` with the argument `log_daily_ror`. Set it to the variable `daily_varaince_sbra`. Then print the results. 

# In[125]:


daily_variance_sbra = np.var(daily_log_returns_sbra)
print(daily_variance_sbra)


# ## Calculate Variance of Daily Log Return for EQR

# 14. Calculate the variance of the daily logarithmetic return for EQR. Use the function `.var()` with the argument `daily_log_returns_eqr`. Set it to the variable `daily_varaince_eqr`. Then print the results. 

# In[138]:


daily_variance_eqr = np.var(daily_log_returns_eqr)
print(daily_variance_eqr)

# comparing each
print('SBRA: ' , daily_variance_sbra, ' EQR: ', daily_variance_eqr)


# ## Compare the Variance of Daily Log Return between EQR and SBRA

# 15. Explain which investment is more riskier based on the Variance of daily log return between EQR and SBRA ?

# 

# ## Calculate the Daily Standard Deviation for SBRA

# 16. Calculate the Standard Deviation of the daily logarithmetic return for SBRA. Use the function `.std()` with the argument `daily_log_returns_sbra`. Set it to the variable `daily_sd_sbra`. Then print the results. 

# In[133]:


daily_sd_sbra = np.std(daily_log_returns_sbra)
print(daily_sd_sbra)


# ## Calculate the Daily Standard Deviation for EQR

# 17. Calculate the Standard Deviation of the daily logarithmetic return for EQR. Use the function `.std()` with the argument `daily_log_returns_eqr`. Set it to the variable `daily_sd_eqr`. Then print the results. 

# In[139]:


daily_sd_eqr = np.std(daily_log_returns_eqr)
print(daily_sd_eqr)

# comparing each
print('SBRA: ' , daily_sd_sbra, ' EQR: ', daily_sd_eqr)


# ## Compare the Daily Standard Deviation between EQR and SBRA

# 18. Has your previous variance risk assessment changed based on the Daily Standard Deviation and why?

# 

# ## Calculate the Correlation between SBRA and EQR

# 19. Calculate the Correlation of the daily logarithmetic return between SBRA and ERQ assets. Use the function `.corrcoef()` with the arguments `daily_log_returns_sbra` and `daily_log_returns_eqr`. Set it to the variable `corr_sbra_eqr`. Then print the results. 

# In[137]:


corr_sbra_eqr = np.corrcoef(daily_log_returns_sbra, daily_log_returns_eqr)
print(corr_sbra_eqr)


# ## Interpret the Correlation between SBRA and EQR

# 20. Interpret and explain the correlation between the stocks SBRA and EQR?

# ## Final Analysis

# 21. Which stock would you invest in based on risk and profitability?
