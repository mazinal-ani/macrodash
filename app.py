from os import name
import pandas as pd
import pandas_datareader.data as web
import plotly.express as px
import numpy as np
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import datetime

# auto test
start = datetime.datetime(2000, 1, 1)

retail_sales_total = web.DataReader('MRTSSM44000USS', 'fred', start).rename(columns={'MRTSSM44000USS': 'Retail_sales_total'})

retail_ex_auto_gas = retail_sales_total.copy()
retail_food = web.DataReader('RSAFS', 'fred', start)
retail_food_ex_auto_gas = web.DataReader('MRTSSM44W72USS', 'fred', start)
auto_gas = retail_food
auto_gas['RSAFS'] -=  retail_food_ex_auto_gas['MRTSSM44W72USS']
retail_ex_auto_gas['Retail_sales_total'] -= auto_gas['RSAFS']
retail_ex_auto_gas = retail_ex_auto_gas.rename(columns={'Retail_sales_total': 'Retail_sales_ex_auto_gas'})

cpi_total = web.DataReader('CPIAUCSL', 'fred', start).rename(columns={'CPIAUCSL': 'CPI_total'})
cpi_less_food_gas = web.DataReader('CPILFESL', 'fred', start).rename(columns={'CPILFESL': 'CPI_less_food_gas'})
cpi_food_beverages = web.DataReader('CPIFABSL', 'fred', start).rename(columns={'CPIFABSL': 'CPI_food_bev'})
cpi_housing = web.DataReader('CPIHOSSL', 'fred', start).rename(columns={'CPIHOSSL': 'CPI_housing'})
cpi_apparel = web.DataReader('CPIAPPSL', 'fred', start).rename(columns={'CPIAPPSL': 'CPI_apparel'})
cpi_transportation = web.DataReader('CPITRNSL', 'fred', start).rename(columns={'CPITRNSL': 'CPI_transportation'})
cpi_medical = web.DataReader('CPIMEDSL', 'fred', start).rename(columns={'CPIMEDSL': 'CPI_medical'})
cpi_recreation = web.DataReader('CPIRECSL', 'fred', start).rename(columns={'CPIRECSL': 'CPI_rec'})
cpi_edu_comm = web.DataReader('CPIEDUSL', 'fred', start).rename(columns={'CPIEDUSL': 'CPI_edu'})
cpi_other = web.DataReader('CPIOGSSL', 'fred', start).rename(columns={'CPIOGSSL': 'CPI_other'})

jobless_claims = web.DataReader('ICSA', 'fred', start).rename(columns={'ICSA': 'Jobless_claims'})

ism_mfg = pd.read_csv('csv_files/ism_mfg.csv', index_col=0)
ism_mfg.index = pd.to_datetime(ism_mfg.index)

non_farm_payroll = web.DataReader('PAYEMS', 'fred', start).rename(columns={'PAYEMS': 'Non_farm_payroll'})

average_hourly_earnings = web.DataReader('CES0500000003', 'fred', start).rename(columns={'CES0500000003': 'Avg_hourly_earnings'})

pmi = pd.read_csv('csv_files/pmi.csv', index_col=0)
pmi.index = pd.to_datetime(pmi.index)

credit_card_borrowings = web.DataReader('CCLACBW027SBOG', 'fred', start).rename(columns={'CCLACBW027SBOG': 'CC_borrowing'})

umich_consumer_sentiment = web.DataReader('UMCSENT', 'fred', start).rename(columns={'UMCSENT': 'UMich_sentiment'})

housing_permits = web.DataReader('PERMIT', 'fred', start).rename(columns={'PERMIT': 'Housing_permits'})

housing_starts = web.DataReader('HOUST', 'fred', start).rename(columns={'HOUST': 'Housing_starts'})

mortgage_applications = web.DataReader('M0264AUSM500NNBR', 'fred', start)

existing_home_sales = web.DataReader('EXHOSLUSM495S', 'fred', start).rename(columns={'EXHOSLUSM495S': 'Existing_home_sales'})

new_home_sales = web.DataReader('HSN1F', 'fred', start).rename(columns={'HSN1F': 'New_home_sales'})

mortgage_rate_30 = web.DataReader('MORTGAGE30US', 'fred', start).rename(columns={'MORTGAGE30US': '30Yr_mortgage_rate'})

mba_mortgage = pd.read_csv('csv_files/mba_mortgage.csv', index_col=0)
mba_mortgage.index = pd.to_datetime(mba_mortgage.index)

construction_spending = web.DataReader('TTLCONS', 'fred', start).rename(columns={'TTLCONS': 'Construction_spending'})

job_openings = web.DataReader('JTSJOL', 'fred', start).rename(columns={'JTSJOL': 'Job_openings'})

hires = web.DataReader('JTSHIL', 'fred', start).rename(columns={'JTSHIL': 'Hires'})

separation = web.DataReader('JTSTSL', 'fred', start).rename(columns={'JTSTSL': 'Separations'})

jolts = web.DataReader('JTSOSL', 'fred', start).rename(columns={'JTSOSL': 'JOLTS'})

oil_wti = web.DataReader('DCOILWTICO', 'fred', start).rename(columns={'DCOILWTICO': 'WTI_oil'})

oil_brent = web.DataReader('DCOILBRENTEU', 'fred', start).rename(columns={'DCOILBRENTEU': 'Brent_oil'})

nat_gas_us = web.DataReader('DHHNGSP', 'fred', start).rename(columns={'DHHNGSP': 'US_ng'})

nat_gas_eu = web.DataReader('PNGASEUUSDM', 'fred', start).rename(columns={'PNGASEUUSDM': 'EU_ng'})

copper = web.DataReader('PCOPPUSDM', 'fred', start).rename(columns={'PCOPPUSDM': 'Copper'})

diesel = web.DataReader('GASDESW', 'fred', start).rename(columns={'GASDESW': 'Diesel'})

hot_rolled_steel = pd.read_csv('csv_files/hot_rolled_steel.csv', index_col=0)
hot_rolled_steel.index = pd.to_datetime(hot_rolled_steel.index)

aluminum = web.DataReader('PALUMUSDM', 'fred', start).rename(columns={'PALUMUSDM': 'Aluminum'})

crude = web.DataReader('WCOILWTICO', 'fred', start) #weekly
gas = web.DataReader('WGASUSGULF', 'fred', start) #weekly
gas['WGASUSGULF'] *= 42 # 42 gallons in a barrel
diesel_crack = web.DataReader('GASDESGCW', 'fred', start) #weekly
diesel_crack['GASDESGCW'] *= 42
diesel_crack.index = diesel_crack.index - (3*pd.offsets.Day())
crack_spread = crude.join(gas.join(diesel_crack))
crack_spread['Crack_spread'] = crack_spread['WGASUSGULF'] * 2 + crack_spread['GASDESGCW'] - crack_spread['WCOILWTICO'] * 3
crack_spread = crack_spread[['Crack_spread']]

gold = pd.read_csv('csv_files/gold.csv', index_col=0)
gold.index = pd.to_datetime(gold.index)

iron_ore = web.DataReader('PIORECRUSDM', 'fred', start).rename(columns={'PIORECRUSDM': 'Iron_ore'})

lumber = web.DataReader('WPU081','fred', start).rename(columns={'WPU081': 'Lumber'})

polyethylene = pd.read_csv('csv_files/polyethylene.csv', index_col=0)
polyethylene.index = pd.to_datetime(polyethylene.index)
pvc = pd.read_csv('csv_files/pvc.csv', index_col=0)
pvc.index = pd.to_datetime(pvc.index)

polypropylene = pd.read_csv('csv_files/polypropylene.csv', index_col=0)
polypropylene.index = pd.to_datetime(polypropylene.index)
hdpe = pd.read_csv('csv_files/hdpe.csv', index_col=0)
hdpe.index = pd.to_datetime(hdpe.index)

pet = pd.read_csv('csv_files/pet.csv', index_col=0)
pet.index = pd.to_datetime(pet.index)

titanium_dioxide = pd.read_csv('csv_files/titanium_dioxide.csv', index_col=0)
titanium_dioxide.index = pd.to_datetime(titanium_dioxide.index)

naphtha = pd.read_csv('csv_files/naphtha.csv', index_col=0)
naphtha.index = pd.to_datetime(naphtha.index)

asphalt = web.DataReader('PCU3241232412', 'fred', start).rename(columns={'PCU3241232412': 'Asphalt'})

urea = pd.read_csv('csv_files/urea.csv', index_col=0)
urea.index = pd.to_datetime(urea.index)

ammonia = pd.read_csv('csv_files/ammonia.csv', index_col=0)
ammonia.index = pd.to_datetime(ammonia.index)

nitrogen_fertilizer = web.DataReader('PCU325311325311', 'fred', start).rename(columns={'PCU325311325311': 'Nitrogen_fertilizer'})
nitrogen_fertilizer.index = pd.to_datetime(nitrogen_fertilizer.index)

trucking_conditions = pd.read_csv('csv_files/trucking_conditions.csv', index_col=0)
trucking_conditions.index = pd.to_datetime(trucking_conditions.index)

