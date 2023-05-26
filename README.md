# Polycystic Ovarian Syndrome, Inside and Out
### Why This Project? 
As per the [Center for Disease Control and Prevention (CDC)](https://www.cdc.gov/diabetes/basics/pcos.html#:~:text=What%20is%20PCOS%3F,beyond%20the%20child%2Dbearing%20years.), Polycystic Ovarian Syndrome (PCOS) affects 6-12% of all reproductive-aged women worldwide, and is one of the most common reasons for infertility. Though it is widely prevalent, it is also extremely under-researched, with no known underlying cause. With this personal project, I aim to gain an understanding of the hormonal/physiological aspects of PCOS ("PCOS Hormones" notebook), as well as get an understanding of the experiences that those with PCOS undego while living with the disorder ("PCOS Experience" notebook). 

### Goal
I have created this project with the mind of a hypothetical: **how can the data provided be beneficial for a company who would like to create an all-in-one supplement to treat PCOS?**

I have separated this project into two parts, based on two areas: biological/hormonal factors, based on the provided dataset, and the overall affects PCOS has on real people, based on personal experiences shared on Reddit. 

For part 1 ("PCOS Hormones" notebook), the overall goal is to analyze the dataset provided to discover any relationshups between features, to compare these relationships with those that have already been found in scientific research studies, and build a binary classifier that can identify whether someone may have PCOS or not. 

For part 2 ("PCOS Experience" notebook), the goal is to gather personal experiences from Reddit users who have PCOS, and try to understand what the conversations are that occur within the PCOS community. Through information gathered directly from those who have PCOS, I attempt to find the most common topics discussed, and gain an idea of what topics should be considered when attempting to create an all-in-one supplement. 

### Data Sources
The dataset used in *"PCOS Hormones"* is from Kaggle ([here](https://www.kaggle.com/datasets/prasoonkottarathil/polycystic-ovary-syndrome-pcos)), with the following credit: <br>
__Author:__ Prasoon Kottarathil <br>
__Title:__ Polycystic ovary syndrome (PCOS) <br>
__Year:__ 2020 <br>
__Publisher:__ Kaggle <br>
__Journal:__ Kaggle Dataset <br>

The above data contains 541 rows and 45 features (including whether the paitent has PCOS or not, various hormone levels, vital signs, and physical traits)

*"PCOS Experience"* used exclusively data extracted through the Python Reddit API Wrapper (PRAW), Reddit's official API. The data comes from the following subreddits: 
1. **r/PCOS**: Subreddit where those with PCOS (or those who are caring for someone who has PCOS) can ask questions, share experiences, rant, and seek support to deal with the symptoms that come with PCOS.
2. **r/PCOSRECIPES**: Subreddit to share PCOS-friendly recipes
3. **r/PCOSloseit**: Subreddit where those with PCOS can seek help/advice, and share their experience of losing weight, in any way
4. **r/PCOS_CICO**: Subreddit where those who have PCOS can share their experiences and seek advice for using the "calories in, calories out" method of losing weight
5. **r/PCOSandPregnant**: Subreddit where those who have PCOS and are pregnant can share their experiences and seek advice for maintaining a healthy pregnancy. 
6. **r/TTC_PCOS**: Subreddit for those with PCOS who are trying to conceive, and are looking for advice from others who have gone through a similar situation
7. **r/LeanPCOS**: Subreddit for those who have the "Lean" type of PCOS, to ask questions and seek advice about how to maintain their health, tailored to their specific type of PCOS. 
8. **r/PCOS_Folks**: Subreddit for PCOS, emphasizing LGBTQIA+ inclusivity

### Skills Used 
__PCOS Hormones__:
* Python Programming
* Exploratory Data Analysis
* Numpy/Pandas
* Binary Classification and Classifier Comparison (Using Scikit-Learn, including Naive Bayes, Random Forest, Decision Trees, and Logistic Regression)
* Principal Component Analysis (PCA)
* Visualization (Matplotlib, Seaborn)

__PCOS Experience__:
* Python Programming
* Text Data Cleaning
* Exploratory Data Analysis
* Visualization (Matplotlib, Seaborn, WordCloud, Plotly)
* Feature Construction
* Natural Langauge Processing (Unsupervised Learning, Topic Modeling/Latent Drischlett Allocation/WordCloud)
* API usage/understanding 

### Key Results  
#### Part A. PCOS Hormones <br>
Based on research of the hormones included, it was found that Body Mass Index ('BMI'), menstrual cycle length ('Cycle length(days)'), HCG (' I   beta-HCG(mIU/mL)' and 'II    beta-HCG(mIU/mL)'), follicular stimulating hormone and luteinizing hormone ('FSH/LH'), thyroid stimulating hormone ('TSH (mIU/L)'), anti-Mullerian hormone ('AMH(ng/mL)'), prolactin ('PRL(ng/mL)'), vitamin D3 ('Vit D3 (ng/mL)'), and glucose through the random glucose test ('RBS(mg/dl)') should potentially show some patterns of correlation (see notebook for specific information). To check this correlation, I created 4 correlation matrices, one for those without PCOS, one for those with PCOS, one looking at these features for the entire participant pool, and one covering the entire feature space. <br>

Correlation of Features of Interest in Those WITHOUT PCOS <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/9f257ba9-27f5-418e-a513-3b434a1ce1fe) <br>

Correlation of Features of Interest in Those WITH PCOS <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/5453e443-72cc-4d43-936e-344d60d64611) <br> 

In the above two correlation matrices, it seems like there are no strong correlations between the features, except between I beta-HCG and II beta-HCG. In those with PCOS, it seems that there may be a slight positive relationship between BMI and FSH/LH ratio. For refereence, the closer the correlation value is to -1, the stronger the negative correlation between variables. Closer to +1 indicates a stronger positive relationship, and closer to 0 would be indicitive of a neutral relationship. The majority of values nearing 0 (neutral) could be due to the data being separated into subsets, separating the amount of data.  For this reason, I chose to look at the correlation matrix of the features of interest, with all participants. 

Correlation of Features of Interest Among All Participants <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/ca1a78f8-4817-4512-8222-e331c1341d2b) <br>

