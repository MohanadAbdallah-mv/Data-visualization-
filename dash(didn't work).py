# -*- coding: utf-8 -*-
"""
Created on Mon Jan 10 01:51:49 2022

@author: mvako
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import pandas as pd


#load data set
imdb = pd.read_csv("C:\\Users\\mvako\\Desktop\\projects\\fcds\\data vis\\imdb_top_1000.csv")

#create dash app

app=dash.Dash()

#set up the layout

app.layout = html.Div(children=[
    html.H1(children='no of votes-gross plot'),
    dcc.Dropdown(id='genre-dropdown', 
                 options = [{'label':i, 'value':i}
                           for i in imdb['Genre'].unique()],
                 value='Drama'),
        dcc.Graph(id='no of votes-gross plot based on Genre')
       ])
    
    
#set up the callback function
@app.callback(
    Output(component_id='no of votes-gross plot based on Genre',component_property='figure'),
    Input(component_id='genre-dropdown', component_property='value')
)

def update_graph(selected_genre):
    filterd_genre=imdb[imdb['Genre']=='selected_genre']
    fig = px.scatter(filterd_genre, x='Gross', y='No_of_Votes', hover_data=['Series_Title'],title=f'gross-votes plot in {selected_genre}')
    return fig

#run local server
if __name__=='__main__':
    app.run_server(debug=True)

