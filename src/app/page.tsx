"use client";
import styles from "./page.module.css";
import GoogleSignInButton from "@/components/atoms/buttons/GoogleSignInButton";
import CredentialsSignInForm from "@/components/molecules/forms/credentials-form";
import { CredentialsFormModel } from "@/components/molecules/forms/credentials-form.model";
import { useSession } from "next-auth/react";
export default function Login() {
  return (
    <div className={styles["login-form__container"]}>
      <h1>CS458 - Project</h1>
      <CredentialsSignInForm
        formModel={CredentialsFormModel.create({ email: "", password: "" })}
      />
      <div className={styles["login-form__divider"]} />
      <GoogleSignInButton />
      <footer>© Copyright 2025: Muhammad Rowaha (All Rights Reserved)</footer>
    </div>
  );
}
