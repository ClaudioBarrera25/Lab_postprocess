import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.tools as tls
import plotly.graph_objects as go

# Generate some example data
data = np.random.rand(10, 10)

# Create a matplotlib figure
# fig, ax = plt.subplots()
# im = ax.imshow(data, cmap='viridis')
# plt.axis('off')  # Turn off axis for better visualization

# # Convert the matplotlib figure to plotly format
# def matplotlib_to_plotly(fig):
#     # Convert the matplotlib figure to a plotly figure
#     return go.Figure(data=[go.Image(z=fig)])

# # Convert matplotlib figure to plotly figure
# fig = matplotlib_to_plotly(fig)

fig = px.imshow(data)

# Create the Dash app
app = dash.Dash(__name__)

# Define the layout of the Dash app
app.layout = html.Div([
    html.H1("Dash imshow Example"),
    dcc.Graph(figure=fig)
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
