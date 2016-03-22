FROM python:onbuild
EXPOSE 8000

CMD [ "python", "./moby.py" ]
