from manim import *
import pandas as pd

class GraphVisualization(Scene):
    def construct(self):
        # Read the data from the CSV file and parse the 'date' column as datetime
        data = pd.read_csv("C:\\Users\\Somdeb\\Downloads\\your_data.csv", parse_dates=['date'])

        # Sort the DataFrame by date (optional, if the data is not already sorted)
        data = data.sort_values(by='date')

        # Get the maximum high value to focus on the highest portion
        max_high = data['high'].max()

        # Define the axes
        axes = Axes(
            x_range=(data['date'].min(), data['date'].max(), 1),  # Set the step value manually to 1
            y_range=(data['low'].min(), max_high, (max_high - data['low'].min()) / 10),
            axis_config={"include_tip": False}
        )

        # Create the graph using the 'date' column as x-axis values
        graph = axes.plot(data['date'], data['high'], color=WHITE)

        # Add labels to the axes
        axes_labels = axes.get_axis_labels(x_label="Date", y_label="High")

        # Add the graph and labels to the scene
        self.add(axes, axes_labels, graph)

        # Animate the graph
        self.play(Create(graph))

        # Wait for a moment before ending the animation
        self.wait(3)
