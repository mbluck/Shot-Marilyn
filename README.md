# About
A web app built with Streamlit for a data-based interpretation of Andy Warhol's "Shot Marilyn" using the color data of the images. <br>
The project is a critical response to a critique of the paintings published by The Interior Review. The goal is to assess whether the conclusions of said critique are supported by the actual RGB (and HSV) content of the paintings. <br>
The project is presented as a dashboard/web app built with Streamlit, a popular framework that builts a webpage and renders visualizations made with other Python libraries using entirely Python code, requiring no HTML, CSS, or JavaScript. 

### Visualizations
Simple histograms of the R, G, and B components of each pixel don't reveal much, as each value is only meaningful when combined with the other two. Instead, the color space of each painting is analyzed by plotting each pixel in a 3D graph with R, G, and B as the axes. To allow the user to see the entire distribution, the visualization is animated such that it rotates along the X axis, and saved as a GIF. The graphs all rotate simultaneously so that the user can directly compare the distributions. <br><br>

The images are converted to the HSV color space so that their Saturation, Value (darkness/lightness), and Hue can be compared. Histograms of these values reveal differences and similarities between the paintings. The original photo upon which the paintings are based is also included. <br><br>

Finally, the average color is taken from each section of the painting (eye, lip, skin, hair, etc). They are displayed in a grid such that one can directly compare the color palette of each image. 

# To Do
* The app layout still needs to be designed.
* Streamlit doesn't want to render the image components or the Plotly histogram. May switch back to Matplotlib instead. May use Seaborn as well, given its more appealing style. 
