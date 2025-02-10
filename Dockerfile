# Use an official lightweight Python image
FROM python:3.13.2

# Set the working directory inside the container
WORKDIR /app

# Copy the script and any required files into the container
COPY fetch_commits.py /app/script.py
COPY requirements.txt /app/

# Install dependencies
RUN pip install -r requirements.txt

# Command to run the script
CMD ["python", "script.py"]
