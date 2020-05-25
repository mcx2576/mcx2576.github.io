title: How the curse of dimensionality kills classic statistical methods?
date:	2020-05-24
tags: Machine Learning, Statistical Inferences
keywords: Machine Learning, PCA, Deep Learining
category: Machine Learning
author: Cecilia Miao
summary: What is the curse of dimensionality and how does it happen in the classic machine learning models?
lang: en

# The curse of dimensionality
The curse of dimensionality indicates the phenomenon that as the input parameters of a model increase, the volume of the spaces increases exponentially that the existing data becomes sparse. Inevitably, **Statistical Inference** methods lose their power under this situation.

>*Example:* Assuming you that are a kid, we always play the game "rock, paper, scissors".  If we want to predict the probability of wining the game based on past gaming experiences with our friend Alex, then we need to gather some data to predict the probability of him to take a certain move. Then, when some other friends Carlotta, John and Linda join the game, the prediction becomes harder and harder, as we need to not only predict the conditional probability of our serves, but their conditional probabilities and joint probabilities. In the end, we need to play far more rounds in order to win this game.
# The 'cure' for this issue
## PCA
Some methods such as __PCA__ (principle component analysis)  could help the feature engineering process by decreasing the number of attributes without excluding significant factors within the model. 
>*Example:* If you are a fan of music, there must be a type of music that makes you happy the most. The style of the music could be decided by different features, the chords, the rhythm, the melody and the strength of the music, etc. These features  might **jointly** decide the style of the music, which means that you can't easily decide the style just by one or two individual features. However, some features might be redundant to decide a style of music, like the specific node in a music piece, this information is already cover in chords, or correlated with other keys. How do we smartly decide important features to use for avoiding the __curse of dimensionality__ and effectively deciding a specific style of music.
The PCA could be calculated with the following procedure.
1. Calculate the covariance matrix of all features
2. Find the eigen vector of the matrix 
3. Rank eigen vectors based on eigen values
4. Choose the most important eigen vectors as our feature vectors.
>So, what does each of the step mean to a layman?
### Calculate the covariance matrix of all features
The covariance matrix could explicitly describe how much each feature correlated with other features. For instance, we would imagine that the rhythm of a music piece is highly correlated with the beat, while it might be less correlated to the melody. We try to contract table/matrix to calculate the covariance of all features in order to obtain the eigen vector.
### Find the eigen vectors of the matrix
__Eigen vector__ could be regarded as the coordinate mapping of all feature points in the feature space, so that the sum of square distance of original points are minimized after the mapping. How do we preserve the difference between different features at the same time? Eigen vector also has the property of maximizing the variance of a dataset. So that we know some major features such as rhythm, melody and strength will be represented by those eigen vectors. The **minimum square error** and the **maximum variance** will be achieved at the same time in PCA.
### Rank eigen vectors based on eigen values
After we obtain the eigen vectors, we calculated eigen values and rank eigen vectors according to eigen values.
###  Choose the most important eigen vectors as our feature vectors.
After you choose the eigen vectors, you can use them for further predictions or analysis.