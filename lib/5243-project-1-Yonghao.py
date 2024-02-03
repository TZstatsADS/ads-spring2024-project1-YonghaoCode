#!/usr/bin/env python
# coding: utf-8

# # # Yonghao Xu Project 1

# My project aims to evaluate the relationship between Entertainment industry and people's happines, and what is the ratio that people feels happy beacuse of entertainment vs the whole sample happiness moments.

# First of all we need to attach all of the files we need to analysis and get a brief view of them.

# In[17]:


import pandas as pd
clean = pd.read_csv("cleaned_hm.csv")#read the clean data
clean["cleaned_hm"].head()


# In[18]:


demo = pd.read_csv("demographic.csv")# A brief view of demographic which include the person's information 
demo


# In[19]:


ent = pd.read_csv("entertainment-dict.csv")
ent


# Use R studio to get the clean data and absorb more key words of people's happy moment

# In[20]:


processed_moments = pd.read_csv("processed_moments.csv")#read the clean data
processed_moments


# In[21]:


new_filtered_dataset_df = pd.read_csv("filtered_dataset.csv")# A brief view of demographic which include the person's information 
new_filtered_dataset_df


# In[22]:


#分析男女
# Load the new versions of the filtered_dataset and entertainment-dict CSV files
new_filtered_dataset_df = pd.read_csv('filtered_dataset.csv')
new_entertainment_dict_df = pd.read_csv('entertainment-dict.csv')

# Analyzing gender ratio in the filtered dataset
gender_counts = new_filtered_dataset_df['gender'].value_counts()

# Extract the keywords from the 'movie' column
new_keywords = new_entertainment_dict_df['movie'].unique()

# Initialize dictionaries to hold the count of keywords for each gender
male_keyword_counts = {keyword: 0 for keyword in new_keywords}
female_keyword_counts = {keyword: 0 for keyword in new_keywords}

# Iterate through each row in the filtered_dataset dataframe
for _, row in new_filtered_dataset_df.iterrows():
    text = row['text']
    gender = row['gender']
    for keyword in new_keywords:
        if keyword in text:
            if gender == 'm':
                male_keyword_counts[keyword] += 1
            elif gender == 'f':
                female_keyword_counts[keyword] += 1

