FROM unisec/vuepress
RUN  npm install -g vuepress @vuepress/theme-blog --force
WORKDIR /blog
CMD npm run docs:dev
