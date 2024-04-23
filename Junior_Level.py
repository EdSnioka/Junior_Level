import plotly.graph_objects as go
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# Kandidato į prezidentus sąlygų iliustracija
fig1 = go.Figure()

# Kai dalyvavo ne mažiau kaip pusė visų rinkėjų
fig1.add_shape(type="rect",
              x0=50, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Laimėjo", font=dict(size=20)))

# Kai dalyvavo mažiau nei pusė visų rinkėjų
fig1.add_shape(type="rect",
              x0=0, y0=100/3, x1=50, y1=100,
              fillcolor="yellow", opacity=0.5,
              label=dict(text="Laimėjo<br> surinkęs<br> daugiausiai<br> balsų", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig1.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Pridėta vertikali linija ant X ašies ties 50 riba
fig1.add_vline(x=50, line_dash = "dot",
               annotation_text = "50",
               annotation_position = "bottom")
# Pridėta horizontali linija ant Y ašies ties 1/3 riba
fig1.add_hline(y=100/3, line_dash = "dot",
               annotation_text = "33",
               annotation_position = "left")

# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig1.update_layout(
    autosize=False,
    width=1250,
    height=800,
    title={'text' : "Kandidatas išrenkamas pirmajame rinkimų ture",
           'y':0.93,
           'x':0.5},
    xaxis_title='Visi rinkėjai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)
# Kandidato į mero postą sąlygų iliustracija
fig2 = go.Figure()

# Kai rinkėjų aktyvumas didesnis kaip 40%
fig2.add_shape(type="rect",
              x0=40, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Laimėjo", font=dict(size=20))
              )
# Kai rinkėjų aktyvumas mažesnis kaip 40%
fig2.add_shape(type="rect",
              x0=20, y0=20, x1=40, y1=100,
              fillcolor="yellow", opacity=0.5,
              label=dict(text="Laimėjo<br> surinkęs<br> daugiausiai<br> balsų", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig2.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig2.update_layout(
    autosize=False,
    width=1250,
    height=800,
    title={'text' : "Kandidatas išrenkamas pirmajame rinkimų ture",
           'y':0.93,
           'x':0.5},
    xaxis_title='Visi apygardos rinkėjai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)
# Kandidato į seimo nario postą iliustracija
fig3 = go.Figure()

# Kai rinkėjų aktyvumas didesnis kaip 40%
fig3.add_shape(type="rect",
              x0=40, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Laimėjo", font=dict(size=20))
              )
# Kai rinkėjų aktyvumas mažesnis kaip 40%
fig3.add_shape(type="rect",
              x0=20, y0=20, x1=40, y1=100,
              fillcolor="yellow", opacity=0.5,
              label=dict(text="Laimėjo<br> surinkęs<br> daugiausiai<br> balsų", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig3.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig3.update_layout(
     autosize=True,
    width=1250,
    height=800,
    title={'text' : "Kandidatas išrenkamas pirmajame rinkimų ture",
           'y':0.93,
           'x':0.5},
    xaxis_title='Visi apygardos rinkėjai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)

# Konsultacinio referendumo iliustracija
fig4 = go.Figure()

# Sąlyga konsultacinio referendumo sėkmingam priėmimui
fig4.add_shape(type="rect",
              x0=50, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Priimta", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig4.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Pridėta vertikali linija ant X ašies ties 50 riba
fig4.add_vline(x=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "bottom")
# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig4.update_layout(
    autosize=True,
    width=1250,
    height=800,
    title={'text' : "Konsultacinio referendumo priėmimas",
           'y':0.93,
           'x':0.5},
    xaxis_title='Dalyvavę piliečiai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)
# Privalomojo referendumo iliustracija
fig5 = go.Figure()

# Sąlyga privalomojo referendumo sėkmingam priėmimui
fig5.add_shape(type="rect",
              x0=100/3, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Priimta", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig5.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Pridėta vertikali linija ant X ašies ties 1/3 riba
fig5.add_vline(x=100/3, line_dash = "dot",
               annotation_text= "33",
               annotation_position= "bottom")
# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig5.update_layout(
   autosize=True,
    width=1250,
    height=800,
    title={'text' : "Privalomojo referendumo priėmimas",
           'y':0.93,
           'x':0.5},
    xaxis_title='Dalyvavę piliečiai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)
# Privalomojo referendumo Konstitucijos XIV skirsnio nuostatų iliustracija 
fig6 = go.Figure()

# Sąlyga
fig6.add_shape(type="rect",
              x0=50, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Priimta", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig6.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Pridėta vertikali linija ant X ašies ties 50 riba
fig6.add_vline(x=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "bottom")
# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig6.update_layout(
    autosize=True,
    width=1250,
    height=800,
    title={'text' : "Privalomojo referendumo Kontitucijos XIV skirsnio nuostatų pakeitimas",
           'y':0.93,
           'x':0.5},
    xaxis_title='Dalyvavę piliečiai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)
# Privalomojo referendumo Konstitucijos 1 straipsnio nuostatos iliustracija 
fig7 = go.Figure()

# Sąlyga
fig7.add_shape(type="rect",
              x0=75, y0=50, x1=100, y1=100,
              fillcolor="green", opacity=0.5,
              label=dict(text="Priimta", font=dict(size=20))
              )
# Pridėta horizontali linija ant Y ašies ties 50 riba
fig7.add_hline(y=50, line_dash = "dot",
               annotation_text= "50",
               annotation_position= "left")
# Pridėta vertikali linija ant X ašies ties 75 riba
fig7.add_vline(x=75, line_dash = "dot",
               annotation_text= "75",
               annotation_position= "bottom")
# Sutvarkomi tekstų dydžiai, pridedami titles, pakeičiamas iliustracijos dydis
fig7.update_layout(
    autosize=True,
    width=1250,
    height=800,
    title={'text' : "Privalomojo referendumo Kontitucijos 1 straipsnio nuostatos priėmimas",
           'y':0.93,
           'x':0.5},
    xaxis_title='Dalyvavę piliečiai (%)',
    yaxis_title='Balsų skaičius (%)',
    yaxis=dict(range=[0, 100]),
    xaxis=dict(range=[0, 100]),
    font=dict(size=18),
)
# Sukuriama Dash aplikacija
app = Dash(__name__)

# Aplikacijos struktūra
app.layout = html.Div(children=[
    html.H1('VDA Junior Level',
            style={"fontSize":40,
                   "textAlign":"center"}),
# pridedama rodyklė žemyn su galimais pasirinkimais            
    html.Div([
        dcc.Dropdown(
            id = 'graph-type',
            placeholder = 'Select graph type',
            options = [
                {'label': 'Prezidento Rinkimai', 'value' : 'fig1'},
                {'label': 'Mero Rinkimai', 'value' : 'fig2'},
                {'label': 'Seimo Nario Rinkimai', 'value' : 'fig3'},
                {'label': 'Konsultacinio Referendumo Priėmimas', 'value' : 'fig4'},
                {'label': 'Privalomojo Referendumo Priėmimas', 'value' : 'fig5'},
                {'label': 'Konstitucijos XIV Skirsnio Nuostatų Pakeitimas', 'value' : 'fig6'},
                {'label': 'Konstitucijos 1 Straipsnio Nuostatos Pakeitimas', 'value' : 'fig7'}
                ]
            ),
    dcc.Graph(id='graph')
    ])
])
@app.callback(
    Output('graph','figure'),
    [Input('graph-type', 'value')]
)
# Pasirenkama iliustracija
def choose_graph_type(graph_type):
    if graph_type is None:
        raise Dash.exceptions.PreventUpdate()
    if graph_type == 'fig1':
        return fig1
    if graph_type == 'fig2':
        return fig2
    if graph_type == 'fig3':
        return fig3
    if graph_type == 'fig4':
        return fig4
    if graph_type == 'fig5':
        return fig5
    if graph_type == 'fig6':
        return fig6
    elif graph_type == 'fig7':
        return fig7
    return None

if __name__ == '__main__':
    app.run(debug=True)