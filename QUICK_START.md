# ⚡ Quick Start - Deploy to GitHub & Streamlit Cloud

## 🎯 Quick Steps (5 minutes)

### 1️⃣ Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. Repository name: `ai-project`
3. Description: `AI algorithms with interactive web interface`
4. Choose **Public**
5. **DO NOT** check any boxes (no README, .gitignore, license)
6. Click **"Create repository"**

### 2️⃣ Push Your Code

Copy and run these commands (replace `YOUR_USERNAME` with your GitHub username):

```bash
cd "d:\Ai project"
git remote add origin https://github.com/YOUR_USERNAME/ai-project.git
git branch -M main
git push -u origin main
```

**If asked for credentials:**
- Username: Your GitHub username
- Password: Use a **Personal Access Token** (not your password)
  - Get token: GitHub → Settings → Developer settings → Personal access tokens → Generate new token

### 3️⃣ Deploy to Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"Sign in"** → Sign in with GitHub
3. Click **"New app"**
4. Select repository: `YOUR_USERNAME/ai-project`
5. Main file: `app.py`
6. Click **"Deploy"**

**Done!** Your app is live at: `https://ai-project-YOUR_USERNAME.streamlit.app`

---

## 🔄 Update Your App Later

```bash
git add .
git commit -m "Your update message"
git push
```

Streamlit Cloud will automatically update! ✨

---

## ❓ Need Help?

See `GITHUB_SETUP.md` for detailed instructions.
