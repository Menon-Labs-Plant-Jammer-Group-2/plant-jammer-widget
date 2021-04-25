FROM node:14.4.0-alpine

RUN mkdir /frontend
WORKDIR /frontend

COPY . .

RUN yarn global add @vue/cli
RUN yarn install
CMD ["yarn", "run", "serve"]