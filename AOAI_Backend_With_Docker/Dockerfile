FROM nikolaik/python-nodejs:python3.8-nodejs16-slim

WORKDIR /usr/src/app

COPY package*.json ./
COPY requirements.txt ./

RUN npm install
RUN python3 -m pip install -r requirements.txt

COPY . .

EXPOSE 3000

CMD [ "node", "index.js" ]