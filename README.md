# Polycystic Ovarian Syndrome, Inside and Out
## Why This Project? 
As per the [Center for Disease Control and Prevention (CDC)](https://www.cdc.gov/diabetes/basics/pcos.html#:~:text=What%20is%20PCOS%3F,beyond%20the%20child%2Dbearing%20years.), Polycystic Ovarian Syndrome (PCOS) affects 6-12% of all reproductive-aged women worldwide, and is one of the most common reasons for infertility. Though it is widely prevalent, it is also extremely under-researched, with no known underlying cause. With this personal project, I aim to gain an understanding of the hormonal/physiological aspects of PCOS ("PCOS Hormones" notebook), as well as get an understanding of the experiences that those with PCOS undego while living with the disorder ("PCOS Experience" notebook). 

## Goal
I have created this project with the mind of a hypothetical: **how can the data provided be beneficial for a company who would like to create an all-in-one supplement to treat PCOS?**

I have separated this project into two parts, based on two areas: biological/hormonal factors combined with lifestyle choices, based on the provided dataset, and the overall affects PCOS has on real people, based on personal experiences shared on Reddit. 

For part 1 ("PCOS Hormones" notebook), the overall goal is to analyze the dataset provided to discover any relationshups between features, to compare these relationships with those that have already been found in scientific research studies, and build a binary classifier that can identify whether someone may have PCOS or not. 

For part 2 ("PCOS Experience" notebook), the goal is to gather personal experiences from Reddit users who have PCOS, and try to understand what the conversations are that occur within the PCOS community. Through information gathered directly from those who have PCOS, I attempt to find the most common topics discussed, and gain an idea of what topics should be considered when attempting to create an all-in-one supplement. 

## Data Sources
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

## Skills Used 
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

## Key Results  
### Part A. PCOS Hormones <br>

#### Feature Correlations 
Based on research of the hormones included, it was found that Body Mass Index ('BMI'), menstrual cycle length ('Cycle length(days)'), HCG (' I   beta-HCG(mIU/mL)' and 'II    beta-HCG(mIU/mL)'), follicular stimulating hormone and luteinizing hormone ('FSH/LH'), thyroid stimulating hormone ('TSH (mIU/L)'), anti-Mullerian hormone ('AMH(ng/mL)'), prolactin ('PRL(ng/mL)'), vitamin D3 ('Vit D3 (ng/mL)'), and glucose through the random glucose test ('RBS(mg/dl)') should potentially show some patterns of correlation (see notebook for specific information). To check this correlation, I created 4 correlation matrices, one for those without PCOS, one for those with PCOS, one looking at these features for the entire participant pool, and one covering the entire feature space. <br>

**Correlation of Features of Interest in Those WITHOUT PCOS** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/9f257ba9-27f5-418e-a513-3b434a1ce1fe) <br>

**Correlation of Features of Interest in Those WITH PCOS** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/5453e443-72cc-4d43-936e-344d60d64611) <br> 

In the above two correlation matrices, it seems like there are no strong correlations between the features, except between I beta-HCG and II beta-HCG. In those with PCOS, it seems that there may be a slight positive relationship between BMI and FSH/LH ratio. For refereence, the closer the correlation value is to -1, the stronger the negative correlation between variables. Closer to +1 indicates a stronger positive relationship, and closer to 0 would be indicitive of a neutral relationship. The majority of values nearing 0 (neutral) could be due to the data being separated into subsets, separating the amount of data.  For this reason, I chose to look at the correlation matrix of the features of interest, with all participants. 

**Correlation of Features of Interest Among All Participants** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/ca1a78f8-4817-4512-8222-e331c1341d2b) <br>

In the above 3 correlations matrices, there appears to be no strong correlations between features, except for a positive correlation between I beta-HCG and II beta-HCG. There is also a slightly positive correlation  in those with PCOS, between BMI and the FSH/LH ratio. This may be due to the smaller amount of data within each subset (with PCOS vs. no PCOS). Among all participants, there seems to be a slight positive correlation between AMH (anti-mullerian hormone) and PCOS, as well as BMI and PCOS. 

