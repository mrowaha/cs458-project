"use client";
import { useSession } from "next-auth/react";
import { useEffect, useMemo } from "react";
import { useRouter } from "next/navigation";

function Dashboard() {
  const { data: session, status } = useSession();
  const router = useRouter();
  useEffect(() => {
    if (status === "unauthenticated") router.replace("/");
  }, [status]);

  if (status === "loading") {
    return <h1>Loading...</h1>;
  }

  if (status === "unauthenticated") {
    return <h1>Access Denied</h1>;
  }

  return <h1>Welcome, {session.user.email}</h1>;
}

export default Dashboard;
