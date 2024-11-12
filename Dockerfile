FROM ghcr.io/kiran21-s/flask_testing:0.0.1.release
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 3000
CMD python ./index.py