**Correlation of All Features Among All Participants** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/b9c1fe94-a965-4651-b874-900c9074af63) <br> 
Based on the coloring alone, I can already tell that I will be able to make better insights with the entire dataframe being taken into account.
The first distinct purple (positive correlation) pattern that can be seen is the sqaure towards the bottom right of the matrix. These positively-correlated features include the following (note that they are all binary): weight gain (y/n), hair growth (y/n), skin darkening (y/n), hair loss (y/n), pimples (y/n), and fast food (y/n). These binary features are also positively correlated with PCOS, and have the highest correlation with PCOS out of all of the features. Why could this be? These binary features (aside from fast food) are all commonly correlated with each other, with the underlying cause being testosterone and insulin resistance, which is common in those with PCOS. Fast food can aggrevate these features, especially when eaten on a regular basis. <br> 
Another interesting correlation to note is the highly positive correlation between FSH and the FSH/LH ratio. While there is a highly positive correlation between the two, there is a correlation value closer to 0 (no detectable correlation) between the FSH/LH ratio and LH. Why could this be? In many with PCOS, it is common to see a high LH value. Because our data contains data for both patients with PCOS and patients without PCOS, it is possible that there is a mix of LH values that can make the correlations less noticable. 

#### Building and Comparing Classification Algorithms (Random Forest, Decision Trees, Naive Bayes, Logistic Regression)
To be able to build the most optimal classification model, it is important to test different classification methods. ALong with this, it is important to test different testing set sizes. To build the classification model to predict whether a person has PCOS or not, random forest, decision trees, Naive Bayes, and logistic regression classifiers were created with different training-test set splits. Below is the accuracy outputs for the different testing sizes (%) <br>
**Classifiers Accuracy Outputs with Different Testing Sizes** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/d5dae979-f3d8-4915-9301-6416f735e682) <br> 
10% testing size showed to have the best outcome for the models. However, 10% testing size and 90% training could leave room for overfitting of the models, so I chose to continue the classifications by using the next-best split of 82% training, 18% testing. 

After classification of the models with the desired train-test split, the ROC curves were plotted to visualize the true positive rates vs. false positive rates: <br> 
**ROC Curve of Classifiers (testing size = 18%)** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/281d7b51-f085-466b-a0c2-8c4b4fd54040) <br> 
Based on the above, it seems that  the Random Forest Classifier and the Naive Bayes classifier showed the best performances, with decision trees showing the worst performance. 

Logistic Regression is often a popular and powerful choice for binary classification models. In this case, however, it was only the third-best classifier of the group. To try and imporve the model, Principal Componenet Analysis (PCA) was applied to the data, with n_components = 6. Below are the ROC curves for the original logistic regression, and the logistic regression with PCA applied. <br> 
**ROC Curve Comparing Original Logistic Regression, and Logistic Regression with Principal Component Analysis (n_components = 6)** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/4f888bb9-b964-41ad-8afc-60fddbbb4701) <br> 
PCA has shown to improve the logistic regression model, but only slightly. I suspect that there would be a larger difference if there were more features, and overall more patients in the study from which this dataset is from.

In the above classifiers, I provided all of the features to use. However, in looking at the dataset, we can see that there are some features that are dependent on the others (example: FSH/LH ratio depends on LH and FSH values).

To see if there are any changes with the classifiers given the information, I used the dataset, but dropped the features that are dependent on others (FSH/LH ratio, Waist Hop Ratio), and built the classifiers with the resulting data. Below are the resulting ROC curves: <br>
**ROC Curve With Classifiers Fit to Features, Removing the Redundant Features (Waist:Hip Ratio, FSH:LH ratio)** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/e1f40f10-34d3-4806-ae88-6fb227d71ddc) <br> 
Comparing the above to the original ROC curves, there were no huge changes, and the overall placement of best-to-worst classifiers remained consistent with the original.

### Part B. PCOS Experience 
To build the dataset used for this part of the project, Reddit's official API was used to gather post data from the "hot", "new", "rising", and "top" posts on the subreddits mentioned earlier. Each post consists of a title and body, so all pre-processing was done on both title and body features. Namely, the titles and bodies were tokenized for analysis of the words. 

