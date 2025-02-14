"use client";
import { useSession } from "next-auth/react";
import { useEffect, useMemo } from "react";
import { useRouter } from "next/navigation";

function Dashboard() {
  const { data: session } = useSession();
  const loggedIn = useMemo(() => session && session.user, [session]);
  const router = useRouter();
  useEffect(() => {
    if (!loggedIn) setTimeout(() => router.replace("/"), 1000);
  }, [loggedIn]);

  if (loggedIn) {
    return <h1>Welcome, {session.user.email}</h1>;
  }

  return <h1>Redirecting to Sign In</h1>;
}

export default Dashboard;
