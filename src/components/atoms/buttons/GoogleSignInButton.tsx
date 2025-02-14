import { googleIcon } from "@/assets/icons";
import { Button } from "devextreme-react/button";
import { signIn } from "next-auth/react";
const GoogleSignInButton = () => {
  return (
    <Button
      text="Sign In with Google"
      stylingMode="contained"
      icon={googleIcon}
      onClick={() => signIn("google")}
    />
  );
};

export default GoogleSignInButton;
