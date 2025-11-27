# YouTube Global Trends Analysis 📊

A comprehensive data analysis project examining YouTube trending videos across 10 countries to uncover patterns in views, likes, categories, and engagement metrics. This analysis combines datasets from multiple regions to understand what makes videos go viral globally.

## 📋 Table of Contents

1. Overview
2. Dataset
3. Key Questions
4. Installation
5. Project Structure
6. Analysis Workflow
7. Key Findings
8. Visualizations
9. Future Enhancements
10. Author

## 🎯 Overview
This project analyzes YouTube trending videos from 10 countries USA, Great Britain, Germany, Canada, France, Russia, Mexico, South Korea, Japan and India (US, GB, DE, CA, FR, RU, MX, KR, JP and IN, respectively) covering the period from November 2017 to June 2018. The analysis includes:

1. Data cleaning and preprocessing of 375,942+ trending video records
2. Category mapping and feature engineering
3. Exploratory Data Analysis (EDA)
4. Cross-country and cross-category comparisons
5. Trend identification and correlation analysis
6. Engagement metrics and virality patterns

Dataset Source: Kaggle - YouTube Trending Videos
Link: https://www.kaggle.com/datasets/datasnaek/youtube-new
## 📊 Dataset
#### Files Structure

CSV Files: Country-specific video data (e.g., USvideos.csv, CAvideos.csv)
JSON Files: Category ID mappings (e.g., US_category_id.json)

#### Key Columns

video_id, trending_date, title, channel_title
category_id, publish_time, tags
views, likes, dislikes, comment_count
comments_disabled, ratings_disabled, video_error_or_removed
thumbnail_link, description

#### Dataset Statistics

Total Records: 375,942 (reduced to 323,730 after deduplication)
Countries: 10
Time Period: Late 2017 to Mid-2018
Categories: 18 (Music, Entertainment, Comedy, Gaming, etc.)

## ❓ Key Questions

1. What categories receive the most views globally?
2. How do engagement metrics vary across countries and categories?
3. Are there seasonal trends in video performance?
4. Which channels dominate in total views vs. engagement rate?
5. How quickly do videos trend after publishing?
6. What are the most common tags used in trending videos?

## 🛠️ Installation
#### Prerequisites
```
Python 3.8+
pip install pandas matplotlib seaborn numpy
```

#### Clone the repository
```
git clone https://github.com/poorvapathak/YouTube-Global-Trends-Analysis.git
cd YouTube-Global-Trends-Analysis
```

#### Run the Jupyter notebook
```
jupyter notebook YouTube_Global_Trends_Analysis.ipynb
```

## 🔄 Analysis Workflow
#### 1. Data Collection & Combination

- Upload country-specific CSV and JSON files
- Combine datasets with country labels
- Result: 375,942 rows × 17 columns

#### 2. Category Mapping

- Map numeric category IDs to human-readable names
- Merge category mappings from all JSON files
- Handle missing categories with 'Unknown' fallback

#### 3. Data Cleaning

- Convert trending_date to datetime format
- Fill missing descriptions
- Cast boolean columns for efficiency
- Final Dataset: 44.1 MB, no null values

#### 4. Feature Engineering
Created new metrics:

- Engagement Rate: (likes + comments) / views
- Trend Lag Days: Days between publish and trending dates
- Month: Extracted from trending_date for seasonal analysis

#### 5. Outlier Handling

- Detected outliers using boxplots
- Capped views and likes at 99th percentile (~17.9M views)
- Improved statistical robustness without data loss

#### 6. Deduplication

- Removed duplicate video-date combinations
- Reduced dataset to 323,730 unique trending instances

#### 7. Exploratory Data Analysis
Comprehensive analysis including:

- Descriptive statistics
- Category and country aggregations
- Channel rankings
- Tag frequency analysis
- Correlation matrices
- Time-series trends

## 🔍 Key Findings
#### Top Categories by Average Views

1.Music - 6.02M avg views
2. Movies - 1.95M avg views
3. Film & Animation - 1.32M avg views
4. Science & Technology - 1.13M avg views
5. Entertainment - 959K avg views

