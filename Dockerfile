from mongo:8.2.2

EXPOSE 27017

VOLUME /data/db
CMD["mongod"]