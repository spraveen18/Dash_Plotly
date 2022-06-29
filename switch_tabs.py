import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd   
from dash.dependencies import Input, Output



app = dash.Dash()

app.layout = html.Div([
    html.H1(' Analysis Tool'),
    dcc.Tabs(id='tabs-example', value='tab-0', children=[
        dcc.Tab(label='tab-0', value='tab-0'),
        dcc.Tab(id='tab1', label='tab-1', value='tab-1',children=[            
            html.Button('button 1', id='submit-val', n_clicks=0,
                    style={'width':185,'display':'inline-block','padding-right':80})
        ]),
        dcc.Tab(id= 'tab2', label='tab-2', value='tab-2',children=[            
            html.Button('button 2', id='submit-col', n_clicks=0,
                    style={'width':185,'display':'inline-block','padding-right':80})
        ]),
        dcc.Tab(id= 'tab3', label='tab-3', value='tab-3',children=[            
            html.Button('button 3', id='submit-rev', n_clicks=0,
                    style={'width':185,'display':'inline-block','padding-right':80})
        ]),
        dcc.Tab(id='tab4', label='tab-4', value='tab-4')                     
    ]),
    html.Div(id='tabs-example-content') 
])    


@app.callback(Output('tabs-example', 'value'),
              [Input('submit-val', 'n_clicks'),
              Input('submit-col', 'n_clicks'),
              Input('submit-rev', 'n_clicks')])
def on_click_val(click1, click2, click3):

    btn = dash.callback_context.triggered[0]["prop_id"].split(".")[0]

    if btn == "submit-val":
        return "tab-2"
    elif btn == "submit-col":
        return "tab-3"
    elif btn == "submit-rev":
        return "tab-4"
    else:
        return "tab-0"
    
    
    
if __name__ == '__main__':
    app.run_server(debug=True)   # "debug = True" allows us to see the changes in the browser without running the file again.     
