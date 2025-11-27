# YouTube Global Trends Analysis 📊

A comprehensive data analysis project examining YouTube trending videos across 10 countries to uncover patterns in views, likes, categories, and engagement metrics. This analysis combines datasets from multiple regions to understand what makes videos go viral globally.

## 📋 Table of Contents

Overview
Dataset
Key Questions
Installation
Project Structure
Analysis Workflow
Key Findings
Visualizations
Future Enhancements
Author

## 🎯 Overview
This project analyzes YouTube trending videos from 10 countries (CA, DE, FR, GB, IN, JP, KR, MX, RU, US) covering the period from November 2017 to June 2018. The analysis includes:

Data cleaning and preprocessing of 375,942+ trending video records
Category mapping and feature engineering
Exploratory Data Analysis (EDA)
Cross-country and cross-category comparisons
Trend identification and correlation analysis
Engagement metrics and virality patterns

Dataset Source: Kaggle - YouTube Trending Videos
Link: https://www.kaggle.com/datasets/datasnaek/youtube-new
## 📊 Dataset
Files Structure

CSV Files: Country-specific video data (e.g., USvideos.csv, CAvideos.csv)
JSON Files: Category ID mappings (e.g., US_category_id.json)

Key Columns

video_id, trending_date, title, channel_title
category_id, publish_time, tags
views, likes, dislikes, comment_count
comments_disabled, ratings_disabled, video_error_or_removed
thumbnail_link, description

Dataset Statistics

Total Records: 375,942 (reduced to 323,730 after deduplication)
Countries: 10
Time Period: Late 2017 to Mid-2018
Categories: 18 (Music, Entertainment, Comedy, Gaming, etc.)

## ❓ Key Questions

What categories receive the most views globally?
How do engagement metrics vary across countries and categories?
Are there seasonal trends in video performance?
Which channels dominate in total views vs. engagement rate?
How quickly do videos trend after publishing?
What are the most common tags used in trending videos?

## 🛠️ Installation
Prerequisites
bashPython 3.8+
pip install pandas matplotlib seaborn numpy
Setup
bash# Clone the repository
```
git clone https://github.com/poorvapathak/YouTube-Global-Trends-Analysis.git
cd YouTube-Global-Trends-Analysis
```

# Run the Jupyter notebook
```
jupyter notebook YouTube_Global_Trends_Analysis.ipynb
```

## 🔄 Analysis Workflow
1. Data Collection & Combination

Upload country-specific CSV and JSON files
Combine datasets with country labels
Result: 375,942 rows × 17 columns

2. Category Mapping

Map numeric category IDs to human-readable names
Merge category mappings from all JSON files
Handle missing categories with 'Unknown' fallback

3. Data Cleaning

Convert trending_date to datetime format
Fill missing descriptions
Cast boolean columns for efficiency
Final Dataset: 44.1 MB, no null values

4. Feature Engineering
Created new metrics:

Engagement Rate: (likes + comments) / views
Trend Lag Days: Days between publish and trending dates
Month: Extracted from trending_date for seasonal analysis

5. Outlier Handling

Detected outliers using boxplots
Capped views and likes at 99th percentile (~17.9M views)
Improved statistical robustness without data loss

6. Deduplication

Removed duplicate video-date combinations
Reduced dataset to 323,730 unique trending instances

7. Exploratory Data Analysis
Comprehensive analysis including:

Descriptive statistics
Category and country aggregations
Channel rankings
Tag frequency analysis
Correlation matrices
Time-series trends

## 🔍 Key Findings
Top Categories by Average Views

Music - 6.02M avg views
Movies - 1.95M avg views
Film & Animation - 1.32M avg views
Science & Technology - 1.13M avg views
Entertainment - 959K avg views

<img width="1458" height="810" alt="image" src="https://github.com/user-attachments/assets/4505dab8-d8b6-4970-ab3f-40bcc1d008bb" />

Top Channels by Total Views

Marvel Entertainment - 2.04B total views
Dude Perfect - 2.00B total views
jypentertainment - 1.76B total views
20th Century Fox - 1.74B total views
ibighit - 1.71B total views

