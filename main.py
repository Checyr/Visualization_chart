# Importing libraries
import matplotlib.pyplot as plt
import pandas as pd
import plotly.graph_objects as go

data = pd.read_csv("dados_paises.csv", usecols=[0, 1, 3], skiprows=353, nrows=15, header=None)

data_array = data.to_numpy(dtype=str)

year = []
age = []

for row in data_array:
    year.append(row[1])
    age.append(float(row[2]))

year.reverse()
age.reverse()

fig, ax = plt.subplots(figsize=(15, 7))
width = 0.6

bars = ax.bar(year, age, color='tab:orange', width=width)

ax.set_ylim(10, max(age) * 1.2)


ax.set_ylabel('Idade', fontsize=18)
ax.set_xlabel('Ano', fontsize=18)
ax.set_title('Expectativa de Vida - Brasil (2001-2015)', fontsize=18)


for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width() / 2, height,
            f'{height:.1f}', ha='center', va='bottom')


# Graphic 2

data_brazil = pd.read_csv("dados_paises.csv", usecols=[0, 4, 5], skiprows=353, nrows=16, header=None)
data_germany = pd.read_csv("dados_paises.csv", usecols=[0, 4, 5], skiprows=995, nrows=16, header=None)

arr_brazil = data_brazil.to_numpy(dtype=str)
arr_germany = data_germany.to_numpy(dtype=str)

germany_adult = []
germany_infant = []
brazil_adult = []
brazil_infant = []

for row1 in arr_brazil:
    brazil_adult.append(int(row1[1]))
    brazil_infant.append(int(row1[2]))

for row2 in arr_germany:
    germany_adult.append(int(row2[1]))
    germany_infant.append(int(row2[2]))

pie_data = [brazil_infant[-1], brazil_adult[-1], germany_infant[-1], germany_adult[-1]]
pie_labels = ['Brasil Infantil', 'Brasil Adulto', 'Alemanha Infantil', 'Alemanha Adulto']

total = sum(pie_data)

fig2, ax2 = plt.subplots(figsize=(15, 7))
wedges, texts, autotexts = ax2.pie(pie_data, wedgeprops={'linewidth': 0.5, 'edgecolor': 'white'}, autopct='%1.1f%%')

for i, a in enumerate(autotexts):
    percentage = pie_data[i] / total * 100
    a.set_text(f"{percentage:.1f}% - {pie_labels[i]}")

ax2.set_title('Taxa de mortalidade adulto e infantil no Brasil e Alemanha - 2015', fontsize=16)

# Graphic 3

data_brazil2 = pd.read_csv("dados_paises.csv", usecols=[0, 17], skiprows=353, nrows=16, header=None)
data_arg = pd.read_csv("dados_paises.csv", usecols=[0, 17], skiprows=81, nrows=16, header=None)

arr_brazil = data_brazil2.to_numpy(dtype=str)
arr_arg = data_arg.to_numpy(dtype=str)

brazil_population = []
arg_population = []

for row1 in arr_brazil:
    brazil_population.append(float(row1[1]) / 1e4)  

for row2 in arr_arg:
    arg_population.append(float(row2[1]) / 1e6)  

brazil_population_formatted = ["{:,.1f}M".format(pop) for pop in brazil_population]
arg_population_formatted = ["{:.2f}M".format(pop) for pop in arg_population]

data = {
    'country': ['Brazil', 'Argentina'],
    'population': [brazil_population_formatted[0], arg_population_formatted[0]]
}

fig = go.Figure(data=go.Choropleth(
    locations=data['country'],
    locationmode='country names',
    z=[float(pop[:-1].replace(',', '')) for pop in data['population']],
    text=data['population'],
    colorscale='Reds',
    colorbar_title='Population',
))

fig.update_layout(
    title_text='População do Brasil e da Argentina em 2015',
    geo_scope='south america',
)

fig.show()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()