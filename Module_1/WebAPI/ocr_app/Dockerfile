FROM python:3.8

# Create a folder /app if it doesn't exist,
# the /app folder is the current working directory
WORKDIR /app

# Copy necessary files to our app
COPY ./main.py /app

COPY ./requirements.txt /app

COPY ./my_model /app/my_model

EXPOSE 30000

# Disable pip cache to shrink the image size a little bit,
# since it does not need to be re-installed
RUN pip install -r requirements.txt --no-cache-dir

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "30000"]


#sudo docker build -t kaisa199/ocr:0.01 -f Dockerfile .
#sudo docker run -p 30000:30000 -d kaisa199/ocr:0.01