Engagement Insights

Highest Engagement: Howto & Style (6.25%)
Lowest Engagement: Trailers (0.64%)
Correlation: Higher views often correlate with lower relative engagement (Music: -0.24)

Trending Speed

Fastest: News & Politics (2.5 days average lag)
Slowest: Education (19.2 days average lag)
Insight: Timely content trends faster; evergreen content takes longer

Regional Variations

GB has 243% more Music videos than CA
US leads in Howto & Style (73% more than CA)
IN has highest News & Politics representation
JP and KR show distinct preferences in Gaming and Entertainment

<img width="1779" height="876" alt="image" src="https://github.com/user-attachments/assets/c3bc30cc-869a-4443-a813-490cf8e0d9dd" />

Tag Analysis
Most Common Tags:

[none] - 34,031 occurrences

"funny" - 11,604

"2018" - 9,672

"comedy" - 9,380

"news" - 5,261

Temporal Trends

Peak Period: May-June 2018 (~1.6M avg views)
Growth Pattern: Steady increase from November 2017
Seasonal Effect: Spring/summer months show higher engagement

<img width="1771" height="878" alt="image" src="https://github.com/user-attachments/assets/e1b3e717-15f7-4d9a-8bf3-42766b59061d" />

Correlation Matrix Insights

Views-Likes: Strong positive correlation (0.86)
Views-Engagement Rate: Slight negative correlation (-0.067)
Comments-Likes: Moderate correlation (0.52)
Dislikes-Comments: Strong correlation (0.74) - controversial content drives discussion

<img width="1096" height="950" alt="image" src="https://github.com/user-attachments/assets/dd9de601-2c4c-4732-a559-2922cdf96c00" />

## 📈 Visualizations
The project includes multiple visualizations:

Category Performance

Bar chart of top categories by views

<img width="1454" height="810" alt="image" src="https://github.com/user-attachments/assets/be3321bd-b838-4b75-86c8-bd1c9cae7cfc" />


Time-Series Analysis

Category performance over time
Country-specific trends
<img width="987" height="499" alt="image" src="https://github.com/user-attachments/assets/90ba734e-c15a-44f2-86ab-ea97327ae9a7" />
<img width="1004" height="492" alt="image" src="https://github.com/user-attachments/assets/2cdfe0f6-dc47-47d4-8138-b8eff114e568" />


## 🚀 Future Enhancements

 Machine Learning Models: Predict video virality using features like tags, lag, and category
 Interactive Dashboards: Build Plotly/Dash visualizations for dynamic exploration
 Sentiment Analysis: Analyze comment sentiment (requires additional data)
 Real-Time Analysis: Update with current YouTube trending data
 Network Analysis: Explore channel collaborations and cross-promotions
 Deep Learning: Implement NLP for title/description analysis
 A/B Testing Framework: Optimize content strategies based on findings

## 💡 Recommendations for Content Creators
Based on the analysis:

1. Category Selection: Focus on Music or Entertainment for maximum views
2. Engagement Strategy: Target Howto & Style or Gaming for higher interaction
3. Timing: Publish News content for quick trending; Education for long-term growth
4. Tagging: Use simple, descriptive tags like "funny", "2018", category-specific keywords
5. Regional Targeting: Tailor content to regional preferences (e.g., Music for GB/US)
6. Optimal Period: Aim for spring/summer releases for peak performance
7. Engagement Tactics: Include giveaways, challenges, or interactive elements

## 📝 Limitations

Data covers only November 2017 to June 2018
Limited to 10 countries
Does not include video content analysis (thumbnails, audio, etc.)
Comment sentiment data not available
Algorithm changes since 2018 may affect current applicability

## 👨‍💻 Author
Poorva Pathak

Date: 20 September 2025

## 🙏 Acknowledgments

Dataset provided by Kaggle.

Built with Python, Pandas, Matplotlib, and Seaborn.

Inspired by the need to understand global content virality patterns.


### ⭐ If you find this project useful, please consider giving it a star!
