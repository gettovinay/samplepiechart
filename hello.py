import plotly.graph_objects as go # or plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
labels = ['Offroad','Motorcycle','XUV','SUVs','Sedan']
values = [1060658, 84361, 120372, 221083,135040]

fig = go.Figure(data=[go.Pie(labels=labels, values=values, textinfo='label+percent',
                             insidetextorientation='radial'
                            )])
# or any Plotly Express function e.g. px.bar(...)
# fig.add_trace( ... )
# fig.update_layout( ... )

fig.update_layout(title = {'text':"Sales Summary" ,'xanchor':'center','yanchor':'top' ,'y':0.9,'x':.5})
app = dash.Dash()
app.layout = html.Div([
    dcc.Graph(figure=fig)
])
if __name__ == '__main__':
    app.run_server()
#    app.run_server(port=4040) (debug=True)