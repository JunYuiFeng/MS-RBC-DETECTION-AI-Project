import { ILoginRequest } from "@/config/interfaces";
import axios, { AxiosResponse } from "axios";

// Define the API base URL (replace with your actual URL)
const API_URL = "http://localhost";

interface ImageData {
  data: string; // Base64 encoded image data
}

export interface PredictionResponse {
  "Deformed cells detected": number;
  "Healthy cells detected": number;
  annotatedImage: ImageData;
}

export default class ApiClient {
  static async predict(image: File): Promise<PredictionResponse> {
    const formData = new FormData();
    formData.append("image", image);

    try {
      const response: AxiosResponse<PredictionResponse> = await axios.post(
        `${API_URL}/predict`,
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        }
      );
      return response.data;
    } catch (error) {
      throw new Error("Error predicting image: " + error);
    }
  }

  static async login(data: ILoginRequest): Promise<any> {
    try {
      const response: AxiosResponse<PredictionResponse> = await axios.post(
        `${API_URL}/auth`,
        data,
         {
          headers: {
            "Content-Type": "application/json"
          },
        }
      );
      return response.data;
    } catch (error) {
      throw new Error("Error in Login Request: " + error);
    }
  }
}
