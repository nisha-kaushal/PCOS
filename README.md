# Polycystic Ovarian Syndrome, Inside and Out
### Why This Project? 
As per the [Center for Disease Control and Prevention (CDC)](https://www.cdc.gov/diabetes/basics/pcos.html#:~:text=What%20is%20PCOS%3F,beyond%20the%20child%2Dbearing%20years.), Polycystic Ovarian Syndrome (PCOS) affects 6-12% of all reproductive-aged women worldwide, and is one of the most common reasons for infertility. Though it is widely prevalent, it is also extremely under-researched, with no known underlying cause. With this personal project, I aim to gain an understanding of the hormonal/physiological aspects of PCOS ("PCOS Hormones" notebook), as well as get an understanding of the experiences that those with PCOS undego while living with the disorder ("PCOS Experience" notebook). 

### Goal
I have created this project with the mind of a hypothetical: how can the data provided be beneficial for a company who would like to create an all-in-one supplement to treat PCOS? 

I have separated this project into two parts, based on two parts: biological/hormonal factors, and the overall affects PCOS has on real people, based on personal experiences. For part 1 ("PCOS Hormones" notebook), the overall goal is to analyze the dataset provided to discover any relationshups between features, to compare these relationships with those that have already been found in scientific research studies, and build a binary classifier that can identify whether someone may have PCOS or not. 

For part 2 ("PCOS Experience" notebook), the goal is to gather personal experiences from Reddit users who have PCOS, and try to understand what the conversations are that occur within the PCOS community. Through information gathered directly from those who have PCOS, I attempt to find the most common topics discussed, and gain an idea of what topics should be considered when attempting to create an all-in-one supplement. 

### Data Sources
The dataset used in *"PCOS Hormones"* is from Kaggle, with the following credit: <br>
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
* Visualization (Matplotlib, Seaborn)

__PCOS Experience__:
* Python Programming
* Text Data Cleaning
* Exploratory Data Analysis
* Visualization (Matplotlib, Seaborn, WordCloud, Plotly)
* Feature Construction
* Natural Langauge Processing (Unsupervised Learning, Topic Modeling/Latent Drischlett Allocation/WordCloud)
* API usage/understanding 

### Results and Evaluation 
#### Part A. PCOS Hormones 

Correlation of Features of Interest in Those WITHOUT PCOS
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/9f257ba9-27f5-418e-a513-3b434a1ce1fe)

Correlation of Features of Interest in Those WITH PCOS
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/5453e443-72cc-4d43-936e-344d60d64611)

Correlation of Features of Interest Among All Participants
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/ca1a78f8-4817-4512-8222-e331c1341d2b)


Correlation of All Features Among All Participants
![image](https://github.com/nisha-kaushal/PCOS/assets/100887571/b9c1fe94-a965-4651-b874-900c9074af63)




#### Part B. PCOS Experience 

### Future Project Improvements


