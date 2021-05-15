import axios from "axios";

export function tryLogin(mail, password) {
  let status = false;
  let code = -1;
  let user_id = -1;
  axios
    .post("/login", {
      mail: mail,
      password: password,
    })
    .catch((err) => {
      console.log(err);
    })
    .then((response) => {
      status = response.data.sigh_in_success;
      code = response.data.wrong_code;
      user_id = response.data.user_id;
    })
    .catch((err) => {
      console.log(err);
    });
  return { status: status, code: code, id: user_id };
}

export function trySignup(phone_number, mail, user_name, password) {
  let status = false;
  let code = -1;
  axios
    .post("/registry", {
      phone_number: phone_number,
      mail: mail,
      user_name: user_name,
      password: password,
    })
    .catch((err) => {
      console.log(err);
    })
    .then((response) => {
      status = response.data.regist_success;
      code = response.data.wrong_code;
    })
    .catch((err) => {
      console.log(err);
    });
  return { status: status, code: code };
}
