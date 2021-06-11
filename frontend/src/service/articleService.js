import { commonPost } from "./common";

export async function fetchArticles(userId, method) {
  let data = {};
  switch (method) {
    case "follow":
      data = await commonPost("/follow", {
        user_id: userId,
      });
      break;
    case "hot":
      data = await commonPost("/hot", {
        user_id: userId,
      });
      break;
    default:
      data = await commonPost("/index", {
        user_id: userId,
      });
      break;
  }

  return {
    hasMore: data && data.hasMore,
    articles: data && data.article_list,
  };
}

export async function fetchComments(targetId) {
  const data = await commonPost("/get_comment", {
    target_id: targetId,
  });
  console.log(data.comment_infor);
  return data.comment_infor;
}

export function fetchFakeArticles() {
  let articles = [];

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