When looking at text data, the amount of words used in the text is a beginning step into analysis. Below is the descriptive statisitics found for the word counts, for both the titles and bodies: <br>
#### Descriptive Statistics and Post Polarities/Subjectivities
**Descriptive Stats for the Amount of Words in the titles and bodies of posts, per subreddit** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/a4e92999-431f-4aee-9ab4-f6b863254ed6)
Based on the above, it can be said that each subreddit has a largely spread-out amount of words used in the posts, with some posts only containing a few words, with others containing thousands. 

#### Sentiment Analysis
To get an idea of whether the posts are genrally positive, negative, or neutral in nature, I found the subjectivity and polarity of each post's titles and bodies, using the TextBlob module. Below is the distribution of the polarities and subjectivities: <br>
**Distribution of the titles' and bodies' polarities and subjectivities** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/7556a000-ddaa-4577-8fde-26532bdde5cc) <br>
In terms of polarity, the closer to -1, the more negative sentiment, and the closer to +1, the more positive the sentiment. For subjectivity, the closer to 0, the more objective, and the closer to 1, the more subjective. <br>
In terms of polarity, it looks as if both the titles and the bodies are about normally distributed. For the titles, the polarities are overwhelmingly situated in the 0-0.25 bin, showing generally-neutral polarity. This also has influenced the mean polarity to be just over 0. The same can be said for the polarities of the bodies of the submissions, though there is a bit more values binned in the -0.25 - 0 bins and 0.25-0.5 bins. This is likely why the mean is a bit more than that of the titles' mean. <br> 
While the polarities for both titles and bodies show similar sentiment distributions, this cannot be said about the subjectivity between the two text types. For the titles, it looks like the majority of titles are objective, skewing right. For the bodies, there is an almost-normal distribution in subjectivity, with a slight bias towards being subjective, and about 1750 submission bodies being clearly subjective (subjectivity score between 0 and 0.1). The differences between the titles' and bodies' distributions may demonstrate that the users may want to create titles that are generally objective, and then add in their subjectivity when going into detail in the body of their post(s).

#### Topic Modeling 
The main purpose of Part B of this project is to find the topics that those with PCOS have the most concerns about. To do this, I created a function that applied pre-processing techniques and Latent Drichlett Allocation (LDA) for topic modeling, returning the topics. The LDAModel from the Gensim library was used. **Based on the dataset from part 1, I suspected the topics would be related to the features from that dataset, particularly the specific hormones.** 

After initially applying LDA, I chose random topics to get an idea of what topics were represented. If I found that some words were filler-like words, I would add them to the stopwords list in the pre-processing section of the function, and re-run the code to generate more accurate topics. Once I felt that the topics were more useful terms, I evaluated the topics by visualizing them in WordClouds, one for the titles and another for the bodies, and using human judgement. In each WordCloud, I chose to visualize up to 85 topics. <br> 
**WordCloud for Titles (using LDA)** <br>
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/52aa5c07-3a8b-41c9-bf12-77889ca34c48) <br>

**WordCloud for Bodies (using LDA)** <br> 
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/e8728bd2-3ac7-420b-a049-188f6f0fe7b1) <br>
Based on the above WordClouds, it seems that the main topics of the post have to deal with the overall health of the individual Redditors, from areas ranging from hormonal health to physical health. More about this will be discussed in the "Discussion" section.