container_shipping = pd.read_csv('csv_files/container_shipping.csv', index_col=0)
container_shipping.index = pd.to_datetime(container_shipping.index)

baltic_dry_index = pd.read_csv('csv_files/baltic_dry_index.csv', index_col=0)
baltic_dry_index.index = pd.to_datetime(baltic_dry_index.index)

wheat = web.DataReader('PWHEAMTUSDM', 'fred', start).rename(columns={'PWHEAMTUSDM': 'Wheat'})

pork = web.DataReader('WPU022104', 'fred', start).rename(columns={'WPU022104': 'Pork'})

beef = web.DataReader('APU0000703112', 'fred', start).rename(columns={'APU0000703112': 'Beef'})

chicken = web.DataReader('APU0000FF1101', 'fred', start).rename(columns={'APU0000FF1101': 'Chicken'})

cooking_oil = web.DataReader('PCU3112253112252', 'fred', start).rename(columns={'PCU3112253112252': 'Cooking_oil'})

flour = web.DataReader('WPU02120301', 'fred', start).rename(columns={'WPU02120301': 'Flour'})

daily_dfs = [oil_wti, oil_brent, nat_gas_us, hot_rolled_steel, gold, polyethylene, pvc, naphtha, baltic_dry_index]
for df in daily_dfs: df.index = pd.to_datetime(df.index, format='%y-%m-%d %H:%M:%S', errors='coerce')
daily = pd.concat(daily_dfs, axis=1)

weekly_dfs = [jobless_claims, credit_card_borrowings, mortgage_rate_30, mba_mortgage, diesel, crack_spread, hdpe, pet, titanium_dioxide, urea, ammonia, container_shipping]
for df in weekly_dfs: df.index = pd.to_datetime(df.index, format='%y-%m-%d %H:%M:%S', errors='coerce')
weekly = pd.concat(weekly_dfs, axis=1)
weekly = weekly.resample('W').agg('first')

monthly_dfs = [retail_sales_total, retail_ex_auto_gas, cpi_total, cpi_less_food_gas, cpi_food_beverages, cpi_housing, cpi_apparel, cpi_transportation, cpi_medical, cpi_recreation, cpi_edu_comm, cpi_other, non_farm_payroll, average_hourly_earnings, umich_consumer_sentiment, housing_permits, housing_starts, existing_home_sales, new_home_sales, construction_spending, job_openings, hires, separation, jolts, nat_gas_eu, copper, aluminum, iron_ore, lumber, asphalt, nitrogen_fertilizer, wheat, pork, beef, chicken, cooking_oil, flour, ism_mfg, pmi, trucking_conditions]
for df in monthly_dfs: df.index = pd.to_datetime(df.index, format='%y-%m-%d %H:%M:%S', errors='coerce')
monthly = pd.concat(monthly_dfs, axis=1)
monthly = monthly.resample('M').agg('first')

quarterly_dfs = [polypropylene]
for df in quarterly_dfs: df.index = pd.to_datetime(df.index, format='%y-%m-%d %H:%M:%S', errors='coerce')
quarterly = pd.concat(quarterly_dfs, axis=1)

datenow = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")

def chart_this(df, xaxis='Date', yaxis='Value', chart_title=name):
    figure=px.line(df, title=chart_title)
    figure.update_layout(
        legend_title_text='Dataset', xaxis_title=xaxis, yaxis_title=yaxis
    )
    return figure


cpi_df = monthly[['CPI_total', 'CPI_less_food_gas', 'CPI_food_bev', 'CPI_housing', 'CPI_apparel', 'CPI_transportation', 'CPI_medical', 'CPI_rec', 'CPI_edu', 'CPI_other']].dropna()

retail_df = monthly[['Retail_sales_total', 'Retail_sales_ex_auto_gas']].dropna()
retail_df = retail_df.pct_change(12)
retail_df *= 100

food_df = monthly[['Wheat', 'Pork', 'Beef', 'Chicken', 'Cooking_oil', 'Flour']].dropna()
food_df = food_df.pct_change(12)
food_df *= 100

oil_gas_df = daily[['WTI_oil', 'Brent_oil', 'US_ng']]
oil_gas_df = oil_gas_df.merge(monthly[['EU_ng']], how='left', left_index=True, right_index=True)
crack = weekly[['Crack_spread', 'Diesel']]
crack.index = crack.index.shift(1, freq='D')
oil_gas_df = oil_gas_df.merge(crack, how='left', left_index=True, right_index=True)
oil_gas_df = oil_gas_df.dropna(subset='WTI_oil')
oil_gas_df.interpolate(method ='linear', limit_direction ='forward', inplace=True)
oil_gas_df['WTI_oil'] = oil_gas_df['WTI_oil'].pct_change(21)
oil_gas_df['Brent_oil'] = oil_gas_df['Brent_oil'].pct_change(21)
oil_gas_df['US_ng'] = oil_gas_df['US_ng'].pct_change(21)
oil_gas_df['Diesel'] = oil_gas_df['Diesel'].pct_change(4)
oil_gas_df['Crack_spread'] = oil_gas_df['Crack_spread'].pct_change(4)
oil_gas_df['EU_ng'] = oil_gas_df['EU_ng'].pct_change()
oil_gas_df *= 100


transport_df = daily[['Baltic_dry_index']]
wk = weekly[['Container_shipping']]
wk.index = wk.index.shift(1, freq='D')
transport_df = transport_df.merge(wk, how='left', left_index=True, right_index=True)
transport_df.interpolate(method ='linear', limit_direction ='forward', inplace=True)
transport_df['Baltic_dry_index'] = transport_df['Baltic_dry_index'].pct_change(260)
transport_df['Container_shipping'] = transport_df['Container_shipping'].pct_change(52)
transport_df *= 100

plastics_df = daily[['Polyethylene', 'PVC']]
pet_temp = weekly[['PET', 'HDPE']]
pet_temp.index = pet_temp.index.shift(1, freq='D')
plastics_df = plastics_df.merge(pet_temp, how='left', left_index=True, right_index=True)
polyprop = quarterly[['Polypropylene']]
plastics_df = plastics_df.merge(polyprop, how='left', left_index=True, right_index=True)
plastics_df.interpolate(method='linear', limit_direction='forward', inplace=True)
plastics_df['Polyethylene'] = plastics_df['Polyethylene'].pct_change(260)
plastics_df['PVC'] = plastics_df['PVC'].pct_change(260)
plastics_df['HDPE'] = plastics_df['HDPE'].pct_change(52)
plastics_df['PET'] = plastics_df['PET'].pct_change(52)
plastics_df['Polypropylene'] = plastics_df['Polypropylene'].pct_change(4)
plastics_df *= 100



def daily_to_month_pct(df):
    return (df.groupby(pd.Grouper(freq='M')).tail(1).dropna().pct_change().dropna() * 100)

def daily_to_month_diff(df):
    return df.groupby(pd.Grouper(freq='M')).tail(1).dropna().diff().dropna()

def weekly_to_month_yoy_pct(df):
    return (df.groupby(pd.Grouper(freq='M')).tail(1).dropna().pct_change(12).dropna() * 100)


df = pd.read_excel('SourceTable.xlsx')

app = Dash(__name__)
server = app.server

