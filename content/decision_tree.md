title: Decision trees, can we make it easier?
date:	2020-05-23
tags: Machine Learning, Classical methods, Supervised Learning
keywords: Trees, Loss functions, sampling methods, parameters
category: Machine Learning
author: Cecilia Miao
summary: An overview about decision tree methods in Machine Learning and their corresponding loss functions
lang: en
translation	Is: false
status: draft
# What are decision trees?

Decision trees are tree structured algorithms which map the input feature variables to a specific target. The algorithm is implemented with tree-structure, where at each node is a decision point and the end-nodes will be equipped with right and left leaves. The target variable could be discrete or continuous, which results in the classification trees and regression trees.
___
# Explain decision trees to a child
## The decision part
imagining that you are playing the monopoly game. You need to make a lot of decisions during this process, for instance, at the beginning of the game, you need to decide whether you should spend the money to buy more assets or spend it to upgrade your house. Based on each of the decision that you made, you could encounter more subsequent decisions. In the end, you would be directed to the result of winning or losing the game.
Therefore, in order to win this game, you should estimate the probability of each decision leading to the final results or wining and losing the game. After you played a lot of games, you could gradually learn to make the best decision that could lead to your triumph, this process is called parameter updates.

## The tree part
Probably you could be tired of playing so many games. it will be great if there is a robot that could help you to automatically play the game. How can we tell the computer to calculate all results and make the right decision for us? if we draw this process on a blank paper, you could probability observe this kind of representation.

Look at the picture, if you rotate it a little bit, doesn't it just look like a normal tree. Basically, it has the root since the beginning of the game, branch for each decision point, and leaf for the ending results. We could represent it with a specific computer data structure-tree in order to solve it. The computer could use that data structure to compute all results and update the probability of choosing the left or right branch for you, Then you could easily win this game.
___
# Technical details

Above-mentioned explanations could already be sufficient to explain to a child about what decision trees look like. However, since we are enthusiastic machine learning practitioners, we would like to more technical details. For instance, based on what criteria does the tree split, what's the difference between a classification tree and regression trees, are there any variations in different decision trees?

## Decision tree algorithms
1. ID3 (Iterative Dichotomiser 3)
2. CART (Classification And Regression Tree)
3. Chi-square automatic interaction detection (CHAID)

These algorithms differentiate with each other mainly based on different __impurity__ measures. 
### impurity
impurity measures the homogeneity of the labels of that node. if a node has only one label, we would say its impurity is 0.
### Information gain
Information gain is the difference between the parent node impurity and the weighted sum of the two child node impurities. The
### ID3
ID3 mainly uses **entropy** to measure the information gain by each split. The entropy could be calculated by the entropy gain $-t_ilog_2(t_i)$ across all classes (t_i includes the class t_1, t_2, t_3...).
### CART 
Classification and regression trees are most classic decision tree algorithms. their calculation are also pretty intuitive. For **Classification**, the model uses **Gini index** to measure the impurity of each node. **Gini index** is calculated by aggregate the frequency calculation of each class, $-f_i(1-f_i)$. Where f_I is the frequency of i class appearing in the specific node. The higher the  **Gini index**, the higher the homogeneity  for the specific tree.
**Regression**, on the other hand, uses a totally different impurity measures to calculate the impurity-variance. In general, variance is calculated by $\frac{1}{N}\sum^N_{i=1}(y_i-\mu)^2$, where $y_I$ is the label of that instance while $\mu$ is the mean of labels ($\frac{1}{N}\sum^N_{i=1}y_i$).
### CHAID
CHAID uses chi-square to measure impurity. The higher the chi-square value, the higher the statistical significance between sub-node and parent node. Chi-square value in statistics is always calculated by $\sqrt{\frac{(ActualObservation-ExpectedObservation)^2}{ExpectedObservation}}$. It could be used for both classification and regression trees.

___
# Variations
## Ensemble method
Ensemble methods refers to the approach to combine different machine learners (usually weak learners) to get strong learner. In layman words, it means combine the wisdom of the crowd so that we could lower the variance. Typical examples are random forest and gradient boosting trees.
## Random forest
Random forest is an ensemble machine learning methods for classification or regression tasks (CART) raised by Breiman,2001. During the training process, the model builds a user-specified number of classifiers and regressors as trees. The mode of the classifying results is the predicted class for the classification model. The mean of the regressor trees will be the predicted value of the regression model. Traditionally, the decision trees approach suffers from the problem of "low-bias, high-variance" due to the over-fit of the training dataset. In other words, the model performs well on the training dataset, but generates relative poorer performance on the validation dataset. 