# Plotting gender ratio
plt.figure(figsize=(6, 6))
plt.pie(gender_counts, labels=gender_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Gender Ratio')
plt.axis('equal')
plt.show()

# Filter out keywords with low counts to avoid cluttering the charts
filtered_male_keyword_counts = {k: v for k, v in male_keyword_counts.items() if v > 10}
filtered_female_keyword_counts = {k: v for k, v in female_keyword_counts.items() if v > 10}


# In[23]:


# Plotting keyword proportions for males
plt.figure(figsize=(10, 8))
plt.pie(filtered_male_keyword_counts.values(), labels=filtered_male_keyword_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Keyword Proportions for Males')
plt.axis('equal')
plt.show()


# In[24]:


# Data for plotting
male_keywords = filtered_male_keyword_counts.keys()
male_counts = filtered_male_keyword_counts.values()

# Plotting the bar chart
plt.figure(figsize=(10, 8))
plt.bar(male_keywords, male_counts, color='blue')
plt.xlabel('Keywords')
plt.ylabel('Counts')
plt.title('Keyword Proportions for Males')
plt.xticks(rotation=90)  # Rotate the x labels to make them readable
plt.tight_layout()  # Adjust layout to make room for the x labels
plt.show()


# In[25]:


4# Plotting keyword proportions for females
plt.figure(figsize=(10, 8))
plt.pie(filtered_female_keyword_counts.values(), labels=filtered_female_keyword_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Keyword Proportions for Females')
plt.axis('equal')
plt.show()


# In[26]:


female_keywords = filtered_female_keyword_counts.keys()
female_counts = filtered_female_keyword_counts.values()

# Plotting the bar chart
plt.figure(figsize=(10, 8))
plt.bar(female_keywords, female_counts, color='pink')
plt.xlabel('Keywords')
plt.ylabel('Counts')
plt.title('Keyword Proportions for Females')
plt.xticks(rotation=90)  # Rotate the x labels to make them readable
plt.tight_layout()  # Adjust layout to make room for the x labels
plt.show()


# # What is the top 10 entertainment in USA?

# In[32]:


# Load the second file (entertainment-dict.csv) to extract the keywords
keywords_file_path = 'entertainment-dict.csv'
keywords_data = pd.read_csv(keywords_file_path)
# Load the first file (filtered_dataset.csv)
filtered_file_path = 'filtered_dataset.csv'
filtered_data = pd.read_csv(filtered_file_path)

from collections import defaultdict

# Extract the list of keywords
keywords_list = keywords_data['movie'].tolist()

# Initialize a dictionary to hold the count of keyword occurrences by country
country_keyword_counts = defaultdict(lambda: defaultdict(int))

# Search for keywords in the 'text' column and count occurrences by country
for _, row in filtered_data.iterrows():
    text = row['text']
    country = row['country']
    for keyword in keywords_list:
        if keyword in text:
            country_keyword_counts[country][keyword] += 1

country_keyword_counts

import matplotlib.pyplot as plt

# Select the country for the bar chart
country_for_bar_chart = 'USA'

# Get the top N keywords for the selected country
top_n = 10
top_keywords = dict(sorted(country_keyword_counts[country_for_bar_chart].items(), key=lambda item: item[1], reverse=True)[:top_n])

# Generate the bar chart
plt.figure(figsize=(10, 6))
plt.bar(top_keywords.keys(), top_keywords.values(), color='skyblue')
plt.title(f'Top {top_n} Keywords in {country_for_bar_chart}')
plt.xlabel('Keywords')
plt.ylabel('Occurrences')
plt.xticks(rotation=45, ha='right')
plt.show()


# # what about the entertainment for adults and minors?

# In[28]:


# Load the new versions of the filtered_dataset and entertainment-dict CSV files
new_age_filtered_dataset_df = pd.read_csv('filtered_dataset.csv')
new_age_entertainment_dict_df = pd.read_csv('entertainment-dict.csv')

# Convert the 'age' column to numeric values, coercing non-numeric entries to NaN
new_age_filtered_dataset_df['age'] = pd.to_numeric(new_age_filtered_dataset_df['age'], errors='coerce')

# Drop rows where 'age' is NaN after conversion
new_age_filtered_dataset_df = new_age_filtered_dataset_df.dropna(subset=['age'])

# Classify ages into adults and minors based on the age criteria
new_age_filtered_dataset_df['age_group'] = new_age_filtered_dataset_df['age'].apply(lambda x: 'Adult' if x >= 22 else 'Minor')

# Analyzing age group ratio in the filtered dataset
new_age_group_counts = new_age_filtered_dataset_df['age_group'].value_counts()

# Extract the keywords from the 'movie' column
new_age_keywords = new_age_entertainment_dict_df['movie'].unique()

# Initialize dictionaries to hold the count of keywords for each age group
new_adult_keyword_counts = {keyword: 0 for keyword in new_age_keywords}
new_minor_keyword_counts = {keyword: 0 for keyword in new_age_keywords}

# Iterate through each row in the filtered_dataset dataframe
for _, row in new_age_filtered_dataset_df.iterrows():
    text = row['text']
    age_group = row['age_group']
    for keyword in new_age_keywords:
        if keyword in text:
            if age_group == 'Adult':
                new_adult_keyword_counts[keyword] += 1
            elif age_group == 'Minor':
                new_minor_keyword_counts[keyword] += 1

# Plotting age group ratio
plt.figure(figsize=(6, 6))
plt.pie(new_age_group_counts, labels=new_age_group_counts.index, autopct='%1.1f%%', startangle=140)
plt.title('Age Group Ratio')
plt.axis('equal')
plt.show()


# In[29]:


# Filter out keywords with low counts to avoid cluttering the charts
filtered_new_adult_keyword_counts = {k: v for k, v in new_adult_keyword_counts.items() if v > 10}
filtered_new_minor_keyword_counts = {k: v for k, v in new_minor_keyword_counts.items() if v > 10}

# Plotting keyword proportions for adults
plt.figure(figsize=(10, 8))
plt.pie(filtered_new_adult_keyword_counts.values(), labels=filtered_new_adult_keyword_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Keyword Proportions for Adults')
plt.axis('equal')
plt.show()

# Plotting keyword proportions for minors
plt.figure(figsize=(10, 8))
plt.pie(filtered_new_minor_keyword_counts.values(), labels=filtered_new_minor_keyword_counts.keys(), autopct='%1.1f%%', startangle=140)
plt.title('Keyword Proportions for Minors')
plt.axis('equal')
plt.show()


# In[30]:


# Data for plotting
adult_keywords = filtered_new_adult_keyword_counts.keys()
adult_counts = filtered_new_adult_keyword_counts.values()

# Plotting the bar chart
plt.figure(figsize=(12, 8))
plt.bar(adult_keywords, adult_counts, color='brown')
plt.xlabel('Keywords')
plt.ylabel('Counts')
plt.title('Keyword Proportions for Adults')
plt.xticks(rotation=90)  # Rotate the x labels to make them readable
plt.tight_layout()  # Adjust layout to make room for the x labels
plt.show()

# Data for plotting
minor_keywords = filtered_new_minor_keyword_counts.keys()
minor_counts = filtered_new_minor_keyword_counts.values()

# Plotting the bar chart
plt.figure(figsize=(12, 8))
plt.bar(minor_keywords, minor_counts, color='green')
plt.xlabel('Keywords')
plt.ylabel('Counts')
plt.title('Keyword Proportions for Minors')
plt.xticks(rotation=90)  # Rotate the x labels to make them readable
plt.tight_layout()  # Adjust layout to make room for the x labels
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




