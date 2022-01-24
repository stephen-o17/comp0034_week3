from pathlib import Path
import pandas as pd
import plotly.express as px
import dash
from dash import html
from dash import dcc
import prepare_data


app = dash.Dash(__name__)

app.layout = html.Div(children=[

    html.H1('Lollapalooza Experience'),

    html.H2("Where did she go during the festival?")

])

file_path = Path(__file__).parent.joinpath('data', 'purchase_data.csv')
df_purchase = pd.read_csv(file_path)
# #-----BAR CHART-----#
# purchase_df = prepare_data.prepare_purchase_data(df_purchase)
# fig_bar = px.bar(purchase_df, x="spend", y="date", color="place", title="Purchases by Place", template="plotly_dark")
#
# #Changing defaults
# px.defaults.width = 500
# px.defaults.height = 500
# px.defaults.template = "plotly_dark"
# fig_bar = px.bar(purchase_df, x="spend", y="date", color="place", title="Purchases by Place")
#
# dcc.Graph(
#     id='spend-bar-graph',
#     figure=fig_bar
# )
#
# fig_bar.show()


#-----HEATMAP-----#
heatmap_df = prepare_data.prepare_purchase_data_heatmap(df_purchase)
fig_heatmap = px.imshow(heatmap_df)

dcc.Graph(
    id='spend-heatmap',
    figure=fig_heatmap
),

file_path_stages = Path(__file__).parent.joinpath('data', 'stages.csv')
df_stages = pd.read_csv(file_path_stages)

mapbox_token = "pk.eyJ1Ijoic3RlcGhlbi1vMTciLCJhIjoiY2t5c2t3NTJtMHlibjJ1dGdyODQ1NW44ZSJ9.ox4o5M561WhWitoAruw6Cg" # Add your mapbox token here
px.set_mapbox_access_token(mapbox_token)

fig_map = px.scatter_mapbox(df_stages,
                            lat="latitude",
                            lon="longitude",
                            color="stage",
                            center=dict(lat=-23.701057, lon=-46.6970635),
                            hover_name="stage",
                            zoom=14.5,
                            title='Lollapalooza Brazil 2018 map')
fig_heatmap.show()

if __name__ == '__main__':
    app.run_server(debug=True)
