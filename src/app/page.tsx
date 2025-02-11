"use client";

import { login } from "@/actions/login.action";
import { LoginResponseDto } from "@/dto/login-response.dto";
import { useActionState } from "react";
import { useFormStatus } from "react-dom";

const initialState: LoginResponseDto = {
  message: "",
};

export default function LoginForm() {
  const [state, loginFormAction] = useActionState(login, initialState);

  return (
    <form action={loginFormAction}>
      <label htmlFor="login__email">Email: </label>
      <input id="login__email" type="email" name="email" required />
      <label htmlFor="login__password">Password: </label>
      <input id="login__password" type="password" name="password" required />
      <SubmitButton />
      <p>{state?.message}</p>
    </form>
  );
}

// helpers ///////////////
function SubmitButton() {
  const { pending } = useFormStatus();

  return (
    <button type="submit" disabled={pending}>
      Login
    </button>
  );
}
