# Here's a installation instuction, you might need more than that though
# Just type pip install + model name
# pip install dash==0.18.3  # The core dash backend
# pip install dash-renderer==0.11.0  # The dash front-end
# pip install dash-html-components==0.7.0  # HTML components
# pip install dash-core-components==0.12.6  # Supercharged components
# pip install plotly --upgrade  # Latest Plotly graphing library


import dash
from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html
from loremipsum import get_sentences

app = dash.Dash()

app.scripts.config.serve_locally = True

app.layout = html.Div([
    
    html.H1(children='Dashboard Demo'),
    html.Div(children='''
         Dash: This is a demo web application framework for Python.
     '''),

    dcc.Tabs(
        tabs=[
            {'label': 'Tab {}'.format(i), 'value': i} for i in range(1, 4)
        ],
        value=3,
        id='tabs'
    ),
    html.Div(id='tab-output')
], style={
    'width': '80%',
    'fontFamily': 'Sans-Serif',
    'margin-left': 'auto',
    'margin-right': 'auto'
})




@app.callback(Output('tab-output', 'children'), [Input('tabs', 'value')])
def display_content(value):
    data = [
        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [219, 146, 112, 127, 124, 180, 236, 207, 236, 263,
                  350, 430, 474, 526, 488, 537, 500, 439],
            'name': 'Beef',
            'marker': {
                'color': 'rgb(55, 83, 109)'
            },
            'type': ['bar', 'scatter', 'box'][int(value) % 3]
        },
        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [16, 13, 10, 11, 28, 37, 43, 55, 56, 88, 105, 156, 270,
                  299, 340, 403, 549, 499],
            'name': 'Chicken',
            'marker': {
                'color': 'rgb(26, 118, 255)'
            },
            'type': ['bar', 'scatter', 'box'][int(value) % 3]
        },

        {
            'x': [1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003,
                  2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012],
            'y': [111, 132, 321, 457, 678, 345, 168, 180, 567, 645,
                  263, 177, 234, 765, 233, 444, 333, 777],
            'name': 'Pork',
            'marker': {
                'color': 'rgb(10, 200, 150)'
            },
            'type': ['bar', 'scatter', 'box'][int(value) % 3]
        },
    ]

    return html.Div([
        dcc.Graph(
            id='graph',
            figure={
                'data': data,
                'layout': {
                    'margin': {
                        'l': 30,
                        'r': 0,
                        'b': 30,
                        't': 0
                    },
                    'legend': {'x': 0, 'y': 1}
                }
            }
        ),
        # html.Div(' '.join(get_sentences(10)))
    ])


if __name__ == '__main__':
    app.run_server(debug=True)