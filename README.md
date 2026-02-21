# AI Project - Search Algorithms & Machine Learning

A Python project demonstrating various AI algorithms including search algorithms and machine learning classifiers with both **interactive command-line interface** and **web application**.

## 🌐 Live Demo

**👉 [Try the Web App Online](https://ai-project-29salahmo.streamlit.app)** *(Deploy on Streamlit Cloud to activate this link)*

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://ai-project-29salahmo.streamlit.app)

## 🚀 Features

- **Uniform Cost Search**: Finds the shortest path in a weighted graph
- **Greedy Search**: Pathfinding using heuristic-based search
- **Decision Tree Classifier**: Binary classification on the Iris dataset

## 📋 Requirements

- Python 3.7 or higher
- Required packages (see `requirements.txt`)

## 🔧 Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd "Ai project"
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

## 🚀 Quick Deployment

**Ready to deploy?** See `QUICK_START.md` for a 5-minute setup guide!

**For detailed instructions:**
- `GITHUB_SETUP.md` - Complete GitHub setup guide
- `DEPLOYMENT.md` - Deployment options for all platforms
- `SETUP_INSTRUCTIONS.txt` - Step-by-step instructions

## 💻 Usage

### 🌐 Web Application (Recommended)

Run the Streamlit web application:
```bash
streamlit run app.py
```

The web app will open in your browser at `http://localhost:8501`

**Features:**
- Beautiful, interactive web interface
- Real-time algorithm execution
- Visual results and graphs
- Custom graph input support
- Decision tree visualization

### 💻 Command-Line Interface

Run the interactive main menu:
```bash
python main.py
```

The menu will allow you to:
1. Run Uniform Cost Search with custom or default graphs
2. Run Greedy Search algorithm
3. Train and evaluate a Decision Tree Classifier on the Iris dataset
4. Exit the program

### Running Individual Scripts

You can also run each algorithm independently:

```bash
# Uniform Cost Search
python uniform_cost_search.py

# Greedy Search
python greedy_search.py

# Decision Tree Classifier
python decision_tree_classifier.py
```

## 📖 Algorithm Details

### Uniform Cost Search
- Finds the optimal path (lowest cost) from start to goal
- Uses a priority queue to explore nodes in order of increasing cost
- Guarantees finding the shortest path if one exists

### Greedy Search
- Uses a heuristic function to guide the search
- Always expands the node that appears closest to the goal
- Fast but may not find the optimal solution

### Decision Tree Classifier
- Trains a decision tree on the Iris dataset
- Performs binary classification (Setosa vs. Non-Setosa)
- Displays accuracy, classification report, and confusion matrix
- Optional visualization of the decision tree

## 🌐 Web Deployment

### Deploy to Streamlit Cloud (Free & Easy)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Click "New app"
5. Select your repository and set main file to `app.py`
6. Click "Deploy"

Your app will be live at `https://your-app-name.streamlit.app`

### Deploy to Heroku

1. Install Heroku CLI
2. Login: `heroku login`
3. Create app: `heroku create your-app-name`
4. Deploy: `git push heroku main`

### Deploy to Other Platforms

The app can be deployed to any platform that supports Python:
- **Railway**: Connect GitHub repo, auto-deploys
- **Render**: Connect GitHub repo, set build command: `pip install -r requirements.txt` and start command: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
- **PythonAnywhere**: Upload files and run `streamlit run app.py`

## 📁 Project Structure

```
Ai project/
├── app.py                       # Streamlit web application
├── main.py                      # Interactive CLI menu
├── uniform_cost_search.py       # Uniform Cost Search implementation
├── greedy_search.py             # Greedy Search implementation
├── decision_tree_classifier.py  # Decision Tree Classifier
├── requirements.txt             # Python dependencies
├── Procfile                     # Heroku deployment config
├── setup.sh                     # Setup script for deployment
├── streamlit_config.toml        # Streamlit configuration
├── README.md                    # This file
└── .gitignore                  # Git ignore file
```

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

**Salah El Dein** - [@29SalahMo](https://github.com/29SalahMo)

## 🙏 Acknowledgments

- Scikit-learn for machine learning tools
- Iris dataset for classification examples
