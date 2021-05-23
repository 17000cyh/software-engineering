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
