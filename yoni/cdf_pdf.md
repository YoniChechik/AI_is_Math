We are writing lecture notes for my computer vision course. Write lecture notes with math notations in latex format. Here are some points that needs to be expanded:
cumulative distribution function (CDF) of a real-valued random variable 𝑋 is the probability that 𝑋 will take a value less than or equal to 𝑥:
𝐹_𝑋 (𝑥)=𝑃(𝑋≤𝑥)
Properties of CDF:
.

Monotonically non decreasing.
The probability density function (PDF) of a continuous random variable can be determined from the cumulative distribution function by differentiating.
Lecture Notes:

The cumulative distribution function (CDF) of a real-valued random variable X is a function that describes the probability that X will take a value less than or equal to x. It is defined as follows:

$F_X(x) = P(X \leq x)$

The CDF is a non-decreasing function, meaning that as the value of x increases, the value of the CDF also increases. In other words, the probability of X taking a value less than or equal to x increases as x increases.

Properties of CDF:

Monotonically non decreasing: $F_X(x_1) \leq F_X(x_2)$ for $x_1 < x_2$.

The CDF of a continuous random variable can be determined from the probability density function (PDF) by taking the integral of the PDF with respect to x:

$F_X(x) = \int_{-\infty}^{x} f_X(t) dt$

Also, the probability density function (PDF) of a continuous random variable can be determined from the cumulative distribution function by differentiating the CDF with respect to x:

$f_X(x) = \frac{d}{dx} F_X(x)$

CDF is an important concept in statistics and probability and is used in various applications such as image processing, pattern recognition, and machine learning.


===============

We are writing lecture notes for my computer vision course. Write lecture notes with math notations in latex format. Here are some points that needs to be expanded:
Probability density function (PDF) can be interpreted as providing a ”relative likelihood” that the value of the random variable would equal that sample.
The absolute likelihood for a continuous random variable to take on any particular value is 0 (since there are an infinite set of possible values to begin with).
In a more precise sense, the PDF is used to specify the probability of the random variable falling within a particular range of values. This probability is given by the integral of this variable's PDF over that range and is actually the CDF.

Lecture Notes:

The probability density function (PDF) is a function that describes the relative likelihood that a continuous random variable will take on a particular value. It is defined as the derivative of the cumulative distribution function (CDF) with respect to the random variable.

$f_X(x) = \frac{d}{dx} F_X(x)$

The PDF can be thought of as providing a "relative likelihood" that the value of the random variable would equal that sample. However, it is important to note that the absolute likelihood for a continuous random variable to take on any particular value is 0, since there are an infinite set of possible values to begin with.

Instead, the PDF is used to specify the probability of the random variable falling within a particular range of values. This probability is given by the integral of this variable's PDF over that range and is actually the CDF.

$F_X(b) - F_X(a) = \int_{a}^{b} f_X(x) dx$

It is important to note that if $X$ is a discrete random variable, the PDF is called probability mass function (PMF).

In summary, the PDF is used to specify the relative likelihood of a continuous random variable taking on a particular value, while the CDF is used to specify the probability of the random variable falling within a particular range of values. These concepts are important in computer vision and are used in various applications such as image processing, pattern recognition, and machine learning.