#%%
import plotly.express as px#pip install plotly==4.3
import cv2

im = cv2.imread("c_08_features/chess.jpg")

fig = px.imshow(im)
fig.show()


# %%
import plotly.express as px
iris = px.data.iris()
fig = px.scatter(iris, x="sepal_width", y="sepal_length",width=800,height=400)
fig.show()

# %%
im.shape

# %%
