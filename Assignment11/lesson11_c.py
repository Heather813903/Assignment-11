import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px

# Load gapminder data
gapminder = px.data.gapminder()

# Extract unique country names
countries = gapminder['country'].drop_duplicates()

# Initialize Dash app
app = dash.Dash(__name__)

# Define layout
app.layout = html.Div([
    dcc.Dropdown(
        id='country-dropdown',
        options=[{'label': country, 'value': country} for country in countries],
        value='Canada'  # Initial value
    ),
    dcc.Graph(id='gdp-growth')
])

# Define callback
@app.callback(
    Output('gdp-growth', 'figure'),
    Input('country-dropdown', 'value')
)
def update_graph(selected_country):
    filtered_df = gapminder[gapminder['country'] == selected_country]
    fig = px.line(
        filtered_df,
        x='year',
        y='gdpPercap',
        title=f'GDP Per Capita Over Time for {selected_country}'
    )
    return fig

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
