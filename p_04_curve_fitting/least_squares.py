# %% [markdown]
# # Least squares
# [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YoniChechik/AI_is_Math/blob/master/p_04_curve_fitting/least_squares.ipynb)

# %%
import numpy as np
import matplotlib.pyplot as plt
fig_size = (10,10)
# %%
x_max = 10
x_step = 0.01
x = np.arange(0, x_max, x_step)
y = 3*x-3

# add noise to data
std = 1
y = y+np.random.normal(scale=std, size=x.shape)

plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
plt.title("noisy data")

# %%
# calc LS matrices
x_vec = x.reshape(-1, 1)
X = np.concatenate((x_vec, np.ones(x_vec.shape)), axis=1)
print(X.shape)
y_vec = y.reshape(-1, 1)

# %%
b = np.linalg.inv(X.T@X)@X.T@y_vec
print(b)

# plot fit results
plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
# x_axis = np.arange(x_max+x_step)
plt.plot(x, b[0]*x+b[1], 'r')
plt.title("noisy data + best LS fit. $b^T$="+str(b.T))
# %%comparison to np.linalg.lstsq
b_np = np.linalg.lstsq(X, y_vec, rcond=None)[0]
mse = np.mean((b-b_np)**2)
print(mse)
# %% vertical dataset
data_sz = 100
x = np.ones(data_sz)
y = np.arange(data_sz)

# add noise to data
std = 0.1
x = x+np.random.normal(scale=std, size=x.shape)

plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
axes = plt.gca()
axes.set_xlim([-3, 3])
plt.title("noisy vertical data")

# %%
# calc LS matrices
x_vec = x.reshape(-1, 1)
X = np.concatenate((x_vec, np.ones(x_vec.shape)), axis=1)
y_vec = y.reshape(-1, 1)

# %%
b = np.linalg.inv(X.T@X)@X.T@y_vec
print(b)

# plot fit results
plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
x_axis = np.arange(3)
plt.plot(x_axis, b[0]*x_axis+b[1], 'r')
plt.title("vertical data + best LS fit. $b^T$="+str(b.T))


# %% TLS

X = np.concatenate((x.reshape(-1, 1)-np.mean(x),
                    y.reshape(-1, 1)-np.mean(y)), axis=1)


def linear_tls(X):
    w, v = np.linalg.eig(X.T@X)
    return v[:, np.argmin(w)]


tls_res = linear_tls(X)

a = tls_res[0]
b = tls_res[1]

c = -a*np.mean(x)-b*np.mean(y)
x_fit = np.array([x.min(), x.max()])
y_fit = -a/b*x_fit-c/b

plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
plt.plot(x_fit, y_fit)
axes = plt.gca()
axes.set_xlim([-3, 3])
axes.set_ylim([0, 100])
plt.title("noisy vertical data + linear TLS fit")

# %% non linear LS
x_step = 0.01
x = np.arange(-10, 10+x_step, x_step)

y = 0.5*x**2+2*x+5

# add noise to data
std = 5
y = y+np.random.normal(scale=std, size=y.shape)

plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
plt.title("noisy parabola data")
# %%
# calc LS matrices
x_vec = x.reshape(-1, 1)
X = np.concatenate((x_vec**2, x_vec, np.ones(x_vec.shape)), axis=1)
y_vec = y.reshape(-1, 1)

b = np.linalg.lstsq(X, y_vec, rcond=None)[0]
print(b)
# %%
plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
plt.plot(x, b[0]*x**2+b[1]*x+b[2], 'r')
plt.title("data + best LS fit. $b^T$="+str(b.T))

# %% outliers
x_max = 10

x = np.arange(10)
y = 4*x+2

# let's change the last data point
y[-1] -= 20

plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
plt.title("data with outlier")


# %%
# calc LS matrices
x_vec = x.reshape(-1, 1)
X = np.concatenate((x_vec, np.ones(x_vec.shape)), axis=1)
y_vec = y.reshape(-1, 1)

# %%
b = np.linalg.inv(X.T@X)@X.T@y_vec
print(b)

# plot fit results
plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
x_axis = np.arange(x_max)
plt.plot(x_axis, b[0]*x_axis+b[1], 'r')
plt.title("data with outlier + best LS fit. $b^T$="+str(b.T))

#%% [markdown]
# ## RANSAC
# ### arrange data
# %% 

x = np.arange(0, 10, 0.1)
y = 3*x-3

# add noise to data
std = 1
y = y+np.random.normal(scale=std, size=x.shape)

# add random noise unrelated to noisy line
noise_sz = int(x.shape[0]*5)
x_noise = np.random.uniform(x.min(), x.max(), size=noise_sz)
y_noise = np.random.uniform(y.min(), y.max(), size=noise_sz)

plt.figure(figsize=fig_size)
plt.plot(x, y, '*')
plt.plot(x_noise, y_noise, '*')

#%%
x = np.concatenate((x, x_noise))
y = np.concatenate((y, y_noise))

#%% [markdown]
# ### run naive RANSAC
#%%

def basic_ransac(x,TH):
    #====== choose 2 random inds
    rand_indices = np.random.choice(x.shape[0], size=2)

    #====== build LS data:
    x_vec = x[rand_indices].reshape(-1, 1)
    X = np.concatenate((x_vec, np.ones(x_vec.shape)), axis=1)
    y_vec = y[rand_indices].reshape(-1, 1)

    b = np.linalg.lstsq(X, y_vec, rcond=None)[0].flatten()

    #====== build fitted line
    line_p1 = np.array([x.min(), b[0]*x.min()+b[1]])
    line_p2 = np.array([x.max(), b[0]*x.max()+b[1]])
    inlier_ind = []
    
    #====== distance of fit line from each sample to determine inliers
    for j in range(x.shape[0]):
        p_j = np.array([x[j], y[j]])

        # https://en.wikipedia.org/wiki/Cross_product#Geometric_meaning
        # |a X b| = |a||b|sin(t) -> |a X b|/|b| = |a|sin(t)
        d_j = np.linalg.norm(np.cross(line_p2-line_p1, line_p1-p_j))/np.linalg.norm(line_p2-line_p1)
        if d_j <= TH:
            inlier_ind.append(j)

    inlier_ind = np.array(inlier_ind)
    return b, inlier_ind

#%%
TH = 1
best_inliers = np.array([])
best_b = None

inliers_inds_list = []
for i in range(10):
    b, inlier_ind = basic_ransac(x,TH)
    inliers_inds_list.append(inlier_ind)

    #====== save best model
    if best_inliers.shape[0] < inlier_ind.shape[0]:
        best_inliers = inlier_ind
        best_b = b


# plot best fit
plt.figure(figsize=fig_size)
ax = plt.gca()
x_axis = np.arange(11)
ax.plot(x_axis, best_b[0]*x_axis+best_b[1], 'r')
ax.plot(x, y, '*')
ax.plot(x[best_inliers], y[best_inliers], '*k')
ax.set_xlim([0, 10])
ax.set_ylim([0, 25])
plt.title("best fit")
plt.show()


#%%
