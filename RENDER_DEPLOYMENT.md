# Render Deployment Guide for TaskFlow

This guide explains how to deploy TaskFlow on Render.com

## Prerequisites

- GitHub account with TaskFlow repository pushed
- Render account (https://render.com)
- Free tier is sufficient

## Deployment Steps

### Step 1: Prepare Repository

All files are ready:
- ✅ `Procfile` - Tells Render how to run the app
- ✅ `requirements.txt` - Python dependencies with gunicorn
- ✅ `main.py` - Entry point for Gunicorn
- ✅ `.env.example` - Configuration template

### Step 2: Create Render Web Service

1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Select "GitHub" and authorize
4. Choose `taskflow-app` repository
5. Fill in details:
   - **Name:** `taskflow-api` (or your choice)
   - **Environment:** `Python 3`
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn -w 4 -b 0.0.0.0:$PORT main:app`
   - **Instance Type:** Free

### Step 3: Configure Environment Variables

In Render Dashboard → Your Service → Environment:

Add these variables:
```
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
FRONTEND_URL=https://ashish-yadav10.github.io/taskflow-app
```

### Step 4: Deploy

Click "Create Web Service" and wait for deployment (2-3 minutes)

Your backend URL will be: `https://taskflow-api.onrender.com`

### Step 5: Update Frontend

Update `frontend/app.js` and `docs/app.js`:

Change API base URL from:
```javascript
const API_BASE_URL = 'http://127.0.0.1:8000';
```

To:
```javascript
const API_BASE_URL = 'https://taskflow-api.onrender.com';
```

### Step 6: Deploy Frontend to GitHub Pages

GitHub Pages is already enabled for `/docs` folder
- Frontend will be live at: `https://ashish-yadav10.github.io/taskflow-app/`
- Backend will be live at: `https://taskflow-api.onrender.com`

---

## Troubleshooting

### Service won't start
- Check build logs in Render dashboard
- Verify `requirements.txt` has all dependencies
- Check `Procfile` syntax

### CORS errors
- Make sure `FRONTEND_URL` is set in Environment variables
- CORS is auto-configured to allow GitHub Pages

### Database issues (SQLite)
- SQLite works on Render but data is ephemeral (lost on redeploy)
- For persistent data, upgrade to PostgreSQL (Render offers free tier)

---

## Next: PostgreSQL for Production

For production with persistent data:
1. Create Render PostgreSQL Database
2. Update `DATABASE_URL` environment variable
3. Update `backend/database.py` to use PostgreSQL connection string
4. Redeploy
