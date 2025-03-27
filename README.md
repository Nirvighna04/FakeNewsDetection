# Fake News Detection

## Overview
This project is a machine learning-based system designed to detect fake news from user-input text or extracted content from a news article link. It utilizes various classification models and an interactive web interface for real-time predictions.

## Features
- **Machine Learning Models**: Implements Logistic Regression, Decision Tree, and Random Forest for classification.
- **Text Processing**: Utilizes TF-IDF vectorization for efficient feature extraction from news content.
- **Web Scraping**: Uses BeautifulSoup to extract news content from provided URLs.
- **Interactive UI**: Built with Streamlit, allowing users to input text or provide a link for fake news detection.
- **Real-time Prediction**: Provides instant feedback on whether the given news is likely to be fake or real.

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/fake-news-detection.git
   cd fake-news-detection
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

## Usage
Run the application using the following command:
```sh
streamlit run app.py
```

### How to Use
- Enter news text manually or paste a news article URL.
- Click the "Predict" button to check if the news is fake or real.
- View the classification result instantly.

## Dataset
The model is trained on a publicly available fake news dataset, preprocessed using TF-IDF vectorization.

## Technologies Used
- Python
- Scikit-learn
- BeautifulSoup
- Streamlit
- Pandas & NumPy

## Model Performance
- Achieved high accuracy with Random Forest being the best-performing model.
- Performance evaluation was done using precision, recall, and F1-score metrics.

## Contributing
Contributions are welcome! Feel free to submit issues or pull requests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Author
Developed by Nirvighna Datar.

## Acknowledgements
- Thanks to the creators of the datasets used for model training.
- Inspired by various machine learning projects on fake news detection.

## Contact
For any queries, feel free to reach out via [GitHub Issues](https://github.com/Nirvighna04/fake-news-detection/issues).
