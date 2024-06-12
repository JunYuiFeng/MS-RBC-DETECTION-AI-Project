import { ILoginRequest } from "@/config/interfaces";
import store from "@/store";
import axios, { AxiosError, AxiosResponse } from "axios";

const API_URL = "http://127.0.0.1:5000";

// INTERFACES
export interface PredictionResponse {
  deformedCellsDetected: number;
  healthyCellsDetected: number;
  annotatedImage: string;
}

export interface MultiplePredictionResponse extends Omit<PredictionResponse, 'annotatedImage'> {
  annotatedImages: string[];
}

export interface ComparisonResponse {
  patient1: MultiplePredictionResponse;
  patient2: MultiplePredictionResponse; 
  comparison: {
    deformedCellsDifference: number;
    healthyCellsDifference: number;
  };
}

export interface User {
  id: number;
  email: string;
  username: string;
  passwd: string;
}

export interface UserResponse {
  id: number;
  email: string;
  username: string;
  passwd: string;
  role: string;
}

export interface CreateUserData {
  email: string;
  username: string;
  passwd: string;
}
// -----------------

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
      throw new Error('Error predicting image: ' + (error as AxiosError).message);
    }
  }

  static async compare(
    patient1Images: File[],
    patient2Images: File[]
  ): Promise<ComparisonResponse> {
    const formData = new FormData();
    patient1Images.forEach((image, index) => {
      formData.append('patient1_images', image, `patient1_image${index + 1}`);
    });
    patient2Images.forEach((image, index) => {
      formData.append('patient2_images', image, `patient2_image${index + 1}`);
    });

    try {
      const response: AxiosResponse<ComparisonResponse> = await axios.post(
        `${API_URL}/compare/`,
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
      throw new Error('Error comparing images: ' + (error as AxiosError).message);
    }
  }

  static async login(data: ILoginRequest): Promise<any> {
    try {
      const response: AxiosResponse<any> = await axios.post(
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
      throw new Error(error.response?.data?.message ?? (error as AxiosError).message);
    }
  }

  static async fetchUsers(): Promise<{users: UserResponse[]}> {
    try {
      const response: AxiosResponse<{users: UserResponse[]}> = await axios.get(
        `${API_URL}/users/`,
        {
          headers: {
            Authorization: `Bearer ${store.getters.getToken}`,
          },
        }
      );
      return response.data;
    } catch (error: any) {
      throw new Error(error.response?.data?.message ?? (error as AxiosError).message);
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
            return status === 200; 
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
          validateStatus: function (status) {
            return status === 200;
          },
        }
      );
      return response;
    } catch (error: any) {
      return error.response
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
      throw new Error(error.response?.data?.message ?? (error as AxiosError).message);
    }
  }
}
