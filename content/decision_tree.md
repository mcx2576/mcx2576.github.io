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
..* ID3 (Iterative Dichotomiser 3)
..* CART (Classification And Regression Tree)
..* Chi-square automatic interaction detection (CHAID)

These algorithms differentiate with each other mainly based on different __impurity__ measures. 
### mpurity
impurity measures the homogeneity of the labels of that node. if a node has only one label, we would say its impurity is 0.
### Information gain
Information gain is the difference between the parent node impurity and the weighted sum of the two child node impurities. The
### ID3
ID3 mainly uses **entropy** to measure the information gain by each split. The entropy could be calculated by the entropy gain $-t_ilog_2(t_i)$ across all classes (t_i includes the class t_1, t_2, t_3...).
### CART 
Classification and regression trees are most classic decision tree algorithms. their calculation are also pretty intuitive. For **Classification**, the model uses **Gini index** to measure the impurity of each node. **Gini index** is calculated by aggregate the frequency calculation of each class, $-f_i(1-f_i)$. Where f_I is the frequency of i class appearing in the specific node. The higher the  **Gini index**, the higher the homogeneity  for the specific tree.
**Regression**, on the other hand, uses a totally different impurity measures to calculate the impurity-variance. In general, variance is calculated by $1/NSUM^N_{I=1}(y_i-\mu)^2$, where $y_I$ is the label of that instance while $\mu$ is the mean of labels (1/NSUM^N_{I=1}y_i).
### CHAID
CHAID uses chi-square to measure impurity. The higher the chi-square value, the higher the statistical significance between sub-node and parent node. Chi-square value in statistics is always calculated by $\sqrt{(Actual_observation-Expected_observation)^2/expected_observation}$. It could be used for both classification and regression trees.