dataframes = {

    'WTI_oil_price': daily[['WTI_oil']],
    'WTI_oil_dod': daily[['WTI_oil']].pct_change(),
    'WTI_oil_mom': daily_to_month_pct(daily[['WTI_oil']]),
    'WTI_oil_mom_diff': daily_to_month_diff(daily[['WTI_oil']]),

    'Brent_oil_price': daily[['Brent_oil']],
    'Brent_oil_dod': daily[['Brent_oil']].pct_change(),
    'Brent_oil_mom': daily_to_month_pct(daily[['Brent_oil']]),
    'Brent_oil_mom_diff': daily_to_month_diff(daily[['Brent_oil']]),

    'US_ng_price': daily[['US_ng']],
    'US_ng_dod': daily[['US_ng']].pct_change(),
    'US_ng_mom': daily_to_month_pct(daily[['US_ng']]),
    'US_ng_mom_diff': daily_to_month_diff(daily[['US_ng']]),

    'Hot_rolled_steel_price': daily[['Hot_rolled_steel']],
    'Hot_rolled_steel_dod': daily[['Hot_rolled_steel']].pct_change(),
    'Hot_rolled_steel_mom': daily_to_month_pct(daily[['Hot_rolled_steel']]),
    'Hot_rolled_steel_mom_diff': daily_to_month_diff(daily[['Hot_rolled_steel']]),

    'Gold_price': daily[['Gold']],
    'Gold_dod': daily[['Gold']].pct_change(),
    'Gold_mom': daily_to_month_pct(daily[['Gold']]),
    'Gold_mom_diff': daily_to_month_diff(daily[['Gold']]),

    'Polyethylene_price': daily[['Polyethylene']],
    'Polyethylene_dod': daily[['Polyethylene']].pct_change(),
    'Polyethylene_mom': daily_to_month_pct(daily[['Polyethylene']]),
    'Polyethylene_mom_diff': daily_to_month_diff(daily[['Polyethylene']]),

    'PVC_price': daily[['PVC']],
    'PVC_dod': daily[['PVC']].pct_change(),
    'PVC_mom': daily_to_month_pct(daily[['PVC']]),
    'PVC_mom_diff': daily_to_month_diff(daily[['PVC']]),

    'Naphtha_price': daily[['Naphtha']],
    'Naphtha_dod': daily[['Naphtha']].pct_change(),
    'Naphtha_mom': daily_to_month_pct(daily[['Naphtha']]),
    'Naphtha_mom_diff': daily_to_month_diff(daily[['Naphtha']]),

    'Baltic_dry_index_price': daily[['Baltic_dry_index']],
    'Baltic_dry_index_dod': daily[['Baltic_dry_index']].pct_change(),
    'Baltic_dry_index_mom': daily_to_month_pct(daily[['Baltic_dry_index']]),
    'Baltic_dry_index_mom_diff': daily_to_month_diff(daily[['Baltic_dry_index']]),

    'Jobless_claims_price': weekly[['Jobless_claims']],
    'Jobless_claims_wow': weekly[['Jobless_claims']].pct_change(),
    'Jobless_claims_mom': weekly[['Jobless_claims']].pct_change(4),
    'Jobless_claims_yoy': weekly_to_month_yoy_pct(weekly[['Jobless_claims']]),
    'Jobless_claims_mom_diff': weekly[['Jobless_claims']].diff(4),

    'CC_borrowing_price': weekly[['CC_borrowing']],
    'CC_borrowing_wow': weekly[['CC_borrowing']].pct_change(),
    'CC_borrowing_mom': weekly[['CC_borrowing']].pct_change(4),
    'CC_borrowing_yoy': weekly_to_month_yoy_pct(weekly[['CC_borrowing']]),
    'CC_borrowing_mom_diff': weekly[['CC_borrowing']].diff(4),

    '30Yr_mortgage_rate_price': weekly[['30Yr_mortgage_rate']],
    '30Yr_mortgage_rate_wow': weekly[['30Yr_mortgage_rate']].pct_change(),
    '30Yr_mortgage_rate_mom': weekly[['30Yr_mortgage_rate']].pct_change(4),
    '30Yr_mortgage_rate_yoy': weekly_to_month_yoy_pct(weekly[['30Yr_mortgage_rate']]),
    '30Yr_mortgage_rate_mom_diff': weekly[['30Yr_mortgage_rate']].diff(4),

    'MBA_mortgage_chng_price': weekly[['MBA_mortgage_chng']],
    'MBA_mortgage_chng_wow': weekly[['MBA_mortgage_chng']].pct_change(),
    'MBA_mortgage_chng_mom': weekly[['MBA_mortgage_chng']].pct_change(4),
    'MBA_mortgage_chng_yoy': weekly_to_month_yoy_pct(weekly[['MBA_mortgage_chng']]),
    'MBA_mortgage_chng_mom_diff': weekly[['MBA_mortgage_chng']].diff(4),

    'Diesel_price': weekly[['Diesel']],
    'Diesel_wow': weekly[['Diesel']].pct_change(),
    'Diesel_mom': weekly[['Diesel']].pct_change(4),
    'Diesel_yoy': weekly_to_month_yoy_pct(weekly[['Diesel']]),
    'Diesel_mom_diff': weekly[['Diesel']].diff(4),

    'Crack_spread_price': weekly[['Crack_spread']],
    'Crack_spread_wow': weekly[['Crack_spread']].pct_change(),
    'Crack_spread_mom': weekly[['Crack_spread']].pct_change(4),
    'Crack_spread_yoy': weekly_to_month_yoy_pct(weekly[['Crack_spread']]),
    'Crack_spread_mom_diff': weekly[['Crack_spread']].diff(4),

    'HDPE_price': weekly[['HDPE']],
    'HDPE_wow': weekly[['HDPE']].pct_change(),
    'HDPE_mom': weekly[['HDPE']].pct_change(4),
    'HDPE_yoy': weekly_to_month_yoy_pct(weekly[['HDPE']]),
    'HDPE_mom_diff': weekly[['HDPE']].diff(4),

    'PET_price': weekly[['PET']],
    'PET_wow': weekly[['PET']].pct_change(),
    'PET_mom': weekly[['PET']].pct_change(4),
    'PET_yoy': weekly_to_month_yoy_pct(weekly[['PET']]),
    'PET_mom_diff': weekly[['PET']].diff(4),

    'Titanium_dioxide_price': weekly[['Titanium_dioxide']],
    'Titanium_dioxide_wow': weekly[['Titanium_dioxide']].pct_change(),
    'Titanium_dioxide_mom': weekly[['Titanium_dioxide']].pct_change(4),
    'Titanium_dioxide_yoy': weekly_to_month_yoy_pct(weekly[['Titanium_dioxide']]),
    'Titanium_dioxide_mom_diff': weekly[['Titanium_dioxide']].diff(4),

    'Urea_price': weekly[['Urea']],
    'Urea_wow': weekly[['Urea']].pct_change(),
    'Urea_mom': weekly[['Urea']].pct_change(4),
    'Urea_yoy': weekly_to_month_yoy_pct(weekly[['Urea']]),
    'Urea_mom_diff': weekly[['Urea']].diff(4),

    'Ammonia_price': weekly[['Ammonia']],
    'Ammonia_wow': weekly[['Ammonia']].pct_change(),
    'Ammonia_mom': weekly[['Ammonia']].pct_change(4),
    'Ammonia_yoy': weekly_to_month_yoy_pct(weekly[['Ammonia']]),
    'Ammonia_mom_diff': weekly[['Ammonia']].diff(4),

    'Container_shipping_price': weekly[['Container_shipping']],
    'Container_shipping_wow': weekly[['Container_shipping']].pct_change(),
    'Container_shipping_mom': weekly[['Container_shipping']].pct_change(4),
    'Container_shipping_yoy': weekly_to_month_yoy_pct(weekly[['Container_shipping']]),
    'Container_shipping_mom_diff': weekly[['Container_shipping']].diff(4),

    'Retail_sales_total_price': monthly[['Retail_sales_total']],
    'Retail_sales_total_mom': monthly[['Retail_sales_total']].pct_change(),
    'Retail_sales_total_yoy': monthly[['Retail_sales_total']].pct_change(12),
    'Retail_sales_total_mom_diff': monthly[['Retail_sales_total']].diff(),

    'Retail_sales_ex_auto_gas_price': monthly[['Retail_sales_ex_auto_gas']],
    'Retail_sales_ex_auto_gas_mom': monthly[['Retail_sales_ex_auto_gas']].pct_change(),
    'Retail_sales_ex_auto_gas_yoy': monthly[['Retail_sales_ex_auto_gas']].pct_change(12),
    'Retail_sales_ex_auto_gas_mom_diff': monthly[['Retail_sales_ex_auto_gas']].diff(),

    'CPI_total_price': monthly[['CPI_total']],
    'CPI_total_mom': monthly[['CPI_total']].pct_change(),
    'CPI_total_yoy': monthly[['CPI_total']].pct_change(12),
    'CPI_total_mom_diff': monthly[['CPI_total']].diff(),

    'CPI_less_food_gas_price': monthly[['CPI_less_food_gas']],
    'CPI_less_food_gas_mom': monthly[['CPI_less_food_gas']].pct_change(),
    'CPI_less_food_gas_yoy': monthly[['CPI_less_food_gas']].pct_change(12),
    'CPI_less_food_gas_mom_diff': monthly[['CPI_less_food_gas']].diff(),

    'CPI_food_bev_price': monthly[['CPI_food_bev']],
    'CPI_food_bev_mom': monthly[['CPI_food_bev']].pct_change(),
    'CPI_food_bev_yoy': monthly[['CPI_food_bev']].pct_change(12),
    'CPI_food_bev_mom_diff': monthly[['CPI_food_bev']].diff(),

    'CPI_housing_price': monthly[['CPI_housing']],
    'CPI_housing_mom': monthly[['CPI_housing']].pct_change(),
    'CPI_housing_yoy': monthly[['CPI_housing']].pct_change(12),
    'CPI_housing_mom_diff': monthly[['CPI_housing']].diff(),

    'CPI_apparel_price': monthly[['CPI_apparel']],
    'CPI_apparel_mom': monthly[['CPI_apparel']].pct_change(),
    'CPI_apparel_yoy': monthly[['CPI_apparel']].pct_change(12),
    'CPI_apparel_mom_diff': monthly[['CPI_apparel']].diff(),

    'CPI_transportation_price': monthly[['CPI_transportation']],
    'CPI_transportation_mom': monthly[['CPI_transportation']].pct_change(),
    'CPI_transportation_yoy': monthly[['CPI_transportation']].pct_change(12),
    'CPI_transportation_mom_diff': monthly[['CPI_transportation']].diff(),

    'CPI_medical_price': monthly[['CPI_medical']],
    'CPI_medical_mom': monthly[['CPI_medical']].pct_change(),
    'CPI_medical_yoy': monthly[['CPI_medical']].pct_change(12),
    'CPI_medical_mom_diff': monthly[['CPI_medical']].diff(),

    'CPI_rec_price': monthly[['CPI_rec']],
    'CPI_rec_mom': monthly[['CPI_rec']].pct_change(),
    'CPI_rec_yoy': monthly[['CPI_rec']].pct_change(12),
    'CPI_rec_mom_diff': monthly[['CPI_rec']].diff(),

    'CPI_edu_price': monthly[['CPI_edu']],
    'CPI_edu_mom': monthly[['CPI_edu']].pct_change(),
    'CPI_edu_yoy': monthly[['CPI_edu']].pct_change(12),
    'CPI_edu_mom_diff': monthly[['CPI_edu']].diff(),

    'CPI_other_price': monthly[['CPI_other']],
    'CPI_other_mom': monthly[['CPI_other']].pct_change(),
    'CPI_other_yoy': monthly[['CPI_other']].pct_change(12),
    'CPI_other_mom_diff': monthly[['CPI_other']].diff(),

    'Non_farm_payroll_price': monthly[['Non_farm_payroll']],
    'Non_farm_payroll_mom': monthly[['Non_farm_payroll']].pct_change(),
    'Non_farm_payroll_yoy': monthly[['Non_farm_payroll']].pct_change(12),
    'Non_farm_payroll_mom_diff': monthly[['Non_farm_payroll']].diff(),

    'Avg_hourly_earnings_price': monthly[['Avg_hourly_earnings']],
    'Avg_hourly_earnings_mom': monthly[['Avg_hourly_earnings']].pct_change(),
    'Avg_hourly_earnings_yoy': monthly[['Avg_hourly_earnings']].pct_change(12),
    'Avg_hourly_earnings_mom_diff': monthly[['Avg_hourly_earnings']].diff(),

    'UMich_sentiment_price': monthly[['UMich_sentiment']],
    'UMich_sentiment_mom': monthly[['UMich_sentiment']].pct_change(),
    'UMich_sentiment_yoy': monthly[['UMich_sentiment']].pct_change(12),
    'UMich_sentiment_mom_diff': monthly[['UMich_sentiment']].diff(),

    'Housing_permits_price': monthly[['Housing_permits']],
    'Housing_permits_mom': monthly[['Housing_permits']].pct_change(),
    'Housing_permits_yoy': monthly[['Housing_permits']].pct_change(12),
    'Housing_permits_mom_diff': monthly[['Housing_permits']].diff(),

    'Housing_starts_price': monthly[['Housing_starts']],
    'Housing_starts_mom': monthly[['Housing_starts']].pct_change(),
    'Housing_starts_yoy': monthly[['Housing_starts']].pct_change(12),
    'Housing_starts_mom_diff': monthly[['Housing_starts']].diff(),

    'Existing_home_sales_price': monthly[['Existing_home_sales']],
    'Existing_home_sales_mom': monthly[['Existing_home_sales']].pct_change(),
    'Existing_home_sales_yoy': monthly[['Existing_home_sales']].pct_change(12),
    'Existing_home_sales_mom_diff': monthly[['Existing_home_sales']].diff(),

    'New_home_sales_price': monthly[['New_home_sales']],
    'New_home_sales_mom': monthly[['New_home_sales']].pct_change(),
    'New_home_sales_yoy': monthly[['New_home_sales']].pct_change(12),
    'New_home_sales_mom_diff': monthly[['New_home_sales']].diff(),

    'Construction_spending_price': monthly[['Construction_spending']],
    'Construction_spending_mom': monthly[['Construction_spending']].pct_change(),
    'Construction_spending_yoy': monthly[['Construction_spending']].pct_change(12),
    'Construction_spending_mom_diff': monthly[['Construction_spending']].diff(),

    'Job_openings_price': monthly[['Job_openings']],
    'Job_openings_mom': monthly[['Job_openings']].pct_change(),
    'Job_openings_yoy': monthly[['Job_openings']].pct_change(12),
    'Job_openings_mom_diff': monthly[['Job_openings']].diff(),

    'Hires_price': monthly[['Hires']],
    'Hires_mom': monthly[['Hires']].pct_change(),
    'Hires_yoy': monthly[['Hires']].pct_change(12),
    'Hires_mom_diff': monthly[['Hires']].diff(),

    'Separations_price': monthly[['Separations']],
    'Separations_mom': monthly[['Separations']].pct_change(),
    'Separations_yoy': monthly[['Separations']].pct_change(12),
    'Separations_mom_diff': monthly[['Separations']].diff(),

    'JOLTS_price': monthly[['JOLTS']],
    'JOLTS_mom': monthly[['JOLTS']].pct_change(),
    'JOLTS_yoy': monthly[['JOLTS']].pct_change(12),
    'JOLTS_mom_diff': monthly[['JOLTS']].diff(),

    'EU_ng_price': monthly[['EU_ng']],
    'EU_ng_mom': monthly[['EU_ng']].pct_change(),
    'EU_ng_yoy': monthly[['EU_ng']].pct_change(12),
    'EU_ng_mom_diff': monthly[['EU_ng']].diff(),

    'Copper_price': monthly[['Copper']],
    'Copper_mom': monthly[['Copper']].pct_change(),
    'Copper_yoy': monthly[['Copper']].pct_change(12),
    'Copper_mom_diff': monthly[['Copper']].diff(),

    'Aluminum_price': monthly[['Aluminum']],
    'Aluminum_mom': monthly[['Aluminum']].pct_change(),
    'Aluminum_yoy': monthly[['Aluminum']].pct_change(12),
    'Aluminum_mom_diff': monthly[['Aluminum']].diff(),

    'Iron_ore_price': monthly[['Iron_ore']],
    'Iron_ore_mom': monthly[['Iron_ore']].pct_change(),
    'Iron_ore_yoy': monthly[['Iron_ore']].pct_change(12),
    'Iron_ore_mom_diff': monthly[['Iron_ore']].diff(),

    'Lumber_price': monthly[['Lumber']],
    'Lumber_mom': monthly[['Lumber']].pct_change(),
    'Lumber_yoy': monthly[['Lumber']].pct_change(12),
    'Lumber_mom_diff': monthly[['Lumber']].diff(),

    'Asphalt_price': monthly[['Asphalt']],
    'Asphalt_mom': monthly[['Asphalt']].pct_change(),
    'Asphalt_yoy': monthly[['Asphalt']].pct_change(12),
    'Asphalt_mom_diff': monthly[['Asphalt']].diff(),

    'Nitrogen_fertilizer_price': monthly[['Nitrogen_fertilizer']],
    'Nitrogen_fertilizer_mom': monthly[['Nitrogen_fertilizer']].pct_change(),
    'Nitrogen_fertilizer_yoy': monthly[['Nitrogen_fertilizer']].pct_change(12),
    'Nitrogen_fertilizer_mom_diff': monthly[['Nitrogen_fertilizer']].diff(),

    'Wheat_price': monthly[['Wheat']],
    'Wheat_mom': monthly[['Wheat']].pct_change(),
    'Wheat_yoy': monthly[['Wheat']].pct_change(12),
    'Wheat_mom_diff': monthly[['Wheat']].diff(),

    'Pork_price': monthly[['Pork']],
    'Pork_mom': monthly[['Pork']].pct_change(),
    'Pork_yoy': monthly[['Pork']].pct_change(12),
    'Pork_mom_diff': monthly[['Pork']].diff(),

    'Beef_price': monthly[['Beef']],
    'Beef_mom': monthly[['Beef']].pct_change(),
    'Beef_yoy': monthly[['Beef']].pct_change(12),
    'Beef_mom_diff': monthly[['Beef']].diff(),

    'Chicken_price': monthly[['Chicken']],
    'Chicken_mom': monthly[['Chicken']].pct_change(),
    'Chicken_yoy': monthly[['Chicken']].pct_change(12),
    'Chicken_mom_diff': monthly[['Chicken']].diff(),

    'Cooking_oil_price': monthly[['Cooking_oil']],
    'Cooking_oil_mom': monthly[['Cooking_oil']].pct_change(),
    'Cooking_oil_yoy': monthly[['Cooking_oil']].pct_change(12),
    'Cooking_oil_mom_diff': monthly[['Cooking_oil']].diff(),

    'Flour_price': monthly[['Flour']],
    'Flour_mom': monthly[['Flour']].pct_change(),
    'Flour_yoy': monthly[['Flour']].pct_change(12),
    'Flour_mom_diff': monthly[['Flour']].diff(),

    'ISM_mfg_price': monthly[['ISM_mfg']],
    'ISM_mfg_mom': monthly[['ISM_mfg']].pct_change(),
    'ISM_mfg_yoy': monthly[['ISM_mfg']].pct_change(12),
    'ISM_mfg_mom_diff': monthly[['ISM_mfg']].diff(),

    'PMI_price': monthly[['PMI']],
    'PMI_mom': monthly[['PMI']].pct_change(),
    'PMI_yoy': monthly[['PMI']].pct_change(12),
    'PMI_mom_diff': monthly[['PMI']].diff(),

    'Trucking_conditions_price': monthly[['Trucking_conditions']],
    'Trucking_conditions_mom': monthly[['Trucking_conditions']].pct_change(),
    'Trucking_conditions_yoy': monthly[['Trucking_conditions']].pct_change(12),
    'Trucking_conditions_mom_diff': monthly[['Trucking_conditions']].diff(),

    'Polypropylene_price': quarterly[['Polypropylene']],
    'Polypropylene_qoq': quarterly[['Polypropylene']].pct_change(),
    'Polypropylene_yoy': quarterly[['Polypropylene']].pct_change(4),
    'Polypropylene_qoq_diff': quarterly[['Polypropylene']].diff(),

}

