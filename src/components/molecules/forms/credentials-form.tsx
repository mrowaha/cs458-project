"use client";
import { signInIcon } from "@/assets/icons";
import { Button, TextBox } from "devextreme-react";
import { observer } from "mobx-react";
import { useState } from "react";
import { ICredentialsFormModel } from "./credentials-form.model";
import { signIn } from "next-auth/react";
const CredentialsSignInForm = ({
  formModel,
}: {
  formModel: ICredentialsFormModel;
}) => {
  const [submit, setSubmit] = useState(false);
  const handleSubmit = async () => {
    setSubmit(true);
    if (Boolean(formModel.errors.email) || Boolean(formModel.errors.password))
      return;
    const signInResponse = await signIn("credentials", {
      ...formModel.toJson,
      callbackUrl: "/dashboard",
    });
  };

  return (
    <div style={{ display: "flex", flexDirection: "column", gap: 5 }}>
      <div>
        <TextBox
          value={formModel.email}
          onValueChanged={({ value }) => formModel.setEmail(value)}
          label="Email"
          placeholder="Enter Email"
          labelMode="static"
        />
        {Boolean(formModel.errors.email) && submit && (
          <ErrorToast error={formModel.errors.email} />
        )}
      </div>

      <div>
        <TextBox
          value={formModel.password}
          onValueChanged={({ value }) => formModel.setPassword(value)}
          label="Password"
          placeholder="Enter Password"
          labelMode="static"
        />
        {Boolean(formModel.errors.password) && submit && (
          <ErrorToast error={formModel.errors.password} />
        )}
      </div>
      <Button text="Sign In" icon={signInIcon} onClick={handleSubmit} />
    </div>
  );
};

export default observer(CredentialsSignInForm);

// helpers //////////
function ErrorToast({ error }: { error: string }) {
  return (
    <div
      style={{ display: "flex", backgroundColor: "#F87171", borderRadius: 10 }}
    >
      <div
        style={{
          flex: 1,
          color: "#92400E",
          padding: "0.15rem",
          backgroundColor: "#FEF2F2",
        }}
      >
        <p
          style={{
            width: "100%",
            display: "flex",
            alignItems: "center",
            gap: 2.5,
            position: "relative",
            fontSize: "0.75em",
          }}
        >
          <span className="dx-icon-clear" style={{ color: "#F87171" }} />
          {error}
        </p>
      </div>
    </div>
  );
}
