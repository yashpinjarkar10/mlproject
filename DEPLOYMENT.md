# 🚀 Deployment Guide for Hugging Face Spaces

This guide will help you deploy the Student Performance Predictor on Hugging Face Spaces using Docker.

## 📋 Prerequisites

1. A Hugging Face account ([Sign up here](https://huggingface.co/join))
2. Git installed on your local machine
3. Your trained model artifacts (should be in the `artifacts/` folder)

## 🔧 Deployment Steps

### Step 1: Create a New Space

1. Go to [Hugging Face Spaces](https://huggingface.co/spaces)
2. Click "Create new Space"
3. Fill in the details:
   - **Space name**: `student-performance-predictor` (or your preferred name)
   - **License**: MIT
   - **SDK**: Docker
   - **Space hardware**: CPU basic (free tier)

### Step 2: Clone Your Space Repository

```bash
git clone https://huggingface.co/spaces/YOUR_USERNAME/student-performance-predictor
cd student-performance-predictor
```

### Step 3: Copy Your Project Files

Copy the following files from your ML project to the Spaces repository:

```bash
# Essential files
cp /path/to/your/project/Dockerfile .
cp /path/to/your/project/requirements.txt .
cp /path/to/your/project/app.py .
cp /path/to/your/project/README.md .

# Copy source code
cp -r /path/to/your/project/src/ .
cp -r /path/to/your/project/templates/ .

# Copy trained model artifacts
cp -r /path/to/your/project/artifacts/ .

# Copy data (if needed)
cp -r /path/to/your/project/notebook/data/ .
```

### Step 4: Verify Space Configuration

Make sure your `README.md` file starts with the proper Hugging Face Spaces configuration header:

```yaml
---
title: Student Performance Predictor
emoji: 🎓
colorFrom: blue
colorTo: purple
sdk: docker
sdk_version: "latest"
app_file: app.py
pinned: false
license: mit
---
```

This configuration should be at the very top of your README.md file, followed by your project documentation.

### Step 5: Verify Docker Configuration

Make sure your `Dockerfile` is properly configured:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE=1 \\
    PYTHONUNBUFFERED=1 \\
    FLASK_APP=app.py \\
    FLASK_ENV=production

RUN apt-get update && apt-get install -y \\
    gcc \\
    g++ \\
    && rm -rf /var/lib/apt/lists/*

COPY requirements_docker.txt requirements.txt
RUN pip install --no-cache-dir --upgrade pip && \\
    pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p logs artifacts && \\
    chmod -R 755 /app

EXPOSE 7860

HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \\
    CMD curl -f http://localhost:7860/ || exit 1

CMD ["python", "app.py"]
```

### Step 6: Deploy to Hugging Face Spaces

```bash
# Add all files
git add .

# Commit changes
git commit -m "Initial deployment: Student Performance Predictor ML app"

# Push to Hugging Face Spaces
git push origin main
```

### Step 7: Monitor Deployment

1. Go to your Space URL: `https://huggingface.co/spaces/YOUR_USERNAME/student-performance-predictor`
2. Watch the build logs in the "Logs" tab
3. Once built successfully, your app will be available at the Space URL

## 🔍 Troubleshooting

### Common Issues

1. **Permission Denied Errors (logs/artifacts)**:
   - **Issue**: `PermissionError: [Errno 13] Permission denied: '/app/logs/...'`
   - **Solution**: The updated Dockerfile creates directories with proper permissions
   - **Fallback**: Logger automatically falls back to console logging if file logging fails

2. **Build Timeout**: If the build takes too long, consider:
   - Using smaller/more specific package versions
   - Removing unnecessary dependencies
   - Using multi-stage Docker builds

3. **Memory Issues**: 
   - Use CPU basic tier for initial deployment
   - Optimize model size if needed
   - Consider model compression techniques

4. **Port Issues**: 
   - Ensure your app listens on port 7860
   - Check the `app_port: 7860` in README.md header

5. **File Not Found Errors**:
   - Verify all artifacts are copied correctly
   - Check file paths in your code
   - Ensure model files exist in the artifacts folder

### Docker Environment Fixes

The current setup includes several Docker-specific fixes:

- **Robust Logging**: Falls back to console logging if file permissions fail
- **Multiple Log Locations**: Tries `/app/logs`, `/tmp/logs`, and `/tmp` directories
- **Proper Permissions**: Creates directories with 777 permissions for HF Spaces
- **Error Handling**: Graceful degradation when logging setup fails

### Build Optimization Tips

1. **Layer Caching**: Requirements are copied first for better caching
2. **Image Size**: Using Python slim image reduces build time
3. **Dependencies**: Only essential packages in requirements_docker.txt

## 📊 Performance Considerations

- **Cold Start**: First request may take longer as the container starts
- **Resource Limits**: Free tier has CPU and memory limitations
- **Concurrent Users**: Consider upgrading to paid tiers for production use

## 🔄 Updates and Maintenance

To update your deployment:

```bash
# Make changes to your code
# Commit and push changes
git add .
git commit -m "Update: [describe your changes]"
git push origin main
```

The Space will automatically rebuild and redeploy.

## 📞 Support

If you encounter issues:

1. Check the Space logs for error messages
2. Verify your Dockerfile and requirements
3. Test locally with Docker before deploying
4. Consult Hugging Face Spaces documentation

---

🎉 **Congratulations!** Your ML application is now live on Hugging Face Spaces!