The CART can not be trained on the graph instance directly, as graph instances with different graph sizes can not be represented as one fixed-size matrix. Instead, we used extracted features from previous literature to represent each graph instance. This operation results in fixed-size vectors despite different graph sizes. Then we train models with these features. In general, tree-based methods are invariant due to the strictly monotone transformations of ordered individual predictor variables. This can be intuitively linked to the construction process of trees. This process can be imagined as partition space into disjoint sub-spaces which predict classes or values. The monotone transformation of feature values can not change the partition structure. Therefore, no feature pre-processing steps such as feature normalization are required for this research. Extracted features that represent a graph instance $i$ can be defined as a feature vector 
$\vec{x_i}$. In a tree ensemble model with $K$ trees,  $f_k(x_i)$ is defined as the predictive function of $k^{th}$ tree within the model. $\hat{y_i}$ stands for the aggregation of all predicted values from the tree. Then we can define the model and the objective function in the following equations.
\begin{align*}
\text{Classification Model: }  &\hat{y_i}=\sum_{k=1}^Kf_k(\vec{x_i})\\
  \text{Regression Model: }  &\hat{y_i}=\frac{\sum_{k=1}^Kf_k(\vec{x_i})}{K}\\
  \text{Objective function: }  &\sum_{i=1}^nl(y_i, \hat{y_i})+\sum_{k=1}^K\Omega(f_k)
\end{align*}
 For a classification model, $f_k$ outputs a binary value which indicates whether an input instance belongs to a class or not. Then $\hat{y_i}$ will be the aggregated value of all graph instances for a problem. The logistic loss of a single predictive class $\hat{y_i}$ against $y_i$ is aggregated among all instances to obtain the total loss. $\Omega(f_k)$ is a regularization term within the model to avoid over-fitting.
 In the regression case, $f_k$ linearly transforms $\vec{x_i}$ and outputs a continuous value $\hat{y_i}$. Subsequently, $l(y_i, \hat{y_i})$ is obtained by minimum square loss (MSE) for i-th instance. 
 
 Random Forest differs from the decision tree with the bagging process, which performs sampling with replacement with the training dataset. In this way, each tree is trained with different training sets, which makes it de-correlate with the other tree. The bootstrap sampling also grows a deeper tree, which further reduces the model class variance, but potentially leads to the problem of higher bias/overfitting. In addition to the bootstrap sampling, random forest adopts the "feature bagging" training procedure that selects a random subset of the features at each candidate split. "feature bagging" allows fewer predictors for the response variable have an equal chance to be selected in trees compared to strong predictors, further decreasing the variance of predictions from the model. 
 >**Bootstrap** refers to the process that you sample dataset with replacements. In other words, a small sub-dataset will never get trained during this proces. They will be called as the out-of-sample instances.
 
 ## Boosting trees
 Similar to Random Forest, Boosted trees  is also a CART where the output class/value depends on the individual tree within the ensembles model. The main difference between the Boosted model and the Random Forest is the training/optimization process. After the loss function is defined for the tree ensembles model, it is optimized based on traditional gradient descent. However, it is intractable to learn all trees at one time. Friedman proposed the Gradient Boosting concept, where the model applies the additive strategy to learn the model parameters. Chen implements this concept with the XGBoost software. 
 
 The objective function of XGBoost is the same as Random Forest. From time 1 to time $t$ the model for the training dataset will evolve as the process described below:
 \begin{align}
 \hat{y}_i^{(0)} &=0\\
  \hat{y}_i^{(1)} &=f_1(x_i) =  \hat{y}_i^{(0)}+f_1(x_i)\\
    \hat{y}_i^{(2)} &=f_2(x_i) = f_1(x_i)+f_2(x_i)\\
    \ldots\\
    \hat{y}_i^{(t)} &=f_t(x_i) = f_{(t-1)}(x_i)+f_t(x_i)\\
 \end{align}
 Here $f_1(x_i), f_2(x_i)\ldots f_t(x_i)$ are added tree models that minimize the loss function. In the regression case, $f_t(x_i)$ will be the model that minimizes residuals. Schapire explicitly demonstrates the benefits of using the 'boosting' strategy in addition to the 'bagging' operation. 'Boosting' reduces the bias of the model by gradually adding more learners (trees) into the current model, re-modeling the bias and residuals within the current CART and combine all learners with the different weights to obtain the final model.

>**Bagging**aggregates the trained weak learners and generate the predicted results. It can used for reducing variance which helps avoid overfitting.
