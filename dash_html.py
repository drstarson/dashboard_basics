import dash
import dash_html_components as html

app = dash.Dash()

style_1 = {'color': 'green',
           'border': '2px green solid'}

style_2 = {'color': 'red',
           'border': '2px red dashed'}


div_1 = 'This is the outmost div'
div_2 = html.Div(['Innter Div'], style=style_2)


app.layout = html.Div([div_1,
                       div_2], style=style_1)


if __name__ == '__main__':
    app.run_server()