<img width="1458" height="810" alt="image" src="https://github.com/user-attachments/assets/4505dab8-d8b6-4970-ab3f-40bcc1d008bb" />

#### Top Channels by Total Views

1. Marvel Entertainment - 2.04B total views
2. Dude Perfect - 2.00B total views
3. jypentertainment - 1.76B total views
4. 20th Century Fox - 1.74B total views
5. ibighit - 1.71B total views

#### Engagement Insights

1. Highest Engagement: Howto & Style (6.25%)
2. Lowest Engagement: Trailers (0.64%)
3. Correlation: Higher views often correlate with lower relative engagement (Music: -0.24)

#### Trending Speed

1.Fastest: News & Politics (2.5 days average lag)
2. Slowest: Education (19.2 days average lag)
3. Insight: Timely content trends faster; evergreen content takes longer

#### Regional Variations

1. GB has 243% more Music videos than CA
2. US leads in Howto & Style (73% more than CA)
3. IN has highest News & Politics representation
4. JP and KR show distinct preferences in Gaming and Entertainment

<img width="1779" height="876" alt="image" src="https://github.com/user-attachments/assets/c3bc30cc-869a-4443-a813-490cf8e0d9dd" />

#### Tag Analysis
Most Common Tags:

[none] - 34,031 occurrences

"funny" - 11,604

"2018" - 9,672

"comedy" - 9,380

"news" - 5,261

#### Temporal Trends

1. Peak Period: May-June 2018 (~1.6M avg views)
2. Growth Pattern: Steady increase from November 2017
3. Seasonal Effect: Spring/summer months show higher engagement

<img width="1771" height="878" alt="image" src="https://github.com/user-attachments/assets/e1b3e717-15f7-4d9a-8bf3-42766b59061d" />

#### Correlation Matrix Insights

1. Views-Likes: Strong positive correlation (0.86)
2. Views-Engagement Rate: Slight negative correlation (-0.067)
3. Comments-Likes: Moderate correlation (0.52)
4. Dislikes-Comments: Strong correlation (0.74) - controversial content drives discussion

<img width="1096" height="950" alt="image" src="https://github.com/user-attachments/assets/dd9de601-2c4c-4732-a559-2922cdf96c00" />

## 📈 Visualizations
The project includes multiple visualizations:

#### Category Performance

Bar chart of top categories by views

<img width="1454" height="810" alt="image" src="https://github.com/user-attachments/assets/be3321bd-b838-4b75-86c8-bd1c9cae7cfc" />


#### Time-Series Analysis

Category performance over time
Country-specific trends
<img width="987" height="499" alt="image" src="https://github.com/user-attachments/assets/90ba734e-c15a-44f2-86ab-ea97327ae9a7" />
<img width="1004" height="492" alt="image" src="https://github.com/user-attachments/assets/2cdfe0f6-dc47-47d4-8138-b8eff114e568" />


## 🚀 Future Enhancements

- Machine Learning Models: Predict video virality using features like tags, lag, and category
- Interactive Dashboards: Build Plotly/Dash visualizations for dynamic exploration
- Sentiment Analysis: Analyze comment sentiment (requires additional data)
- Real-Time Analysis: Update with current YouTube trending data
- Network Analysis: Explore channel collaborations and cross-promotions
- Deep Learning: Implement NLP for title/description analysis
- A/B Testing Framework: Optimize content strategies based on findings

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

- Data covers only November 2017 to June 2018
- Limited to 10 countries
- Does not include video content analysis (thumbnails, audio, etc.)
- Comment sentiment data not available
- Algorithm changes since 2018 may affect current applicability

## 👨‍💻 Author
Poorva Pathak

Date: 20 September 2025

## 🙏 Acknowledgments

- Dataset provided by Kaggle.

- Built with Python, Pandas, Matplotlib, and Seaborn.

- Inspired by the need to understand global content virality patterns.


### ⭐ If you find this project useful, please consider giving it a star!
