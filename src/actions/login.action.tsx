"use server";

import { LoginResponseDto } from "@/dto/login-response.dto";
import { revalidatePath } from "next/cache";

export async function login(prevState: LoginResponseDto, formData: FormData) {
  revalidatePath("/");
  return {
    message: `logged in test ${Date.now().toString()}`,
  };
}
