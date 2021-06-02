import axios from "axios";
import { getBaseURL } from "../static/config";

axios.defaults.baseURL = getBaseURL();

export function fetchLike(params) {
  let data;
  axios
    .post("/like", {
      userId: userId,
    })
    .then((response) => {
      data = response.data;
    })
    .catch((err) => {
      console.log(err);
    });
  return data;
}
