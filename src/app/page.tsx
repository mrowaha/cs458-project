"use client";
import styles from "./page.module.css";
import GoogleSignInButton from "@/components/atoms/buttons/GoogleSignInButton";
import CredentialsSignInForm from "@/components/molecules/forms/CredentialsSignInForm";

export default function LoginForm() {
  return (
    <div className={styles["login-form__container"]}>
      <GoogleSignInButton />
      <div className={styles["login-form__divider"]} />
      <CredentialsSignInForm />
    </div>
  );
}
