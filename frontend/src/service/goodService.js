import { commonPost } from "./common";

export async function fetchGoods(userId) {
  const data = await commonPost("/hot", {
    user_id: userId,
  });
  return data;
}
