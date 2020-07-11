FROM python
RUN mkdir /root/src
ADD ./packages.txt /root/src
WORKDIR /root/src
RUN pip install -r packages.txt
CMD python -u app.py
#CMD ["tail", "-f", "/dev/null"]
