import pandas as pd
import pandas_datareader.data as web
import plotly.express as px
import numpy as np
from dash import Dash, dcc, html, dash_table
from dash.dependencies import Input, Output
import datetime

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
cpi_total = cpi_total.pct_change(12)
cpi_total *= 100
cpi_less_food_gas = web.DataReader('CPILFESL', 'fred', start).rename(columns={'CPILFESL': 'CPI_less_food_gas'})
cpi_less_food_gas = cpi_less_food_gas.pct_change(12)
cpi_less_food_gas *= 100
cpi_food_beverages = web.DataReader('CPIFABSL', 'fred', start).rename(columns={'CPIFABSL': 'CPI_food_bev'})
cpi_food_beverages = cpi_food_beverages.pct_change(12)
cpi_food_beverages *= 100
cpi_housing = web.DataReader('CPIHOSSL', 'fred', start).rename(columns={'CPIHOSSL': 'CPI_housing'})
cpi_housing = cpi_housing.pct_change(12)
cpi_housing *= 100
cpi_apparel = web.DataReader('CPIAPPSL', 'fred', start).rename(columns={'CPIAPPSL': 'CPI_apparel'})
cpi_apparel = cpi_apparel.pct_change(12)
cpi_apparel *= 100
cpi_transportation = web.DataReader('CPITRNSL', 'fred', start).rename(columns={'CPITRNSL': 'CPI_transportation'})
cpi_transportation = cpi_transportation.pct_change(12)
cpi_transportation *= 100
cpi_medical = web.DataReader('CPIMEDSL', 'fred', start).rename(columns={'CPIMEDSL': 'CPI_medical'})
cpi_medical = cpi_medical.pct_change(12)
cpi_medical *= 100
cpi_recreation = web.DataReader('CPIRECSL', 'fred', start).rename(columns={'CPIRECSL': 'CPI_rec'})
cpi_recreation = cpi_recreation.pct_change(12)
cpi_recreation *= 100
cpi_edu_comm = web.DataReader('CPIEDUSL', 'fred', start).rename(columns={'CPIEDUSL': 'CPI_edu'})
cpi_edu_comm = cpi_edu_comm.pct_change(12)
cpi_edu_comm *= 100
cpi_other = web.DataReader('CPIOGSSL', 'fred', start).rename(columns={'CPIOGSSL': 'CPI_other'})
cpi_other = cpi_other.pct_change(12)
cpi_other *= 100

jobless_claims = web.DataReader('ICSA', 'fred', start).rename(columns={'ICSA': 'Jobless_claims'})

ism_mfg = pd.read_csv('H:/MAl-Ani/csv_files/ism_mfg.csv', index_col=0)
ism_mfg.index = pd.to_datetime(ism_mfg.index)

non_farm_payroll = web.DataReader('PAYEMS', 'fred', start).rename(columns={'PAYEMS': 'Non_farm_payroll'})

average_hourly_earnings = web.DataReader('CES0500000003', 'fred', start).rename(columns={'CES0500000003': 'Avg_hourly_earnings'})

pmi = pd.read_csv('H:/MAl-Ani/csv_files/pmi.csv', index_col=0)
pmi.index = pd.to_datetime(pmi.index)

credit_card_borrowings = web.DataReader('CCLACBW027SBOG', 'fred', start).rename(columns={'CCLACBW027SBOG': 'CC_borrowing'})

umich_consumer_sentiment = web.DataReader('UMCSENT', 'fred', start).rename(columns={'UMCSENT': 'UMich_sentiment'})

housing_permits = web.DataReader('PERMIT', 'fred', start).rename(columns={'PERMIT': 'Housing_permits'})

housing_starts = web.DataReader('HOUST', 'fred', start).rename(columns={'HOUST': 'Housing_starts'})

mortgage_applications = web.DataReader('M0264AUSM500NNBR', 'fred', start)

existing_home_sales = web.DataReader('EXHOSLUSM495S', 'fred', start).rename(columns={'EXHOSLUSM495S': 'Existing_home_sales'})

new_home_sales = web.DataReader('HSN1F', 'fred', start).rename(columns={'HSN1F': 'New_home_sales'})

