import { apiFetch } from "@/lib/api/client";

export interface Hobby {
  label: string;
  icon_key: string;
}

export interface Education {
  institution: string;
  institution_icon_key: string;
  degree: string;
  degree_icon_key: string;
}

export interface UserProfile {
  id: number;
  name: string;
  title: string;
  bio: string;
  email: string;
  github_url: string;
  linkedin_url: string;
  leetcode_url: string;
  location: string;
  hobbies: Hobby[];
  education: Education[];
}

export async function getProfile(): Promise<UserProfile> {
  
  const data = await apiFetch<UserProfile[]>("/api/profile/");

  // Throw error if the Array is empty, expect 1
  if (data.length === 0) {
    throw new Error(
      "No profile data returned from /api/profile/ — expected exactly one profile record."
    );
  }

  return data[0];
}
