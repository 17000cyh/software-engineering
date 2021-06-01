import axios from "axios";
import { getBaseURL } from "../static/config";
import { commonPost } from "./common";

export function tryLogin(mail, password) {
  // let status = false;
  // let code = -1;
  // let user_id = -1;
  axios.defaults.baseURL = getBaseURL();
  // axios
  //   .post("/login", {
  //     mail: mail,
  //     password: password,
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   })
  //   .then((response) => {
  //     status = response.data.sign_in_success;
  //     code = response.data.wrong_code;
  //     user_id = response.data.user_id;
  //   })
  //   .catch((err) => {
  //     console.log(err);
  //   });
  const data = commonPost("/login", {
    mail: mail,
    password: password,
  });
  return {
    status: data.sign_in_success || false,
    code: data.wrong_code || -1,
    id: data.user_id || -1,
  };
}

export function trySignup(phone_number, mail, user_name, password) {
  // let status = false;
  // let code = -1;
  const data = commonPost("/registry", {
    phone_number: phone_number,
    mail: mail,
    user_name: user_name,
    password: password,
  });
  // .catch((err) => {
  //   console.log(err);
  // })
  // .then((response) => {
  //   status = response.data.regist_success;
  //   code = response.data.wrong_code;
  // })
  // .catch((err) => {
  //   console.log(err);
  // });
  return { status: data.regist_success || false, code: data.wrong_code || -1 };
}