mortgage_rate_30 = web.DataReader('MORTGAGE30US', 'fred', start).rename(columns={'MORTGAGE30US': '30Yr_mortgage_rate'})

mba_mortgage = pd.read_csv('H:/MAl-Ani/csv_files/mba_mortgage.csv', index_col=0)
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

hot_rolled_steel = pd.read_csv('H:/MAl-Ani/csv_files/hot_rolled_steel.csv', index_col=0)
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

gold = pd.read_csv('H:/MAl-Ani/csv_files/gold.csv', index_col=0)
gold.index = pd.to_datetime(gold.index)

iron_ore = web.DataReader('PIORECRUSDM', 'fred', start).rename(columns={'PIORECRUSDM': 'Iron_ore'})

lumber = web.DataReader('WPU081','fred', start).rename(columns={'WPU081': 'Lumber'})

polyethylene = pd.read_csv('H:/MAl-Ani/csv_files/polyethylene.csv', index_col=0)
polyethylene.index = pd.to_datetime(polyethylene.index)
pvc = pd.read_csv('H:/MAl-Ani/csv_files/pvc.csv', index_col=0)
pvc.index = pd.to_datetime(pvc.index)

polypropylene = pd.read_csv('H:/MAl-Ani/csv_files/polypropylene.csv', index_col=0)
polypropylene.index = pd.to_datetime(polypropylene.index)
hdpe = pd.read_csv('H:/MAl-Ani/csv_files/hdpe.csv', index_col=0)
hdpe.index = pd.to_datetime(hdpe.index)

pet = pd.read_csv('H:/MAl-Ani/csv_files/pet.csv', index_col=0)
pet.index = pd.to_datetime(pet.index)

titanium_dioxide = pd.read_csv('H:/MAl-Ani/csv_files/titanium_dioxide.csv', index_col=0)
titanium_dioxide.index = pd.to_datetime(titanium_dioxide.index)

naphtha = pd.read_csv('H:/MAl-Ani/csv_files/naphtha.csv', index_col=0)
naphtha.index = pd.to_datetime(naphtha.index)

asphalt = web.DataReader('PCU3241232412', 'fred', start).rename(columns={'PCU3241232412': 'Asphalt'})

urea = pd.read_csv('H:/MAl-Ani/csv_files/urea.csv', index_col=0)
urea.index = pd.to_datetime(urea.index)

ammonia = pd.read_csv('H:/MAl-Ani/csv_files/ammonia.csv', index_col=0)
ammonia.index = pd.to_datetime(ammonia.index)

nitrogen_fertilizer = web.DataReader('PCU325311325311', 'fred', start).rename(columns={'PCU325311325311': 'Nitrogen_fertilizer'})
nitrogen_fertilizer.index = pd.to_datetime(nitrogen_fertilizer.index)

trucking_conditions = pd.read_csv('H:/MAl-Ani/csv_files/trucking_conditions.csv', index_col=0)
trucking_conditions.index = pd.to_datetime(trucking_conditions.index)

container_shipping = pd.read_csv('H:/MAl-Ani/csv_files/container_shipping.csv', index_col=0)
container_shipping.index = pd.to_datetime(container_shipping.index)

baltic_dry_index = pd.read_csv('H:/MAl-Ani/csv_files/baltic_dry_index.csv', index_col=0)
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

def chart_this(df, name, xaxis='Date', yaxis='Value'):
    figure=px.line(df, title=name)
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


df = pd.read_excel('H:\MAl-Ani\SourceTable.xlsx')

app = Dash(__name__)
server = app.server

