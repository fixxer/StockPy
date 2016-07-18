FROM python:2-wheezy
RUN pip install --no-cache-dir beautifulsoup4
RUN pip install --no-cache-dir requests
RUN pip install --no-cache-dir html5lib
RUN pip install --no-cache-dir --upgrade html5lib==1.0b8

ADD ./main.py /opt/StockPy/main.py
ADD ./data_service.py /opt/StockPy/data_service.py

WORKDIR /opt/StockPy

CMD ["python2"]