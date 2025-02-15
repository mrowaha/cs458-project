import {spotifyIcon} from "@/assets/icons";
import { Button } from "devextreme-react/button";
import { signIn } from "next-auth/react";
const SpotifySignIn = () => {
  return (
    <Button
      id="oauth__spotify-button"
      text="Sign In with Spotify"
      stylingMode="contained"
      icon={spotifyIcon}
      onClick={() => signIn("spotify", { callbackUrl: "/dashboard" })}
    />
  );
};

export default SpotifySignIn;