frequency_options = [
    {'label': 'Daily', 'value': 'daily'},
    {'label': 'Weekly', 'value': 'weekly'},
    {'label': 'Monthly', 'value': 'monthly'},
    {'label': 'Quarterly', 'value': 'quarterly'}
]

dataset_options = {
    'daily': [
        {'label': 'WTI Barrel', 'value': 'WTI_oil'},
        {'label': 'Brent Barrel', 'value': 'Brent_oil'},
        {'label': 'US Natural Gas', 'value': 'US_ng'},
        {'label': 'Hot Rolled Steel', 'value': 'Hot_rolled_steel'},
        {'label': 'Gold', 'value': 'Gold'},
        {'label': 'Polyethylene', 'value': 'Polyethylene'},
        {'label': 'PVC', 'value': 'PVC'},
        {'label': 'Naphtha', 'value': 'Naphtha'},
        {'label': 'Baltic Dry Index', 'value': 'Baltic_dry_index'}
    ],
    'weekly': [
        {'label': 'Jobless Claims', 'value': 'Jobless_claims'},
        {'label': 'Credit Card Borrowing', 'value': 'CC_borrowing'},
        {'label': '30-Year Mortgage Rate', 'value': '30Yr_mortgage_rate'},
        {'label': 'MBA Mortgage Index Change', 'value': 'MBA_mortgage_chng'},
        {'label': 'Diesel', 'value': 'Diesel'},
        {'label': 'Crack Spread', 'value': 'Crack_spread'},
        {'label': 'HDPE', 'value': 'HDPE'},
        {'label': 'PET', 'value': 'PET'},
        {'label': 'Titanium Dioxide', 'value': 'Titanium_dioxide'},
        {'label': 'Urea', 'value': 'Urea'},
        {'label': 'Ammonia', 'value': 'Ammonia'},
        {'label': 'Container Shipping Rates', 'value': 'Container_shipping'}
    ],
    'monthly': [
        {'label': 'Total Retail Sales', 'value': 'Retail_sales_total'},
        {'label': 'Total Retail Sales, ex Auto/Gas', 'value': 'Retail_sales_ex_auto_gas'},
        {'label': 'CPI', 'value': 'CPI_total'},
        {'label': 'Core CPI', 'value': 'CPI_less_food_gas'},
        {'label': 'CPI, Food/beverage', 'value': 'CPI_food_bev'},
        {'label': 'CPI, Housing', 'value': 'CPI_housing'},
        {'label': 'CPI, Apparel', 'value': 'CPI_apparel'},
        {'label': 'CPI, Transportation', 'value': 'CPI_transportation'},
        {'label': 'CPI, Medical', 'value': 'CPI_medical'},
        {'label': 'CPI, Recreation', 'value': 'CPI_rec'},
        {'label': 'CPI, Education and Communication', 'value': 'CPI_edu'},
        {'label': 'CPI, Other', 'value': 'CPI_other'},
        {'label': 'Non-farm Payrolls', 'value': 'Non_farm_payroll'},
        {'label': 'Average hourly Earnings', 'value': 'Avg_hourly_earnings'},
        {'label': 'UMichigan Consumer Sentiment Index', 'value': 'UMich_sentiment'},
        {'label': 'Housing Permits', 'value': 'Housing_permits'},
        {'label': 'Housing Starts', 'value': 'Housing_starts'},
        {'label': 'Existing Home Sales', 'value': 'Existing_home_sales'},
        {'label': 'New Home Sales', 'value': 'New_home_sales'},
        {'label': 'Construction Spending', 'value': 'Construction_spending'},
        {'label': 'Job Openings', 'value': 'Job_openings'},
        {'label': 'Hires', 'value': 'Hires'},
        {'label': 'Separations', 'value': 'Separations'},
        {'label': 'JOLTS', 'value': 'JOLTS'},
        {'label': 'EU Natural Gas', 'value': 'EU_ng'},
        {'label': 'Copper', 'value': 'Copper'},
        {'label': 'Aluminum', 'value': 'Aluminum'},
        {'label': 'Iron Ore', 'value': 'Iron_ore'},
        {'label': 'Lumber', 'value': 'Lumber'},
        {'label': 'Asphalt', 'value': 'Asphalt'},
        {'label': 'Nitrogen Fertilizer', 'value': 'Nitrogen_fertilizer'},
        {'label': 'Wheat', 'value': 'Wheat'},
        {'label': 'Pork', 'value': 'Pork'},
        {'label': 'Beef', 'value': 'Beef'},
        {'label': 'Chicken', 'value': 'Chicken'},
        {'label': 'Cooking Oil', 'value': 'Cooking_oil'},
        {'label': 'Flour', 'value': 'Flour'},
        {'label': 'ISM Manufacturang Index', 'value': 'ISM_mfg'},
        {'label': 'PMI Index', 'value': 'PMI'},
        {'label': 'Trucking Conditions Index', 'value': 'Trucking_conditions'}
    ],
    'quarterly' : [
        {'label': 'Polypropylene', 'value': 'Polypropylene'}
    ]
}

