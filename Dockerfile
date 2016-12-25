FROM vimagick/scrapyd

RUN apt-get update
RUN apt-get install -y python-psycopg2
RUN rm -rf /var/lib/apt/lists/*

RUN pip install sqlalchemy==1.0.12
