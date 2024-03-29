import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas

exports_df = pandas.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/'
                             'c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


def generate_table(df: pandas.DataFrame, max_rows=10):
    return html.Table(
        # Header
        [html.Tr([html.Th(col) for col in df.columns])] +
        # Body
        [
            html.Tr([
                html.Td(df.iloc[i][col]) for col in df.columns
            ]) for i in range(min(len(df), max_rows))
        ]
    )


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(exports_df)
])

if __name__ == '__main__':
    app.run_server()
