FROM  node:16.13.0-alpine3.11 as build-stage

# make the 'app' folder the current working directory
WORKDIR /app/

COPY package*.json ./

RUN npm cache verify

# install project dependencies
RUN npm install

# copy project files and folders to the current working directory (i.e. 'app' folder)
COPY . .
RUN npm run build-only

EXPOSE 8080

CMD ["npm", "run", "dev"]

# # Stage 2: Serve Vue app with Nginx
# FROM --platform=linux/amd64 nginx:1.25.1 as prod-stage
# COPY --from=build-stage /app/dist /usr/share/nginx/html
# EXPOSE 80
# CMD ["nginx", "-g", "daemon off;"]