import { commonPost } from "./common";

export function fetchArticles(userId) {
  // let articles = [];

  // let hasMore = false;
  // axios.defaults.baseURL = getBaseURL();
  let data = {};
  data = commonPost("/articles", {
    userId: userId,
  });
  // .catch((err) => {
  //   console.log(err);
  // })
  // .then((response) => {
  //   articles = response.data.article_list;
  //   hasMore = response.data.hasMore;
  // })
  // .catch((err) => {
  //   console.log(err);
  // });
  return {
    hasMore: data.hasMore || false,
    articles: data.article_list || [],
  };
}

export function fetchFakeArticles() {
  let articles = [];
  // let hasMore = false;
  // hasMore = true;
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