transformation_options = {
    'WTI_oil': [
        {'label': 'Price', 'value': 'WTI_oil_price'},
        {'label': 'DoD %', 'value': 'WTI_oil_dod'},
        {'label': 'MoM %', 'value': 'WTI_oil_mom'},
        {'label': 'MoM Diff', 'value': 'WTI_oil_mom_diff'}
    ],

    'Brent_oil': [
        {'label': 'Price', 'value': 'Brent_oil_price'},
        {'label': 'DoD %', 'value': 'Brent_oil_dod'},
        {'label': 'MoM %', 'value': 'Brent_oil_mom'},
        {'label': 'MoM Diff', 'value': 'Brent_oil_mom_diff'}
    ],

    'US_ng': [
        {'label': 'Price', 'value': 'US_ng_price'},
        {'label': 'DoD %', 'value': 'US_ng_dod'},
        {'label': 'MoM %', 'value': 'US_ng_mom'},
        {'label': 'MoM Diff', 'value': 'US_ng_mom_diff'}
    ],

    'Hot_rolled_steel': [
        {'label': 'Price', 'value': 'Hot_rolled_steel_price'},
        {'label': 'DoD %', 'value': 'Hot_rolled_steel_dod'},
        {'label': 'MoM %', 'value': 'Hot_rolled_steel_mom'},
        {'label': 'MoM Diff', 'value': 'Hot_rolled_steel_mom_diff'}
    ],

    'Gold': [
        {'label': 'Price', 'value': 'Gold_price'},
        {'label': 'DoD %', 'value': 'Gold_dod'},
        {'label': 'MoM %', 'value': 'Gold_mom'},
        {'label': 'MoM Diff', 'value': 'Gold_mom_diff'}
    ],

    'Polyethylene': [
        {'label': 'Price', 'value': 'Polyethylene_price'},
        {'label': 'DoD %', 'value': 'Polyethylene_dod'},
        {'label': 'MoM %', 'value': 'Polyethylene_mom'},
        {'label': 'MoM Diff', 'value': 'Polyethylene_mom_diff'}
    ],

    'PVC': [
        {'label': 'Price', 'value': 'PVC_price'},
        {'label': 'DoD %', 'value': 'PVC_dod'},
        {'label': 'MoM %', 'value': 'PVC_mom'},
        {'label': 'MoM Diff', 'value': 'PVC_mom_diff'}
    ],

    'Naphtha': [
        {'label': 'Price', 'value': 'Naphtha_price'},
        {'label': 'DoD %', 'value': 'Naphtha_dod'},
        {'label': 'MoM %', 'value': 'Naphtha_mom'},
        {'label': 'MoM Diff', 'value': 'Naphtha_mom_diff'}
    ],

    'Baltic_dry_index': [
        {'label': 'Price', 'value': 'Baltic_dry_index_price'},
        {'label': 'DoD %', 'value': 'Baltic_dry_index_dod'},
        {'label': 'MoM %', 'value': 'Baltic_dry_index_mom'},
        {'label': 'MoM Diff', 'value': 'Baltic_dry_index_mom_diff'}
    ],

    'Jobless_claims': [
        {'label': 'Price', 'value': 'Jobless_claims_price'},
        {'label': 'WoW %', 'value': 'Jobless_claims_wow'},
        {'label': 'MoM %', 'value': 'Jobless_claims_mom'},
        {'label': 'YoY %', 'value': 'Jobless_claims_yoy'},
        {'label': 'MoM Diff', 'value': 'Jobless_claims_mom_diff'}
    ],

    'CC_borrowing': [
        {'label': 'Price', 'value': 'CC_borrowing_price'},
        {'label': 'WoW %', 'value': 'CC_borrowing_wow'},
        {'label': 'MoM %', 'value': 'CC_borrowing_mom'},
        {'label': 'YoY %', 'value': 'CC_borrowing_yoy'},
        {'label': 'MoM Diff', 'value': 'CC_borrowing_mom_diff'}
    ],

    '30Yr_mortgage_rate': [
        {'label': 'Price', 'value': '30Yr_mortgage_rate_price'},
        {'label': 'WoW %', 'value': '30Yr_mortgage_rate_wow'},
        {'label': 'MoM %', 'value': '30Yr_mortgage_rate_mom'},
        {'label': 'YoY %', 'value': '30Yr_mortgage_rate_yoy'},
        {'label': 'MoM Diff', 'value': '30Yr_mortgage_rate_mom_diff'}
    ],

    'MBA_mortgage_chng': [
        {'label': 'Price', 'value': 'MBA_mortgage_chng_price'},
        {'label': 'WoW %', 'value': 'MBA_mortgage_chng_wow'},
        {'label': 'MoM %', 'value': 'MBA_mortgage_chng_mom'},
        {'label': 'YoY %', 'value': 'MBA_mortgage_chng_yoy'},
        {'label': 'MoM Diff', 'value': 'MBA_mortgage_chng_mom_diff'}
    ],

    'Diesel': [
        {'label': 'Price', 'value': 'Diesel_price'},
        {'label': 'WoW %', 'value': 'Diesel_wow'},
        {'label': 'MoM %', 'value': 'Diesel_mom'},
        {'label': 'YoY %', 'value': 'Diesel_yoy'},
        {'label': 'MoM Diff', 'value': 'Diesel_mom_diff'}
    ],

    'Crack_spread': [
        {'label': 'Price', 'value': 'Crack_spread_price'},
        {'label': 'WoW %', 'value': 'Crack_spread_wow'},
        {'label': 'MoM %', 'value': 'Crack_spread_mom'},
        {'label': 'YoY %', 'value': 'Crack_spread_yoy'},
        {'label': 'MoM Diff', 'value': 'Crack_spread_mom_diff'}
    ],

    'HDPE': [
        {'label': 'Price', 'value': 'HDPE_price'},
        {'label': 'WoW %', 'value': 'HDPE_wow'},
        {'label': 'MoM %', 'value': 'HDPE_mom'},
        {'label': 'YoY %', 'value': 'HDPE_yoy'},
        {'label': 'MoM Diff', 'value': 'HDPE_mom_diff'}
    ],

    'PET': [
        {'label': 'Price', 'value': 'PET_price'},
        {'label': 'WoW %', 'value': 'PET_wow'},
        {'label': 'MoM %', 'value': 'PET_mom'},
        {'label': 'YoY %', 'value': 'PET_yoy'},
        {'label': 'MoM Diff', 'value': 'PET_mom_diff'}
    ],

    'Titanium_dioxide': [
        {'label': 'Price', 'value': 'Titanium_dioxide_price'},
        {'label': 'WoW %', 'value': 'Titanium_dioxide_wow'},
        {'label': 'MoM %', 'value': 'Titanium_dioxide_mom'},
        {'label': 'YoY %', 'value': 'Titanium_dioxide_yoy'},
        {'label': 'MoM Diff', 'value': 'Titanium_dioxide_mom_diff'}
    ],

    'Urea': [
        {'label': 'Price', 'value': 'Urea_price'},
        {'label': 'WoW %', 'value': 'Urea_wow'},
        {'label': 'MoM %', 'value': 'Urea_mom'},
        {'label': 'YoY %', 'value': 'Urea_yoy'},
        {'label': 'MoM Diff', 'value': 'Urea_mom_diff'}
    ],

    'Ammonia': [
        {'label': 'Price', 'value': 'Ammonia_price'},
        {'label': 'WoW %', 'value': 'Ammonia_wow'},
        {'label': 'MoM %', 'value': 'Ammonia_mom'},
        {'label': 'YoY %', 'value': 'Ammonia_yoy'},
        {'label': 'MoM Diff', 'value': 'Ammonia_mom_diff'}
    ],

    'Container_shippings': [
        {'label': 'Price', 'value': 'Container_shipping_price'},
        {'label': 'WoW %', 'value': 'Container_shipping_wow'},
        {'label': 'MoM %', 'value': 'Container_shipping_mom'},
        {'label': 'YoY %', 'value': 'Container_shipping_yoy'},
        {'label': 'MoM Diff', 'value': 'Container_shipping_mom_diff'}
    ],

    'Retail_sales_total': [
        {'label': 'Price', 'value': 'Retail_sales_total_price'},
        {'label': 'MoM %', 'value': 'Retail_sales_total_mom'},
        {'label': 'YoY %', 'value': 'Retail_sales_total_yoy'},
        {'label': 'MoM Diff', 'value': 'Retail_sales_total_mom_diff'}
    ],

    'Retail_sales_ex_auto_gas': [
        {'label': 'Price', 'value': 'Retail_sales_ex_auto_gas_price'},
        {'label': 'MoM %', 'value': 'Retail_sales_ex_auto_gas_mom'},
        {'label': 'YoY %', 'value': 'Retail_sales_ex_auto_gas_yoy'},
        {'label': 'MoM Diff', 'value': 'Retail_sales_ex_auto_gas_mom_diff'}
    ],

    'CPI_total': [
        {'label': 'Price', 'value': 'CPI_total_price'},
        {'label': 'MoM %', 'value': 'CPI_total_mom'},
        {'label': 'YoY %', 'value': 'CPI_total_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_total_mom_diff'}
    ],

    'CPI_less_food_gas': [
        {'label': 'Price', 'value': 'CPI_less_food_gas_price'},
        {'label': 'MoM %', 'value': 'CPI_less_food_gas_mom'},
        {'label': 'YoY %', 'value': 'CPI_less_food_gas_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_less_food_gas_mom_diff'}
    ],

    'CPI_food_bev': [
        {'label': 'Price', 'value': 'CPI_food_bev_price'},
        {'label': 'MoM %', 'value': 'CPI_food_bev_mom'},
        {'label': 'YoY %', 'value': 'CPI_food_bev_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_food_bev_mom_diff'}
    ],

    'CPI_housing': [
        {'label': 'Price', 'value': 'CPI_housing_price'},
        {'label': 'MoM %', 'value': 'CPI_housing_mom'},
        {'label': 'YoY %', 'value': 'CPI_housing_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_housing_mom_diff'}
    ],
    
    'CPI_apparel': [
        {'label': 'Price', 'value': 'CPI_apparel_price'},
        {'label': 'MoM %', 'value': 'CPI_apparel_mom'},
        {'label': 'YoY %', 'value': 'CPI_apparel_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_apparel_mom_diff'}
    ],

    'CPI_transportation': [
        {'label': 'Price', 'value': 'CPI_transportation_price'},
        {'label': 'MoM %', 'value': 'CPI_transportation_mom'},
        {'label': 'YoY %', 'value': 'CPI_transportation_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_transportation_mom_diff'}
    ],

    'CPI_medical': [
        {'label': 'Price', 'value': 'CPI_medical_price'},
        {'label': 'MoM %', 'value': 'CPI_medical_mom'},
        {'label': 'YoY %', 'value': 'CPI_medical_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_medical_mom_diff'}
    ],

    'CPI_rec': [
        {'label': 'Price', 'value': 'CPI_rec_price'},
        {'label': 'MoM %', 'value': 'CPI_rec_mom'},
        {'label': 'YoY %', 'value': 'CPI_rec_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_rec_mom_diff'}
    ],

    'CPI_edu': [
        {'label': 'Price', 'value': 'CPI_edu_price'},
        {'label': 'MoM %', 'value': 'CPI_edu_mom'},
        {'label': 'YoY %', 'value': 'CPI_edu_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_edu_mom_diff'}
    ],

    'CPI_other': [
        {'label': 'Price', 'value': 'CPI_other_price'},
        {'label': 'MoM %', 'value': 'CPI_other_mom'},
        {'label': 'YoY %', 'value': 'CPI_other_yoy'},
        {'label': 'MoM Diff', 'value': 'CPI_other_mom_diff'}
    ],

    'Non_farm_payroll': [
        {'label': 'Price', 'value': 'Non_farm_payroll_price'},
        {'label': 'MoM %', 'value': 'Non_farm_payroll_mom'},
        {'label': 'YoY %', 'value': 'Non_farm_payroll_yoy'},
        {'label': 'MoM Diff', 'value': 'Non_farm_payroll_mom_diff'}
    ],

    'Avg_hourly_earnings': [
        {'label': 'Price', 'value': 'Avg_hourly_earnings_price'},
        {'label': 'MoM %', 'value': 'Avg_hourly_earnings_mom'},
        {'label': 'YoY %', 'value': 'Avg_hourly_earnings_yoy'},
        {'label': 'MoM Diff', 'value': 'Avg_hourly_earnings_mom_diff'}
    ],

    'UMich_sentiment': [
        {'label': 'Price', 'value': 'UMich_sentiment_price'},
        {'label': 'MoM %', 'value': 'UMich_sentiment_mom'},
        {'label': 'YoY %', 'value': 'UMich_sentiment_yoy'},
        {'label': 'MoM Diff', 'value': 'UMich_sentiment_mom_diff'}
    ],

    'Housing_permits': [
        {'label': 'Price', 'value': 'Housing_permits_price'},
        {'label': 'MoM %', 'value': 'Housing_permits_mom'},
        {'label': 'YoY %', 'value': 'Housing_permits_yoy'},
        {'label': 'MoM Diff', 'value': 'Housing_permits_mom_diff'}
    ],

    'Housing_starts': [
        {'label': 'Price', 'value': 'Housing_starts_price'},
        {'label': 'MoM %', 'value': 'Housing_starts_mom'},
        {'label': 'YoY %', 'value': 'Housing_starts_yoy'},
        {'label': 'MoM Diff', 'value': 'Housing_starts_mom_diff'}
    ],

    'Existing_home_sales': [
        {'label': 'Price', 'value': 'Existing_home_sales_price'},
        {'label': 'MoM %', 'value': 'Existing_home_sales_mom'},
        {'label': 'YoY %', 'value': 'Existing_home_sales_yoy'},
        {'label': 'MoM Diff', 'value': 'Existing_home_sales_mom_diff'}
    ],

    'New_home_sales': [
        {'label': 'Price', 'value': 'New_home_sales_price'},
        {'label': 'MoM %', 'value': 'New_home_sales_mom'},
        {'label': 'YoY %', 'value': 'New_home_sales_yoy'},
        {'label': 'MoM Diff', 'value': 'New_home_sales_mom_diff'}
    ],

    'Construction_spending': [
        {'label': 'Price', 'value': 'Construction_spending_price'},
        {'label': 'MoM %', 'value': 'Construction_spending_mom'},
        {'label': 'YoY %', 'value': 'Construction_spending_yoy'},
        {'label': 'MoM Diff', 'value': 'Construction_spending_mom_diff'}
    ],

    'Job_openings': [
        {'label': 'Price', 'value': 'Job_openings_price'},
        {'label': 'MoM %', 'value': 'Job_openings_mom'},
        {'label': 'YoY %', 'value': 'Job_openings_yoy'},
        {'label': 'MoM Diff', 'value': 'Job_openings_mom_diff'}
    ],

    'Hires': [
        {'label': 'Price', 'value': 'Hires_price'},
        {'label': 'MoM %', 'value': 'Hires_mom'},
        {'label': 'YoY %', 'value': 'Hires_yoy'},
        {'label': 'MoM Diff', 'value': 'Hires_mom_diff'}
    ],

    'Separations': [
        {'label': 'Price', 'value': 'Separations_price'},
        {'label': 'MoM %', 'value': 'Separations_mom'},
        {'label': 'YoY %', 'value': 'Separations_yoy'},
        {'label': 'MoM Diff', 'value': 'Separations_mom_diff'}
    ],

    'JOLTS': [
        {'label': 'Price', 'value': 'JOLTS_price'},
        {'label': 'MoM %', 'value': 'JOLTS_mom'},
        {'label': 'YoY %', 'value': 'JOLTS_yoy'},
        {'label': 'MoM Diff', 'value': 'JOLTS_mom_diff'}
    ],

    'EU_ng': [
        {'label': 'Price', 'value': 'EU_ng_price'},
        {'label': 'MoM %', 'value': 'EU_ng_mom'},
        {'label': 'YoY %', 'value': 'EU_ng_yoy'},
        {'label': 'MoM Diff', 'value': 'EU_ng_mom_diff'}
    ],

    'Copper': [
        {'label': 'Price', 'value': 'Copper_price'},
        {'label': 'MoM %', 'value': 'Copper_mom'},
        {'label': 'YoY %', 'value': 'Copper_yoy'},
        {'label': 'MoM Diff', 'value': 'Copper_mom_diff'}
    ],

    'Aluminum': [
        {'label': 'Price', 'value': 'Aluminum_price'},
        {'label': 'MoM %', 'value': 'Aluminum_mom'},
        {'label': 'YoY %', 'value': 'Aluminum_yoy'},
        {'label': 'MoM Diff', 'value': 'Aluminum_mom_diff'}
    ],

    'Iron_ore': [
        {'label': 'Price', 'value': 'Iron_ore_price'},
        {'label': 'MoM %', 'value': 'Iron_ore_mom'},
        {'label': 'YoY %', 'value': 'Iron_ore_yoy'},
        {'label': 'MoM Diff', 'value': 'Iron_ore_mom_diff'}
    ],

    'Lumber': [
        {'label': 'Price', 'value': 'Lumber_price'},
        {'label': 'MoM %', 'value': 'Lumber_mom'},
        {'label': 'YoY %', 'value': 'Lumber_yoy'},
        {'label': 'MoM Diff', 'value': 'Lumber_mom_diff'}
    ],

    'Asphalt': [
        {'label': 'Price', 'value': 'Asphalt_price'},
        {'label': 'MoM %', 'value': 'Asphalt_mom'},
        {'label': 'YoY %', 'value': 'Asphalt_yoy'},
        {'label': 'MoM Diff', 'value': 'Asphalt_mom_diff'}
    ],

    'Nitrogen_fertilizer': [
        {'label': 'Price', 'value': 'Nitrogen_fertilizer_price'},
        {'label': 'MoM %', 'value': 'Nitrogen_fertilizer_mom'},
        {'label': 'YoY %', 'value': 'Nitrogen_fertilizer_yoy'},
        {'label': 'MoM Diff', 'value': 'Nitrogen_fertilizer_mom_diff'}
    ],

    'Wheat': [
        {'label': 'Price', 'value': 'Wheat_price'},
        {'label': 'MoM %', 'value': 'Wheat_mom'},
        {'label': 'YoY %', 'value': 'Wheat_yoy'},
        {'label': 'MoM Diff', 'value': 'Wheat_mom_diff'}
    ],

    'Pork': [
        {'label': 'Price', 'value': 'Pork_price'},
        {'label': 'MoM %', 'value': 'Pork_mom'},
        {'label': 'YoY %', 'value': 'Pork_yoy'},
        {'label': 'MoM Diff', 'value': 'Pork_mom_diff'}
    ],

    'Beef': [
        {'label': 'Price', 'value': 'Beef_price'},
        {'label': 'MoM %', 'value': 'Beef_mom'},
        {'label': 'YoY %', 'value': 'Beef_yoy'},
        {'label': 'MoM Diff', 'value': 'Beef_mom_diff'}
    ],

    'Chicken': [
        {'label': 'Price', 'value': 'Chicken_price'},
        {'label': 'MoM %', 'value': 'Chicken_mom'},
        {'label': 'YoY %', 'value': 'Chicken_yoy'},
        {'label': 'MoM Diff', 'value': 'Chicken_mom_diff'}
    ],

    'Cooking_oil': [
        {'label': 'Price', 'value': 'Cooking_oil_price'},
        {'label': 'MoM %', 'value': 'Cooking_oil_mom'},
        {'label': 'YoY %', 'value': 'Cooking_oil_yoy'},
        {'label': 'MoM Diff', 'value': 'Cooking_oil_mom_diff'}
    ],

    'Flour': [
        {'label': 'Price', 'value': 'Flour_price'},
        {'label': 'MoM %', 'value': 'Flour_mom'},
        {'label': 'YoY %', 'value': 'Flour_yoy'},
        {'label': 'MoM Diff', 'value': 'Flour_mom_diff'}
    ],

    'ISM_mfg': [
        {'label': 'Price', 'value': 'ISM_mfg_price'},
        {'label': 'MoM %', 'value': 'ISM_mfg_mom'},
        {'label': 'YoY %', 'value': 'ISM_mfg_yoy'},
        {'label': 'MoM Diff', 'value': 'ISM_mfg_mom_diff'}
    ],

    'PMI': [
        {'label': 'Price', 'value': 'PMI_price'},
        {'label': 'MoM %', 'value': 'PMI_mom'},
        {'label': 'YoY %', 'value': 'PMI_yoy'},
        {'label': 'MoM Diff', 'value': 'PMI_mom_diff'}
    ],

    'Trucking_conditions': [
        {'label': 'Price', 'value': 'Trucking_conditions_price'},
        {'label': 'MoM %', 'value': 'Trucking_conditions_mom'},
        {'label': 'YoY %', 'value': 'Trucking_conditions_yoy'},
        {'label': 'MoM Diff', 'value': 'Trucking_conditions_mom_diff'}
    ],

    'Polypropylene': [
        {'label': 'Price', 'value': 'Polypropylene_price'},
        {'label': 'QoQ %', 'value': 'Polypropylene_qoq'},
        {'label': 'YoY %', 'value': 'Polypropylene_yoy'},
        {'label': 'QoQ Diff', 'value': 'Polypropylene_qoq_diff'}
    ]
}

