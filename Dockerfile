FROM python:3.7 
RUN pip3 install -r requirements.txt
RUN git clone https://github.com/MiguelEVeliz/fibonacci_web_service.git
WORKDIR /fibonacci_web_service
ENTRYPOINT ["python"]
CMD ["fibonacci_web_service.py"]
