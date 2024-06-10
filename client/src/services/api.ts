import { ILoginRequest } from "@/config/interfaces";
import store from "@/store";
import axios, { AxiosError, AxiosResponse } from "axios";

// Define the API base URL (replace with your actual URL)
const API_URL = "http://127.0.0.1:5000";

interface ImageData {
  data: string; // Base64 encoded image data
}

export interface PredictionResponse {
  "Deformed cells detected": number;
  "Healthy cells detected": number;
  annotatedImage: ImageData;
}

export interface User {
  id: number;
  email: string;
  username: string;
  passwd: string;
}

export interface CreateUserData {
  email: string;
  username: string;
  passwd: string;
}

export default class ApiClient {
  static async predict(image: File): Promise<PredictionResponse> {
    const formData = new FormData();
    formData.append('image', image);

    try {
      const response: AxiosResponse<PredictionResponse> = await axios.post(
        `${API_URL}/predict/`,
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data',
            Authorization: `Bearer ${store.getters.getToken}`,
          },
        }
      );
      return response.data;
    } catch (error) {
      throw new Error('Error predicting image: ' + error);
    }
  }

  static async login(data: ILoginRequest): Promise<any> {
    try {
      const response: AxiosResponse<PredictionResponse> = await axios.post(
        `${API_URL}/auth/`,
        data,
        {
          headers: {
            'Content-Type': 'application/json',
          },
        }
      );
      return response.data;
    } catch (error: any) {
      throw new Error(error.response.data.message ?? error);
    }
  }

  static async fetchUsers(): Promise<any> {
    try {
      const response: AxiosResponse<User[]> = await axios.get(
        `${API_URL}/users/`,
        {
          headers: {
            Authorization: `Bearer ${store.getters.getToken}`,
          },
        }
      );
      return response.data;
    } catch (error: any) {
      throw new Error(error.response.data.message);
    }
  }

  static async createUser(data: CreateUserData): Promise<any> {
    try {
      const response: AxiosResponse<any> = await axios.post(
        `${API_URL}/user/`,
        data,
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${store.getters.getToken}`,
          },
          validateStatus: function (status) {
            return status === 200; // Resolve only if the status code is 200
          },
        }
      );
  
      return response;
    } catch (error: any) {
      return error.response
    }
  }

  static async updateUser(data: User): Promise<any> {
    try {
      const response: AxiosResponse<any> = await axios.put(
        `${API_URL}/user/`,
        data,
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${store.getters.getToken}`,
          },
        }
      );
      return response.data;
    } catch (error: any) {
      throw new Error(error.response.data.message);
    }
  }

  static async deleteUser(id: number): Promise<any> {
    try {
      const response: AxiosResponse<any> = await axios.delete(
        `${API_URL}/user/`,
        {
          headers: {
            'Content-Type': 'application/json',
            Authorization: `Bearer ${store.getters.getToken}`,
          },
          data: {
            id,
          },
        }
      );
      return response.data;
    } catch (error: any) {
      throw new Error(error.response.data.message);
    }
  }
}
