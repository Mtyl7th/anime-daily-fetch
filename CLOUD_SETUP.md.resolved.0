# Cloud Setup Guide (GitHub Actions)

Follow these steps to migrate your anime image agent to the cloud.

## 1. Create a GitHub Repository
1.  Go to [GitHub.com](https://github.com) and sign in.
2.  Click the **+** icon in the top right and select **New repository**.
3.  Name it (e.g., `anime-daily-fetch`).
4.  Make it **Public** (required for free GitHub Pages) or Private (if you have Pro).
5.  Click **Create repository**.

## 2. Upload Code
Open your terminal and run these commands to push your code:

```bash
cd /Users/linchuan/.gemini/antigravity/brain/4838b3fe-93ca-44a3-ba32-d37f4b912c9b
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/anime-daily-fetch.git
git push -u origin main
```
*(Replace `<YOUR_USERNAME>` with your actual GitHub username)*

## 3. Enable Permissions
The agent needs permission to save images back to the repository.
1.  Go to your repository **Settings**.
2.  Click **Actions** > **General** in the sidebar.
3.  Scroll down to **Workflow permissions**.
4.  Select **Read and write permissions**.
5.  Click **Save**.

## 4. Enable Gallery (GitHub Pages)
To view your images online:
1.  Go to **Settings** > **Pages**.
2.  Under **Build and deployment** > **Source**, select **Deploy from a branch**.
3.  Select **main** branch and **/(root)** folder.
4.  Click **Save**.
5.  Your gallery will be available at: `https://<YOUR_USERNAME>.github.io/anime-daily-fetch/images/gallery.html`

## 5. Done!
- The workflow `Daily Anime Image Fetcher` will run automatically every day at 10:00 AM (Beijing Time).
- You can manually trigger it in the **Actions** tab to test it.