app.layout = html.Div(
    children=[
        html.H1(
            children="Nowcasting Data Dashboard",
            style={
            'textAlign': 'center',
            "fontSize": "40px",
            'color': 'darkslategray'
        }),
        html.H3(
            children="Last Updated: "+datenow,
            style={
            'textAlign': 'center',
            "fontSize": "25px",
            'color': 'darkslategray'
            }
        ),
        html.Hr(style={'borderWidth': "0.4vh", "width": "100%", "color": "#FEC700"}),
        html.H2(
            children="Charts",
            style={
            'textAlign': 'center',
            "fontSize": "30px",
            'color': 'darkslategray',
            'text-decoration': 'underline'
        }),
        html.Div([
            html.Label('Frequency'),
            dcc.Dropdown(
                id='frequency-dropdown',
                options=frequency_options,
                value='daily'
            ),
            html.Br(),
            html.Label('Dataset'),
            dcc.Dropdown(
                id='dataset-dropdown',
                options=dataset_options,
                value='dataset1'
            ),
            html.Br(),
            html.Label('Transformation'),
            dcc.Dropdown(
                id='transformation-dropdown',
                value='transformation1'
            ),
            html.Br(),
            html.Div(id='chart-container')
        ]),
        html.Hr(style={'borderWidth': "0.4vh", "width": "100%", "color": "#FEC700"}),
        html.Div(children=[
            dcc.Graph(id = "cpi", figure=chart_this(cpi_df.pct_change(12), yaxis='% Change, YoY', chart_title='Inflation Indices'), style={'width': '100%', 'height': '100%'}),
            dcc.Graph(id = "retail", figure=chart_this(retail_df, yaxis='% Change, YoY', chart_title='Retail Sales'), style={'width': '100%', 'height': '100%'})
        ], style={'display': 'flex', 'justify-content': 'center'}),
        html.Div(children=[
            dcc.Graph(id = "food", figure=chart_this(food_df, yaxis='% Change, YoY', chart_title='Food Prices, US Cities Average'), style={'width': '100%', 'height': '100%'}),
            dcc.Graph(id = "energy", figure=chart_this(oil_gas_df, yaxis='% Change, MoM', chart_title='Energy Prices'), style={'width': '100%', 'height': '100%'})
        ], style={'display': 'flex', 'justify-content': 'center'}),
        html.Div(children=[
            dcc.Graph(id = "shipping", figure=chart_this(transport_df, yaxis='% Change, YoY', chart_title='Shipping'), style={'width': '100%', 'height': '100%'}),
            dcc.Graph(id = "plastics", figure=chart_this(plastics_df, yaxis='% Change, YoY', chart_title='Plastics Indices and Prices'), style={'width': '100%', 'height': '100%'})
        ], style={'display': 'flex', 'justify-content': 'center'}),
        html.Hr(style={'borderWidth': "0.4vh", "width": "100%", "color": "#FEC700"}),
        html.H2(
            children="Mapping Table",
            style={
            'textAlign': 'center',
            "fontSize": "30px",
            'color': 'darkslategray',
            'text-decoration': 'underline'
        }),
        html.Div(
            children=[
                dash_table.DataTable(
                    style_data={'whiteSpace': 'normal', 'height': 'auto'},
                    id='table',
                    columns=[{"name": col, "id": col} for col in df.columns],
                    data=df.to_dict('records'),
                )
            ],
            style={'display': 'flex', 'justify-content': 'center'}
        )
    ]
)

