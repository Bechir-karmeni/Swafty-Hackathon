# Step 1: Use an official Python runtime as a parent image
FROM python:3.10



# Step 3: Set up the working directory
WORKDIR /app

# Step 4: Install dependencies
# Copy requirements and install them
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the Django application code to the working directory
COPY . /app



# Step 7: Expose the port on which Django will run
EXPOSE 9000

# Step 8: Define the command to run the Django app
CMD ["python", "manage.py", "runserver", "0.0.0.0:9000"]