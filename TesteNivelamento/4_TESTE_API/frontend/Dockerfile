FROM node:20-alpine

WORKDIR /app

COPY vue-project/package*.json ./
RUN npm install

COPY vue-project/. ./
RUN npm run build

RUN npm install -g serve
CMD ["serve", "-s", "dist", "-l", "3000"]