The WordClouds only look at single terms. **What about common phrases (n-grams)?** For this, I used Gensim's Phrases to find the most common phases (in this case, bigrams). After creating the bigrams, each bigram's total appearances throughout the posts titles (or bodies) were accumulated, and the distributions visualized (below) <br>
**Bigrams Mentioned >100 times, for Bodies (note not all are labeled on the x-axis)** 
![pcos_bigrams_over_100](https://github.com/nisha-kaushal/PCOS/assets/100887571/a7ad79de-5d4f-4a18-8a88-d2f1bd44d558) <br>
Above, I chose the bigrams that appeared over 100 times. Note that the labels do not fully characterize each bar. Because there were so many, I chose to focus on those shown over 200 times (below)

**Bigrams Mentioned >200 times, for Bodies**
![pcos_bigrams_over_200](https://github.com/nisha-kaushal/PCOS/assets/100887571/ef23fdd5-c89d-42fc-b41c-faa76df5d5c7) <br>
From the above topics, I gather that, much like the topics found through the WordClouds, there are a few main topics that are widely talked about within the PCOS community, including: weight (including weight loss and gaining weright), insulin resistance, mestruation, hair, and pregnancy. More about this will be discussed in the "Discussion" section.

### Discussion Overview
Because this project is based on the idea that it would be of use for a company that is interested in creating an all-in-one supplement to assist in relieving PCOS symptoms, it is important to consider this hypothetical while discussing the project in detail, and will be referenced throughout the discussion. Refer to the notebooks for in-depth discussions. 

As shown in "PCOS Hormones", Polycystic Ovarian Syndrome can be predicted using different hormone levels, body features, and lifestyle choices. *Why does the prediction capabiloty matter to a company that is attempting to create an all-in-one supplement/medication that can relieve PCOS symptoms?*
When looking into what can potentially affect PCOS, creating and comparing classifiers may be a helpful option. We can pick and choose which features to include in the classifiers, and see how they affect the ability to predict whether the patients have PCOS or not. If there is a large drop in accuracy when a feature is dropped, we can assume that the feature does have a significant relationship with PCOS. This would eliminate the need to include an element in the all-in-one supplement that will specifically target any features that do not have siginificance in the prediction of PCOS. As a continuation of this first part of the project, if I were to continue, I would choose to create a Random Forest Classifier to do the comparisions mentioned, as it had the overall best accuracy output. 

To go back to the question of "what do those with PCOS tend to talk about the most with their fellow "cysters" (a common term that is used among those with PCOS to add a sense of community, though note it may not be considered inclusive of all bodies experiencing the disorder)?", it seems that my suspicion was *partly* correct: ***a large portion of topics covered in the subreddit submissions are related to weight and ovulation.*** This can be seen through the WordClouds and bigrams created. I did not expect there to be heavy emphasis on appearance, and supplements/medication. <br>
* **Appearance:** along with weight, it seems that many posters in the subreddits of interest are concerned about their hair and facial appearance. <br>
    * ***Why this makes sense:*** [At least 75% of those with PCOS have insulin resistance.](https://journals.sagepub.com/doi/pdf/10.2217/WHE.14.73) The excess insulin levels can cause the ovaries to over-produce testosterone. These heightened androgen levels can lead to **hirsutism**, excess female body and facial hair. Excess androgens in females can also cause **male-pattern baldness**. Generally, westernized society has been conditioned to believe that those who identify as female must have feminine features, including little-to-no facial hair. This standard set by westernized standards can cause mental and emotional distress to those who do not fit the norms, thus causing them to find ways to change in order to fit those standards (and increase the confidence that may have been diminished). These appearance-related topics (as well as a few other negatively-connotationed "topics"/"words" menationed, like "struggle") make me believe that the subredditors are trying to find suggestions to help change their features, by looking to others who may have successfully been able to do so. 
* **Supplements/Vitamins and Medication:** Based on the WordClouds, it looks like several posters are talking about potential supplements and medications that can be taken, possibly to alleviate PCOS symptoms. The most-mentioned of these is ***inositol***
    * ***Why this makes sense:*** With the lack of information about PCOS, many of those with PCOS are suggested to take medications that are used for different illnesses/disorders (e.g, metformin, which is usually for type II diabetes). Many are also suggested to take more "natural" supplements for various reasone, such as their insurance not covering the prescription medications, or if thy are trying to avoid prescribed drugs and prefer more natural approaches. Inositol is one of the most researched supplements for PCOS, and has been shown to [increase insulin sensitivity in those with PCOS, and decrease testosterone levels](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5655679/). The significant amount of posts with inositol as their topic could be the Redditors inquiring about potential dosage, safety, and potential reactions that others have experienced.
    
If a company wanted to look into a potential all-in-one supplenent to handle PCOS symptoms, it may be worth looking into the above concerns found through topic modeling, and then look into supplements that have already been researched for these symptoms, like inositol (finding that inositol is widely talked about in the community has given the idea to look into other potential supplements). After searching, the following are some other supplements that are taken, and why they have been shown to be successful in treating PCOS symptoms. <br> 
* **Berberine:** Berberine is a [yellow-colored chemical found in a few variety of plants](https://www.webmd.com/vitamins/ai/ingredientmono-1126/berberine), such as the European barberry, goldenseal, and Oregon grape. In [a clincial study](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8890747/) comparing the effects of berberine, metformin, and myo-inositol in those with PCOS, berberine has been found to show more potential to reduce cardiovascular disease risk than in PCOS, as the group that was administered berberine showed greater improvement in their clinical, hormonal, and lipid profiles. Based on this finding, Berberine would be able to assits in many of the concerns shown through the topics found in Part 3 of this notebook, including: weightloss, blood glucose levels, and cycle regulation. 
* **Spearmint:** Spearmint, a specific species of mint, has been shown to have [anti-androgenic effects](https://pubmed.ncbi.nlm.nih.gov/17310494/), with the ability to treat mild cases of hirsutism. 
* **Magnesium:** People with PCOS tend to be more likely to have lower levels of magnesium than those who do not have PCOS. Magnesium plays an [important role in glucose metabolism](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0058278#:~:text=Magnesium%20has%20been%20proposed%20to,type%202%20diabetes%20%5B28%5D.), through its interaction with tyrosine-kinase activity on the insulin receptor. The lack of magnesium can negatively influence glucose metabolism, leading to lessened insulin sensitivity/heightened insulin resistance. Taking magnesium supplements can assist in increasing insulin sensitivity/decreasing insulin resistance.
* **Omega-3s:** Popular sources of Omega-3s include fish (and fish oil), algae oil, and flaxseed (and flaxseed oil). Omega 3s have the potential to [decrease the cardiovascular disease risks](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5461594/) in those with PCOS, who tend to have heightened LDL (low-density lipoprotein). 
* **N-Acetyl Cysteine (NAC):** Cysteine is one of the amino acids found in the human body, which act as the building blocks for protein. NAC is the common supplement form, which is then converted into cysteine when consumed. NAC acts as a powerful antioxidant, and have been found to [decrease fasting glucose levels, decrease total testosterone and increase FSH levels](https://www.cambridge.org/core/journals/british-journal-of-nutrition/article/abs/effects-of-nacetylcysteine-on-ovulation-and-sex-hormones-profile-in-women-with-polycystic-ovary-syndrome-a-systematic-review-and-metaanalysis/411E42E184DE550924D72725D0519A45) in those with PCOS. 

While the above supplements have been shown to provide PCOS symptom relief, it is important to recognize that these supplements work on an individual basis, and not every supplement will be beneficial for every person with PCOS. Understanding the conversations surrounding PCOS can further provide insight into the symptoms that are overwhelmingly prevalent in the community, and through this understanding, it will be less challenging to find the components of an all-in-one supplement. 

### Pitfalls and Future Project Improvements
While developing this project, there were a few aspects relating to the data used that may have affected the models' accuracies and overall results, particularly in the "PCOS Hormones" section of the project, as this section is based on data that was previously collected from an outside party. The most significant of these aspects is the amount of data provided in the dataset. The dataset used included 541 patients, which, while large for the interest area (Kerala, India), classifiers would likely perform better with more data. In addition to the sparsity of the data, the data included in the dataset was imbalanced, meaning that the amount of patients included with PCOS was different from the amount of patients included who did not have PCOS. This can also affect the outcome of the classifiers, because classifiers overall tend to be biased towards the majority class. Imbalanced data also can affect the correlation between features, which is why we may not have seen many strong correlations between features, though according to the mechanisms of actions of the hormones discussed in detail, there likely should have been. To improve the quality of the outcome and analysis, I would collect more data, trying to balance the amount of those with PCOS and those without PCOS, or collect more data and then filter the majority class to be equal to that of the minority to achieve balance. 

