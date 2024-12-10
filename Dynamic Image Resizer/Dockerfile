FROM python:3.8

# Set working directory
WORKDIR /usr/src/app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port 5000 and run the application
EXPOSE 5000
CMD ["python", "app.py"]
