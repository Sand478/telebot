FROM python:slim
ENV TOKEN='5559736503:AAGVNU915kHAjx6aopVEUP8ga-46xonPY4s'
COPY . .
RUN pip install -r req.txt
CMD python bot.py