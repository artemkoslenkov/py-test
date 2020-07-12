FROM python
RUN mkdir /root/app
ADD packages.txt /root/app
WORKDIR /root/app
RUN pip install -r packages.txt
WORKDIR /root/app
CMD python -u ./src/app.py
#CMD ["tail", "-f", "/dev/null"]
