import dash
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State
# from src.graph import matchresult, homeawayrecord, rivalresult, showrivaldataframe

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWlwgP.css']

app = dash.Dash(__name__, external_stylesheets = external_stylesheets)



app.layout = html.Div(children=[
    html.H1('International Football Dashboard', style = {'text-align' : 'center','padding' : '25px'}),
    html.P('Created by Fandri', style = {'text-align' : 'center'}),

    html.Div(children = [
        html.P('Choose country : ', className = 'col-3',style = {'margin-left' : '0px'}),
        html.P('n-year : ', className = 'col-3',style = {'margin-left' : '0px'})
        ], className = 'row'),
    html.Div(children = [
        html.Div(dcc.Input(id='choose-country', value='Indonesia', type='text'),className = 'col-3', style = {'margin-left' : '0px'}),
        html.Div(dcc.Input(id='n-year', value=15, type='number'),className = 'col-3', style = {'margin-left' : '0px'})
        ], className = 'row'),
    ## Add search button
    html.Div(html.Button('Search', id = 'search'), style = {'margin-top' : '25px', 'margin-bottom' : '25px'}),
    ## Add tab
    dcc.Tabs(value = 'tabs', id = 'tabs-1',children = [
        dcc.Tab(label= 'Match Result', value = 'tab-nol', children =[
        html.H3('Ika Alfina, Rio Mulia, Mohamad Ivan Fanany, and Yudo Ekanata, "Hate Speech Detection in Indonesian Language: A Dataset and Preliminary Study ", in Proceeding of 9th International Conference on Advanced Computer Science and Information Systems 2017(ICACSIS 2017). '),
        html.H3('Ibrohim, M.O., Budi, I.. A Dataset and Preliminaries Study for Abusive Language Detection in Indonesian Social Media. Procedia Computer Science 2018;135:222-229. ')
        ])
    ]
    , content_style = {
        'fontFamily' : 'Arial',
        'borderBottom' : '1px solid #d6d6d6',
        'borderLeft' : '1px solid #d6d6d6',
        'borderRight' : '1px solid #d6d6d6',
        'padding' : '44px'
    })

    ],
    style = {
    'maxWidth': '1100px',
    'margin' : '0 auto'
}
)



if __name__ == '__main__':
    app.run_server(debug = True)