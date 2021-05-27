import axios from "axios";
import { getBaseURL } from "../static/config";

export function fetchArticles(userId) {
  let articles = [];
  let hasMore = false;
  axios.defaults.baseURL = getBaseURL();
  axios
    .post("/articles", {
      userId: userId,
    })
    .catch((err) => {
      console.log(err);
    })
    .then((response) => {
      articles = response.data.article_list;
      hasMore = response.data.hasMore;
    })
    .catch((err) => {
      console.log(err);
    });
  return {
    hasMore: hasMore,
    articles: articles,
  };
}

export function fetchFakeArticles() {
  let articles = [];
  let hasMore = false;
  hasMore = true;
  articles = [
    {
      article_name: "Some Article Name",
      article_content: "Some Article Content",
    },
  ];
  return {
    hasMore: true,
    articles: articles,
  };
}