dataframes = {
    'WTI_oil': daily[['WTI_oil']],
    'Brent_oil': daily[['Brent_oil']],
    'US_ng': daily[['US_ng']],
    'Hot_rolled_steel': daily[['Hot_rolled_steel']],
    'Gold': daily[['Gold']],
    'Polyethylene': daily[['Polyethylene']],
    'PVC': daily[['PVC']],
    'Naphtha': daily[['Naphtha']],
    'Baltic_dry_index': daily[['Baltic_dry_index']],
    'Jobless_claims': weekly[['Jobless_claims']],
    'CC_borrowing': weekly[['CC_borrowing']],
    '30Yr_mortgage_rate': weekly[['30Yr_mortgage_rate']],
    'MBA_mortgage_chng': weekly[['MBA_mortgage_chng']],
    'Diesel': weekly[['Diesel']],
    'Crack_spread': weekly[['Crack_spread']],
    'HDPE': weekly[['HDPE']],
    'PET': weekly[['PET']],
    'Titanium_dioxide': weekly[['Titanium_dioxide']],
    'Urea': weekly[['Urea']],
    'Ammonia': weekly[['Ammonia']],
    'Container_shipping': weekly[['Container_shipping']],
    'Retail_sales_total': monthly[['Retail_sales_total']],
    'Retail_sales_ex_auto_gas': monthly[['Retail_sales_ex_auto_gas']],
    'CPI_total': monthly[['CPI_total']],
    'CPI_less_food_gas': monthly[['CPI_less_food_gas']],
    'CPI_food_bev': monthly[['CPI_food_bev']],
    'CPI_housing': monthly[['CPI_housing']],
    'CPI_apparel': monthly[['CPI_apparel']],
    'CPI_transportation': monthly[['CPI_transportation']],
    'CPI_medical': monthly[['CPI_medical']],
    'CPI_rec': monthly[['CPI_rec']],
    'CPI_edu': monthly[['CPI_edu']],
    'CPI_other': monthly[['CPI_other']],
    'Non_farm_payroll': monthly[['Non_farm_payroll']],
    'Avg_hourly_earnings': monthly[['Avg_hourly_earnings']],
    'UMich_sentiment': monthly[['UMich_sentiment']],
    'Housing_permits': monthly[['Housing_permits']],
    'Housing_starts': monthly[['Housing_starts']],
    'Existing_home_sales': monthly[['Existing_home_sales']],
    'New_home_sales': monthly[['New_home_sales']],
    'Construction_spending': monthly[['Construction_spending']],
    'Job_openings': monthly[['Job_openings']],
    'Hires': monthly[['Hires']],
    'Separations': monthly[['Separations']],
    'JOLTS': monthly[['JOLTS']],
    'EU_ng': monthly[['EU_ng']],
    'Copper': monthly[['Copper']],
    'Aluminum': monthly[['Aluminum']],
    'Iron_ore': monthly[['Iron_ore']],
    'Lumber': monthly[['Lumber']],
    'Asphalt': monthly[['Asphalt']],
    'Nitrogen_fertilizer': monthly[['Nitrogen_fertilizer']],
    'Wheat': monthly[['Wheat']],
    'Pork': monthly[['Pork']],
    'Beef': monthly[['Beef']],
    'Chicken': monthly[['Chicken']],
    'Cooking_oil': monthly[['Cooking_oil']],
    'Flour': monthly[['Flour']],
    'ISM_mfg': monthly[['ISM_mfg']],
    'PMI': monthly[['PMI']],
    'Trucking_conditions': monthly[['Trucking_conditions']],
    'Polypropylene': quarterly[['Polypropylene']]
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
                value='dataset1'
            ),
            html.Br(),
            html.Div(id='chart-container')
        ]),
        html.Div(children=[
            dcc.Graph(id = "cpi", figure=chart_this(cpi_df, 'CPI', yaxis='% Change, YoY'), style={'width': '100%', 'height': '100%'}),
            dcc.Graph(id = "retail", figure=chart_this(retail_df, 'Retail Sales', yaxis='% Change, YoY'), style={'width': '100%', 'height': '100%'})
        ], style={'display': 'flex', 'justify-content': 'center'}),
        html.Div(children=[
            dcc.Graph(id = "food", figure=chart_this(food_df, 'Food Prices, US Cities Average', yaxis='% Change, YoY'), style={'width': '100%', 'height': '100%'}),
            dcc.Graph(id = "energy", figure=chart_this(oil_gas_df, 'Energy Prices', yaxis='% Change, MoM'), style={'width': '100%', 'height': '100%'})
        ], style={'display': 'flex', 'justify-content': 'center'}),
        html.Div(children=[
            dcc.Graph(id = "shipping", figure=chart_this(transport_df, 'Shipping', yaxis='% Change, YoY'), style={'width': '100%', 'height': '100%'}),
            dcc.Graph(id = "plastics", figure=chart_this(plastics_df, 'Plastics Indices and Prices', yaxis='% Change, YoY'), style={'width': '100%', 'height': '100%'})
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
    Output('chart-container', 'children'),
    [Input('dataset-dropdown', 'value')]
)
def update_chart(dataset):
    df = dataframes.get(dataset)
    if 'CPI' in dataset:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='% Change, YoY'))
    elif dataset == 'dataset1':
        return 'Please select a dataset'
    elif dataset in ['WTI_oil', 'Brent_oil', 'Crack_spread']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Barrel'))
    elif dataset in ['US_ng', 'EU_ng']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Million BTUs'))
    elif dataset in ['Diesel']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Gallon'))
    elif dataset in ['Gold']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Troy Ounce'))
    elif dataset in ['Hot_rolled_steel', 'PET', 'Titanium_dioxide']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='¥CNY per Metric Tonne'))
    elif dataset in ['Polyethylene']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='¥5 CNY per Point, 5 Metric Tonne Futures'))
    elif dataset in ['PVC']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='¥5 CNY per Point, 5 Metric Tonne Futures'))
    elif dataset in ['Naphtha', 'Polypropylene', 'HDPE']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Metric Tonne'))
    elif dataset in ['Baltic_dry_index']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index 1000 = January 4 1985'))
    elif 'Retail' in dataset:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD, Millions, Seasonally Adjusted'))
    elif dataset in ['Jobless_claims']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Number of Claims'))
    elif dataset in ['ISM_mfg', 'PMI', 'Trucking_conditions']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index'))
    elif dataset in ['Non_farm_payroll']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Thousands of Persons'))
    elif dataset in ['Avg_hourly_earnings']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Hour, Seasonally Adjusted'))
    elif dataset in ['CC_borrowing']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD, Billions, Seasonally Adjusted'))
    elif dataset in ['UMich_sentiment']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index 1966, Q1 = 100, Not Seasonally Adjusted'))
    elif dataset in ['New_home_sales', 'Housing_permits', 'Housing_starts']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Thousands of Units, Seasonally Adjusted Annual Rate'))
    elif dataset in ['Existing_home_sales']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Number of Units, Seasonally Adjusted Annual Rate'))
    elif dataset in ['30Yr_mortgage_rate']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Percent, Not Seasonally Adjusted'))
    elif dataset in ['MBA_mortgage_chng']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='% Change, WoW'))
    elif dataset in ['TTLCONS']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD, Millions, Seasonally Adjusted Annual Rate'))
    elif dataset in ['JTSJOL', 'JTSHIL', 'JTSTSL', 'JTSOSL']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Level in Thousands, Seasonally Adjusted'))
    elif dataset in ['Copper', 'Aluminum', 'Iron_ore', 'Wheat']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Metric Tonne, Not Seasonally Adjusted'))
    elif dataset in ['Lumber', 'Pork']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index 1982 = 100, Not Seasonally Adjusted'))
    elif dataset in ['Asphalt']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index Dec 1984 = 100, Not Seasonally Adjusted'))
    elif dataset in ['Urea', 'Ammonia']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Short Ton'))
    elif dataset in ['Nitrogen_fertilizer']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index Dec 1979 = 100, Not Seasonally Adjusted'))
    elif dataset in ['Container_shipping']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per 40ft Box'))
    elif dataset in ['Beef', 'Chicken']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='$USD per Pound, Not Seasonally Adjusted'))
    elif dataset in ['Cooking_oil']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index Dec 1981 = 100, Not Seasonally Adjusted'))
    elif dataset in ['Flour']:
        return dcc.Graph(figure=chart_this(df, dataset, yaxis='Index Jun 1983 = 100, Not Seasonally Adjusted'))
    else:
        return dcc.Graph(figure=chart_this(df, dataset))

if __name__ == "__main__":
    app.run_server(debug=True)