In the above 3 correlations matrices, there appears to be no strong correlations between features, except for a positive correlation between I beta-HCG and II beta-HCG. There is also a slightly positive correlation  in those with PCOS, between BMI and the FSH/LH ratio. This may be due to the smaller amount of data within each subset (with PCOS vs. no PCOS). 

Correlation of All Features Among All Participants <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/b9c1fe94-a965-4651-b874-900c9074af63) <br> 

Classifiers Accuracy Outputs with Different Testing Sizes <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/d5dae979-f3d8-4915-9301-6416f735e682) <br> 

ROC Curve of Classifiers (testing size = 18%) <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/281d7b51-f085-466b-a0c2-8c4b4fd54040) <br> 

ROC Curve Comparing Original Logistic Regression, and Logistic Regression with Principal Component Analysis (n_components = 6) <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/4f888bb9-b964-41ad-8afc-60fddbbb4701) <br> 

ROC Curve With Classifiers Fit to Features, Removing the Redundant Features (Waist:Hip Ratio, FSH:LH ratio) <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/e1f40f10-34d3-4806-ae88-6fb227d71ddc) <br> 


#### Part B. PCOS Experience 

Descriptive Stats for the Amount of Words in the titles and bodies of posts, per subreddit
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/a4e92999-431f-4aee-9ab4-f6b863254ed6)

Distribution of the titles' and bodies' polarities and subjectivities 
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/7556a000-ddaa-4577-8fde-26532bdde5cc)

Topic Modeling 

WordCloud for Titles (using LDA)
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/52aa5c07-3a8b-41c9-bf12-77889ca34c48)

WordCloud for Bodies (using LDA) 
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/e8728bd2-3ac7-420b-a049-188f6f0fe7b1)

Bigrams Mentioned >100 times, for Bodies (note not all are labeled on the x-axis) 
![pcos_bigrams_over_100](https://github.com/nisha-kaushal/PCOS/assets/100887571/a7ad79de-5d4f-4a18-8a88-d2f1bd44d558)

Bigrams Mentioned >200 times, for Bodies
![pcos_bigrams_over_200](https://github.com/nisha-kaushal/PCOS/assets/100887571/ef23fdd5-c89d-42fc-b41c-faa76df5d5c7)

### Discussion  
Because this project is based on the idea that it would be of use for a company that is interested in creating an all-in-one supplement to assist in relieving PCOS symptoms, it is important to consider this hypothetical while discussing the project in detail, and will be referenced throughout the discussion. 

As shown in "PCOS Hormones", Polycystic Ovarian Syndrome can be predicted using different hormone levels, body features, and lifestyle choices. *Why does the prediction capabiloty matter to a company that is attempting to create an all-in-one supplement/medication that can relieve PCOS symptoms?*
When looking into what can potentially affect PCOS, creating and comparing classifiers may be a helpful option. We can pick and choose which features to include in the classifiers, and see how they affect the ability to predict whether the patients have PCOS or not. If there is a large drop in accuracy when a feature is dropped, we can assume that the feature does have a significant relationship with PCOS. This would eliminate the need to include an element in the all-in-one supplement that will specifically target any features that do not have siginificance in the prediction of PCOS. As a continuation of this first part of the project, if I were to continue, I would choose to create a Random Forest Classifier to do the comparisions mentioned, as it had the overall best accuracy output. While these features can potentially also be seen through correlation matrices, it is not always certain that there will be significantly discernible patterns found, as seen in the matrices created in this project. 


### Pitfalls and Future Project Improvements
While developing this project, there were a few aspects relating to the data used that may have affected the models' accuracies and overall results, particularly in the "PCOS Hormones" section of the project, as this section is based on data that was previously collected from an outside party. The most significant of these aspects is the amount of data provided in the dataset. The dataset used included 541 patients, which, while large for the interest area (Kerala, India), classifiers would likely perform better with more data. In addition to the sparsity of the data, the data included in the dataset was imbalanced, meaning that the amount of patients included with PCOS was different from the amount of patients included who did not have PCOS. This can also affect the outcome of the classifiers, because classifiers overall tend to be biased towards the majority class. Imbalanced data also can affect the correlation between features, which is why we may not have seen many strong correlations between features, though according to the mechanisms of actions of the hormones discussed in detail, there likely should have been. To improve the quality of the outcome and analysis, I would collect more data, trying to balance the amount of those with PCOS and those without PCOS, or collect more data and then filter the majority class to be equal to that of the minority to achieve balance. 


