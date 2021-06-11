import axios from "axios";
import { getBaseURL } from "../static/config";
import { commonPost } from "./common";

axios.defaults.baseURL = getBaseURL();

export async function fetchReplyList(userId) {
  const data = await commonPost("/get_reply", {
    user_id: userId,
  });
  return data.reply_list;
}
