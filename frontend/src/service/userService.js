import { commonPost } from "./common";

export async function tryLogin(mail, password) {
  const data = await commonPost("/login", {
    mail: mail,
    password: password,
  });
  return {
    status: data.sign_in_success || false,
    code: data.wrong_code || -1,
    id: data.user_id || -1,
    jwt: data.jwt || -1,
  };
}

export async function trySignup(phone_number, mail, user_name, password) {
  const data = await commonPost("/registry", {
    phone_number: phone_number,
    mail: mail,
    user_name: user_name,
    password: password,
  });

  return { status: data.regist_success || false, code: data.wrong_code || -1 };
}