@app.callback(
    Output('dataset-dropdown', 'options'),
    [Input('frequency-dropdown', 'value')]
)
def update_dataset_options(frequency):
    return dataset_options.get(frequency, [])

@app.callback(
    Output('transformation-dropdown', 'options'),
    [Input('dataset-dropdown', 'value')]
)
def update_transformation_options(dataset):
    return transformation_options.get(dataset, [])

@app.callback(
    Output('chart-container', 'children'),
    [Input('transformation-dropdown', 'value')]
)
def update_chart(dataset):
    df = dataframes.get(dataset)
    if dataset == 'transformation1':
        return 'Please select a dataset and transformation to begin'
    elif 'price' in dataset:
        name_holder = dataset.replace('_',' ')[:-6].upper()
        if 'CPI' in dataset:
            if dataset in ['CPI_rec', 'CPI_edu']:

                return dcc.Graph(figure=chart_this(df, yaxis='Index Dec 1997=100, Seasonally Adjusted', chart_title=name_holder))
            else:
                return dcc.Graph(figure=chart_this(df, yaxis='Index 1982-1984=100, Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['WTI_oil_price', 'Brent_oil_price', 'Crack_spread_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Barrel', chart_title=name_holder))
        elif dataset in ['US_ng_price', 'EU_ng_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Million BTUs', chart_title=name_holder))
        elif dataset in ['Diesel_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Gallon', chart_title=name_holder))
        elif dataset in ['Gold_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Troy Ounce', chart_title=name_holder))
        elif dataset in ['Hot_rolled_steel_price', 'PET_price', 'Titanium_dioxide_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='¥CNY per Metric Tonne', chart_title=name_holder))
        elif dataset in ['Polyethylene_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='¥5 CNY per Point, 5 Metric Tonne Futures', chart_title=name_holder))
        elif dataset in ['PVC_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='¥5 CNY per Point, 5 Metric Tonne Futures', chart_title=name_holder))
        elif dataset in ['Naphtha_price', 'Polypropylene_price', 'HDPE_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Metric Tonne', chart_title=name_holder))
        elif dataset in ['Baltic_dry_index_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index 1000 = January 4 1985', chart_title=name_holder))
        elif 'Retail' in dataset:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD, Millions, Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Jobless_claims_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Number of Claims', chart_title=name_holder))
        elif dataset in ['ISM_mfg_price', 'PMI_price', 'Trucking_conditions_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index', chart_title=name_holder))
        elif dataset in ['Non_farm_payroll_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Thousands of Persons', chart_title=name_holder))
        elif dataset in ['Avg_hourly_earnings_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Hour, Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['CC_borrowing_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD, Billions, Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['UMich_sentiment_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index 1966, Q1 = 100, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['New_home_sales_price', 'Housing_permits_price', 'Housing_starts_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Thousands of Units, Seasonally Adjusted Annual Rate', chart_title=name_holder))
        elif dataset in ['Existing_home_sales_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Number of Units, Seasonally Adjusted Annual Rate', chart_title=name_holder))
        elif dataset in ['30Yr_mortgage_rate_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Percent, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['MBA_mortgage_chng_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='% Change, WoW', chart_title=name_holder))
        elif dataset in ['TTLCONS_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD, Millions, Seasonally Adjusted Annual Rate', chart_title=name_holder))
        elif dataset in ['Job_openings_price', 'Hires_price', 'Separations_price', 'JOLTS_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Level in Thousands, Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Copper_price', 'Aluminum_price', 'Iron_ore_price', 'Wheat_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Metric Tonne, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Lumber_price', 'Pork_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index 1982 = 100, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Asphalt_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index Dec 1984 = 100, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Urea_price', 'Ammonia_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Short Ton', chart_title=name_holder))
        elif dataset in ['Nitrogen_fertilizer_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index Dec 1979 = 100, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Container_shipping_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per 40ft Box', chart_title=name_holder))
        elif dataset in ['Beef_price', 'Chicken_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='$USD per Pound, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Cooking_oil_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index Dec 1981 = 100, Not Seasonally Adjusted', chart_title=name_holder))
        elif dataset in ['Flour_price']:
            return dcc.Graph(figure=chart_this(df, yaxis='Index Jun 1983 = 100, Not Seasonally Adjusted', chart_title=name_holder))
    elif 'mom_diff' in dataset:
        name_holder = dataset.replace('_',' ')[:-9].upper()
        return dcc.Graph(figure=chart_this(df, yaxis='Month over Month Change', chart_title=name_holder))
    elif 'qoq_diff' in dataset:
        name_holder = dataset.replace('_',' ')[:-9].upper()
        return dcc.Graph(figure=chart_this(df, yaxis='Quarter over Quarter Change', chart_title=name_holder))
    elif 'dod' in dataset:
        name_holder = dataset.replace('_',' ')[:-4].upper()
        return dcc.Graph(figure=chart_this(df, yaxis='% Change, DoD', chart_title=name_holder))
    elif 'wow' in dataset:
        name_holder = dataset.replace('_',' ')[:-4].upper()
        return dcc.Graph(figure=chart_this(df, yaxis='% Change, WoW', chart_title=name_holder))
    elif 'mom' in dataset:
        name_holder = dataset.replace('_',' ')[:-4].upper()
        return dcc.Graph(figure=chart_this(df, yaxis='% Change, MoM', chart_title=name_holder))
    elif 'qoq' in dataset:
        name_holder = dataset.replace('_',' ')[:-4].upper()
        return dcc.Graph(figure=chart_this(df, yaxis='% Change, QoQ', chart_title=name_holder))
    else:
        return dcc.Graph(figure=chart_this(df))
    

if __name__ == "__main__":
    app.run_server(debug=True)