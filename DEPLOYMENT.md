# 🚀 Deployment Guide

This guide will help you deploy the AI Project web application to various platforms.

## Quick Start - Local Testing

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the web app locally:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser:**
   The app will automatically open at `http://localhost:8501`

## 🌐 Deploy to Streamlit Cloud (Recommended - Free)

Streamlit Cloud is the easiest way to deploy your app for free.

### Steps:

1. **Push to GitHub:**
   - Create a new repository on GitHub
   - Push all project files to the repository

2. **Deploy on Streamlit Cloud:**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account
   - Click "New app"
   - Select your repository
   - Set main file path to: `app.py`
   - Click "Deploy"

3. **Your app is live!**
   - Your app will be available at: `https://your-app-name.streamlit.app`
   - Updates are automatic when you push to GitHub

## 🚢 Deploy to Heroku

### Prerequisites:
- Heroku CLI installed
- Git repository

### Steps:

1. **Login to Heroku:**
   ```bash
   heroku login
   ```

2. **Create a new app:**
   ```bash
   heroku create your-app-name
   ```

3. **Deploy:**
   ```bash
   git push heroku main
   ```

4. **Open your app:**
   ```bash
   heroku open
   ```

## 🚂 Deploy to Railway

1. Go to [railway.app](https://railway.app)
2. Sign in with GitHub
3. Click "New Project"
4. Select "Deploy from GitHub repo"
5. Choose your repository
6. Railway will auto-detect Python and deploy
7. Add environment variable if needed: `PORT=8501`

## 🎨 Deploy to Render

1. Go to [render.com](https://render.com)
2. Sign in with GitHub
3. Click "New +" → "Web Service"
4. Connect your repository
5. Configure:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
6. Click "Create Web Service"

## 📦 Environment Variables

Some platforms may require these environment variables:

- `PORT`: Port number (usually auto-set by platform)
- `STREAMLIT_SERVER_PORT`: Streamlit server port
- `STREAMLIT_SERVER_ADDRESS`: Server address (use `0.0.0.0` for cloud)

## 🔧 Troubleshooting

### App won't start:
- Check that `requirements.txt` includes all dependencies
- Verify `app.py` is in the root directory
- Check platform logs for error messages

### Port issues:
- Ensure your start command includes `--server.port=$PORT`
- For Render/Railway, use `--server.address=0.0.0.0`

### Import errors:
- Make sure all Python files are in the same directory
- Check that all modules are properly imported

## 📝 Notes

- **Streamlit Cloud** is recommended for easiest deployment
- All platforms support automatic deployments from GitHub
- The app works on both free and paid tiers
- File size limits may apply on free tiers

## 🆘 Need Help?

- Check Streamlit documentation: [docs.streamlit.io](https://docs.streamlit.io)
- Platform-specific docs:
  - [Streamlit Cloud](https://docs.streamlit.io/streamlit-community-cloud)
  - [Heroku](https://devcenter.heroku.com)
  - [Railway](https://docs.railway.app)
  - [Render](https://render.com/docs)
