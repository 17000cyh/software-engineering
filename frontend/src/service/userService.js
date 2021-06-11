import { commonPost } from "./common";

export async function tryLogin(mail, password) {
  const data = await commonPost("/login", {
    mail: mail,
    password: password,
  });
  return {
    status: data && data.sign_in_success,
    code: data && data.wrong_code,
    id: data && data.user_id,
  };
}

export async function trySignup(phone_number, mail, user_name, password) {
  const data = await commonPost("/registry", {
    phone_number: phone_number,
    mail: mail,
    user_name: user_name,
    password: password,
  });

  return { status: data && data.regist_success, code: data && data.wrong_code };
}
