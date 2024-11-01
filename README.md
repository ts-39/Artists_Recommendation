# Artists Recommendation System

This repository contains a recommendation system for music artists, designed to suggest artists based on user preferences collected through a survey. The system leverages the Pearson similarity algorithm to calculate similarities between artists based on users' input, providing personalized recommendations.

## Features

- **Survey-Based Data Collection**: Data on user preferences were collected through a survey, allowing for a personalized recommendation experience.
- **Pearson Similarity Algorithm**: Used to measure the similarity between users' preferences, enhancing recommendation accuracy.
- **User-Centered Recommendations**: Tailored artist suggestions based on each user's unique taste.

## Lessons Learned

Due to a limited dataset, the recommendations may lack variety. This experience underscored the importance of having a substantial dataset to improve the quality and diversity of recommendations.

## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/ts-39/Artists_Recommendation.git
   cd Artists_Recommendation
   ```

2. **Run the recommendation system**:
   ```bash
   python main.py
   ```

3. **Input User Preferences**: Follow the prompts to input user preferences, which will then be used to generate artist recommendations.

## Future Improvements

To improve the model's accuracy and variety in recommendations, future work will focus on increasing the dataset size and exploring alternative similarity algorithms.
